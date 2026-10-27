# Callout Studio → 静态网页渲染手册

> 本文档从 Obsidian 插件 **Callout Studio**（`PaperBell/.obsidian/plugins/callout-studio/`）的配置中完整提取，
> 用于在任意静态站点（Jekyll / Hugo / 纯 HTML）中还原与 Obsidian 一致的 Callout 外观。
>
> **数据源**：`data.json`（最后修改 2026-10-27，33 条定义 / 25 条可用）
> **写笔记时怎么选类型**：见 TECH_GUIDE.md §4.5「Callout 语义映射规范」
> **图标库版本**：12 个数学类用 **Font Awesome 6.4.2**（`_layouts/note.html` 已 CDN 引入 `all.min.css`）；其余类型用 Lucide `lucide-static@1.61.0` · Tabler `@tabler/icons@3.49.0` · Octicons `@primer/octicons@19.42.0` · Material Symbols（缓存在 `_icon-src/`，不入库）

---

## v4 变更（当前线上实现）

`assets/css/obsidian-callouts.css` 现在是双轨制：

- **12 个数学类**（`theorem` `definition` `conclusion` `corollary` `lemma` `formula` `context` `seealso` `idea` `motivation` `keypoint` `understand`）
  图标改用 **Font Awesome 6 字形**：`content: var(--callout-icon-glyph)` + `font-family: "Font Awesome 6 Free"; font-weight: 900`；
  背景改成**显式 `rgba()`**（亮 0.08 / 暗 0.15），不再依赖 `color-mix`。
- **其余类型**：原样保留 v3 的 `mask + Base64 SVG`，一行没动。
- `corollary` / `lemma` / `understand` 是 v4 新增类型（v3 文档里没有）。

| ID | 显示名 | 图标 | 码点 | 语义 | 亮色 | 暗色 |
|---|---|---|---|---|---|---|
| `theorem` | Theorem | FA solid | `\f698` | 平方根 | `#1e3a8a` | `#60a5fa` |
| `definition` | Definition | FA solid | `\f02d` | 书本 | `#15803d` | `#4ade80` |
| `conclusion` | Conclusion | FA solid | `\f058` | 对勾 | `#10b981` | `#34d399` |
| `corollary` | Corollary | FA solid | `\f126` | 分支 | `#6b21a8` | `#c084fc` |
| `lemma` | Lemma | FA solid | `\f12e` | 拼图 | `#475569` | `#94a3b8` |
| `formula` | Formula | FA solid | `\f1ec` | 计算器 | `#0284c7` | `#38bdf8` |
| `context` | Context | FA solid | `\f276` | 定位 | `#0d9488` | `#2dd4bf` |
| `seealso` | Seealso | FA solid | `\f0c1` | 链接 | `#475569` | `#94a3b8` |
| `idea` | Idea | FA solid | `\f0eb` | 灯泡 | `#d97706` | `#fbbf24` |
| `motivation` | Motivation | FA solid | `\f14e` | 指南针 | `#f97316` | `#fb923c` |
| `keypoint` | Keypoint | FA solid | `\f140` | 靶心 | `#dc2626` | `#f87171` |
| `understand` | Understand | FA solid | `\e2ca` | 星火 | `#c026d3` | `#e879f9` |

> `understand` 原计划用 `\f890`，但 FA 6.4.2 的私有区里没有这个字形（会渲染成豆腐块），改用同语义的 `\e2ca`（`wand-magic-sparkles`）。
> 下文 Part A 的表格仍是 **v3** 的 mask / base64 记录；凡涉及上面 12 个数学类，以本表为准。

---

## 0. 数据总览

`data.json` 里共 **33 条** Callout 定义，其中 **25 条可用**：

