#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Obsidian -> Jekyll 笔记同步脚本。

把 ``origin/`` 里的原始 Obsidian 笔记转换成 Jekyll + kramdown 能正确渲染的
Markdown，输出到 ``notes/``。

处理的语法：

1. **Obsidian Callout**：``> [!note] 标题`` + 后续引用行
   -> ``<details class="callout note" data-callout="note" markdown="block">`` +
   ``<summary class="callout-title">`` + ``<div class="callout-content" markdown="block">``。
   ``data-callout`` 和 ``callout-title`` 是为了直接复用
   assets/css/obsidian-callouts.css 里已有的图标与边框样式。
   ``[!note]+`` 加 ``open`` 属性（默认展开），``[!note]-`` 默认折叠。
2. **数学公式转义（只处理行内 ``$...$``）**：公式里的 ``\{`` ``\}`` -> ``\\{`` ``\\}``，
   ``|`` -> ``\mid``，避免被 kramdown 先吃掉（kramdown 只把 ``$$`` 当数学，
   单 ``$`` 的公式内容会先走 Markdown 解析）。已转义过的写法不会重复转义。
   ``$$...$$`` 块级公式**不做任何转义**：kramdown 的数学引擎会把块内容原样透传给
   MathJax，在块内再加反斜杠反而会让公式渲染出错。
