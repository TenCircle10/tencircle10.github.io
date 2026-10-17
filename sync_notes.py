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
2. **数学公式全量转义（只对行内 ``$...$``）**：先把公式整体抽成占位符（避免后续
   Markdown 规则误伤公式内容），再对**行内公式**的内容做转义，最后放回。转义表
   （都用负向断言 ``(?<!\\)`` 实现幂等，已经转义过的不会重复转义）：
   ``#`` -> ``\#``、``_`` -> ``\_``、``*`` -> ``\*``、``\{`` -> ``\\{``、``\}`` -> ``\\}``、
   ``|`` -> ``\mid``、``<`` -> ``\lt``、``>`` -> ``\gt``、``&`` -> ``\&``、``%`` -> ``\%``、
   ``~`` -> ``\sim``。
   原因：kramdown 只把 ``$$`` 当数学，单 ``$`` 的内容会**先按 Markdown 解析**，所以
   ``a*b`` 会变强调、``\{`` 会丢反斜杠、``<b>`` 会被当 HTML 标签。
   ``$$...$$`` 块级公式**保持原样不做任何转义**：kramdown 的数学引擎会把整段内容透传给
   MathJax，而块内 ``&`` 是矩阵对齐符、``_`` 是下标，加转义反而会把矩阵和下标记号弄坏。
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
6. **slug 自动生成与映射（决定输出文件名与 URL）**：front matter 里写了
   ``slug: math-analysis-szy`` 就直接用；没写的话把文件名用 ``pypinyin`` 转成拼音
   （``数学学习漫谈——Attention`` -> ``shu-xue-xue-xi-man-tan-attention``），
   非字母数字统一压成 ``-`` 并转小写；连拼音都为空（文件名全是 emoji）时，
   用正文 MD5 的前 6 位兜底。输出文件为 ``notes/<slug>.md``，并写入
   ``permalink: /notes/<slug>/``（源文件里已有的 permalink 会被覆盖）。
   front matter 里没有 ``title`` 时，自动用原文件名（中文）作为标题。
   正文里的 ``[[中文笔记名]]`` 会按「源文件名 / title -> slug」的映射重写成 slug URL，
   **自动生成的 slug 同样参与映射**，所以中文互链能正确指向 ``/notes/<拼音>/``；
   找不到对应笔记时保持原样，显示文本始终保留中文原名。
7. **Obsidian 扩展语法**：``%%隐藏注释%%`` 整段删除；``==高亮==`` -> ``<mark>``；
   ``- [ ]`` / ``- [x]`` -> ``- ☐`` / ``- ☑``；``#标签`` **原样保留**（不做标签系统）；
   ``:smile:`` 这类 emoji 短码换成字符；
   ``![[图片.png|300]]`` -> ``<img width="300">``（``|200x150`` 时同时给 height）；
   ``![[笔记]]``（非图片扩展名）-> ``*(嵌入笔记：笔记)*``；
   ``[[笔记#标题]]`` -> ``[笔记#标题](/notes/slug/#标题)``。
   块 ID 支持两种写法：独占一行的 ``^abc123``、以及行尾的 ``内容 ^abc123``
   （含 callout 标题里的 ``> [!note] 标题 ^abc123``），都转成 ``<a id="abc123"></a>``。
   ```dataview 查询块整块删除、```mermaid 块包成 ``<div class="mermaid">``，
   这两者与 ``` 代码块一样在「代码块保护」阶段处理，块内内容不会被其它规则改写。

````` 围起来的代码块（``` 或 ~~~）整体跳过，不做任何替换。

用法::

    python sync_notes.py                       # origin/ -> notes/
    python sync_notes.py --src other --dest out
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

try:
    from pypinyin import lazy_pinyin
except ImportError:  # 没装 pypinyin 时降级为「保留原文件名」，不中断同步
    lazy_pinyin = None

ROOT = Path(__file__).resolve().parent
DEFAULT_SRC = ROOT / "origin"
DEFAULT_DEST = ROOT / "notes"


# --------------------------------------------------------------------------- #
# 代码块保护：先整段抽出来，最后再原样放回，保证代码块里不做任何替换。
# dataview 查询块在 Obsidian 里也是代码块，直接整块删掉；mermaid 代码块转成
# <div class="mermaid"> 但同样走占位符，块内内容不会被后续规则改写。
# --------------------------------------------------------------------------- #
_CODE_PLACEHOLDER = "\x00SYNC_CODE_BLOCK_{}\x00"
_MERMAID_PLACEHOLDER = "\x00SYNC_MERMAID_{}\x00"
_FENCE_OPEN_RE = re.compile(r"^[ \t]*(`{3,}|~{3,})")
_DATAVIEW_SKIPPED = "<!-- Dataview query skipped -->"


def protect_code_blocks(
    text: str, counts: dict[str, int]
) -> tuple[str, list[str], list[str]]:
    """抽出 fenced code block，返回 (处理后的文本, 普通代码块, mermaid 代码块)。"""
    lines = text.split("\n")
    output: list[str] = []
    blocks: list[str] = []
    mermaid_blocks: list[str] = []
    index = 0
    while index < len(lines):
        match = _FENCE_OPEN_RE.match(lines[index])
        if not match:
            output.append(lines[index])
            index += 1
            continue
        fence = match.group(1)
        info = lines[index][match.end():].strip().lower()
        close_re = re.compile(
            r"^[ \t]*" + re.escape(fence[0]) + "{%d,}[ \t]*$" % len(fence)
        )
        start = index
        index += 1
        while index < len(lines) and not close_re.match(lines[index]):
            index += 1
        body_lines = lines[start + 1:index]
        if body_lines and close_re.match(body_lines[-1]):
            body_lines = body_lines[:-1]
        if index < len(lines):  # 吃掉结束 fence
            index += 1

        if info.startswith("dataview"):
            output.append(_DATAVIEW_SKIPPED)
            counts["extra"] += 1
        elif info.startswith("mermaid"):
            mermaid_blocks.append("\n".join(body_lines))
            output.append(_MERMAID_PLACEHOLDER.format(len(mermaid_blocks) - 1))
            counts["extra"] += 1
        else:
            blocks.append("\n".join(lines[start:index]))
            output.append(_CODE_PLACEHOLDER.format(len(blocks) - 1))
    return "\n".join(output), blocks, mermaid_blocks


def restore_code_blocks(
    text: str, blocks: list[str], mermaid_blocks: list[str]
) -> str:
    """把占位符还原成原始代码块 / mermaid div。"""
    for position, block in enumerate(blocks):
        text = text.replace(_CODE_PLACEHOLDER.format(position), block)
    for position, block in enumerate(mermaid_blocks):
        text = text.replace(
            _MERMAID_PLACEHOLDER.format(position),
            '<div class="mermaid">\n%s\n</div>' % block,
        )
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

        # 块 ID 优先绑定到 <details> 本身，这样锚点跳转能精确落在 callout 上，
        # 也才能被 CSS 的 scroll-margin-top 保护。来源有三种：标题行尾的 ID、
        # 正文行尾的 ID、以及紧跟 callout 之后独占一行的 ID（Obsidian 导出时最常见）。
        callout_id = ""
        title_block_id = _BLOCK_ID_TAIL_RE.search(title)
        if title_block_id:
            callout_id = title_block_id.group(1)
            title = title[: title_block_id.start()].strip()
        if not callout_id:
            for position, line in enumerate(body):
                body_block_id = _BLOCK_ID_TAIL_RE.search(line)
                if body_block_id:
                    callout_id = body_block_id.group(1)
                    body[position] = line[: body_block_id.start()].rstrip()
                    break
        if not callout_id and index < len(lines):
            following_block_id = _BLOCK_ID_RE.match(lines[index])
            if following_block_id:
                callout_id = following_block_id.group(1)
                index += 1  # 吞掉这一行，避免再输出一个多余的 <a id>
        if callout_id:
            counts["block_id"] += 1
        id_attr = ' id="%s"' % callout_id if callout_id else ""

        # Obsidian 里 [!note] 和 [!note]+ 都默认展开，只有 [!note]- 才是折叠
        open_attr = "" if fold == "-" else " open"
        counts["callout"] += 1
        output.append(
            '<details class="callout %s"%s data-callout="%s" markdown="block"%s>'
            % (callout_type, id_attr, callout_type, open_attr)
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
# 2. Obsidian 扩展语法（%%注释%%、==高亮==、待办、emoji、嵌入、标题链接、块 ID）
# --------------------------------------------------------------------------- #
_COMMENT_RE = re.compile(r"%%[\s\S]*?%%")
_HIGHLIGHT_RE = re.compile(r"==([^=\n]+?)==")
_TASK_EMPTY_RE = re.compile(r"^- \[ \] ", re.MULTILINE)
_TASK_DONE_RE = re.compile(r"^- \[[xX]\] ", re.MULTILINE)
# 行尾块 ID（Obsidian 块引用写法）："内容 ^abc123"。要求 ^ 前有空白、id 至少 4 位，
# 避免误伤公式里的上标（如 $x^2$）和 kramdown 的 ^上标^ 语法
_BLOCK_ID_TAIL_RE = re.compile(r"[ \t]+\^([A-Za-z0-9-]{4,})[ \t]*$", re.MULTILINE)
_BLOCK_HEADING_RE = re.compile(r"\[\[([^\]\|#]+)#([^\]\|]+)\]\]")
_EMBED_SIZED_RE = re.compile(r"!\[\[([^\]\|]+)\|(\d+)(?:x(\d+))?\]\]")
_EMBED_ANY_RE = re.compile(r"!\[\[([^\]]+?)\]\]")
_IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp", ".avif")
_EMOJI_MAP = {
    ":smile:": "😄",
    ":laughing:": "😆",
    ":joy:": "😂",
    ":heart:": "❤️",
    ":+1:": "👍",
    ":-1:": "👎",
    ":thumbsup:": "👍",
    ":rocket:": "🚀",
    ":warning:": "⚠️",
    ":bulb:": "💡",
    ":fire:": "🔥",
    ":star:": "⭐",
    ":check:": "✅",
    ":x:": "❌",
    ":tada:": "🎉",
    ":book:": "📖",
    ":pencil:": "📝",
    ":bug:": "🐛",
    ":eyes:": "👀",
    ":coffee:": "☕",
}


def strip_obsidian_comments(text: str, counts: dict[str, int]) -> str:
    """删除 Obsidian 的 %%隐藏注释%%（可跨行）。"""
    text, replaced = _COMMENT_RE.subn("", text)
    counts["extra"] += replaced
    return text


def convert_highlights(text: str, counts: dict[str, int]) -> str:
    """==高亮== -> <mark>高亮</mark>。"""
    text, replaced = _HIGHLIGHT_RE.subn(r"<mark>\1</mark>", text)
    counts["extra"] += replaced
    return text


def convert_tasks(text: str, counts: dict[str, int]) -> str:
    """- [ ] / - [x] -> - ☐ / - ☑。"""
    text, empty = _TASK_EMPTY_RE.subn("- ☐ ", text)
    text, done = _TASK_DONE_RE.subn("- ☑ ", text)
    counts["extra"] += empty + done
    return text


def convert_emoji(text: str, counts: dict[str, int]) -> str:
    """把 :smile: 这类常见 emoji 短码替换成字符。"""
    for token, emoji in _EMOJI_MAP.items():
        if token in text:
            counts["extra"] += text.count(token)
            text = text.replace(token, emoji)
    return text


def convert_block_heading_links(
    text: str, counts: dict[str, int], slug_map: dict[str, str], url_prefix: str
) -> str:
    """[[笔记#标题]] -> [笔记#标题](/notes/slug/#标题)。"""

    def replace(match: re.Match[str]) -> str:
        raw_target = match.group(1).strip()
        heading = match.group(2).strip()
        target = resolve_note_target(raw_target, slug_map)
        counts["extra"] += 1
        return "[%s#%s](%s%s/#%s)" % (raw_target, heading, url_prefix, target, heading)

    return _BLOCK_HEADING_RE.sub(replace, text)


def convert_embeds(text: str, counts: dict[str, int]) -> str:
    """处理 ![[...]]：带尺寸的图片 -> <img>，图片扩展名 -> Markdown 图片，其余当笔记嵌入。"""

    def sized(match: re.Match[str]) -> str:
        name = match.group(1).strip()
        width = match.group(2)
        height = match.group(3)
        counts["image"] += 1
        height_attr = ' height="%s"' % height if height else ""
        return '<img src="/assets/img/obsidian/%s" width="%s"%s />' % (
            name,
            width,
            height_attr,
        )

    def plain(match: re.Match[str]) -> str:
        target = match.group(1).strip()
        name = target.split("|", 1)[0].strip()
        if name.lower().endswith(_IMAGE_EXTS):
            counts["image"] += 1
            return "![%s](/assets/img/obsidian/%s)" % (name, name)
        counts["extra"] += 1
        return "*(嵌入笔记：%s)*" % name

    text = _EMBED_SIZED_RE.sub(sized, text)
    text = _EMBED_ANY_RE.sub(plain, text)
    return text


# --------------------------------------------------------------------------- #
# 3. 数学公式保护 + 全量转义
#    思路和代码块一致：先把公式抽成占位符，避免后续 Markdown 规则误伤公式内容；
#    只对**行内**公式内容做转义（$$ 块原样保留，原因见上）。
# --------------------------------------------------------------------------- #
_DISPLAY_MATH_RE = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
# 定界符前面不能是反斜杠或 $：排除 $ 是为了跳过 $$ 块，排除反斜杠是为了
# 避免 $$ 块里的 \$（例如 \$100）被当成行内公式的定界符——那会让正则跨过
# 整个 $$ 块去和后面正文里的 $ 配对，把真正的行内公式吃掉。
_INLINE_MATH_RE = re.compile(r"(?<![\\$])\$(?!\$)(.+?)(?<![\\$])\$(?!\$)", re.DOTALL)
_MATH_PLACEHOLDER = "\x00SYNC_MATH_{}\x00"

# 行内公式里会被 kramdown 抢先解释的字符 -> LaTeX 转义写法。
# 每条都用 (?<!\\) 做负向断言，保证对已经转义过的内容幂等。
_MATH_ESCAPE_RULES: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"(?<!\\)#"), r"\\#"),
    (re.compile(r"(?<!\\)_"), r"\\_"),
    (re.compile(r"(?<!\\)\*"), r"\\*"),
    (re.compile(r"(?<!\\)\\\{"), r"\\\\{"),
    (re.compile(r"(?<!\\)\\\}"), r"\\\\}"),
    # 下面四条会替换成字母命令（\mid \lt \gt \sim），必须补一个尾随空格；
    # 否则紧跟字母/数字时 TeX 会把它合并成 \midb、\ltc、\gtd 这类未定义命令。
    # 数学模式下空格本身被忽略，所以不会影响渲染间距。
    (re.compile(r"(?<!\\)\|"), r"\\mid "),
    (re.compile(r"(?<!\\)<"), r"\\lt "),
    (re.compile(r"(?<!\\)>"), r"\\gt "),
    (re.compile(r"(?<!\\)&"), r"\\&"),
    (re.compile(r"(?<!\\)%"), r"\\%"),
    (re.compile(r"(?<!\\)~"), r"\\sim "),
]


