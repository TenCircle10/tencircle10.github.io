#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Obsidian -> Jekyll 笔记同步脚本。

把 ``origin/`` 里的原始 Obsidian 笔记转换成 Jekyll + kramdown 能正确渲染的
Markdown，输出到 ``notes/``。

处理的语法：

1. **Obsidian Callout**：``> [!note] 标题`` + 后续引用行
   -> ``<details class="callout note" markdown="block">`` +
   ``<summary>`` + ``<div class="callout-content" markdown="block">``。
   ``[!note]+`` 加 ``open`` 属性（默认展开），``[!note]-`` 默认折叠。
2. **数学公式转义**：``$...$`` / ``$$...$$`` 里的 ``\\{`` ``\\}`` -> ``\\\\{`` ``\\\\}``，
   ``|`` -> ``\\mid``，避免被 kramdown 先吃掉（kramdown 只把 ``$$`` 当数学，
   单 ``$`` 的公式内容会先走 Markdown 解析）。已转义过的写法不会重复转义。
3. **Obsidian 内部链接**：
   ``[[笔记]]`` -> ``[笔记](/notes/笔记/)``；
   ``[[笔记|文本]]`` -> ``[文本](/notes/笔记/)``；
   ``[[#^块ID|文本]]`` -> ``[文本](#块ID)``；
   单独成行的块 ID ``^块ID`` -> ``<a id="块ID"></a>``。
4. **图片嵌入**：``![[图片.png]]`` -> ``![图片.png](/assets/img/obsidian/图片.png)``。
5. **Front Matter**：文件头没有 ``---`` 包裹的 YAML 时，自动补
   ``layout: note`` 和 ``title``（取文件名）。

````` 围起来的代码块（``` 或 ~~~）整体跳过，不做任何替换。

用法::

    python sync_notes.py                       # origin/ -> notes/
    python sync_notes.py --src other --dest out
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEFAULT_SRC = ROOT / "origin"
DEFAULT_DEST = ROOT / "notes"


# --------------------------------------------------------------------------- #
# 代码块保护：先整段抽出来，最后再原样放回，保证代码块里不做任何替换
# --------------------------------------------------------------------------- #
_CODE_PLACEHOLDER = "\x00SYNC_CODE_BLOCK_{}\x00"
_FENCE_OPEN_RE = re.compile(r"^[ \t]*(`{3,}|~{3,})")


def protect_code_blocks(text: str) -> tuple[str, list[str]]:
    """把 fenced code block 换成占位符，返回 (处理后的文本, 被抽出的代码块)。"""
    lines = text.split("\n")
    output: list[str] = []
    blocks: list[str] = []
    index = 0
    while index < len(lines):
        match = _FENCE_OPEN_RE.match(lines[index])
        if not match:
            output.append(lines[index])
            index += 1
            continue
        fence = match.group(1)
        close_re = re.compile(
            r"^[ \t]*" + re.escape(fence[0]) + "{%d,}[ \t]*$" % len(fence)
        )
        start = index
        index += 1
        while index < len(lines) and not close_re.match(lines[index]):
            index += 1
        if index < len(lines):  # 吃掉结束 fence
            index += 1
        blocks.append("\n".join(lines[start:index]))
        output.append(_CODE_PLACEHOLDER.format(len(blocks) - 1))
    return "\n".join(output), blocks


def restore_code_blocks(text: str, blocks: list[str]) -> str:
    """把占位符还原成原始代码块。"""
    for position, block in enumerate(blocks):
        text = text.replace(_CODE_PLACEHOLDER.format(position), block)
    return text


# --------------------------------------------------------------------------- #
# 1. Callout
# --------------------------------------------------------------------------- #
_CALLOUT_HEAD_RE = re.compile(r"^[ \t]*>[ \t]*\[!([A-Za-z0-9_-]+)\]([+-]?)[ \t]*(.*)$")
_QUOTE_LINE_RE = re.compile(r"^[ \t]*>(?:[ \t]?(.*))?$")


def convert_callouts(text: str, counts: dict[str, int]) -> str:
    """把 Obsidian callout 引用块转成 <details class="callout ..."> 结构。"""
    lines = text.split("\n")
    output: list[str] = []
    index = 0
    while index < len(lines):
        head = _CALLOUT_HEAD_RE.match(lines[index])
        if not head:
            output.append(lines[index])
            index += 1
            continue

        callout_type = head.group(1).lower()
        fold = head.group(2)
        title = head.group(3).strip()
        index += 1

        # 收集紧随其后的引用行（Obsidian 里 callout 的每一行都以 > 开头；
        # 空行或非引用行表示 callout 结束，所以两个 callout 之间用空行分隔不会被合并）
        body: list[str] = []
        while index < len(lines):
            quote = _QUOTE_LINE_RE.match(lines[index])
            if not quote:
                break
            body.append(quote.group(1) or "")
            index += 1
        while body and body[-1].strip() == "":
            body.pop()

        if not title:
            title = callout_type.capitalize()

        open_attr = " open" if fold == "+" else ""
        counts["callout"] += 1
        output.append(
            '<details class="callout %s" markdown="block"%s>' % (callout_type, open_attr)
        )
        output.append("<summary>%s</summary>" % title)
        output.append('<div class="callout-content" markdown="block">')
        output.append("")
        output.extend(body)
        output.append("")
        output.append("</div>")
        output.append("</details>")
        # kramdown 需要空行来结束 HTML 块
        if index < len(lines) and lines[index].strip() != "":
            output.append("")

    return "\n".join(output)


# --------------------------------------------------------------------------- #
# 2. 数学公式转义
# --------------------------------------------------------------------------- #
_DISPLAY_MATH_RE = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
_INLINE_MATH_RE = re.compile(r"(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)", re.DOTALL)
_UNESCAPED_OPEN_BRACE_RE = re.compile(r"(?<!\\)\\\{")
_UNESCAPED_CLOSE_BRACE_RE = re.compile(r"(?<!\\)\\\}")
_UNESCAPED_PIPE_RE = re.compile(r"(?<!\\)\|")


def escape_math_body(body: str) -> str:
    """转义单条公式内部的 kramdown 雷区字符（对已转义的内容幂等）。"""
    body = _UNESCAPED_OPEN_BRACE_RE.sub(r"\\\\{", body)
    body = _UNESCAPED_CLOSE_BRACE_RE.sub(r"\\\\}", body)
    body = _UNESCAPED_PIPE_RE.sub(r"\\mid", body)
    return body


def escape_math(text: str, counts: dict[str, int]) -> str:
    """转义 ``$$...$$`` 和 ``$...$`` 内部的 kramdown 雷区字符。"""

    def display(match: re.Match[str]) -> str:
        counts["math"] += 1
        return "$$" + escape_math_body(match.group(1)) + "$$"

    def inline(match: re.Match[str]) -> str:
        counts["math"] += 1
        return "$" + escape_math_body(match.group(1)) + "$"

    text = _DISPLAY_MATH_RE.sub(display, text)
    text = _INLINE_MATH_RE.sub(inline, text)
    return text


# --------------------------------------------------------------------------- #
# 3. Wikilink / 块 ID / 4. 图片
# --------------------------------------------------------------------------- #
_EMBED_RE = re.compile(r"!\[\[([^\]\|]+?)(?:\|[^\]]*)?\]\]")
_BLOCK_LINK_RE = re.compile(r"\[\[#\^([A-Za-z0-9-]+)(?:\|([^\]]+))?\]\]")
_ALIAS_LINK_RE = re.compile(r"\[\[([^\]\|#^]+)\|([^\]]+)\]\]")
_PLAIN_LINK_RE = re.compile(r"\[\[([^\]\|#^]+)\]\]")
_BLOCK_ID_RE = re.compile(r"^[ \t]*\^([A-Za-z0-9-]{4,})[ \t]*$", re.MULTILINE)


def convert_links(text: str, counts: dict[str, int]) -> str:
    """转换图片嵌入、wikilink 和块 ID。图片必须先处理，否则会被 wikilink 规则吃掉。"""

    def embed(match: re.Match[str]) -> str:
        name = match.group(1).strip()
        counts["image"] += 1
        return "![%s](/assets/img/obsidian/%s)" % (name, name)

    def block_link(match: re.Match[str]) -> str:
        block_id = match.group(1)
        label = (match.group(2) or block_id).strip()
        counts["block_link"] += 1
        return "[%s](#%s)" % (label, block_id)

    def alias_link(match: re.Match[str]) -> str:
        target = match.group(1).strip()
        label = match.group(2).strip()
        counts["wikilink"] += 1
        return "[%s](/notes/%s/)" % (label, target)

    def plain_link(match: re.Match[str]) -> str:
        target = match.group(1).strip()
        counts["wikilink"] += 1
        return "[%s](/notes/%s/)" % (target, target)

    def block_id(match: re.Match[str]) -> str:
        counts["block_id"] += 1
        return '<a id="%s"></a>' % match.group(1)

    text = _EMBED_RE.sub(embed, text)
    text = _BLOCK_LINK_RE.sub(block_link, text)
    text = _ALIAS_LINK_RE.sub(alias_link, text)
    text = _PLAIN_LINK_RE.sub(plain_link, text)
    text = _BLOCK_ID_RE.sub(block_id, text)
    return text


# --------------------------------------------------------------------------- #
# 5. Front Matter
# --------------------------------------------------------------------------- #
_FRONT_MATTER_RE = re.compile(r"\A---[ \t]*\r?\n.*?\r?\n---[ \t]*(?:\r?\n|\Z)", re.DOTALL)


def split_front_matter(text: str) -> tuple[str | None, str]:
    """拆出已有的 front matter（含结尾换行）和正文。"""
    match = _FRONT_MATTER_RE.match(text)
    if not match:
        return None, text
    return match.group(0), text[match.end():]


def build_front_matter(title: str) -> str:
    """生成默认 front matter。"""
    safe_title = title.replace("\\", "\\\\").replace('"', '\\"')
    return '---\nlayout: note\ntitle: "%s"\n---\n\n' % safe_title


# --------------------------------------------------------------------------- #
# 主流程
# --------------------------------------------------------------------------- #
def convert_document(text: str, stem: str) -> tuple[str, dict[str, int], bool]:
    """转换单个笔记，返回 (结果文本, 各类替换计数, 是否新插入 front matter)。"""
    counts = {
        "callout": 0,
        "math": 0,
        "wikilink": 0,
        "block_link": 0,
        "block_id": 0,
        "image": 0,
    }
    front_matter, body = split_front_matter(text)
    body, code_blocks = protect_code_blocks(body)
    body = convert_callouts(body, counts)
    body = escape_math(body, counts)
    body = convert_links(body, counts)
    body = restore_code_blocks(body, code_blocks)

    added_front_matter = front_matter is None
    if added_front_matter:
        front_matter = build_front_matter(stem)
    return front_matter + body, counts, added_front_matter


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="把 origin/ 里的 Obsidian 笔记转换成 Jekyll 可渲染的 Markdown。"
    )
    parser.add_argument("--src", default=str(DEFAULT_SRC), help="源目录（默认 ./origin）")
    parser.add_argument("--dest", default=str(DEFAULT_DEST), help="输出目录（默认 ./notes）")
    args = parser.parse_args(argv)

    src = Path(args.src).resolve()
    dest = Path(args.dest).resolve()
    if not src.is_dir():
        print("[error] 源目录不存在：%s" % src, file=sys.stderr)
        return 1

    dest.mkdir(parents=True, exist_ok=True)

    sources = sorted(path for path in src.rglob("*.md") if path.is_file())
    if not sources:
        print("[warn] %s 下没有找到 .md 文件" % src)

    for path in sources:
        relative = path.relative_to(src)
        target = dest / relative
        target.parent.mkdir(parents=True, exist_ok=True)

        converted, counts, added = convert_document(
            path.read_text(encoding="utf-8"), path.stem
        )
        target.write_text(converted, encoding="utf-8", newline="\n")
        print(
            "[ok] %s -> %s  (callout=%d, math=%d, wikilink=%d, block_link=%d, block_id=%d, image=%d, front_matter=%s)"
            % (
                relative,
                target,
                counts["callout"],
                counts["math"],
                counts["wikilink"],
                counts["block_link"],
                counts["block_id"],
                counts["image"],
                "generated" if added else "kept",
            )
        )

    print("[done] 共处理 %d 个文件，输出目录：%s" % (len(sources), dest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