3. **Obsidian 内部链接**：
   ``[[笔记]]`` -> ``[笔记](/notes/笔记/)``；
   ``[[笔记|文本]]`` -> ``[文本](/notes/笔记/)``；
   ``[[#^块ID|文本]]`` -> ``[文本](#块ID)``；
   单独成行的块 ID ``^块ID`` -> ``<a id="块ID"></a>``。
4. **图片嵌入**：``![[图片.png]]`` -> ``![图片.png](/assets/img/obsidian/图片.png)``。
5. **Front Matter（layout 强制注入）**：输出文件的 front matter 一定包含
   ``layout: note``。源文件没有 front matter 时自动生成 ``layout`` + ``title``
   （取文件名）；源文件已有 front matter 时，缺 ``layout`` 就补上、写错了就覆盖。
   ``layout`` 决定页面套用 _layouts/note.html，缺了它 MathJax 和笔记专属样式
   都不会加载（公式会变成源码）。
6. **slug 映射（决定输出文件名与 URL）**：源笔记 front matter 里写
   ``slug: math-analysis-szy`` 时，输出文件为 ``notes/math-analysis-szy.md``，
   并写入 ``permalink: /notes/math-analysis-szy/``（源文件里已有的 permalink 会被覆盖）。
   没写 ``slug`` 时回退用源文件名。正文里的 ``[[中文笔记名]]`` 会按
   「源文件名 / front matter title -> slug」的映射重写成 slug URL，
   显示文本仍保留原来的中文名；找不到对应笔记时保持原样。

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
            '<details class="callout %s" data-callout="%s" markdown="block"%s>'
            % (callout_type, callout_type, open_attr)
        )
        output.append('<summary class="callout-title">%s</summary>' % title)
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
# 2. 数学公式转义（只处理行内 $...$，$$...$$ 块保持原样）
# --------------------------------------------------------------------------- #
# 定界符前面不能是反斜杠或 $：排除 $ 是为了跳过 $$ 块，排除反斜杠是为了
# 避免 $$ 块里的 \$（例如 \$100）被当成行内公式的定界符——那会让正则跨过
# 整个 $$ 块去和后面正文里的 $ 配对，把真正的行内公式吃掉。
_INLINE_MATH_RE = re.compile(r"(?<![\\$])\$(?!\$)(.+?)(?<![\\$])\$(?!\$)", re.DOTALL)
_UNESCAPED_OPEN_BRACE_RE = re.compile(r"(?<!\\)\\\{")
_UNESCAPED_CLOSE_BRACE_RE = re.compile(r"(?<!\\)\\\}")
_UNESCAPED_PIPE_RE = re.compile(r"(?<!\\)\|")


def escape_math_body(body: str) -> str:
    """转义单条行内公式内部的 kramdown 雷区字符（对已转义的内容幂等）。"""
    body = _UNESCAPED_OPEN_BRACE_RE.sub(r"\\\\{", body)
    body = _UNESCAPED_CLOSE_BRACE_RE.sub(r"\\\\}", body)
    body = _UNESCAPED_PIPE_RE.sub(r"\\mid", body)
    return body


def escape_math(text: str, counts: dict[str, int]) -> str:
    """只转义行内 ``$...$`` 内部的 kramdown 雷区字符。

    ``$$...$$`` 块级公式不做任何处理：kramdown 的数学引擎会把整段块内容原样交给
    MathJax，块内再补反斜杠会让 MathJax 收到 ``\\{`` 这类错误的转义序列。
    """

    def inline(match: re.Match[str]) -> str:
        counts["math"] += 1
        return "$" + escape_math_body(match.group(1)) + "$"

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


def convert_links(
    text: str,
    counts: dict[str, int],
    slug_map: dict[str, str],
    url_prefix: str,
) -> str:
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
        raw_target = match.group(1).strip()
        target = resolve_note_target(raw_target, slug_map)
        label = match.group(2).strip()
        counts["wikilink"] += 1
        return "[%s](%s%s/)" % (label, url_prefix, target)

    def plain_link(match: re.Match[str]) -> str:
        # 显示文本保留 Obsidian 里的原名（中文），只把 URL 换成 slug
        raw_target = match.group(1).strip()
        target = resolve_note_target(raw_target, slug_map)
        counts["wikilink"] += 1
        return "[%s](%s%s/)" % (raw_target, url_prefix, target)

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
# 5. Front Matter、slug 与 permalink
# --------------------------------------------------------------------------- #
_FRONT_MATTER_RE = re.compile(r"\A---[ \t]*\r?\n.*?\r?\n---[ \t]*(?:\r?\n|\Z)", re.DOTALL)
_FM_FIELD_RE = re.compile(r"^([A-Za-z0-9_-]+)[ \t]*:[ \t]*(.*)$")
_PERMALINK_LINE_RE = re.compile(r"^[ \t]*permalink[ \t]*:.*$", re.MULTILINE)


def split_front_matter(text: str) -> tuple[str | None, str]:
    """拆出已有的 front matter（含结尾换行）和正文。"""
    match = _FRONT_MATTER_RE.match(text)
    if not match:
        return None, text
    return match.group(0), text[match.end():]


def _unquote(value: str) -> str:
    """去掉 YAML 标量两侧的一层引号（只处理最简单的情形）。"""
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def read_front_matter_fields(front_matter: str | None) -> dict[str, str]:
    """读取 front matter 的顶层单行标量字段（title / slug / permalink 等）。"""
    fields: dict[str, str] = {}
    if not front_matter:
        return fields
    for line in front_matter.split("\n"):
        match = _FM_FIELD_RE.match(line)
        if match:
            fields[match.group(1)] = _unquote(match.group(2))
    return fields


def build_front_matter(title: str) -> str:
    """生成默认 front matter。"""
    safe_title = title.replace("\\", "\\\\").replace('"', '\\"')
    return '---\nlayout: note\ntitle: "%s"\n---\n\n' % safe_title


def apply_permalink(front_matter: str, permalink: str) -> str:
    """在 front matter 里写入 permalink；已存在则覆盖，并保证后面留一个空行。"""
    line = 'permalink: "%s"' % permalink
    if _PERMALINK_LINE_RE.search(front_matter):
        updated = _PERMALINK_LINE_RE.sub(lambda _match: line, front_matter, count=1)
    else:
        stripped = front_matter.rstrip("\n")
        if not stripped.endswith("---"):
            return front_matter
        head = stripped[:-3].rstrip("\n")
        updated = head + "\n" + line + "\n---\n"
    # front matter 与正文之间统一保留一个空行
    return updated.rstrip("\n") + "\n\n"


_LAYOUT_LINE_RE = re.compile(r"^[ \t]*layout[ \t]*:.*$", re.MULTILINE)


def apply_layout(front_matter: str, layout: str) -> str:
    """强制注入或覆盖 layout 字段；已有则替换，没有则插到 front matter 第一行。"""
    line = "layout: %s" % layout
    if _LAYOUT_LINE_RE.search(front_matter):
        updated = _LAYOUT_LINE_RE.sub(lambda _match: line, front_matter, count=1)
    else:
        stripped = front_matter.rstrip("\n")
        if not stripped.startswith("---"):
            return front_matter
        body = stripped[3:]  # 形如 "\nslug: xxx\n---"
        updated = "---\n" + line + body
    # front matter 与正文之间统一保留一个空行
    return updated.rstrip("\n") + "\n\n"


def build_slug_map(sources: list[Path]) -> dict[str, str]:
    """建立「源文件名 / front matter title -> slug」的映射，用于重写 wikilink。"""
    mapping: dict[str, str] = {}
    for path in sources:
        front_matter, _ = split_front_matter(path.read_text(encoding="utf-8"))
        fields = read_front_matter_fields(front_matter)
        slug = fields.get("slug", "").strip()
        if not slug:
            continue  # 没有 slug 的笔记 URL 就是文件名本身，不需要映射
        for key in (path.stem, fields.get("title", "").strip()):
            if key:
                mapping.setdefault(key, slug)
    return mapping


def resolve_note_target(target: str, slug_map: dict[str, str]) -> str:
    """把 Obsidian 里的笔记名解析成 slug；找不到对应笔记时原样返回。"""
    candidates = [target]
    if target.endswith(".md"):
        candidates.append(target[:-3])
    if "/" in target:
        candidates.append(target.rsplit("/", 1)[-1])
    for candidate in candidates:
        candidate = candidate.strip()
        if candidate and candidate in slug_map:
            return slug_map[candidate]
    return target


# --------------------------------------------------------------------------- #
# 主流程
# --------------------------------------------------------------------------- #
def convert_document(
    text: str,
    stem: str,
    permalink: str,
    slug_map: dict[str, str],
    url_prefix: str,
) -> tuple[str, dict[str, int], bool]:
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
    body = convert_links(body, counts, slug_map, url_prefix)
    body = restore_code_blocks(body, code_blocks)

    added_front_matter = front_matter is None
    if added_front_matter:
        front_matter = build_front_matter(stem)
    # layout 必须存在：缺了它页面不会套用 _layouts/note.html，MathJax 就不会加载
    front_matter = apply_layout(front_matter, "note")
    front_matter = apply_permalink(front_matter, permalink)
    # permalink 已经保证 front matter 后面带一个空行，正文开头的空行去掉避免重复
    return front_matter + body.lstrip("\n"), counts, added_front_matter


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

    # 第一遍：收集 slug 映射，供第二遍重写 wikilink 时使用
    slug_map = build_slug_map(sources)

    # permalink 前缀跟随输出目录在仓库里的位置（默认 dest 是仓库根的 notes/ -> /notes/）
    try:
        url_prefix = "/" + dest.relative_to(ROOT).as_posix().strip("/") + "/"
    except ValueError:
        url_prefix = "/" + dest.name + "/"

    used_slugs: dict[str, Path] = {}
    for path in sources:
        relative = path.relative_to(src)
        text = path.read_text(encoding="utf-8")
        front_matter, _ = split_front_matter(text)
        fields = read_front_matter_fields(front_matter)

        slug = fields.get("slug", "").strip() or path.stem

        if slug in used_slugs:
            print(
                "[warn] slug 重复：%s 和 %s 都使用 %s，后写入的会覆盖前者"
                % (used_slugs[slug], relative, slug),
                file=sys.stderr,
            )
        used_slugs.setdefault(slug, relative)

        parent = "" if relative.parent == Path(".") else relative.parent.as_posix() + "/"
        permalink = url_prefix + parent + slug + "/"
        target = dest / relative.parent / (slug + ".md")
        target.parent.mkdir(parents=True, exist_ok=True)

        converted, counts, added = convert_document(
            text, path.stem, permalink, slug_map, url_prefix
        )
        target.write_text(converted, encoding="utf-8", newline="\n")
        print(
            "[ok] %s -> %s  (slug=%s, permalink=%s, callout=%d, math=%d, wikilink=%d, block_link=%d, block_id=%d, image=%d, front_matter=%s)"
            % (
                relative,
                target.name,
                slug,
                permalink,
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