def escape_math_body(body: str) -> str:
    """转义单条行内公式内部的 kramdown 雷区字符（对已转义的内容幂等）。"""
    for pattern, replacement in _MATH_ESCAPE_RULES:
        body = pattern.sub(replacement, body)
    return body


def protect_math(text: str, counts: dict[str, int]) -> tuple[str, list[str]]:
    """抽出数学公式，返回 (处理后的文本, 公式列表)。

    - ``$$...$$`` 块：原样抽出。kramdown 的 math engine 会把整段内容透传给 MathJax，
      块内的 ``&`` 是矩阵对齐符、``_`` 是下标，加转义会破坏它们。
    - ``$...$`` 行内：抽出前先做全量转义，因为 kramdown 会先按 Markdown 解析它。
    """
    formulas: list[str] = []

    def stash(raw: str) -> str:
        formulas.append(raw)
        return _MATH_PLACEHOLDER.format(len(formulas) - 1)

    def display(match: re.Match[str]) -> str:
        counts["math"] += 1
        return stash("$$" + match.group(1) + "$$")

    def inline(match: re.Match[str]) -> str:
        counts["math"] += 1
        return stash("$" + escape_math_body(match.group(1)) + "$")

    text = _DISPLAY_MATH_RE.sub(display, text)
    text = _INLINE_MATH_RE.sub(inline, text)
    return text, formulas


