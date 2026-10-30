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
   但 ``\\``（行分隔符）会**先翻倍成 ``\\\\``**：kramdown 的 BackslashEscapes 会把 ``\\``
   还原成单个 ``\``，导致矩阵 / 数组的换行消失、被压平成一行；翻倍后 kramdown 成对还原，
   仍是 ``\\``。行内公式同理也做了翻倍。
   另外两点块级处理：``\[...\]`` 会先统一替换成 ``$$...$$``；块级公式（独占整行或内容跨行）
   **前后各强制补一个换行**，否则 kramdown 会把它和上下段落合进同一个段落，
   导致公式错位、不居中（多余的空行稍后会被压缩成一个）。
3. **Obsidian 内部链接**：
   ``[[笔记]]`` -> ``[笔记](/notes/笔记/)``；
   ``[[笔记|文本]]`` -> ``[文本](/notes/笔记/)``；
   ``[[#^块ID|文本]]`` -> ``[文本](#块ID)``（同页）；
   ``[[笔记名#^块ID|文本]]`` -> ``[文本](/notes/笔记拼音/#块ID)``（跨页）；
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
8. **排版清洗与容错**：漏打空格的 ``##标题`` 自动补成 ``## 标题``（单个 ``#标签`` 不动，
   以免把标签变成 H1）；标题 / 引用块 / 列表首项 / 水平线 / 独占整行的链接上方强制留空行；
   链接文字里的 ``|`` -> ``｜``、``*`` -> ``\*``、``_`` -> ``\_``，``[]()`` 删除、
   ``[文字]()`` 退化成纯文字；``$ x $`` 去掉两端空格（MathJax 不认紧贴空格的定界符）；
   ``$$$$`` 归一成空块级公式；公式里的 HTML 实体（&lt; &gt; &amp;）还原成符号；
   嵌套 callout 只告警、不转换；front matter 没闭合时按正文处理；
   正文为空或单篇转换抛异常时只跳过该篇并告警，不会拖垮整站。

````` 围起来的代码块（``` 或 ~~~）整体跳过，不做任何替换。

**分仓（可见性）**：源目录按子文件夹分仓，决定笔记是否出现在主页列表里::

    origin/public/   ->  front matter 写 public: true   ->  出现在主页笔记列表
    origin/hidden/   ->  front matter 写 public: false  ->  不出现在主页列表
                                                    （但 URL 仍可直接访问）

两个仓共享同一套 slug / 双链映射，跨仓互链照常工作；输出路径基于「仓内相对
路径」，所以把笔记移进 public/ 不会改变既有 URL。

用法::

    python sync_notes.py                       # origin/{public,hidden}/ -> notes/
    python sync_notes.py --src other --dest out
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import sys
from pathlib import Path

try:
    from pypinyin import lazy_pinyin
except ImportError:  # 没装 pypinyin 时降级为「保留原文件名」，不中断同步
    lazy_pinyin = None
else:
    # 若安装了 pypinyin-dict，加载扩充词典（汉典大字词典 + 大词组词典），
    # 改善多音字 / 异读字 / 词组的拼音准确度，例如：
    #   重数 -> chóngshù、会计 -> kuàijì、银行 -> yínháng、奇数 -> jīshù。
    # 不装也不影响运行，仅降级为 pypinyin 自带词典（slug 仍可生成）。
    try:
        from pypinyin_dict.pinyin_data import zdic
        from pypinyin_dict.phrase_pinyin_data import large_pinyin
        zdic.load()
        large_pinyin.load()
    except Exception:
        pass

ROOT = Path(__file__).resolve().parent
DEFAULT_SRC = ROOT / "origin"
DEFAULT_DEST = ROOT / "notes"


# --------------------------------------------------------------------------- #
# 分仓（visibility bucket）
# --------------------------------------------------------------------------- #
# 源笔记按所在子目录决定「是否出现在主页笔记列表」：
#   origin/public/  -> front matter 写 public: true  -> 出现在主页列表
#   origin/hidden/  -> front matter 写 public: false -> 不出现在主页列表
#                                               （但 URL 仍可直接访问，不是密码保护）
#   origin/ 根目录下散落的 .md（历史遗留）-> 按 public 处理，保持向后兼容。
#
# 两个仓共享同一套 slug / 双链映射，所以 public 里的笔记可以用 [[双链]]
# 指向 hidden 里的笔记，反之亦然。
BUCKET_PUBLIC = "public"
BUCKET_HIDDEN = "hidden"
BUCKET_NAMES = (BUCKET_PUBLIC, BUCKET_HIDDEN)
DEFAULT_BUCKET = BUCKET_PUBLIC


# --------------------------------------------------------------------------- #
# 代码块保护：先整段抽出来，最后再原样放回，保证代码块里不做任何替换。
# dataview 查询块在 Obsidian 里也是代码块，直接整块删掉；mermaid 代码块转成
# <div class="mermaid"> 但同样走占位符，块内内容不会被后续规则改写。
# --------------------------------------------------------------------------- #
_CODE_PLACEHOLDER = "\x00SYNC_CODE_BLOCK_{}\x00"
_MERMAID_PLACEHOLDER = "\x00SYNC_MERMAID_{}\x00"
_FENCE_OPEN_RE = re.compile(r"^[ \t]*(`{3,}|~{3,})")
# 行内代码：`code` 或 ``co`de``（反引号数量必须配对，且不跨行）
_INLINE_CODE_RE = re.compile(r"(`+)([^\n]+?)\1")
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

    text = "\n".join(output)

    # 行内代码（`code` / ``code``）也一并保护起来，内部绝不执行任何替换
    def stash_inline_code(match: re.Match[str]) -> str:
        blocks.append(match.group(0))
        return _CODE_PLACEHOLDER.format(len(blocks) - 1)

    text = _INLINE_CODE_RE.sub(stash_inline_code, text)
    return text, blocks, mermaid_blocks


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
_CALLOUT_HEAD_RE = re.compile(
    r"^[ \t]*>[ \t]*\[!([A-Za-z0-9_-]+(?:[ \t]+[A-Za-z0-9_-]+)*)\]([+-]?)[ \t]*(.*)$"
)
_QUOTE_LINE_RE = re.compile(r"^[ \t]*>(?:[ \t]?(.*))?$")


_NESTED_CALLOUT_RE = re.compile(r"^[ \t]*>[ \t]*>[ \t]*\[!", re.MULTILINE)


def convert_callouts(text: str, counts: dict[str, int]) -> str:
    """把 Obsidian callout 引用块转成 <details class="callout ..."> 结构。

    嵌套 callout（``> > [!note]``）暂不支持：只打印警告并保持原样（退化成普通引用块），
    避免生成未闭合的 ``<details>`` 把整页 DOM 弄坏。
    """
    if _NESTED_CALLOUT_RE.search(text):
        print(
            "  [warn] 检测到嵌套 callout（> > [!type]），暂不支持，已降级为普通引用块",
            file=sys.stderr,
        )
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
        # 注意：markdown="block" 只加在 <div class="callout-content"> 上，绝不能加在 <details> 上。
        # 一旦加在 <details> 上，kramdown 会把整个 details 的内容按块级 Markdown 解析，
        # 而 <summary> 不属于它认识的块级 HTML 标签，会被当作普通文本 → 标签直接暴露成字面量。
        output.append(
            '<details class="callout %s"%s data-callout="%s"%s>'
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
# 跨页块引用：[[笔记名#^块ID]] / [[笔记名#^块ID|别名]]
#
# 【为什么必须单独一条正则】—— 上面那四条 wikilink 正则全都漏掉了这个组合：
#   · _BLOCK_LINK_RE      只匹配同页的 [[#^id|text]]
#   · _ALIAS_LINK_RE      笔记名部分 [^\]\|#^]+ 显式排除了 # 和 ^
#   · _PLAIN_LINK_RE      同上
#   · _BLOCK_HEADING_RE   标题部分 [^\]\|]+ 排斥 |，带别名时匹配不上
# 结果就是 [[数学分析笔记#^derivative-rules|四则与链式]] 原样漏到页面上。
#
# 【顺序要求】必须在 _BLOCK_HEADING_RE 之前处理：不带别名的 [[笔记名#^块ID]]
# 会被标题规则当成「笔记名#标题」，生成指向 #^块ID 的死锚点（真实锚点没有 ^）。
_CROSS_BLOCK_LINK_RE = re.compile(
    r"\[\[([^\]\|#]+)#\^([A-Za-z0-9-]+)(?:\|([^\]\|]+))?\]\]"
)
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


def convert_cross_block_links(
    text: str, counts: dict[str, int], slug_map: dict[str, str], url_prefix: str
) -> str:
    """跨页块引用：``[[笔记名#^块ID|别名]]`` -> ``[别名](/notes/slug/#块ID)``。

    这类写法之前没有任何正则覆盖：``_BLOCK_LINK_RE`` 只管同页的 ``[[#^id]]``，
    而 ``_ALIAS_LINK_RE`` / ``_PLAIN_LINK_RE`` 的笔记名部分显式排除了 ``#`` 和 ``^``，
    ``_BLOCK_HEADING_RE`` 的标题部分又排斥 ``|`` —— 于是
    ``[[数学分析笔记#^derivative-rules|四则与链式]]`` 原样漏到页面上。

    块 ID 在目标页里是 ``<a id="块ID"></a>``（没有 ``^``），所以锚点写 ``#块ID``。
    """

    def replace(match: re.Match[str]) -> str:
        raw_target = match.group(1).strip()
        block_id = match.group(2).strip()
        alias = match.group(3)
        label = (alias or "").strip() or ("%s (块引用)" % raw_target)
        target = resolve_note_target(raw_target, slug_map)
        if target == raw_target:
            # 目标笔记不在 origin/ 里：退化处理 —— 仍然输出成链接（指向未生成的页面），
            # 避免又出现「裸 [[...]] 漏到页面上」，但打印告警便于补源文件。
            print(
                "  [warn] 跨页块引用指向不存在的笔记：%s#^%s" % (raw_target, block_id),
                file=sys.stderr,
            )
        counts["block_link"] += 1
        url = "%s%s/#%s" % (url_prefix, target, block_id)
        # label 里含公式时改用原生 <a>：kramdown 对 [文本](url) 的 label 会做额外处理，
        # 里面的 $...$ 经常渲染不出来。注意此时公式已被 protect_math 抽成
        # ZMATHPHnZ 占位符，所以两种形式都要判断。
        if "$" in label or "ZMATHPH" in label:
            return '<a href="%s">%s</a>' % (url, label)
        return "[%s](%s)" % (label, url)

    return _CROSS_BLOCK_LINK_RE.sub(replace, text)


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
# 数学定界符统一：\(...\) -> $...$、\[...\] -> $$...$$
# （kramdown 会把 \( 和 \[ 当成转义符吃掉，所以必须先归一化）
_PAREN_INLINE_RE = re.compile(r"\\\((.+?)\\\)", re.DOTALL)
_BRACKET_DISPLAY_RE = re.compile(r"\\\[(.+?)\\\]", re.DOTALL)
_DISPLAY_MATH_RE = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
# 定界符前面不能是反斜杠或 $：排除 $ 是为了跳过 $$ 块，排除反斜杠是为了
# 避免 $$ 块里的 \$（例如 \$100）被当成行内公式的定界符——那会让正则跨过
# 整个 $$ 块去和后面正文里的 $ 配对，把真正的行内公式吃掉。
_INLINE_MATH_RE = re.compile(r"(?<![\\$])\$(?!\$)(.+?)(?<![\\$])\$(?!\$)", re.DOTALL)
# 占位符必须【纯字母数字】，不能含下划线、\x00 等特殊字符。
# 历史教训（2026-10）：原来用 "\x00SYNC_MATH_{}\x00"，结果 wikilink 里的公式
#   [[#^e-series|$e$ 的级数表示]]
# 被 protect_math 换成 "\x00SYNC_MATH_440\x00" 后，clean_link_text 的
#   label.replace("_", "\\_")
# 把占位符里的下划线转义成 "\_"，restore_math 就再也匹配不上，
# 页面上直接漏出 "SYNC\_MATH\_440"。改成纯字母数字后，任何字符级清洗都动不了它。
_MATH_PLACEHOLDER = "ZMATHPH{}Z"


# 块级公式（$$...$$）只做一件事：把尖括号换成 \lt{} / \gt{}。
# 其它字符（_ # & * % | ~）全部原样透传 —— 数学里它们都有语义，
# 而且 _ 换成 &#95; 之后，实体里的 & 会被 MathJax 误当对齐符，直接报 Misplaced &。
# \left< / \right> 里的尖括号是合法定界符，必须排除。
_DISPLAY_LTGT_RULES: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"(?<!\\left)(?<!\\right)(?<!\\)<"), r"\\lt{}"),
    (re.compile(r"(?<!\\left)(?<!\\right)(?<!\\)>"), r"\\gt{}"),
]


# 行内公式里会被 kramdown 抢先解释的字符 -> LaTeX 转义写法。
# 每条都用 (?<!\\) 做负向断言，保证对已经转义过的内容幂等。
#
# 2026-10 修正（线上报过 "Missing or unrecognized delimiter for \left"）：
#   · ``_`` 用 **HTML 实体** ``&#95;`` 而不是 ``\_``：
#       ``\_`` 是「字面下划线」，会把下标 p_n 变成 p\_n（n 不再是下标）；
#       而完全不转义又会被 Markdown 当成斜体（实测 x'_{lj} = ... b_{lk} 会命中：
#       开始 _ 前面是 ' ，结束 _ 后面是 { ，两侧都不是字母数字，边界成立）。
#       ``&#95;`` 两边都满足：kramdown 看到实体不认作强调，浏览器解码后 MathJax 拿到的仍是 _。
#   · ``*`` 同理用 ``&#42;``（``\*`` 在 LaTeX 里不是合法命令，会直接报错）。
#   · ``\{`` / ``\}`` 改写成 ``\lbrace`` / ``\rbrace``。原来的 ``\\{`` 里 ``\\`` 是换行，
#     会把 \left\{ 拆成「\left + 换行 + {」，MathJax 就报「找不到定界符」。
#     \lbrace / \rbrace 是合法命令，\left\lbrace … \right\rbrace 也完全合法。
#   · ``|`` 改写成 ``\vert``（原来是 ``\mid``）。\left| 被改成 \left\mid 后
#     \mid 不是 \left 的合法定界符，同样会报错；\left\vert 才是对的。
#   · ``<`` / ``>`` 在 \left、\right 后面不转义：\left< 是合法定界符，
#     转成 \left\lt 反而非法。用定长负向后顾排除这两种情况。
def _needs_terminator(text: str, end: int) -> bool:
    """紧跟在定界符命令后面的是不是 ASCII 字母。

    是的话必须补一个空分组 ``{}`` 把命令名切断 ——
    MathJax 的 GetCS() 正则是 ``/^(([a-z]+) ?|...)/i``，**只吃 ASCII 字母**，
    所以 ``\\vertx`` 会被读成一个未定义命令 ``\\vertx``，``\\left`` 就拿不到
    定界符，抛 "Missing or unrecognized delimiter for \\left"。

    不是字母（空格 / ``{`` / ``(`` / ``_`` / ``\\`` / 非 ASCII 字符等）时
    GetCS 会自己停下来，命令名不会被连读 —— 这时**不要**补 ``{}``，
    以免改变原有排版（例如 ``\\big\\vert_{x=x_0}`` 里下标挂载的位置）。
    """
    return end < len(text) and text[end].isascii() and text[end].isalpha()


def _make_delim_repl(prefix: str, delim: str):
    """生成定界符替换函数：``\\left|`` -> ``\\left\\vert``（必要时补 ``{}``）。"""

    def repl(match: re.Match[str]) -> str:
        suffix = "{}" if _needs_terminator(match.string, match.end()) else ""
        return prefix + "\\" + delim + suffix

    return repl


def _size_vert(match: re.Match[str]) -> str:
    r"""``\big|`` -> ``\big\vert``（保留尺寸命令与 l/r/m 变体）。

    末尾的 ``{}`` 只在「后面紧跟 ASCII 字母」时才补 —— 那时候命令名会被
    MathJax 连读成 ``\big\vertx``，定界符就废了。其余情况保持原样。
    """
    suffix = "{}" if _needs_terminator(match.string, match.end()) else ""
    return "\\" + match.group(1) + match.group(2) + "\\vert" + suffix


def _size_Vert(match: re.Match[str]) -> str:
    r"""``\big\|`` -> ``\big\Vert``。"""
    suffix = "{}" if _needs_terminator(match.string, match.end()) else ""
    return "\\" + match.group(1) + match.group(2) + "\\Vert" + suffix


# 匹配 LaTeX 环境（matrix / pmatrix / bmatrix / array / cases / align ...），用于保护
# 环境内部的 |（数组列分隔符 \begin{array}{|c|c|}）不被当成裸竖线换成 \mid。
_BEGIN_ENV_RE = re.compile(r"\\begin\{([a-zA-Z*]+)\}.*?\\end\{\1\}", re.DOTALL)


def _protect_env_pipes(body: str) -> str:
    r"""把 LaTeX 环境内部的 | 临时替换为占位符，避免被 \mid{} 规则误伤。"""

    def repl(match: re.Match[str]) -> str:
        return match.group(0).replace("|", "\x00ENVPIPE\x00")

    return _BEGIN_ENV_RE.sub(repl, body)


_MATH_ESCAPE_RULES: list[tuple[re.Pattern[str], "str | Callable[[re.Match[str]], str]"]] = [
    (re.compile(r"(?<!\\)#"), r"\\#"),
    # 转成 \lbrace{} / \rbrace{}（带空分组），避免 \lbrace 这类【多字母命令】
    # 紧跟字母时被 LaTeX 读成非法命令（\{a_1 -> \lbracea_1 -> \lbracea 未定义 -> 整条公式报红）。
    # 空分组 {} 不可见，不影响渲染。
    (re.compile(r"(?<!\\)\\\{"), r"\\lbrace{}"),
    (re.compile(r"(?<!\\)\\\}"), r"\\rbrace{}"),
    # 用 HTML 实体代替 LaTeX 转义，但【只在真会触发 Markdown 强调的位置】替换：
    # Markdown 的 _ 强调要求开始 _ 左侧不是字母数字。所以
    #   a_1 / A_n / p_n      → 左侧是字母，不会触发强调，保持原样（MathJax 正常渲染下标）
    #   x'_{lj} / )_{m×n}    → 左侧是标点，会触发强调，必须换成实体
    # 这样既挡住斜体，又不让生成物里塞满无意义的实体。
    (re.compile(r"(?<![A-Za-z0-9\\])_"), r"&#95;"),
    (re.compile(r"(?<![A-Za-z0-9\\\s])\*"), r"&#42;"),
    # 定界符优先处理：【行内公式里绝对不能留裸 |】
    # kramdown 会把行内公式里的 | 当成表格列分隔符，直接把这一行切断，
    # 导致定界符失效、后半段公式漏成源码。\left| / \right| / \left\| / \right\| 里的竖线
    # 虽然 LaTeX 合法，但对 kramdown 来说仍是裸的 |，所以要一起换掉。
    #
    # 【为什么有时要补 {}】—— 这是线上 "Missing or unrecognized delimiter for \left"
    # 的根因（2026-10 线上复发）。MathJax v3 取定界符的代码是：
    #     var r = this.GetNext();            // 取一个字符
    #     if (r === "\\") r += this.GetCS();  // 反斜杠 -> 再取一个【控制序列】
    #     if (!this.contains("delimiter", r)) throw MissingOrUnrecognizedDelim;
    # 而 GetCS() 的正则是 /^(([a-z]+) ?|...)/i —— **只吃 ASCII 字母**。于是
    #     \left|x_0   ->  \left\vertx_0
    # 控制序列被读成 "vertx"（一个未定义命令），contains("delimiter","vertx") 为假，
    # \left 拿不到定界符，整条公式直接报错。
    # 修法是给命令补一个空分组 {} 把命令名切断：
    #     \left\vert{}x_0   ->  定界符是 \vert（合法），{} 是空分组，视觉零差别
    # 但**只在后面紧跟 ASCII 字母时才补**（见 _needs_terminator），
    # 其余情况保持原样，避免改变既有排版。
    (re.compile(r"\\left\\\|"), _make_delim_repl("\\left", "Vert")),
    (re.compile(r"\\right\\\|"), _make_delim_repl("\\right", "Vert")),
    (re.compile(r"\\left\|"), _make_delim_repl("\\left", "vert")),
    (re.compile(r"\\right\|"), _make_delim_repl("\\right", "vert")),
    # \middle 后面也必须跟合法定界符（\middle 是 AMS 的对称定界符命令）
    (re.compile(r"\\middle\\\|"), _make_delim_repl("\\middle", "Vert")),
    (re.compile(r"\\middle\|"), _make_delim_repl("\\middle", "vert")),
    # 尺寸命令 + 竖线：\big| \Big| \bigg| \Bigg|（含 l/r/m 变体 \bigl| \bigm| \bigr| …）
    # 必须换成 \vert（双竖线换成 \Vert），绝不能留裸 |（kramdown 当表格列分隔符），
    # 也不能换成 \mid（\mid 不在 MathJax 的定界符表里，会报
    # "Missing or unrecognized delimiter for \big"）。同样要补 {} 切断命令名。
    (re.compile(r"\\(big|Big|bigg|Bigg)([lrm]?)\|"), _size_vert),
    (re.compile(r"\\(big|Big|bigg|Bigg)([lrm]?)\\\|"), _size_Vert),
    # 剩下的：独立的 \| 是范数 -> \Vert{}；裸 | -> \mid{}（环境内部的 | 见 escape_math_body 的保护）
    # \mid{} 只出现在「没有跟着 \left/\right/\middle/\big」的位置，
    # 而 \mid 不是合法定界符，所以它绝不会落到 \left 后面（enforce_math_delimiters 兜底）。
    (re.compile(r"\\\|"), r"\\Vert{}"),
    (re.compile(r"(?<!\\)\|"), r"\\mid{}"),
    # 下面三条会替换成字母命令，用 {} 结尾而不是空格：
    #   \lt{} \gt{} \sim{}
    # 这样后面紧跟字母/数字时不会被当成更长的命令（\ltepsilon），
    # 也不会和原文里的空格叠加出双空格。
    # \left< / \right> / \left> / \right< 里的符号是定界符，必须原样保留。
    (re.compile(r"(?<!\\left)(?<!\\right)(?<!\\)<"), r"\\lt{}"),
    (re.compile(r"(?<!\\left)(?<!\\right)(?<!\\)>"), r"\\gt{}"),
    (re.compile(r"(?<!\\)%"), r"\\%"),
    (re.compile(r"(?<!\\)~"), r"\\sim{}"),
    # 边界守卫：兜底处理【源文件里直接写了 \lbrace / \rbrace】（例如外来 OCR 文本）、
    # 且后面紧接字母/数字的情况。\{ -> \lbrace{} 已覆盖转换出来的情形；这里再兜一层，
    # 把 \lbraceX / \rbraceX 修成 \lbrace{}X / \rbrace{}X，避免被读成非法命令 \lbraceX。
    (re.compile(r"(?<!\\)\\(lbrace|rbrace)(?=[A-Za-z0-9])"), lambda m: "\\" + m.group(1) + "{}"),
]


# --------------------------------------------------------------------------- #
# \left / \right 定界符兜底校验
# --------------------------------------------------------------------------- #
# 上面那批替换规则解决的是「竖线被 kramdown 当成表格列分隔符」，
# 但定界符本身还有两道坎，这里用与 MathJax 完全一致的规则做兜底：
#
#   1) 定界符命令（\vert / \Vert / \lbrace …）后面紧跟字母时，命令名会被连读
#      （GetCS 只吃连续字母），必须补空分组 {} 切断；
#   2) \left / \right / \middle 后面跟的必须是 MathJax 认得的定界符，
#      取不到就会抛 "Missing or unrecognized delimiter for \left"，整条公式报废。
#
# 合法定界符全集来自 MathJax v3 的 DelimiterMap（tex-chtml.js）：
#   "(": ")"  "[" "]"  "<" ">"  "/"  "|"  "."  "\\"  "\|"  "\vert"  "\Vert"
#   "\{"  "\}"  "\lbrace"  "\rbrace"  "\lbrack"  "\rbrack"  "\langle"  "\rangle"
#   "\lceil" "\rceil" "\lfloor" "\rfloor" "\uparrow" "\downarrow" "\updownarrow"
#   "\Uparrow" "\Downarrow" "\Updownarrow" "\backslash" "\lt" "\gt"
#   "\lmoustache" "\rmoustache" "\lgroup" "\rgroup"
#   "\arrowvert" "\Arrowvert" "\bracevert"
# 注意：\mid 不在里面 —— 它只能当关系符用，放在 \left 后面一定报错。
_MATHJAX_DELIMITERS = frozenset(
    {
        "(", ")", "[", "]", "<", ">", "/", "|", ".",
        "\\\\", "\\|", "\\vert", "\\Vert",
        "\\{", "\\}", "\\lbrace", "\\rbrace",
        "\\lbrack", "\\rbrack", "\\langle", "\\rangle",
        "\\lceil", "\\rceil", "\\lfloor", "\\rfloor",
        "\\uparrow", "\\downarrow", "\\updownarrow",
        "\\Uparrow", "\\Downarrow", "\\Updownarrow",
        "\\backslash", "\\lt", "\\gt",
        "\\lmoustache", "\\rmoustache", "\\lgroup", "\\rgroup",
        "\\arrowvert", "\\Arrowvert", "\\bracevert",
    }
)

# 需要跟定界符的「命令位置」：\left \right \middle \big 家族（含 l/r/m 变体）
_DELIM_CMD_RE = re.compile(r"\\(?:left|right|middle|big|Big|bigg|Bigg)[lrm]?\b")
# 控制序列名：反斜杠 + 连续字母（与 MathJax 的 GetCS 行为一致）
_CS_NAME_RE = re.compile(r"\\([a-zA-Z]+)")


def _read_delimiter(text: str, index: int) -> tuple[str | None, int]:
    r"""模拟 MathJax v3 的 GetDelimiter()：从 text[index] 起读取一个定界符 token。

    与 MathJax 的行为严格对齐：
      · 前导空白会被跳过（GetNext 会跳过空格）；
      · 单个字符直接作为候选定界符；
      · 反斜杠 + 连续字母构成控制序列（GetCS 只吃字母）；
        ``\{`` 这种「反斜杠 + 非字母」只吃一个字符（MathJax 的 GetCS 正则第三支）。

    返回 (token, token 的结束位置)；token 为 None 表示此处取不到定界符。
    """
    while index < len(text) and text[index].isspace():
        index += 1
    if index >= len(text):
        return None, index
    if text[index] != "\\":
        return text[index], index + 1
    match = _CS_NAME_RE.match(text, index)
    if match:
        return match.group(0), match.end()
    if index + 1 < len(text):
        return text[index:index + 2], index + 2
    return None, index


def enforce_math_delimiters(body: str) -> tuple[str, list[str]]:
    """保证 \\left / \\right / \\middle / \\big 后面一定跟着 MathJax 认得的定界符。

    这是转义规则之外的**最后一道兜底**：
      · 多字母定界符命令后面紧跟字母 -> 补空分组 ``{}`` 切断命令名
        （``\\left\\vertx`` -> ``\\left\\vert{}x``），修掉粘连；
      · 定界符位置出现 ``\\mid``（合法符号但不是定界符）-> 改写成 ``\\vert{}``；
      · 实在取不到定界符 -> 记一条问题，交给人看，不擅自改写语义。

    返回 (修好的公式, 问题描述列表)。
    """
    problems: list[str] = []

    # --- 1) 逐个校验定界符位置 ---
    # 注意：这里【不做】全局的「命令 + 字母」替换。那样会误伤正文：
    # 例如 LaTeX 换行 \\ 后面跟着单词 label，全局替换会把 \\label 改成
    # \\lt{}abel（"label" 变成 "<abel"）。所以只在真正的定界符位置动手。
    result: list[str] = []
    position = 0
    while True:
        match = _DELIM_CMD_RE.search(body, position)
        if match is None:
            result.append(body[position:])
            break
        result.append(body[position:match.start()])
        command = match.group(0)
        # 保护：``\\ left`` 这种「LaTeX 换行 + 单词 left」不是定界符命令。
        # 字母本来就不是合法定界符，遇到字母直接跳过，别报假警。
        peek = match.end()
        while peek < len(body) and body[peek].isspace():
            peek += 1
        if peek < len(body) and body[peek].isascii() and body[peek].isalpha():
            result.append(command)
            position = match.end()
            continue
        token, end = _read_delimiter(body, match.end())
        if token is None:
            problems.append("%s 后面没有定界符" % command)
            result.append(command)
            position = match.end()
            continue
        if token not in _MATHJAX_DELIMITERS:
            if token == "\\mid":
                # \mid 是关系符，MathJax 的定界符表里没有它，
                # 放在 \left 后面必然报错，改写成视觉一致的 \vert。
                if body[end:end + 2] == "{}":
                    end += 2
                suffix = "{}" if _needs_terminator(body, end) else ""
                result.append(command + "\\vert" + suffix)
                problems.append("%s\\mid 改写成 %s\\vert%s" % (command, command, suffix))
                position = end
                continue
            problems.append("%s 后面跟的不是合法定界符：%s" % (command, token))
            result.append(command)
            position = match.end()
            continue
        # 定界符合法：多字母命令后面紧跟 ASCII 字母时补一个空分组，把命令名切断
        #   \left\vertx -> \left\vert{}x
        suffix = ""
        if token.startswith("\\") and len(token) > 2 and _needs_terminator(body, end):
            suffix = "{}"
        result.append(command)
        result.append(body[match.end():end])
        result.append(suffix)
        position = end
    return "".join(result), problems


def escape_math_body(body: str) -> str:
    """转义单条行内公式内部的 kramdown 雷区字符（对已转义的内容幂等）。"""
    # 1) LaTeX 行分隔符 \\ 必须保留：kramdown 的 BackslashEscapes 会把 \\ 还原成单个 \，
    #    导致矩阵 / 数组的换行消失、被压平成一行文本。先翻倍成 \\\\，kramdown 成对还原后仍是 \\。
    body = re.sub(r"\\\\", r"\\\\\\\\", body)
    # 2) 保护 LaTeX 环境内部的 |（数组列分隔符），避免被下面的 \mid{} 规则误换成 \mid。
    if "|" in body:
        body = _protect_env_pipes(body)
    # 3) 逐条转义（已对转义过的内容幂等）。
    for pattern, replacement in _MATH_ESCAPE_RULES:
        body = pattern.sub(replacement, body)
    # 4) 还原环境内部的 | 占位符。
    if "\x00ENVPIPE\x00" in body:
        body = body.replace("\x00ENVPIPE\x00", "|")
    # 5) 兜底：保证 \left / \right / \middle / \big 后面一定跟着合法定界符，
    #    并且定界符命令不会和后面的字母连读成非法命令。
    body, problems = enforce_math_delimiters(body)
    for problem in problems:
        print("  [warn] 数学定界符：%s" % problem, file=sys.stderr)
    return body


def normalize_math_delimiters(text: str) -> str:
    """统一数学定界符并修掉常见畸形写法。

    - ``\\(...\\)`` -> ``$...$``：行内公式去掉内容两端空格（MathJax 不认 ``$ x $``）
    - ``\\[...\\]`` -> 「$$ / 内容 / $$」三行块（单行 $$a=b$$ 会被 kramdown 当行内）
    - ``$$$$`` / ``$$ $$`` -> 规范的空块级公式
    """
    text = _PAREN_INLINE_RE.sub(lambda match: "$" + match.group(1).strip() + "$", text)
    text = _BRACKET_DISPLAY_RE.sub(
        lambda match: "$$\n" + match.group(1).strip() + "\n$$", text
    )
    return re.sub(r"\$\$[ \t]*\$\$", "$$\n\n$$", text)


_HTML_ENTITY_MAP = (("&lt;", "<"), ("&gt;", ">"), ("&amp;", "&"))


def restore_html_entities(text: str) -> str:
    """把公式里被转义成 HTML 实体的符号还原回原始字符。"""
    for entity, char in _HTML_ENTITY_MAP:
        text = text.replace(entity, char)
    return text


def is_block_math(text: str, match: re.Match[str]) -> bool:
    """判断某个 $$...$$ 是不是块级公式：内容跨行，或者整行只有这个公式。"""
    if "\n" in match.group(0):
        return True
    start, end = match.span()
    line_start = text.rfind("\n", 0, start) + 1
    line_end = text.find("\n", end)
    if line_end == -1:
        line_end = len(text)
    return text[line_start:start].strip() == "" and text[end:line_end].strip() == ""


def wrap_orphan_math(text: str) -> str:
    """把散落在普通文本里、没有被 $ / $$ / \\[ \\] / \\( \\) 包裹的 LaTeX 环境
    （``\\begin{...} ... \\end{...}``）自动包成 ``$$ ... $$`` 块级公式。

    外来 OCR / AI 整理文本经常漏写定界符，导致 ``\\begin{matrix}`` 整块被当成纯文本、
    公式符号直接漏到页面上。这里只处理【环境块】这种 unambiguously 是公式的结构，
    并且会跳过已经被任意定界符包裹的环境，避免重复包裹把公式弄坏。
    """
    # 1) 收集所有已被各类定界符包裹的区间，孤儿检测时一律跳过。
    protected: list[tuple[int, int]] = []
    for rx in (_DISPLAY_MATH_RE, _INLINE_MATH_RE, _BRACKET_DISPLAY_RE, _PAREN_INLINE_RE):
        protected.extend(m.span() for m in rx.finditer(text))

    def overlapped(start: int, end: int) -> bool:
        # 两个半开区间 [s, e) 与 [start, end) 是否相交
        return any(start < e and s < end for (s, e) in protected)

    def repl(match: re.Match[str]) -> str:
        start, end = match.span()
        if overlapped(start, end):
            return match.group(0)
        # 三行块写法，确保 kramdown 把它当成独立的公式块（& 与 \\\\ 原样透传由
        # protect_math 的 display() 负责，这里只负责补定界符）。
        return "$$\n" + match.group(0) + "\n$$"

    return _BEGIN_ENV_RE.sub(repl, text)


def protect_math(text: str, counts: dict[str, int]) -> tuple[str, list[str]]:
    """抽出数学公式，返回 (处理后的文本, 公式列表)。

    - 先 ``wrap_orphan_math``：把漏写定界符的 ``\\begin{...}...\\end{...}`` 包成 ``$$...$$``。
    - ``\\[...\\]`` / ``\\(...\\)`` 统一成 ``$$...$$`` / ``$...$``。
    - 块级公式（独占整行或内容跨行）在占位符前后各补一个换行，保证 kramdown 把它
      识别成独立的 math block，而不是和上下段落粘成一段（多余空行后续会被压缩成一个）。
    - ``$$...$$`` 内容原样抽出。kramdown 的 math engine 会把整段内容透传给 MathJax，
      块内的 ``&`` 是矩阵对齐符、``_`` 是下标，加转义会破坏它们。
    - ``$...$`` 行内：去掉两端空格后做全量转义，因为 kramdown 会先按 Markdown 解析它。
    - 两种公式都会先把 HTML 实体（&lt; &gt; &amp;）还原成原始符号。
    """
    formulas: list[str] = []
    # 先把漏写定界符的 LaTeX 环境包好，再走常规抽取流程
    text = wrap_orphan_math(text)
    text = normalize_math_delimiters(text)

    def stash(raw: str) -> str:
        formulas.append(raw)
        return _MATH_PLACEHOLDER.format(len(formulas) - 1)

    def display(match: re.Match[str]) -> str:
        counts["math"] += 1
        # 块级公式里【只】把尖括号换成 \lt{} / \gt{}，其它字符一律原样透传。
        # 原因：kramdown 不解析 $$ 块内部（math_engine 已关），内容原封不动交给 MathJax；
        # 唯一会让 kramdown 误判的是 < / >（它会当成 HTML 标签开头）。
        # 千万不要在这里调用 escape_math_body：
        #   · _ 换成 &#95; 后，&#95; 里的 & 会被 MathJax 当成对齐符 → Misplaced & 崩溃
        #   · # & * % 在数学里都有语义，转义即破坏
        body = restore_html_entities(match.group(1))
        # 翻倍 \\ 以对抗 kramdown 的 BackslashEscapes（否则块级矩阵 / 数组也会被压平）
        body = re.sub(r"\\\\", r"\\\\\\\\", body)
        body = _DISPLAY_LTGT_RULES[0][0].sub(_DISPLAY_LTGT_RULES[0][1], body)
        body = _DISPLAY_LTGT_RULES[1][0].sub(_DISPLAY_LTGT_RULES[1][1], body)
        # 块级公式同样做一次定界符兜底：块里的 | 是合法定界符不会被改动，
        # 但源文件里写坏的 \left\vertx（命令名粘连）在这里会被修好。
        body, problems = enforce_math_delimiters(body)
        for problem in problems:
            print("  [warn] 数学定界符：%s" % problem, file=sys.stderr)
        placeholder = stash("$$" + body + "$$")
        if is_block_math(text, match):
            # 前后各补一个换行，让 kramdown 把它当成独立的公式块
            return "\n" + placeholder + "\n"
        return placeholder

    def inline(match: re.Match[str]) -> str:
        counts["math"] += 1
        body = restore_html_entities(match.group(1).strip())
        return stash("$" + escape_math_body(body) + "$")

    text = _DISPLAY_MATH_RE.sub(display, text)
    text = _INLINE_MATH_RE.sub(inline, text)
    return text, formulas


def restore_math(text: str, formulas: list[str]) -> str:
    """把公式占位符还原成公式原文。

    还原前后各查一次残留：如果占位符在流水线里被某条清洗规则改过（比如下划线被转义），
    这里就会打印告警，而不是让占位符悄悄漏到页面上。
    """
    pattern = re.compile(r"ZMATHPH(\d+)Z")

    before = pattern.findall(text)
    if before and os.environ.get("SYNC_DEBUG"):
        print("  [debug] restore 前仍有占位符: %d 个" % len(before), file=sys.stderr)

    for position, formula in enumerate(formulas):
        text = text.replace(_MATH_PLACEHOLDER.format(position), formula)

    leftover = pattern.findall(text)
    if leftover:
        print(
            "  [warn] 有 %d 个占位符没能还原（被流水线改坏了）：%s"
            % (len(leftover), ", ".join("ZMATHPH%sZ" % n for n in leftover[:5])),
            file=sys.stderr,
        )
    return text


# --------------------------------------------------------------------------- #
# 4. 排版清洗与容错（标题 / 引用 / 列表 / 水平线 / 链接的隔离与清洗）
# --------------------------------------------------------------------------- #
_HEADING_LINE_RE = re.compile(r"^[ \t]{0,3}#{1,6}[ \t]")
# 漏打空格的标题：只认 ## 及以上（单个 # 在 Obsidian 里通常是 #标签，不能动）
_HEADING_NO_SPACE_RE = re.compile(r"^([ \t]{0,3})(#{2,6})([^#\s])", re.MULTILINE)
_QUOTE_LINE_START_RE = re.compile(r"^[ \t]*>")
_LIST_LINE_RE = re.compile(r"^[ \t]*([-*+] |\d+\. )")
_HR_LINE_RE = re.compile(r"^[ \t]{0,3}(-{3,}|\*{3,}|_{3,})[ \t]*$")
_LONE_LINK_LINE_RE = re.compile(r"^[ \t]*!?\[[^\]\n]*\]\([^)\n]*\)[ \t]*$")
_LINK_TEXT_RE = re.compile(r"\[([^\]\n]*)\]\(([^)\n]*)\)")


def fix_heading_space(text: str) -> str:
    """把漏打空格的 ``##标题`` 修成 ``## 标题``。

    只处理 ``##`` 及以上：单个 ``#`` 紧跟文字在 Obsidian 里通常是 ``#标签``，
    补空格会把它变成 H1 标题，所以单个 # 一律不动（标签保持纯文本）。
    """

    def fix(match: re.Match[str]) -> str:
        return "%s%s %s" % (match.group(1), match.group(2), match.group(3))

    return _HEADING_NO_SPACE_RE.sub(fix, text)


def separate_blocks(text: str) -> str:
    """给紧贴正文的块级元素上方补一个空行，避免 kramdown 把它们并进段落。

    覆盖：标题、引用块起始行、列表首项、水平线、独占整行的链接/图片。
    引用块与列表内部的连续行不补（否则会把它们拆散）。
    """
    lines = text.split("\n")
    output: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        previous = output[-1] if output else ""
        previous_is_quote = bool(_QUOTE_LINE_START_RE.match(previous))
        previous_is_list = bool(_LIST_LINE_RE.match(previous))

        is_heading = bool(_HEADING_LINE_RE.match(line))
        is_quote_start = bool(_QUOTE_LINE_START_RE.match(line)) and not previous_is_quote
        is_list_start = bool(_LIST_LINE_RE.match(line)) and not previous_is_list
        is_rule = bool(_HR_LINE_RE.match(line))
        is_lone_link = bool(_LONE_LINK_LINE_RE.match(line))

        needs_gap = is_heading or is_quote_start or is_list_start or is_rule or is_lone_link
        if needs_gap and previous.strip() != "":
            output.append("")
        output.append(line)

        # 水平线后面也必须补空行，否则 "---" 会被当成上一行的 setext 标题下划线
        if is_rule and index + 1 < len(lines) and lines[index + 1].strip() != "":
            output.append("")
        index += 1
    return "\n".join(output)


def clean_link_text(text: str) -> str:
    """清洗 Markdown 链接/图片：替换冲突字符、清理空链接。

    - 全角空格 / 制表符 -> 半角空格
    - ``|`` -> ``｜``（全角竖线，防止和 kramdown 的表格语法冲突导致链接失效）
    - ``*`` / ``_`` -> ``\\*`` / ``\\_``（防止被当成粗体 / 斜体）
    - ``[]()`` 整个删掉，``[文字]()`` 退化成纯文字
    """

    def fix(match: re.Match[str]) -> str:
        label = match.group(1).replace("\u3000", " ").replace("\t", " ")
        url = match.group(2).strip()
        if not label.strip():
            return ""  # []() -> 什么都不留
        if not url:
            return label.strip()  # [文字]() -> 纯文字
        label = label.replace("|", "｜").replace("*", "\\*").replace("_", "\\_")
        return "[%s](%s)" % (label, url)

    return _LINK_TEXT_RE.sub(fix, text)


def escape_liquid_delimiters(text: str) -> str:
    """把会被 Jekyll/Liquid 误当成模板语法的 ``{{`` / ``{%`` 转成 HTML 实体。

    Jekyll 是先执行 Liquid、再跑 Markdown，所以连代码块里的 ``{{`` 也会被解析
    （这正是构建报错的常见来源）。换成实体后浏览器仍显示成 ``{{``，
    但 Liquid 不会再把它当模板执行。
    """
    text = text.replace("{{", "&#123;&#123;")
    return text.replace("{%", "&#123;%")


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
        # label 里含公式时改用原生 <a>：kramdown 对 [文本](url) 的 label 会做额外处理，
        # 里面的 $...$ 经常渲染不出来。注意此时公式已被 protect_math 抽成
        # ZMATHPHnZ 占位符，所以两种形式都要判断。
        if "$" in label or "ZMATHPH" in label:
            return '<a href="#%s">%s</a>' % (block_id, label)
        return "[%s](#%s)" % (label, block_id)

    def alias_link(match: re.Match[str]) -> str:
        raw_target = match.group(1).strip()
        target = resolve_note_target(raw_target, slug_map)
        label = match.group(2).strip()
        counts["wikilink"] += 1
        if "$" in label or "ZMATHPH" in label:
            return '<a href="%s%s/">%s</a>' % (url_prefix, target, label)
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


def _looks_like_front_matter(block: str) -> bool:
    """粗略校验 ``--- ... ---`` 中间的内容是否真的是 YAML。

    防止这种情况：正文第一行恰好是水平线 ``---``，后面还有一根水平线，
    被非贪婪正则误当成 front matter 的闭合符，把一大段正文吞进 YAML。
    判定标准：除空行 / 注释 / 列表项外，每一行都必须出现半角冒号（``key: value``）。
    """
    for line in block.split("\n"):
        stripped = line.strip()
        if not stripped or stripped == "---" or stripped.startswith("#"):
            continue
        if ":" in line or re.match(r"^[ \t]*-[ \t]", line):
            continue
        return False
    return True


def split_front_matter(text: str) -> tuple[str | None, str]:
    """拆出已有的 front matter（含结尾换行）和正文。

    容错：开头有 ``---`` 但内容不像 YAML、或始终没有闭合的 ``---``（写坏了）时，
    把开头标记和后面的 ``key: value`` 行去掉，整篇当正文处理，
    避免正文被 YAML 解析器吞掉。
    """
    match = _FRONT_MATTER_RE.match(text)
    if match and _looks_like_front_matter(match.group(0)):
        return match.group(0), text[match.end():]
    if text.startswith("---"):
        lines = text.split("\n")
        index = 1
        # 顺带跳过后面形如 "key: value" 的行——那就是写坏的 front matter 内容
        while index < len(lines) and _FM_FIELD_RE.match(lines[index]):
            index += 1
        return None, "\n".join(lines[index:]).lstrip("\n")
    return None, text


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


_PUBLIC_LINE_RE = re.compile(r"^[ \t]*public[ \t]*:.*$", re.MULTILINE)


def apply_public(front_matter: str, is_public: bool) -> str:
    """写入 front matter 的 public 字段，决定这篇笔记是否出现在主页列表。

    写的是真正的 YAML 布尔量（``true`` / ``false``）而不是字符串，所以主页的
    Liquid 可以直接用 ``page.public == true`` 判定。

    仓归属是权威来源：即使源笔记自己写了 ``public:``，也会被这里覆盖成
    所在仓对应的值，避免「手滑写错导致私密笔记被挂到主页」。
    """
    line = "public: %s" % ("true" if is_public else "false")
    if _PUBLIC_LINE_RE.search(front_matter):
        updated = _PUBLIC_LINE_RE.sub(lambda _match: line, front_matter, count=1)
    else:
        stripped = front_matter.rstrip("\n")
        if not stripped.endswith("---"):
            return front_matter
        head = stripped[:-3].rstrip("\n")
        updated = head + "\n" + line + "\n---\n"
    # front matter 与正文之间统一保留一个空行
    return updated.rstrip("\n") + "\n\n"


# --------------------------------------------------------------------------- #
# 6. 输出目录清理
# --------------------------------------------------------------------------- #
# 为什么要清理：
#   笔记从 origin/public/ 挪到 origin/hidden/（或者改名、删掉）之后，它在 notes/
#   下的旧文件**不会自己消失**。旧文件的 front matter 里还写着 public: true，
#   主页的 Liquid（notes.md）只认 public 字段，于是照样把它列出来 ——
#   表现就是「明明已经移到隐藏仓了，主页上还是出现」。
#   而且旧 slug 会留下一堆死链（/notes/<旧slug>/ 仍然能打开）。
#
# 所以每次生成前先把「上一轮的产物」清掉，再重新生成，保证 notes/ 与 origin/ 一一对应。
#
# 只删「脚本自己生成的产物」，手写页面和测试稿一律保留：
#   1. 文件名在 PRESERVE_NOTE_FILENAMES 白名单里      -> 保留
#   2. 文件名里含 test / 测试 / demo / torture / sample -> 保留（测试稿）
#   3. 本轮还会重新生成的                            -> 保留（等下覆盖写）
#   4. 带 generated_by 标记，或者长得像脚本产物         -> 删除
#   5. 其余（手写页面，没有脚本产物的特征）            -> 保留
GENERATED_BY = "sync_notes.py"

# 清理时永远不动的文件（白名单）。即使源笔记被删掉，这些测试稿也要留在 notes/ 里。
PRESERVE_NOTE_FILENAMES = {
    "callout-color-test.md",
    "hell-math-test.md",
    "left-right-test.md",
    "math-bug-test.md",
}

# 文件名里含这些片段的一律当成测试稿，清理时跳过（与主页的排除规则保持一致）
PRESERVE_NAME_HINTS = ("test", "测试", "demo", "torture", "sample")

_GENERATED_BY_LINE_RE = re.compile(r"^[ \t]*generated_by[ \t]*:.*$", re.MULTILINE)


def apply_generated_by(front_matter: str) -> str:
    """写入 ``generated_by: sync_notes.py`` 标记。

    这个标记是清理逻辑的「身份证」：有了它就能百分百确认某个 notes/*.md
    是脚本生成的产物，清理时可以放心删；没有标记的文件（比如手写页面）
    一律不碰。
    """
    line = "generated_by: %s" % GENERATED_BY
    if _GENERATED_BY_LINE_RE.search(front_matter):
        updated = _GENERATED_BY_LINE_RE.sub(lambda _match: line, front_matter, count=1)
    else:
        stripped = front_matter.rstrip("\n")
        if not stripped.endswith("---"):
            return front_matter
        head = stripped[:-3].rstrip("\n")
        updated = head + "\n" + line + "\n---\n"
    # front matter 与正文之间统一保留一个空行
    return updated.rstrip("\n") + "\n\n"


def _is_generated_artifact(path: Path) -> bool:
    """判断 notes/ 下的文件是不是脚本生成的产物（可以安全删除）。"""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return False
    front_matter, _ = split_front_matter(text)
    if not front_matter:
        return False
    fields = read_front_matter_fields(front_matter)
    if fields.get("generated_by", "").strip() == GENERATED_BY:
        return True
    # 老版本产物没有 generated_by 标记，靠「形状」兜底识别：
    # layout: note + permalink: /notes/... 正是脚本输出 front matter 的形状。
    permalink = fields.get("permalink", "").strip()
    return fields.get("layout", "").strip() == "note" and permalink.startswith("/notes/")


def _is_preserved_name(name: str) -> bool:
    """文件名是否属于「一律保留」名单。"""
    if name in PRESERVE_NOTE_FILENAMES:
        return True
    lowered = name.lower()
    return any(hint in lowered for hint in PRESERVE_NAME_HINTS)


def clean_output_dir(dest: Path, planned: set[str]) -> list[str]:
    """删掉 dest 下「上一轮遗留、本轮不会再生成」的旧产物。

    planned 是本轮会写出的文件（相对 dest 的 posix 路径）。
    返回被删除的相对路径列表。
    """
    removed: list[str] = []
    if not dest.is_dir():
        return removed
    for path in sorted(dest.rglob("*.md")):
        relative = path.relative_to(dest).as_posix()
        if relative in planned:
            continue  # 本轮会重新生成，等下覆盖写就行
        if _is_preserved_name(path.name):
            continue  # 测试稿 / 白名单，一律保留
        if not _is_generated_artifact(path):
            continue  # 手写页面，没有脚本产物的特征，不动
        try:
            path.unlink()
        except OSError as error:
            print("[warn] 删除旧产物失败：%s：%s" % (relative, error), file=sys.stderr)
            continue
        removed.append(relative)
    # 清掉因为删文件而空掉的子目录
    for directory in sorted(
        (p for p in dest.rglob("*") if p.is_dir()),
        key=lambda p: len(p.parts),
        reverse=True,
    ):
        try:
            next(directory.iterdir())
        except StopIteration:
            try:
                directory.rmdir()
            except OSError:
                pass
        except OSError:
            pass
    return removed


_RENDER_LIQUID_LINE_RE = re.compile(r"^[ \t]*render_with_liquid[ \t]*:.*$", re.MULTILINE)


def apply_render_with_liquid(front_matter: str) -> str:
    """强制写入 render_with_liquid: false。

    作用：让 Jekyll 4+ 不再把正文里的 {{ }} / {% %} 当模板语法执行。
    注意 GitHub Pages 目前跑的是 Jekyll 3.9，这一项会被忽略（无害），
    真正兜底的是 escape_liquid_delimiters()。
    """
    line = "render_with_liquid: false"
    if _RENDER_LIQUID_LINE_RE.search(front_matter):
        updated = _RENDER_LIQUID_LINE_RE.sub(lambda _match: line, front_matter, count=1)
    else:
        stripped = front_matter.rstrip("\n")
        if not stripped.endswith("---"):
            return front_matter
        head = stripped[:-3].rstrip("\n")
        updated = head + "\n" + line + "\n---\n"
    return updated.rstrip("\n") + "\n\n"


def classify_source(path: Path, src: Path) -> tuple[str, Path]:
    """判断源笔记属于哪个仓，返回 (仓名, 相对该仓目录的路径)。

    - ``origin/public/xxx.md``   -> ("public", "xxx.md")
    - ``origin/hidden/xxx.md``   -> ("hidden", "xxx.md")
    - ``origin/xxx.md``（历史遗留）-> ("public", "xxx.md")

    返回的「相对路径」决定生成文件落在 notes/ 下的什么位置，因此把笔记移进
    public/ 子目录**不会改变**既有 URL（permalink 仍是 /notes/<slug>/）。
    """
    relative = path.relative_to(src)
    parts = relative.parts
    if parts and parts[0] in BUCKET_NAMES:
        return parts[0], Path(*parts[1:])
    return DEFAULT_BUCKET, relative


def build_slug_map(sources: list[Path]) -> dict[str, str]:
    """建立「源文件名 / front matter title -> slug」的映射，用于重写 wikilink。

    没有显式 slug 的笔记也会用 make_slug() 自动生成一个，所以中文互链
    （``[[中文笔记名]]``）能正确指向 ``/notes/<拼音>/``。

    注意：``sources`` 是**全仓扫描**的结果（public/ 与 hidden/ 混在一起），
    所以 public 里的笔记写 ``[[私密笔记]]``、而那篇私密笔记在 hidden/ 里时，
    映射照样能命中，链接依然指向正确的 /notes/<拼音>/。
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
    is_public: bool = True,
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
    if front_matter is None and text.lstrip().startswith("---"):
        print("  [warn] front matter 缺少闭合的 ---，已按正文处理", file=sys.stderr)

    # 流水线顺序（保护优先，替换其次）：
    #   1. 代码块（含 dataview / mermaid）抽成占位符 —— 最高优先级
    #   2. Callout 转换要在数学抽取【之前】：
    #      protect_math 靠"$$ 是否顶格独占一行"来判断块级公式，
    #      而 callout 里的公式原文是 "> $$A=B$$"，行首有 ">" 会被误判成行内公式，
    #      导致块级公式不补前后换行、kramdown 无法识别成 math block。
    #      先转 callout，把 "> " 去掉，$$ 顶格之后判断才准确。
    #   3. 数学公式抽成占位符（行内公式在抽取时同时完成全量转义）
    #   4. 其余 Obsidian / Markdown 语法都在占位符之外处理
    #   5. 还原公式 -> 压缩空行 -> 还原代码块
    body, code_blocks, mermaid_blocks = protect_code_blocks(body, counts)
    body = convert_callouts(body, counts)
    body, formulas = protect_math(body, counts)
    body = strip_obsidian_comments(body, counts)
    body = convert_highlights(body, counts)
    body = convert_embeds(body, counts)
    # 跨页块引用必须在 convert_block_heading_links 之前处理：
    # 不带别名的 [[笔记名#^块ID]] 会被标题规则当成「笔记名#标题」，
    # 生成指向 #^块ID 的死锚点（真实锚点没有 ^）。
    body = convert_cross_block_links(body, counts, slug_map, url_prefix)
    body = convert_block_heading_links(body, counts, slug_map, url_prefix)
    body = convert_tasks(body, counts)
    body = convert_emoji(body, counts)
    body = convert_links(body, counts, slug_map, url_prefix)
    # 第四级：排版清洗（此时公式和代码块还都是占位符，不会被误伤）
    body = fix_heading_space(body)
    body = separate_blocks(body)
    body = clean_link_text(body)
    # %% 注释整段删除后会留下多个连续空行，压缩成一个（此时公式还是占位符，
    # 所以不会影响 $$ 块内部原有的空行）
    body = re.sub(r"\n{3,}", "\n\n", body)
    body = restore_math(body, formulas)
    body = restore_code_blocks(body, code_blocks, mermaid_blocks)
    # 最后一步：转义 {{ / {%，防止 Jekyll 把它们当成 Liquid 模板去执行
    body = escape_liquid_delimiters(body)

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
    # 分仓可见性：public/ 的笔记进主页列表，hidden/ 的不进（URL 仍可直接访问）
    front_matter = apply_public(front_matter, is_public)
    # 产物标记：清理逻辑靠它识别「这个文件是脚本生成的」
    front_matter = apply_generated_by(front_matter)
    # 强制关闭 Liquid 渲染（Jekyll 4+ 生效；GitHub Pages 的 3.9 会忽略，另有 escape 兜底）
    front_matter = apply_render_with_liquid(front_matter)
    # permalink 已经保证 front matter 后面带一个空行，正文开头的空行去掉避免重复
    return front_matter + body.lstrip("\n"), counts, added_front_matter


def check_output_math(dest: Path) -> list[str]:
    """按 MathJax v3 的规则校验生成物里的每一个定界符。

    和 enforce_math_delimiters() 用的是同一套判据（GetDelimiter + GetCS +
    合法定界符全集），所以这里过了，浏览器里就不会再抛
    "Missing or unrecognized delimiter for \\left"。

    返回问题描述列表；空列表代表全部通过。
    """
    problems: list[str] = []
    for path in sorted(dest.rglob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for rx in (_INLINE_MATH_RE, _DISPLAY_MATH_RE):
            for match in rx.finditer(text):
                body = match.group(1)
                for command in _DELIM_CMD_RE.finditer(body):
                    token, end = _read_delimiter(body, command.end())
                    where = "%s: %s" % (path.name, command.group(0))
                    if token is None:
                        problems.append("%s 后面没有定界符" % where)
                    elif token not in _MATHJAX_DELIMITERS:
                        problems.append("%s 后面跟的不是合法定界符：%s" % (where, token))
                    elif token.startswith("\\") and len(token) > 2:
                        following = body[end:end + 1]
                        if following and following.isascii() and following.isalpha():
                            problems.append(
                                "%s 的命令名会被连读成 %s%s（未定义命令）"
                                % (where, token, following)
                            )
    return problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="把 origin/ 里的 Obsidian 笔记转换成 Jekyll 可渲染的 Markdown。"
    )
    parser.add_argument("--src", default=str(DEFAULT_SRC), help="源目录（默认 ./origin）")
    parser.add_argument("--dest", default=str(DEFAULT_DEST), help="输出目录（默认 ./notes）")
    parser.add_argument(
        "--no-clean",
        action="store_true",
        help="跳过清理：保留上一轮遗留的旧文件（调试用，正常跑不要加）",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="生成后按 MathJax 的规则校验全站定界符（不通过则返回非 0）",
    )
    args = parser.parse_args(argv)

    src = Path(args.src).resolve()
    dest = Path(args.dest).resolve()
    if not src.is_dir():
        print("[error] 源目录不存在：%s" % src, file=sys.stderr)
        return 1

    dest.mkdir(parents=True, exist_ok=True)

    # 递归扫描整个源目录：public/ 与 hidden/ 都会被收进来（历史上就是 rglob）
    sources = sorted(path for path in src.rglob("*.md") if path.is_file())
    if not sources:
        print("[warn] %s 下没有找到 .md 文件" % src)

    # 第一遍：收集 slug 映射，供第二遍重写 wikilink 时使用。
    # 这一步用的是**全仓**的 sources（public + hidden 混在一起），
    # 所以跨仓双链（public 指向 hidden）依然能正确解析成 /notes/<拼音>/。
    slug_map = build_slug_map(sources)

    # permalink 前缀跟随输出目录在仓库里的位置（默认 dest 是仓库根的 notes/ -> /notes/）
    try:
        url_prefix = "/" + dest.relative_to(ROOT).as_posix().strip("/") + "/"
    except ValueError:
        url_prefix = "/" + dest.name + "/"

    # 第一遍：算出每篇的 slug / permalink / 所属仓，并检查 slug 冲突
    # plans 的每一项是 (源相对路径, 仓内相对路径, slug, permalink, 原文, 是否公开)
    plans: list[tuple[Path, Path, str, str, str, bool]] = []
    seen_slugs: dict[str, Path] = {}
    conflicts: list[str] = []
    for path in sources:
        relative = path.relative_to(src)
        bucket, inner = classify_source(path, src)
        is_public = bucket == BUCKET_PUBLIC
        text = path.read_text(encoding="utf-8")
        front_matter, _ = split_front_matter(text)
        fields = read_front_matter_fields(front_matter)

        # 没写 slug 时自动用拼音生成（中文文件名 -> shu-xue-...）
        slug = fields.get("slug", "").strip() or make_slug(path.stem, text)

        if slug in seen_slugs:
            conflicts.append(
                "  %s  与  %s  都会生成 slug: %s" % (seen_slugs[slug], relative, slug)
            )
        else:
            seen_slugs[slug] = relative

        # 输出路径基于「仓内相对路径」，所以 public/xxx.md -> notes/<slug>.md，
        # permalink 仍是 /notes/<slug>/ —— 与分仓前完全一致，不会有旧链接失效
        parent = "" if inner.parent == Path(".") else inner.parent.as_posix() + "/"
        plans.append(
            (relative, inner, slug, url_prefix + parent + slug + "/", text, is_public)
        )

    if conflicts:
        print(
            "[error] 检测到 slug 冲突，已停止生成。"
            "请在源笔记的 front matter 里手动指定不同的 slug：",
            file=sys.stderr,
        )
        for line in conflicts:
            print(line, file=sys.stderr)
        return 1

    # ---- 清理上一轮遗留的旧产物（在真正生成之前）----
    # 笔记换仓 / 改名 / 删除之后，它在 notes/ 下的旧文件不会自己消失。
    # 旧文件里还写着 public: true，主页就会继续把它列出来（死链 + 误显示）。
    # 这里把「本轮不会再生成、且确实是脚本产物」的文件删掉，
    # 测试稿和白名单里的文件一律保留。
    planned = {
        (inner.parent / (slug + ".md")).as_posix()
        for _relative, inner, slug, _permalink, _text, _is_public in plans
    }
    if args.no_clean:
        print("[clean] 已跳过（--no-clean）")
    else:
        removed = clean_output_dir(dest, planned)
        if removed:
            print("[clean] 清掉 %d 个上一轮的旧产物：" % len(removed))
            for name in removed:
                print("  - %s" % name)
        else:
            print("[clean] 没有需要清理的旧产物")

    # 第二遍：逐篇转换。单篇失败只跳过它自己，绝不拖垮整站
    processed = 0
    for relative, inner, slug, permalink, text, is_public in plans:
        _, body_only = split_front_matter(text)
        if not body_only.strip():
            print("[skip] %s（正文为空）" % relative, file=sys.stderr)
            continue

        target = dest / inner.parent / (slug + ".md")
        try:
            converted, counts, added = convert_document(
                text, inner.stem, slug, permalink, slug_map, url_prefix, is_public
            )
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(converted, encoding="utf-8", newline="\n")
        except Exception as error:  # noqa: BLE001 - 一篇烂笔记不能拖垮整站
            print(
                "[error] %s 转换失败，已跳过：%s: %s"
                % (relative, type(error).__name__, error),
                file=sys.stderr,
            )
            continue

        processed += 1
        print(
            "[ok] %s -> %s  (slug=%s, permalink=%s, public=%s, callout=%d, math=%d, wikilink=%d, block_link=%d, block_id=%d, image=%d, obsidian=%d, front_matter=%s)"
            % (
                relative,
                target.name,
                slug,
                permalink,
                "true" if is_public else "false",
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

    print("[done] 共处理 %d 个文件，输出目录：%s" % (processed, dest))

    if args.check:
        problems = check_output_math(dest)
        if problems:
            print(
                "[check] 发现 %d 个定界符问题（MathJax 会报错）：" % len(problems),
                file=sys.stderr,
            )
            for problem in problems:
                print("  - %s" % problem, file=sys.stderr)
            return 1
        print("[check] 全站定界符校验通过 ✅")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