| 分类 | 数量 | 说明 |
|---|---|---|
| 内置标准类型 | 12 | `abstract` `danger` `example` `failure` `info` `note` `question` `quote` `success` `tip` `todo` `warning` |
| 自建有效类型 | 13 | `highlight` `definition` `conclusion seealso` `idea` `motivation` `theorem` `context` `formula` `keypoint` `corollary` `lemma` `understand` |
| **合计可用** | **25** | 其中 12 个数学类走 v4 的 FA 字形方案 |
| 模板占位（未清理） | 9 | 见 [A.3](#a3-未清理的占位项9-个)，**不要**用于正式文档 |

**关于颜色字段**：Callout Studio 的每条配置只有 **两个十六进制色值**——`colorLight`（亮色模式）和 `colorDark`（暗色模式）。它没有独立的「背景色 / 边框色 / 标题色」字段，这三种颜色都是从这一个 accent 色**派生**出来的：

```
accent   = colorLight / colorDark
左边框   = accent（4px solid）
标题文字 = accent
背景     = rgba(accent, 0.08) 亮 / rgba(accent, 0.15) 暗    ← v4：12 个数学类显式写死
           其余类型仍是 color-mix(accent 8%, transparent)
图标     = accent（12 类走 FA 字形用 color 上色；其余走 mask 上色）
```

---

## Part A: Callout 资产清单表

### A.1 可用类型（21 个）

| ID（Obsidian 里写 `[!xxx]`） | CSS 选择器 | 显示名 | 图标库 | 图标名 | 亮色 | 暗色 | base64 长度 |
|---|---|---|---|---|---|---|---|
| `abstract` | `[data-callout="abstract"]` | Abstract | Lucide | `clipboard-list` | `#00bfa5` | `#00bfa5` | 496 |
| `danger` | `[data-callout="danger"]` | Danger | Lucide | `zap` | `#e93147` | `#fb464c` | 460 |
| `example` | `[data-callout="example"]` | Example | Lucide | `list` | `#7852ee` | `#a882ff` | 392 |
| `failure` | `[data-callout="failure"]` | Failure | Lucide | `x` | `#e93147` | `#fb464c` | 284 |
| `info` | `[data-callout="info"]` | Info | Lucide | `info` | `#086ddd` | `#027aff` | 324 |
| `note` | `[data-callout="note"]` | Note | Lucide | `pencil` | `#086ddd` | `#027aff` | 440 |
| `question` | `[data-callout="question"]` | Question | Lucide | `help-circle` | `#ec7500` | `#e9973f` | 360 |
| `quote` | `[data-callout="quote"]` | Quote | Lucide | `quote` | `#9e9e9e` | `#9e9e9e` | 592 |
| `success` | `[data-callout="success"]` | Success | Lucide | `check` | `#08b94e` | `#44cf6e` | 260 |
| `tip` | `[data-callout="tip"]` | Tip | Lucide | `flame` | `#00bfbc` | `#53dfdd` | 360 |
| `todo` | `[data-callout="todo"]` | Todo | Lucide | `check-circle-2` | `#086ddd` | `#027aff` | 308 |
| `warning` | `[data-callout="warning"]` | Warning | Lucide | `alert-triangle` | `#ec7500` | `#e9973f` | 392 |
| `highlight` | `[data-callout="highlight"]` | Highlight | Octicons | `sparkles-fill` | `#086ddd` | `#027aff` | 1252 |
| `definition` | `[data-callout="definition"]` | Definition | Material Symbols | `book_ribbon` | `#086ddd` | `#027aff` | 884 |
| `conclusion` | `[data-callout="conclusion"]` | Conclusion | Lucide | `badge-check` | `#086ddd` | `#027aff` | 492 |
| `idea` | `[data-callout="idea"]` | idea | Lucide | `lightbulb` | `#afb42b` | `#dce775` | 428 |
| `motivation` | `[data-callout="motivation"]` | Motivation | Lucide | `sparkles` | `#ec7500` | `#e9973f` | 684 |
| `theorem` | `[data-callout="theorem"]` | Theorem | Lucide | `function-square` | `#086ddd` | `#027aff` | 372 |
| `context` | `[data-callout="context"]` | Context | Lucide | `map-pin` | `#00bfbc` | `#53dfdd` | 416 |
| `formula` | `[data-callout="formula"]` | Formula | Lucide | `pencil` | `#086ddd` | `#027aff` | 440 |
| `keypoint` | `[data-callout="keypoint"]` | Keypoint | Tabler Outline | `target-arrow` | `#ff5722` | `#ff8a65` | 536 |

> **注意图标名的前缀差异**：配置里 `idea` / `motivation` / `theorem` / `context` 的图标值写作 `lucide-lightbulb` / `lucide-sparkles` / `lucide-function-square` / `lucide-map-pin`（带 `lucide-` 前缀），
> 但真实文件名是 `lightbulb` / `sparkles` / `function-square` / `map-pin`。上表已用真实名。
> 另外 `todo` 用的 `check-circle-2` 在 Lucide 新版里已改名为 `circle-check-big`（旧名仍保留别名文件），本文档用的是配置里写的旧名 `check-circle-2`。

### A.2 每个图标的 SVG Path 数据

以下是各图标的原始 `d` 属性（多个 path 用 ` | ` 分隔），可直接用于 `<svg><path d="...">` 或自定义封装。

#### `abstract` — lucide / `clipboard-list`

```
M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2 | M12 11h4 | M12 16h4 | M8 11h.01 | M8 16h.01
```

#### `danger` — lucide / `zap`

```
M15.914 4a1.5 1.5 0 00-2.474-1.561l-9 9A1.5 1.5 0 005.5 14h4.002a.5.5 0 01.471.666L8.086 20a1.5 1.5 0 002.475 1.56l9-9A1.5 1.5 0 0018.5 10h-3.997a.5.5 0 01-.472-.667z
```

#### `example` — lucide / `list`

```
M3 5h.01 | M3 12h.01 | M3 19h.01 | M8 5h13 | M8 12h13 | M8 19h13
```

#### `failure` — lucide / `x`

```
M18 6 6 18 | m6 6 12 12
```

#### `info` — lucide / `info`

```
M12 16v-4 | M12 8h.01
```

#### `note` — lucide / `pencil`

```
M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z | m15 5 4 4
```

#### `question` — lucide / `help-circle`

```
M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3 | M12 17h.01
```

#### `quote` — lucide / `quote`

```
M16 3a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2 1 1 0 0 1 1 1v1a2 2 0 0 1-2 2 1 1 0 0 0-1 1v2a1 1 0 0 0 1 1 6 6 0 0 0 6-6V5a2 2 0 0 0-2-2z | M5 3a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2 1 1 0 0 1 1 1v1a2 2 0 0 1-2 2 1 1 0 0 0-1 1v2a1 1 0 0 0 1 1 6 6 0 0 0 6-6V5a2 2 0 0 0-2-2z
```

#### `success` — lucide / `check`

```
M20 6 9 17l-5-5
```

#### `tip` — lucide / `flame`

```
M12 3q1 4 4 6.5t3 5.5a1 1 0 0 1-14 0 5 5 0 0 1 1-3 1 1 0 0 0 5 0c0-2-1.5-3-1.5-5q0-2 2.5-4
```

#### `todo` — lucide / `check-circle-2`

```
m16 9-5.5 5.5L8 12
```

#### `warning` — lucide / `alert-triangle`

```
m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3 | M12 9v4 | M12 17h.01
```

#### `highlight` — octicons / `sparkles-fill`

```
M14.4 3.419a.639.639 0 0 1 1.2 0l.61 1.668a9.587 9.587 0 0 0 5.703 5.703l1.668.61a.639.639 0 0 1 0 1.2l-1.668.61a9.587 9.587 0 0 0-5.703 5.703l-.61 1.668a.639.639 0 0 1-1.2 0l-.61-1.668a9.587 9.587 0 0 0-5.703-5.703l-1.668-.61a.639.639 0 0 1 0-1.2l1.668-.61a9.587 9.587 0 0 0 5.703-5.703l.61-1.668ZM8 16.675a.266.266 0 0 1 .5 0l.254.694a3.992 3.992 0 0 0 2.376 2.377l.695.254a.266.266 0 0 1 0 .5l-.695.254a3.992 3.992 0 0 0-2.376 2.377l-.254.694a.266.266 0 0 1-.5 0l-.254-.694a3.992 3.992 0 0 0-2.376-2.377l-.695-.254a.266.266 0 0 1 0-.5l.695-.254a3.992 3.992 0 0 0 2.376-2.377L8 16.675ZM4.2.21a.32.32 0 0 1 .6 0l.305.833a4.793 4.793 0 0 0 2.852 2.852l.833.305a.32.32 0 0 1 0 .6l-.833.305a4.793 4.793 0 0 0-2.852 2.852L4.8 8.79a.32.32 0 0 1-.6 0l-.305-.833a4.793 4.793 0 0 0-2.852-2.852L.21 4.8a.32.32 0 0 1 0-.6l.833-.305a4.793 4.793 0 0 0 2.852-2.852L4.2.21Z
```

#### `definition` — material / `book_ribbon`

```
M452-250v-427q-45-30-97.62-46.5Q301.76-740 248-740q-38 0-74.5 9.5T100-707v434q31-14 70.5-20.5T248-300q53.57 0 104.28 12.5Q403-275 452-250Zm30 90q-51-38-111-58.5T248-239q-36.54 0-71.77 9T106-208q-23.1 11-44.55-3Q40-225 40-251v-463q0-15 7-27.5T68-761q42-20 87.39-29.5 45.4-9.5 92.61-9.5 75 0 130.5 19.5T494-723q8 5 13 13.5t5 19.5v440q50-25 98-37.5T712-300q38 0 78.5 6t69.5 16v-496q7.84 2.65 15.42 5.82Q883-765 891-761q14 7 21.5 19.5T920-714v463q0 27.89-22.5 42.45Q875-194 853-208q-34-14-69.23-22.5Q748.54-239 712-239q-63 0-121 21t-109 58Zm130-227v-443l148-50v445l-148 48ZM276-495Z
```

#### `conclusion` — lucide / `badge-check`

```
M3.85 8.62a4 4 0 0 1 4.78-4.77 4 4 0 0 1 6.74 0 4 4 0 0 1 4.78 4.78 4 4 0 0 1 0 6.74 4 4 0 0 1-4.77 4.78 4 4 0 0 1-6.75 0 4 4 0 0 1-4.78-4.77 4 4 0 0 1 0-6.76Z | m16 9-5.5 5.5L8 12
```

#### `idea` — lucide / `lightbulb`

```
M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5 | M9 18h6 | M10 22h4
```

#### `motivation` — lucide / `sparkles`

```
M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z | M20 2v4 | M22 4h-4
```

#### `theorem` — lucide / `function-square`

```
M9 17c2 0 2.8-1 2.8-2.8V10c0-2 1-3.3 3.2-3 | M9 11.2h5.7
```

#### `context` — lucide / `map-pin`

```
M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0
```

#### `formula` — lucide / `pencil`

```
M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z | m15 5 4 4
```

#### `keypoint` — tabler-outline / `target-arrow`

```
M0 0h24v24H0z | M11 12a1 1 0 1 0 2 0a1 1 0 1 0 -2 0 | M12 7a5 5 0 1 0 5 5 | M13 3.055a9 9 0 1 0 7.941 7.945 | M15 6v3h3l3 -3h-3v-3l-3 3 | M15 9l-3 3
```
### A.3 未清理的占位项（9 个）

这些条目仍存在于 `data.json` 里，但**没有在网页里使用**，也不生成 CSS：

| ID | 问题 | 建议 |
|---|---|---|
| `capacities-body` `capacities-card` `capacities-card-prop` `capacities-index` `capacities-prop` `capacities-prop-image` `capacities-sidebar` | 来自 Capacities 导出模板，7 个，图标都是通用 `pencil` | 删除 |
| `seealso` | 自建但图标是通用 `pencil` | 删除或换图标 |
| `bot` | 同上 | 删除或换图标 |

> 2026-10-24 那次清理已移除 15 个：`数学笔记的基本原则`、`例子1.1.1`~`例子1.4.2`（13 个）、`trick 1.2.1`、`trick 1.3.1`、`例子1.2`、`<%= it.colorname %>`（EJS 模板残留）。

---

## Part B: HTML 渲染结构示例

### B.1 标准结构（展开状态）

```html
<details class="callout theorem"
         data-callout="theorem"
         open>
  <summary class="callout-title">定理 1.0.1</summary>
  <div class="callout-content" markdown="block">

  可列个可列集之并也是可列集。

  </div>
</details>
```

要点：

| 属性 / 元素 | 作用 |
|---|---|
| `class="callout xxx"` | 提供 `.callout` 基础样式；`xxx` 是类型名（供自定义扩展用，CSS 主要靠 `data-callout` 匹配） |
| `data-callout="xxx"` | **CSS 的实际匹配依据**，必须是上表 A.1 里的 ID 之一 |
| `markdown="block"` | 让 kramdown 解析内部 Markdown。**只加在这个内层 `<div>` 上**，绝不能加到 `<details>` 上（见 B.5 前的坑） |
| `open` | 默认展开。折叠状态下省略此属性 |
| `<summary class="callout-title">` | 标题行，CSS 通过 `::before` 在此插入图标 |
| `<div class="callout-content">` | 正文容器 |

### B.2 折叠状态

```html
<details class="callout note" data-callout="note">
  <summary class="callout-title">点击展开</summary>
  <div class="callout-content" markdown="block">

  折叠的内容。

  </div>
</details>
```

Obsidian 的折叠约定：`[!note]` 和 `[!note]+` 都默认**展开**，只有 `[!note]-` 才折叠。

### B.3 带块 ID（锚点跳转）

```html
<details class="callout keypoint" id="kp01" data-callout="keypoint" open>
  <summary class="callout-title">一句话理解</summary>
  <div class="callout-content" markdown="block">

  内容

  </div>
</details>
```

配合 CSS 的 `scroll-margin-top` 可以避免锚点跳转时被固定导航栏遮住：

```css
.callout[id],
.callout-content [id] {
  scroll-margin-top: 88px;
}
```

### B.4 嵌套 Callout

**不要嵌套**。`<details>` 嵌套会导致折叠状态互相干扰，且多数 Markdown 解析器处理 `markdown="block"` 嵌套时不可靠。需要分层表达时，用「主 callout + 内部小标题」代替。

> ⚠️ **踩过的坑（2026-10-24）**：`markdown="block"` **只能加在内层 `<div class="callout-content">` 上，
> 绝不能加在 `<details>` 上**。加在 `<details>` 上时，kramdown 会把整个 details 的内容按块级 Markdown 解析，
> 而 `<summary>` 不在它认识的块级 HTML 标签列表里，于是 `<summary>` / `</div>` / `</details>` 全部被当作
> 普通文本输出 —— 表现为**标签直接暴露在页面上、`<details>` 无法闭合、后面的 callout 全部被吞进前一个
> （左侧边框看起来"一级套一级"）**。
>
> 同理 **不要开 `parse_block_html: true`**：它会让所有 HTML 块内部都按 Markdown 解析，放大这个问题。
> `markdown="block"` 是独立机制，不需要 `parse_block_html` 也能生效。
### B.5 Jekyll 必配项

```yaml
# _config.yml
markdown: kramdown
kramdown:
  math_engine: mathjax
  input: GFM
  hard_wrap: false
  # 不要加 parse_block_html！它会让 <summary> 等标签暴露成文本
```

### B.6 生成 callout 的最小 Python 片段

```python
import re

# 支持带空格的类型名（如 "key point"），但不允许首尾空格
_CALLOUT_HEAD_RE = re.compile(
    r"^[ \t]*>[ \t]*\[!([A-Za-z0-9_-]+(?:[ \t]+[A-Za-z0-9_-]+)*)\]([+-]?)[ \t]*(.*)$"
)

def to_details(match_type: str, fold: str, title: str, body_lines: list[str]) -> str:
    open_attr = "" if fold == "-" else " open"
    title = title or match_type.capitalize()
    body = "\n".join(body_lines)
    return (
        f'<details class="callout {match_type}" data-callout="{match_type}"{open_attr}>\n'
        f'<summary class="callout-title">{title}</summary>\n'
        f'<div class="callout-content" markdown="block">\n\n{body}\n\n</div>\n'
        f'</details>\n'
    )
```

---

## Part C: 通用 CSS 代码

### C.1 设计要点

1. **一个变量控制全部颜色**：每个类型只声明 `--callout-color`，边框 / 标题 / 背景 / 图标全部从它派生。
2. **图标用 `mask` 而不是 `<img>`**：`background-color: var(--callout-color)` 就能给图标上色，暗色模式只改一个变量即可。
3. **暗色只覆盖颜色**，不重复声明图标（避免 base64 重复两遍，节省体积）。
4. **`--callout-icon` 是变量**，所以图标和颜色可以分开维护。

### C.2 完整代码

```css
/* ===== 基础结构与变量 ===== */
.callout {
  --callout-color: #086ddd;
  --callout-bg-opacity: 8%;
  border-left: 4px solid var(--callout-color);
  background-color: color-mix(in srgb, var(--callout-color) var(--callout-bg-opacity), transparent);
  padding: 12px 16px;
  margin: 16px 0;
  border-radius: 6px;
}

.callout-title {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 700;
  color: var(--callout-color);
  margin-bottom: 8px;
  list-style: none;
}

/* 彩色图标：mask 上色，颜色由 --callout-color 控制（亮暗自动切换） */
.callout-title::before {
  content: "";
  width: 1.1em;
  height: 1.1em;
  flex: 0 0 auto;
  background-color: var(--callout-color);
  -webkit-mask: var(--callout-icon) center / contain no-repeat;
          mask: var(--callout-icon) center / contain no-repeat;
}

/* ===== 每种类型：只声明颜色 + 图标 ===== */

/* Abstract — lucide / clipboard-list */
.callout[data-callout="abstract"] {
  --callout-color: #00bfa5;
  --callout-icon: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiA+PHJlY3QgeD0iOCIgeT0iMiIgcng9IjEiIHJ5PSIxIiAvPjxwYXRoIGQ9Ik0xNiA0aDJhMiAyIDAgMCAxIDIgMnYxNGEyIDIgMCAwIDEtMiAySDZhMiAyIDAgMCAxLTItMlY2YTIgMiAwIDAgMSAyLTJoMiIgLz48cGF0aCBkPSJNMTIgMTFoNCIgLz48cGF0aCBkPSJNMTIgMTZoNCIgLz48cGF0aCBkPSJNOCAxMWguMDEiIC8+PHBhdGggZD0iTTggMTZoLjAxIiAvPjwvc3ZnPg==");
}

/* Danger — lucide / zap */
.callout[data-callout="danger"] {
  --callout-color: #e93147;
  --callout-icon: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiA+PHBhdGggZD0iTTE1LjkxNCA0YTEuNSAxLjUgMCAwMC0yLjQ3NC0xLjU2MWwtOSA5QTEuNSAxLjUgMCAwMDUuNSAxNGg0LjAwMmEuNS41IDAgMDEuNDcxLjY2Nkw4LjA4NiAyMGExLjUgMS41IDAgMDAyLjQ3NSAxLjU2bDktOUExLjUgMS41IDAgMDAxOC41IDEwaC0zLjk5N2EuNS41IDAgMDEtLjQ3Mi0uNjY3eiIgLz48L3N2Zz4=");
}

/* Example — lucide / list */
.callout[data-callout="example"] {
  --callout-color: #7852ee;
  --callout-icon: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiA+PHBhdGggZD0iTTMgNWguMDEiIC8+PHBhdGggZD0iTTMgMTJoLjAxIiAvPjxwYXRoIGQ9Ik0zIDE5aC4wMSIgLz48cGF0aCBkPSJNOCA1aDEzIiAvPjxwYXRoIGQ9Ik04IDEyaDEzIiAvPjxwYXRoIGQ9Ik04IDE5aDEzIiAvPjwvc3ZnPg==");
}

/* Failure — lucide / x */
.callout[data-callout="failure"] {
  --callout-color: #e93147;
  --callout-icon: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiA+PHBhdGggZD0iTTE4IDYgNiAxOCIgLz48cGF0aCBkPSJtNiA2IDEyIDEyIiAvPjwvc3ZnPg==");
}

/* Info — lucide / info */
.callout[data-callout="info"] {
  --callout-color: #086ddd;
  --callout-icon: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiA+PGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iMTAiIC8+PHBhdGggZD0iTTEyIDE2di00IiAvPjxwYXRoIGQ9Ik0xMiA4aC4wMSIgLz48L3N2Zz4=");
}

/* Note — lucide / pencil */
.callout[data-callout="note"] {
  --callout-color: #086ddd;
  --callout-icon: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiA+PHBhdGggZD0iTTIxLjE3NCA2LjgxMmExIDEgMCAwIDAtMy45ODYtMy45ODdMMy44NDIgMTYuMTc0YTIgMiAwIDAgMC0uNS44M2wtMS4zMjEgNC4zNTJhLjUuNSAwIDAgMCAuNjIzLjYyMmw0LjM1My0xLjMyYTIgMiAwIDAgMCAuODMtLjQ5N3oiIC8+PHBhdGggZD0ibTE1IDUgNCA0IiAvPjwvc3ZnPg==");
}

/* Question — lucide / help-circle */
.callout[data-callout="question"] {
  --callout-color: #ec7500;
  --callout-icon: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiA+PGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iMTAiIC8+PHBhdGggZD0iTTkuMDkgOWEzIDMgMCAwIDEgNS44MyAxYzAgMi0zIDMtMyAzIiAvPjxwYXRoIGQ9Ik0xMiAxN2guMDEiIC8+PC9zdmc+");
}

/* Quote — lucide / quote */
.callout[data-callout="quote"] {
  --callout-color: #9e9e9e;
  --callout-icon: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiA+PHBhdGggZD0iTTE2IDNhMiAyIDAgMCAwLTIgMnY2YTIgMiAwIDAgMCAyIDIgMSAxIDAgMCAxIDEgMXYxYTIgMiAwIDAgMS0yIDIgMSAxIDAgMCAwLTEgMXYyYTEgMSAwIDAgMCAxIDEgNiA2IDAgMCAwIDYtNlY1YTIgMiAwIDAgMC0yLTJ6IiAvPjxwYXRoIGQ9Ik01IDNhMiAyIDAgMCAwLTIgMnY2YTIgMiAwIDAgMCAyIDIgMSAxIDAgMCAxIDEgMXYxYTIgMiAwIDAgMS0yIDIgMSAxIDAgMCAwLTEgMXYyYTEgMSAwIDAgMCAxIDEgNiA2IDAgMCAwIDYtNlY1YTIgMiAwIDAgMC0yLTJ6IiAvPjwvc3ZnPg==");
}

/* Success — lucide / check */
.callout[data-callout="success"] {
  --callout-color: #08b94e;
  --callout-icon: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiA+PHBhdGggZD0iTTIwIDYgOSAxN2wtNS01IiAvPjwvc3ZnPg==");
}

/* Tip — lucide / flame */
.callout[data-callout="tip"] {
  --callout-color: #00bfbc;
  --callout-icon: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiA+PHBhdGggZD0iTTEyIDNxMSA0IDQgNi41dDMgNS41YTEgMSAwIDAgMS0xNCAwIDUgNSAwIDAgMSAxLTMgMSAxIDAgMCAwIDUgMGMwLTItMS41LTMtMS41LTVxMC0yIDIuNS00IiAvPjwvc3ZnPg==");
}

/* Todo — lucide / check-circle-2 */
.callout[data-callout="todo"] {
  --callout-color: #086ddd;
  --callout-icon: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiA+PGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iMTAiIC8+PHBhdGggZD0ibTE2IDktNS41IDUuNUw4IDEyIiAvPjwvc3ZnPg==");
}

/* Warning — lucide / alert-triangle */
.callout[data-callout="warning"] {
  --callout-color: #ec7500;
  --callout-icon: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiA+PHBhdGggZD0ibTIxLjczIDE4LTgtMTRhMiAyIDAgMCAwLTMuNDggMGwtOCAxNEEyIDIgMCAwIDAgNCAyMWgxNmEyIDIgMCAwIDAgMS43My0zIiAvPjxwYXRoIGQ9Ik0xMiA5djQiIC8+PHBhdGggZD0iTTEyIDE3aC4wMSIgLz48L3N2Zz4=");
}

/* Highlight — octicons / sparkles-fill */
.callout[data-callout="highlight"] {
  --callout-color: #086ddd;
  --callout-icon: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE0LjQgMy40MTlhLjYzOS42MzkgMCAwIDEgMS4yIDBsLjYxIDEuNjY4YTkuNTg3IDkuNTg3IDAgMCAwIDUuNzAzIDUuNzAzbDEuNjY4LjYxYS42MzkuNjM5IDAgMCAxIDAgMS4ybC0xLjY2OC42MWE5LjU4NyA5LjU4NyAwIDAgMC01LjcwMyA1LjcwM2wtLjYxIDEuNjY4YS42MzkuNjM5IDAgMCAxLTEuMiAwbC0uNjEtMS42NjhhOS41ODcgOS41ODcgMCAwIDAtNS43MDMtNS43MDNsLTEuNjY4LS42MWEuNjM5LjYzOSAwIDAgMSAwLTEuMmwxLjY2OC0uNjFhOS41ODcgOS41ODcgMCAwIDAgNS43MDMtNS43MDNsLjYxLTEuNjY4Wk04IDE2LjY3NWEuMjY2LjI2NiAwIDAgMSAuNSAwbC4yNTQuNjk0YTMuOTkyIDMuOTkyIDAgMCAwIDIuMzc2IDIuMzc3bC42OTUuMjU0YS4yNjYuMjY2IDAgMCAxIDAgLjVsLS42OTUuMjU0YTMuOTkyIDMuOTkyIDAgMCAwLTIuMzc2IDIuMzc3bC0uMjU0LjY5NGEuMjY2LjI2NiAwIDAgMS0uNSAwbC0uMjU0LS42OTRhMy45OTIgMy45OTIgMCAwIDAtMi4zNzYtMi4zNzdsLS42OTUtLjI1NGEuMjY2LjI2NiAwIDAgMSAwLS41bC42OTUtLjI1NGEzLjk5MiAzLjk5MiAwIDAgMCAyLjM3Ni0yLjM3N0w4IDE2LjY3NVpNNC4yLjIxYS4zMi4zMiAwIDAgMSAuNiAwbC4zMDUuODMzYTQuNzkzIDQuNzkzIDAgMCAwIDIuODUyIDIuODUybC44MzMuMzA1YS4zMi4zMiAwIDAgMSAwIC42bC0uODMzLjMwNWE0Ljc5MyA0Ljc5MyAwIDAgMC0yLjg1MiAyLjg1Mkw0LjggOC43OWEuMzIuMzIgMCAwIDEtLjYgMGwtLjMwNS0uODMzYTQuNzkzIDQuNzkzIDAgMCAwLTIuODUyLTIuODUyTC4yMSA0LjhhLjMyLjMyIDAgMCAxIDAtLjZsLjgzMy0uMzA1YTQuNzkzIDQuNzkzIDAgMCAwIDIuODUyLTIuODUyTDQuMi4yMVoiLz48L3N2Zz4=");
}

/* Definition — material / book_ribbon */
.callout[data-callout="definition"] {
  --callout-color: #086ddd;
  --callout-icon: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgLTk2MCA5NjAgOTYwIj48cGF0aCBkPSJNNDUyLTI1MHYtNDI3cS00NS0zMC05Ny42Mi00Ni41UTMwMS43Ni03NDAgMjQ4LTc0MHEtMzggMC03NC41IDkuNVQxMDAtNzA3djQzNHEzMS0xNCA3MC41LTIwLjVUMjQ4LTMwMHE1My41NyAwIDEwNC4yOCAxMi41UTQwMy0yNzUgNDUyLTI1MFptMzAgOTBxLTUxLTM4LTExMS01OC41VDI0OC0yMzlxLTM2LjU0IDAtNzEuNzcgOVQxMDYtMjA4cS0yMy4xIDExLTQ0LjU1LTNRNDAtMjI1IDQwLTI1MXYtNDYzcTAtMTUgNy0yNy41VDY4LTc2MXE0Mi0yMCA4Ny4zOS0yOS41IDQ1LjQtOS41IDkyLjYxLTkuNSA3NSAwIDEzMC41IDE5LjVUNDk0LTcyM3E4IDUgMTMgMTMuNXQ1IDE5LjV2NDQwcTUwLTI1IDk4LTM3LjVUNzEyLTMwMHEzOCAwIDc4LjUgNnQ2OS41IDE2di00OTZxNy44NCAyLjY1IDE1LjQyIDUuODJRODgzLTc2NSA4OTEtNzYxcTE0IDcgMjEuNSAxOS41VDkyMC03MTR2NDYzcTAgMjcuODktMjIuNSA0Mi40NVE4NzUtMTk0IDg1My0yMDhxLTM0LTE0LTY5LjIzLTIyLjVRNzQ4LjU0LTIzOSA3MTItMjM5cS02MyAwLTEyMSAyMXQtMTA5IDU4Wm0xMzAtMjI3di00NDNsMTQ4LTUwdjQ0NWwtMTQ4IDQ4Wk0yNzYtNDk1WiIvPjwvc3ZnPg==");
}

/* Conclusion — lucide / badge-check */
.callout[data-callout="conclusion"] {
  --callout-color: #086ddd;
  --callout-icon: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiA+PHBhdGggZD0iTTMuODUgOC42MmE0IDQgMCAwIDEgNC43OC00Ljc3IDQgNCAwIDAgMSA2Ljc0IDAgNCA0IDAgMCAxIDQuNzggNC43OCA0IDQgMCAwIDEgMCA2Ljc0IDQgNCAwIDAgMS00Ljc3IDQuNzggNCA0IDAgMCAxLTYuNzUgMCA0IDQgMCAwIDEtNC43OC00Ljc3IDQgNCAwIDAgMSAwLTYuNzZaIiAvPjxwYXRoIGQ9Im0xNiA5LTUuNSA1LjVMOCAxMiIgLz48L3N2Zz4=");
}

/* Idea — lucide / lightbulb */
.callout[data-callout="idea"] {
  --callout-color: #afb42b;
  --callout-icon: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiA+PHBhdGggZD0iTTE1IDE0Yy4yLTEgLjctMS43IDEuNS0yLjUgMS0uOSAxLjUtMi4yIDEuNS0zLjVBNiA2IDAgMCAwIDYgOGMwIDEgLjIgMi4yIDEuNSAzLjUuNy43IDEuMyAxLjUgMS41IDIuNSIgLz48cGF0aCBkPSJNOSAxOGg2IiAvPjxwYXRoIGQ9Ik0xMCAyMmg0IiAvPjwvc3ZnPg==");
}

/* Motivation — lucide / sparkles */
.callout[data-callout="motivation"] {
  --callout-color: #ec7500;
  --callout-icon: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiA+PHBhdGggZD0iTTExLjAxNyAyLjgxNGExIDEgMCAwIDEgMS45NjYgMGwxLjA1MSA1LjU1OGEyIDIgMCAwIDAgMS41OTQgMS41OTRsNS41NTggMS4wNTFhMSAxIDAgMCAxIDAgMS45NjZsLTUuNTU4IDEuMDUxYTIgMiAwIDAgMC0xLjU5NCAxLjU5NGwtMS4wNTEgNS41NThhMSAxIDAgMCAxLTEuOTY2IDBsLTEuMDUxLTUuNTU4YTIgMiAwIDAgMC0xLjU5NC0xLjU5NGwtNS41NTgtMS4wNTFhMSAxIDAgMCAxIDAtMS45NjZsNS41NTgtMS4wNTFhMiAyIDAgMCAwIDEuNTk0LTEuNTk0eiIgLz48cGF0aCBkPSJNMjAgMnY0IiAvPjxwYXRoIGQ9Ik0yMiA0aC00IiAvPjxjaXJjbGUgY3g9IjQiIGN5PSIyMCIgcj0iMiIgLz48L3N2Zz4=");
}

/* Theorem — lucide / function-square */
.callout[data-callout="theorem"] {
  --callout-color: #086ddd;
  --callout-icon: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiA+PHJlY3QgeD0iMyIgeT0iMyIgcng9IjIiIHJ5PSIyIiAvPjxwYXRoIGQ9Ik05IDE3YzIgMCAyLjgtMSAyLjgtMi44VjEwYzAtMiAxLTMuMyAzLjItMyIgLz48cGF0aCBkPSJNOSAxMS4yaDUuNyIgLz48L3N2Zz4=");
}

/* Context — lucide / map-pin */
.callout[data-callout="context"] {
  --callout-color: #00bfbc;
  --callout-icon: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiA+PHBhdGggZD0iTTIwIDEwYzAgNC45OTMtNS41MzkgMTAuMTkzLTcuMzk5IDExLjc5OWExIDEgMCAwIDEtMS4yMDIgMEM5LjUzOSAyMC4xOTMgNCAxNC45OTMgNCAxMGE4IDggMCAwIDEgMTYgMCIgLz48Y2lyY2xlIGN4PSIxMiIgY3k9IjEwIiByPSIzIiAvPjwvc3ZnPg==");
}

/* Formula — lucide / pencil */
.callout[data-callout="formula"] {
  --callout-color: #086ddd;
  --callout-icon: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiA+PHBhdGggZD0iTTIxLjE3NCA2LjgxMmExIDEgMCAwIDAtMy45ODYtMy45ODdMMy44NDIgMTYuMTc0YTIgMiAwIDAgMC0uNS44M2wtMS4zMjEgNC4zNTJhLjUuNSAwIDAgMCAuNjIzLjYyMmw0LjM1My0xLjMyYTIgMiAwIDAgMCAuODMtLjQ5N3oiIC8+PHBhdGggZD0ibTE1IDUgNCA0IiAvPjwvc3ZnPg==");
}

/* Keypoint — tabler-outline / target-arrow */
.callout[data-callout="keypoint"] {
  --callout-color: #ff5722;
  --callout-icon: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiA+PHBhdGggc3Ryb2tlPSJub25lIiBkPSJNMCAwaDI0djI0SDB6IiBmaWxsPSJub25lIiAvPjxwYXRoIGQ9Ik0xMSAxMmExIDEgMCAxIDAgMiAwYTEgMSAwIDEgMCAtMiAwIiAvPjxwYXRoIGQ9Ik0xMiA3YTUgNSAwIDEgMCA1IDUiIC8+PHBhdGggZD0iTTEzIDMuMDU1YTkgOSAwIDEgMCA3Ljk0MSA3Ljk0NSIgLz48cGF0aCBkPSJNMTUgNnYzaDNsMyAtM2gtM3YtM2wtMyAzIiAvPjxwYXRoIGQ9Ik0xNSA5bC0zIDMiIC8+PC9zdmc+");
}

/* ===== 暗色：只覆盖颜色，图标和结构不变 ===== */
@media (prefers-color-scheme: dark) {
  .callout[data-callout="danger"] { --callout-color: #fb464c; }
  .callout[data-callout="example"] { --callout-color: #a882ff; }
  .callout[data-callout="failure"] { --callout-color: #fb464c; }
  .callout[data-callout="info"] { --callout-color: #027aff; }
  .callout[data-callout="note"] { --callout-color: #027aff; }
  .callout[data-callout="question"] { --callout-color: #e9973f; }
  .callout[data-callout="success"] { --callout-color: #44cf6e; }
  .callout[data-callout="tip"] { --callout-color: #53dfdd; }
  .callout[data-callout="todo"] { --callout-color: #027aff; }
  .callout[data-callout="warning"] { --callout-color: #e9973f; }
  .callout[data-callout="highlight"] { --callout-color: #027aff; }
  .callout[data-callout="definition"] { --callout-color: #027aff; }
  .callout[data-callout="conclusion"] { --callout-color: #027aff; }
  .callout[data-callout="idea"] { --callout-color: #dce775; }
  .callout[data-callout="motivation"] { --callout-color: #e9973f; }
  .callout[data-callout="theorem"] { --callout-color: #027aff; }
  .callout[data-callout="context"] { --callout-color: #53dfdd; }
  .callout[data-callout="formula"] { --callout-color: #027aff; }
  .callout[data-callout="keypoint"] { --callout-color: #ff8a65; }
}

/* 手动切到暗色（覆盖系统亮色） */
html[data-theme="dark"] .callout[data-callout="danger"] { --callout-color: #fb464c; }
html[data-theme="dark"] .callout[data-callout="example"] { --callout-color: #a882ff; }
html[data-theme="dark"] .callout[data-callout="failure"] { --callout-color: #fb464c; }
html[data-theme="dark"] .callout[data-callout="info"] { --callout-color: #027aff; }
html[data-theme="dark"] .callout[data-callout="note"] { --callout-color: #027aff; }
html[data-theme="dark"] .callout[data-callout="question"] { --callout-color: #e9973f; }
html[data-theme="dark"] .callout[data-callout="success"] { --callout-color: #44cf6e; }
html[data-theme="dark"] .callout[data-callout="tip"] { --callout-color: #53dfdd; }
html[data-theme="dark"] .callout[data-callout="todo"] { --callout-color: #027aff; }
html[data-theme="dark"] .callout[data-callout="warning"] { --callout-color: #e9973f; }
html[data-theme="dark"] .callout[data-callout="highlight"] { --callout-color: #027aff; }
html[data-theme="dark"] .callout[data-callout="definition"] { --callout-color: #027aff; }
html[data-theme="dark"] .callout[data-callout="conclusion"] { --callout-color: #027aff; }
html[data-theme="dark"] .callout[data-callout="idea"] { --callout-color: #dce775; }
html[data-theme="dark"] .callout[data-callout="motivation"] { --callout-color: #e9973f; }
html[data-theme="dark"] .callout[data-callout="theorem"] { --callout-color: #027aff; }
html[data-theme="dark"] .callout[data-callout="context"] { --callout-color: #53dfdd; }
html[data-theme="dark"] .callout[data-callout="formula"] { --callout-color: #027aff; }
html[data-theme="dark"] .callout[data-callout="keypoint"] { --callout-color: #ff8a65; }

/* 手动切到亮色（覆盖系统暗色） */
html[data-theme="light"] .callout[data-callout="abstract"] { --callout-color: #00bfa5; }
html[data-theme="light"] .callout[data-callout="danger"] { --callout-color: #e93147; }
html[data-theme="light"] .callout[data-callout="example"] { --callout-color: #7852ee; }
html[data-theme="light"] .callout[data-callout="failure"] { --callout-color: #e93147; }
html[data-theme="light"] .callout[data-callout="info"] { --callout-color: #086ddd; }
html[data-theme="light"] .callout[data-callout="note"] { --callout-color: #086ddd; }
html[data-theme="light"] .callout[data-callout="question"] { --callout-color: #ec7500; }
html[data-theme="light"] .callout[data-callout="quote"] { --callout-color: #9e9e9e; }
html[data-theme="light"] .callout[data-callout="success"] { --callout-color: #08b94e; }
html[data-theme="light"] .callout[data-callout="tip"] { --callout-color: #00bfbc; }
html[data-theme="light"] .callout[data-callout="todo"] { --callout-color: #086ddd; }
html[data-theme="light"] .callout[data-callout="warning"] { --callout-color: #ec7500; }
html[data-theme="light"] .callout[data-callout="highlight"] { --callout-color: #086ddd; }
html[data-theme="light"] .callout[data-callout="definition"] { --callout-color: #086ddd; }
html[data-theme="light"] .callout[data-callout="conclusion"] { --callout-color: #086ddd; }
html[data-theme="light"] .callout[data-callout="idea"] { --callout-color: #afb42b; }
html[data-theme="light"] .callout[data-callout="motivation"] { --callout-color: #ec7500; }
html[data-theme="light"] .callout[data-callout="theorem"] { --callout-color: #086ddd; }
html[data-theme="light"] .callout[data-callout="context"] { --callout-color: #00bfbc; }
html[data-theme="light"] .callout[data-callout="formula"] { --callout-color: #086ddd; }
html[data-theme="light"] .callout[data-callout="keypoint"] { --callout-color: #ff5722; }

/* ==========================================================================
   补充：正文区、折叠标记与折叠指示
   （纯 CSS 三角，不依赖任何图标字体）
   ========================================================================== */

.callout-content > :first-child { margin-top: 0; }
.callout-content > :last-child { margin-bottom: 0; }

.callout > summary.callout-title {
  cursor: pointer;
  user-select: none;
}

/* 去掉 <summary> 的原生三角，否则会和我们的图标并排出现两个标记 */
.callout > summary.callout-title::-webkit-details-marker {
  display: none;
}

.callout > summary.callout-title::marker {
  content: "";
}

/* 折叠指示三角：颜色跟随 --callout-color */
.callout > summary.callout-title::after {
  content: "";
  width: 0;
  height: 0;
  margin-left: auto;
  flex: 0 0 auto;
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: 6px solid currentColor;
  opacity: 0.7;
  transition: transform 0.2s ease;
}

.callout:not([open]) > summary.callout-title::after {
  transform: rotate(-90deg);
}

/* ===== 兼容：旧写法 "key point"（带空格） ===== */
.callout[data-callout="key point"] {
  --callout-color: #ff5722;
}
```
### C.3 兼容性说明

| 特性 | 支持情况 |
|---|---|
| CSS `mask` | Chrome 120+ / Safari 15.4+（`-webkit-mask` 兜底更早）/ Firefox 53+ |
| `color-mix()` | Chrome 111+ / Safari 16.2+ / Firefox 113+ |

如果必须支持更老的浏览器，把背景色改成显式的 `rgba()`：

```css
/* 老浏览器兜底：先给一个固定淡色，再用 color-mix 覆盖 */
.callout { background-color: rgba(8, 109, 221, 0.08); }
@supports (background-color: color-mix(in srgb, red 8%, transparent)) {
  .callout {
    background-color: color-mix(in srgb, var(--callout-color) var(--callout-bg-opacity), transparent);
  }
}
```

### C.4 带空格的旧类型名兼容

`keypoint` 在旧版本配置里叫 `key point`（带空格）。若文档里仍有这种写法，**不要把 base64 再抄一遍**，直接把选择器并列写进同一组规则：

```css
/* Part C.2 里 keypoint 那一条，把选择器改成两个并列 */
.callout[data-callout="keypoint"],
.callout[data-callout="key point"] {
  --callout-color: #ff5722;
  --callout-icon: url("data:image/svg+xml;base64,……");   /* 与 keypoint 共用同一份 */
}
```

> ⚠️ **不要**写成 `--callout-icon: var(--callout-icon);` —— CSS 自定义属性不能自我引用，整条声明会被丢弃。
> 也**不能**在 A 选择器里声明变量、在 B 选择器里 `var()` 取出：变量只在元素上继承，不会在选择器之间传递。
> 只有两种正确做法：**选择器并列**（如上），或在生成阶段就把空格去掉（推荐，见 B.6）。

### C.5 全局改色 / 换主题

想整套换配色，只改这 20 行即可（不用碰 base64）：

```css
:root {
  --callout-info:     #086ddd;
  --callout-success:  #08b94e;
  --callout-warning:  #ec7500;
  --callout-danger:   #e93147;
}

.callout[data-callout="info"]    { --callout-color: var(--callout-info); }
.callout[data-callout="success"] { --callout-color: var(--callout-success); }
.callout[data-callout="warning"] { --callout-color: var(--callout-warning); }
.callout[data-callout="danger"]  { --callout-color: var(--callout-danger); }
```

### C.6 与本站现有文件的对应关系

本仓库里已有的 `assets/css/obsidian-callouts.css` 是早期手写的版本（用 Font Awesome 字体图标 + 硬编码颜色）。本文档的 Part C 是它的**升级版**：

| 项目 | 旧版（`obsidian-callouts.css`） | 本文档 Part C |
|---|---|---|
| 图标 | Font Awesome 字体字符（`content: "\f05a"`） | 官方 SVG + `mask` |
| 颜色 | 每个类型写死 4 处（边框/背景/图标/暗色） | 只写 1 个 `--callout-color` |
| 暗色 | 需要重复整段规则 | 只覆盖颜色变量 |
| 新增类型成本 | 要写 4~6 行 + 找 FA 对应字符 | 只写 2 行（颜色 + 图标） |

---

## 附录：数据提取命令

```powershell
# 1. 读配置
$cs = 'D:\szy\szy obsidian仓库\PaperBell\.obsidian\plugins\callout-studio'
$json = Get-Content (Join-Path $cs 'data.json') -Raw -Encoding UTF8 | ConvertFrom-Json
$json.callouts | ForEach-Object {
  '{0,-22} {1,-16} {2,-12} {3,-24} {4,-9} {5}' -f $_.id, $_.displayName, $_.icon.type, $_.icon.value, $_.colorLight, $_.colorDark
}

# 2. 拿图标包（国内需走镜像）
npm config set registry https://registry.npmmirror.com
npm pack lucide-static @primer/octicons @material-symbols/svg-400

# 3. SVG → base64
$svg = [System.IO.File]::ReadAllText('path/to/icon.svg')
$clean = ($svg -replace "`r?`n", '' -replace '>\s+<', '><').Trim()
[Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($clean))
```