def restore_math(text: str, formulas: list[str]) -> str:
    """把公式占位符还原成公式原文。"""
    for position, formula in enumerate(formulas):
        text = text.replace(_MATH_PLACEHOLDER.format(position), formula)
    return text


# --------------------------------------------------------------------------- #
# 4. Wikilink 与块 ID（图片 / 笔记嵌入已由 convert_embeds 处理完）
# --------------------------------------------------------------------------- #
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
    """转换 wikilink 与块 ID（![[...]] 形式的图片与嵌入由 convert_embeds 处理）。"""

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

    def block_id_tail(match: re.Match[str]) -> str:
        counts["block_id"] += 1
        return ' <a id="%s"></a>' % match.group(1)

    text = _BLOCK_LINK_RE.sub(block_link, text)
    text = _ALIAS_LINK_RE.sub(alias_link, text)
    text = _PLAIN_LINK_RE.sub(plain_link, text)
    # 先处理行尾块 ID（"内容 ^abc123"），再处理独占一行的块 ID
    text = _BLOCK_ID_TAIL_RE.sub(block_id_tail, text)
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


_TITLE_LINE_RE = re.compile(r"^[ \t]*title[ \t]*:.*$", re.MULTILINE)
_SLUG_LINE_RE = re.compile(r"^[ \t]*slug[ \t]*:.*$", re.MULTILINE)


def make_slug(stem: str, content: str = "") -> str:
    """把（中文）文件名转成 URL 友好的 slug。

    例：``数学学习漫谈——Attention is all you need`` ->
    ``shu-xue-xue-xi-man-tan-attention-is-all-you-need``。
    转换后若为空（文件名全是 emoji / 符号），用正文 MD5 前 6 位兜底。
    """
    if lazy_pinyin is not None:
        candidate = "-".join(lazy_pinyin(stem))
    else:
        candidate = stem
    # 统一：所有非 a-z0-9 的字符（中文残留、空格、破折号、标点）压成一个 -
    slug = re.sub(r"[^a-z0-9]+", "-", candidate.lower()).strip("-")
    if not slug:
        digest = hashlib.md5(content.encode("utf-8")).hexdigest()
        slug = "note-" + digest[:6]
    return slug


def apply_title(front_matter: str, title: str) -> str:
    """front matter 里没有 title 时补一个（已有 title 则原样保留）。"""
    if _TITLE_LINE_RE.search(front_matter):
        return front_matter
    safe_title = title.replace("\\", "\\\\").replace('"', '\\"')
    stripped = front_matter.rstrip("\n")
    if not stripped.endswith("---"):
        return front_matter
    head = stripped[:-3].rstrip("\n")
    updated = head + '\ntitle: "%s"\n---\n' % safe_title
    # front matter 与正文之间统一保留一个空行
    return updated.rstrip("\n") + "\n\n"


def apply_slug(front_matter: str, slug: str) -> str:
    """front matter 里没有 slug 时把（自动生成的）slug 写进去；已有则保留原值。"""
    if _SLUG_LINE_RE.search(front_matter):
        return front_matter
    stripped = front_matter.rstrip("\n")
    if not stripped.endswith("---"):
        return front_matter
    head = stripped[:-3].rstrip("\n")
    updated = head + '\nslug: "%s"\n---\n' % slug
    # front matter 与正文之间统一保留一个空行
    return updated.rstrip("\n") + "\n\n"


def build_slug_map(sources: list[Path]) -> dict[str, str]:
    """建立「源文件名 / front matter title -> slug」的映射，用于重写 wikilink。

    没有显式 slug 的笔记也会用 make_slug() 自动生成一个，所以中文互链
    （``[[中文笔记名]]``）能正确指向 ``/notes/<拼音>/``。
    """
    mapping: dict[str, str] = {}
    for path in sources:
        text = path.read_text(encoding="utf-8")
        front_matter, _ = split_front_matter(text)
        fields = read_front_matter_fields(front_matter)
        slug = fields.get("slug", "").strip() or make_slug(path.stem, text)
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
    slug: str,
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
        "extra": 0,
    }
    front_matter, body = split_front_matter(text)

    # 流水线顺序（保护优先，替换其次）：
    #   1. 代码块（含 dataview / mermaid）抽成占位符 —— 最高优先级
    #   2. 数学公式抽成占位符（行内公式在抽取时同时完成全量转义）
    #   3. 其余 Obsidian / Markdown 语法都在占位符之外处理
    #   4. 还原公式 -> 压缩空行 -> 还原代码块
    body, code_blocks, mermaid_blocks = protect_code_blocks(body, counts)
    body, formulas = protect_math(body, counts)
    body = convert_callouts(body, counts)
    body = strip_obsidian_comments(body, counts)
    body = convert_highlights(body, counts)
    body = convert_embeds(body, counts)
    body = convert_block_heading_links(body, counts, slug_map, url_prefix)
    body = convert_tasks(body, counts)
    body = convert_emoji(body, counts)
    body = convert_links(body, counts, slug_map, url_prefix)
    # %% 注释整段删除后会留下多个连续空行，压缩成一个（此时公式还是占位符，
    # 所以不会影响 $$ 块内部原有的空行）
    body = re.sub(r"\n{3,}", "\n\n", body)
    body = restore_math(body, formulas)
    body = restore_code_blocks(body, code_blocks, mermaid_blocks)

    added_front_matter = front_matter is None
    if added_front_matter:
        front_matter = build_front_matter(stem)
    # layout 必须存在：缺了它页面不会套用 _layouts/note.html，MathJax 就不会加载
    front_matter = apply_layout(front_matter, "note")
    # front matter 里没有 title 时，用原文件名（中文）当标题
    front_matter = apply_title(front_matter, stem)
    # front matter 里没有 slug 时，把自动生成的（拼音）slug 写进去
    front_matter = apply_slug(front_matter, slug)
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

        # 没写 slug 时自动用拼音生成（中文文件名 -> shu-xue-...）
        slug = fields.get("slug", "").strip() or make_slug(path.stem, text)

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
            text, path.stem, slug, permalink, slug_map, url_prefix
        )
        target.write_text(converted, encoding="utf-8", newline="\n")
        print(
            "[ok] %s -> %s  (slug=%s, permalink=%s, callout=%d, math=%d, wikilink=%d, block_link=%d, block_id=%d, image=%d, obsidian=%d, front_matter=%s)"
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
                counts["extra"],
                "generated" if added else "kept",
            )
        )

    print("[done] 共处理 %d 个文件，输出目录：%s" % (len(sources), dest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
