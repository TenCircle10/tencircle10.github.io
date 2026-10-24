# 个人网站技术指南 / TECH_GUIDE

> 本站 = **Jekyll + Minimal Light 主题**，部署在 GitHub Pages。
> 这份文档是"施工图"：架构、发布流、脚本能力、前端交互、排雷清单。
> 它本身已加入 `_config.yml` 的 `exclude`，不会被发布成网页。

**站点**：https://tencircle10.github.io/
**仓库**：https://github.com/TenCircle10/tencircle10.github.io

---

## 1. 项目架构与核心文件

### 1.1 主页与笔记的分离架构

两类页面由**两个完全独立的整页布局**渲染（都不继承主题的默认布局）：

| 角色 | 入口 | 布局 | URL |
|---|---|---|---|
| 主页 | `index.md`（`layout: homepage`） | `_layouts/homepage.html` | `/` |
| 笔记 | `notes/*.md`（脚本生成，`layout: note`） | `_layouts/note.html` | `/notes/<slug>/` |

- **主页**：经典 Minimal Light 结构 —— 左侧固定侧边栏（头像、社交图标、日夜开关、每日一言）+ 右侧正文
- **笔记页**：后来重做的「顶部导航栏 + 居中阅读区」结构，**没有侧边栏**
  - 顶栏：左=头像+昵称，中=笔记标题（`max-width: 50%` + 省略号），右=返回主页
  - 阅读区 `max-width: 860px` 居中；右下角有返回顶部按钮
- **笔记列表**：`notes.md` 是个没有 front matter 的片段，被 `index.md` 用 `include_relative` 引入；列表用 Liquid 遍历 `site.pages` 自动生成，并按文件名关键词（`test` / `torture` / `测试` / `demo`）过滤掉测试文件

> ⚠️ 布局里刻意用 `<nav>` / `<main>` 而不是 `<header>` / `<section>`：主题 `_sass` 里有 `header{position:fixed;width:232px}`、`section{width:650px;float:right}` 这类**元素选择器**，用 `<section>` 会被那套侧边栏布局命中。

### 1.2 核心配置文件

**`_config.yml`**

```yaml
title: TenCircle10 的主页
position: Student
affiliation: Beijing Institute of Technology(BIT)
email: 3503289621@qq.com
canonical: https://tencircle10.github.io/

enable_footnote: true
auto_dark_mode: true
font: "Serif"

remote_theme: yaoyao-liu/minimal-light@2.0   # 锁定版本，避免上游更新导致构建失败
markdown: kramdown
kramdown:
  math_engine: mathjax
  input: GFM
  hard_wrap: false
```

`exclude` 当前排除：`Gemfile`、`Gemfile.lock`、四个 README、`LICENSE`、`minimal-light.gemspec`、`html_source_file/`、`sync_notes.py`、`deploy.ps1`、`发布博客.bat`、`.gitignore`、`origin/`、`TECH_GUIDE.md`。

**`Gemfile`**（仅供本地参考；GitHub Pages 使用自己的 gem 环境）

```ruby
source "https://rubygems.org"
gem "jekyll", "~> 3.8.5"
gem "webrick", "~> 1.8"
```

> ⚠️ 本机**没有安装 Ruby**，无法 `jekyll build`。所有渲染结果只能在 push 后看线上。

### 1.3 自定义前端资源

| 资源 | 相关文件 | 说明 |
|---|---|---|
| 日夜切换开关 | `_includes/theme-switch.html` + `assets/css/publications.css` | Uiverse 手绘风（mamyapro123 版），`--toggle-size: 16px`，固定右上角 |
| 返回顶部按钮 | `_layouts/note.html` + `assets/css/notes.css` | Uiverse 展开式（vinodjangid07 版），滚动 300px 后出现 |
| 霞鹜文楷字体 | `assets/css/publications.css` 第 1 行 `@import` | 只用于侧边栏「每日一言」 |
| Giscus 评论 | `_includes/giscus.html` + `notes.css` / `publications.css` | 主页留言板 + 每篇文章独立评论区 |
| Callout 样式 | `assets/css/obsidian-callouts.css` | Obsidian Callout Studio 的 20 种类型，SVG mask + Base64 内联，详见 `callout-for-web.md` |

---

## 2. 日常写作与发布流（最重要）

### 2.1 标准流程

1. **在 Obsidian 里写笔记**，文件名直接用中文（如 `泛函分析.md`），**不需要手写任何 front matter**
2. 把文件放进项目根目录的 **`origin/`**（该目录被 `.gitignore` 忽略，原始笔记不会上传 GitHub）
3. 运行一键发布：
   ```powershell
   .\deploy.ps1
   ```
   或者**双击 `发布博客.bat`**（它是纯 ASCII 启动壳，内部调用 `deploy.ps1`）
4. 脚本自动完成：
   - 运行 `python sync_notes.py`，把 `origin/` 的笔记转换到 `notes/`
   - 检测到改动 → `git add .` + `git commit`（信息形如 `auto: sync notes and deploy 2026-10-18 23:30`）
   - 尝试 `git push origin main`
5. **实际推送由站长本人手动执行**

### 2.2 推送约定（重要）

> **约定**：脚本会尝试 push，但推送这件事一律由本人确认后手动执行：
>
> ```bash
> git push origin main
> ```
>
> - 网络不稳时会出现 `Connection was reset` / `Failed to connect ... :443`，开代理或切手机热点后重试
> - `deploy.ps1` 每次运行都会**顺带补推**本地积压的 commit（即使本次没有任何新改动）

### 2.3 不想用脚本时

```bash
python sync_notes.py          # 只做转换
git add -A
git commit -m "你的信息"
# push 自己来
```

---

## 3. Python 转换脚本 `sync_notes.py`

### 3.1 用法

```powershell
python sync_notes.py                           # origin/ -> notes/
python sync_notes.py --src other --dest out    # 自定义目录
```

### 3.2 能力清单

**① 元数据自动化**

| 能力 | 说明 |
|---|---|
| 拼音 slug | 中文文件名 → `pypinyin.lazy_pinyin()` → 小写 → 非字母数字压成 `-`。例：`数学学习漫谈——Attention` → `shu-xue-xue-xi-man-tan-attention` |
| emoji 兜底 | 拼音为空时用 `note-<正文 MD5 前 6 位>` |
| title 自动补 | 没有 `title` 就取原文件名（中文） |
| 强制注入 | `layout: note`、`permalink: /notes/<slug>/`、`render_with_liquid: false` |
| 手写优先 | front matter 里显式写的 `slug` / `title` 永远优先于自动生成 |

**② Liquid 防爆**

- front matter 强制写 `render_with_liquid: false`（Jekyll 4+ 生效；GitHub Pages 的 Jekyll 3.9 会忽略）
- 正文里的 `{{` 与百分号-花括号标签在流水线最后统一转成 HTML 实体（`&#123;&#123;` / `&#123;%`）—— **这一条对 3.9 真正有效**
- 之所以要在最后一步做：Jekyll 是**先跑 Liquid 再跑 Markdown**，连代码块里的 `{{` 也会被解析

**③ LaTeX 公式处理**

- 定界符统一：`\(...\)` → `$...$`；`\[...\]` → 三行 `$$` 块
- 块级公式前后强制补空行（否则 kramdown 会把它和上下段落粘成一段）
- `$$` 块内容**原样透传**：块内 `&` 是矩阵对齐符、`_` 是下标，转义会破坏它们
- 行内 `$...$` 内部转义 11 种字符（因为 kramdown 不把单 `$` 当数学，会先按 Markdown 解析）：

  | 原字符 | 转成 | 目的 |
  |---|---|---|
  | `#` | `\#` | 防宏参数 / 标题误判 |
  | `_` | `\_` | 防斜体 |
  | `*` | `\*` | 防粗体 / 斜体 |
  | `\{` `\}` | `\\{` `\\}` | 保住花括号 |
  | `\|` | `\mid ` | 防表格冲突 |
  | `<` `>` | `\lt ` `\gt ` | 防被当 HTML 标签 |
  | `&` | `\&` | 防表格对齐符 |
  | `%` | `\%` | 防 LaTeX 注释符 |
  | `~` | `\sim ` | 防断行空格 |

  > `\mid` / `\lt` / `\gt` / `\sim` 都是**字母命令**，后面必须带空格，否则会粘成 `\midb` 这种未定义命令。
- 公式内部的 HTML 实体（`&lt;` `&gt;` `&amp;`）会先还原成 `<` `>` `&`
- 全部转义都用负向断言 `(?<!\\)` 实现**幂等**，重复运行不会叠加转义

**④ Obsidian 语法转换**

| 语法 | 转换结果 |
|---|---|
| `> [!type] 标题` | `<details class="callout type" data-callout="type" markdown="block">` + `<summary class="callout-title">` |
| `[!type]+` / `[!type]-` | 带 `open` / 不带 `open`（与 Obsidian 一致：默认和 `+` 展开，只有 `-` 折叠） |
| `^abc123` | 独占行 → `<a id="abc123"></a>`；标题里或行尾 → 绑到 `<details id="abc123">` |
| `[[#^abc123\|文字]]` | `[文字](#abc123)` |
| `[[笔记]]` / `[[笔记\|文字]]` | `[笔记](/notes/<映射后 slug>/)`，映射表包含**自动生成的拼音 slug** |
| `[[笔记#标题]]` | `[笔记#标题](/notes/<slug>/#标题)` |
| `![[图片.png\|300]]` | `<img src="/assets/img/obsidian/图片.png" width="300">` |
| `![[笔记]]` | `*(嵌入笔记：笔记)*` |
| `%%注释%%` | 整段删除（支持跨行） |
| `==高亮==` | `<mark>高亮</mark>` |
| `- [ ]` / `- [x]` / `- [X]` | `- ☐` / `- ☑` |
| `#标签` | **保持纯文本**（不做标签系统） |
| ` ```dataview ` | 整块删除，替换成 `<!-- Dataview query skipped -->` |
| ` ```mermaid ` | 包成 `<div class="mermaid">`（要画图还需自行引入 mermaid.js） |
| `:smile:` 等 | 20 个常用 emoji 短码换成字符 |

**⑤ 保护与排版清洗**

- **代码块最高优先级**：` ``` ` 围栏（含 dataview / mermaid）和行内 `` `code` `` 都先抽成占位符，内部绝不做任何替换
- 标题修空格：漏空格的 `##标题` → `## 标题`；**单个 `#标签` 不动**（否则标签会变成 H1）
- 防粘连：标题 / 引用块 / 列表首项 / 水平线 / 独占整行的链接，上方补空行；水平线**下方也补**
- 链接清洗：文字里的 `|`→`｜`、`*`→`\*`、`_`→`\_`、全角空格和制表符→半角；`[]()` 删除、`[文字]()` 退化成纯文字
- 空行压缩：3 个以上连续空行压成 1 个
- 公式占位符化：`$$` / `$` 内容先抽出再处理正文，避免被 Callout、链接等规则误伤

**⑥ 容错与安全**

- **slug 冲突**：检测到两篇笔记生成相同 slug → **报错并停止生成**，提示手动指定
- **空正文**：跳过并打印 `[skip]`
- **单篇异常**：`try/except` 包住，只跳过该篇并打印 `[error]`，不影响其他笔记
- **front matter 写坏**（未闭合 / 内容不是 YAML）：按正文处理，不会把整篇吞进 YAML
- **嵌套 callout**（`> > [!note]`）：只警告，降级为普通引用块（避免生成未闭合的 `<details>`）
- **重复 slug 检测**、**幂等**：同一份源连跑两次，输出逐字节一致

---

## 4. 前端交互与 UI

### 4.1 日夜切换开关

- **位置**：固定在浏览器视口右上角（`position: fixed !important; top/right: 20px; z-index: 9999`）；窄屏（≤768px）缩到 60% 贴角（`transform: scale(0.6); transform-origin: top right`）
- **定位写了两处**：`_includes/theme-switch.html` 的内联 `<style>`（跟随 HTML 更新，不怕外部 CSS 缓存）+ `publications.css`
- **状态存储**：`localStorage.theme` = `dark` / `light`
- **首屏防闪烁**：`_includes/theme-head.html` 放在 `<head>` 里最早执行，读 `localStorage` 并在 `<html>` 上设 `data-theme`
- **覆盖机制**：主题的暗色是 `@media (prefers-color-scheme: dark)` 写的、无法禁用，所以用 `html[data-theme="dark"]` / `html[data-theme="light"]` + `!important` **双向覆盖**
- **手绘质感**：开关 CSS 依赖 `filter: url(#sketchy)` / `url(#sketchy-sm)`，这两个 SVG 滤镜定义在 `theme-switch.html` 里（原组件没提供）

### 4.2 Giscus 评论区

| 位置 | 映射方式 | 讨论标识 |
|---|---|---|
| 主页留言板 | `specific` | `data-term="homepage-guestbook"` |
| 每篇笔记 | `pathname` | 按 URL 自动区分 |

- 统一由 `_includes/giscus.html` 生成（接受 `mapping` / `term` 参数）
- **不是写死的静态 `<script>`**：用 JS 动态创建，`data-theme` 按当前 `data-theme` 或系统偏好计算（`dark` / `light`），避免 `preferred_color_scheme` 不理会手动切换的问题
- **切换时跨 iframe 同步**：`window.updateGiscusTheme(theme)` 用 `postMessage` 通知；另外监听 `data.giscus.discussion` 事件，在 iframe 就绪后补发一次（解决懒加载时序）
- **尺寸**：`.giscus-container` 保持 100%（不缩放），iframe 加 `color-scheme: light dark` + `border: none` + `width: 100%`
- ⚠️ 头像来自 `avatars.githubusercontent.com`，国内可能加载失败 → **破图通常是网络问题**

### 4.3 每日一言

- **数据源**：`assets/data/quotes.md` —— Markdown 列表，一行一句，共 46 条，Obsidian 里可直接编辑
- **读取**：`fetch("/assets/data/quotes.md")` → 按行拆分 → 剥掉 `- ` 列表符号 → 过滤空行 / `#` 标题 / `<!-- -->` 注释
- **取值**：`Math.floor(Date.now() / 86400000) % quotes.length` —— 按天固定，零点自动切换，**不需要每天跑脚本**
- **兜底**：请求失败时显示「所有的伟大，都源于一个勇敢的开始。」
- **加载动画**：三个小球弹跳（`loader-balls-*` 前缀，含暗色适配），取到句子后被 `textContent` 整体替换
- **字体**：霞鹜文楷，`@import` 必须在 `publications.css` **第一行**（放中间浏览器会直接忽略）

### 4.4 CSS 缓存

两个布局里的关键 CSS 都带构建时间戳：

```html
<link rel="stylesheet" href="/assets/css/publications.css?v={{ site.time | date: '%s' }}">
<link rel="stylesheet" href="/assets/css/notes.css?v={{ site.time | date: '%s' }}">
```

每次部署 URL 都会变 → CDN 和浏览器必然重新拉取。**这是"改了样式线上没反应"的根治方案。**

> `obsidian-callouts.css` 现在也带 `?v=` 时间戳了（`note.html` 和 `homepage.html` 两处）。

### 4.5 Obsidian Callout 渲染

**数据来源**：`PaperBell/.obsidian/plugins/callout-studio/data.json`
**完整手册**：项目根目录 `callout-for-web.md`（含每种类型的 base64 图标和原始 SVG path）

**支持的类型（20 种）**

| 内置 12 种 | 自建 8 种 |
|---|---|
| `abstract` `danger` `example` `failure` `info` `note` `question` `quote` `success` `tip` `todo` `warning` | `definition` `highlight` `idea` `motivation` `theorem` `context` `formula` `keypoint` |

**渲染链路**

```
Obsidian 里写：  > [!theorem] 定理 1.0.1
        ↓ sync_notes.py（convert_callouts）
生成的 HTML：    <details class="callout theorem" data-callout="theorem" markdown="block" open>
                   <summary class="callout-title">定理 1.0.1</summary>
                   <div class="callout-content" markdown="block">…</div>
                 </details>
        ↓ kramdown（需要 parse_block_html: true）
        ↓ obsidian-callouts.css
网页显示：       左边框 + 淡色背景 + 彩色图标 + 标题
```

**技术方案（v2，2026-10 重写）**

| 项目 | 旧版 | 现在 |
|---|---|---|
| 图标 | Font Awesome 字体字符（`content: "\f05a"`，26 处） | 官方 SVG + CSS `mask`，Base64 内联 |
| 颜色 | 每个类型写死 4 处（边框 / 背景 / 图标 / 暗色各一遍） | 只写 1 个 `--callout-color` |
| 暗色 | 需要把整段规则抄一遍 | 只覆盖颜色变量 |
| 折叠箭头 | FA `\f078` / `\f054` | 纯 CSS 三角（`border` 实现） |
| 新增类型成本 | 4~6 行 + 找 FA 对应字符码 | 2 行（颜色 + 图标） |

**核心 CSS 结构**

```css
.callout {
  --callout-color: #086ddd;
  --callout-bg-opacity: 8%;
  border-left: 4px solid var(--callout-color);
  background-color: color-mix(in srgb, var(--callout-color) var(--callout-bg-opacity), transparent);
}

.callout-title::before {
  content: "";
  width: 1.1em; height: 1.1em;
  background-color: var(--callout-color);
  -webkit-mask: var(--callout-icon) center / contain no-repeat;
          mask: var(--callout-icon) center / contain no-repeat;
}

/* 每种类型只写这 2 行 */
.callout[data-callout="theorem"] {
  --callout-color: #086ddd;
  --callout-icon: url("data:image/svg+xml;base64,...");
}

/* 暗色只换颜色，不重复 base64 */
@media (prefers-color-scheme: dark) {
  .callout[data-callout="theorem"] { --callout-color: #027aff; }
}
```

**图标来源（全部官方原版，非近似）**

| 图标库 | 版本 | 用到的图标 |
|---|---|---|
| Lucide | `lucide-static@1.61.0` | 16 个（`clipboard-list` `zap` `list` `x` `info` `pencil` `help-circle` `quote` `check` `flame` `check-circle-2` `alert-triangle` `lightbulb` `sparkles` `function-square` `map-pin`） |
| Tabler Icons | `@tabler/icons@3.49.0` | `target-arrow`（keypoint） |
| Octicons | `@primer/octicons@19.42.0` | `sparkles-fill`（highlight） |
| Material Symbols | `@material-symbols/svg-400@0.48.1` | `book_ribbon`（definition） |

**必须记住的三件事**

1. `_config.yml` 里 **`parse_block_html: true`** 不能删 —— 删了之后 callout 内部的公式、列表、粗体会原样显示成 Markdown 源码
2. `data-callout` 的值必须和 `callout-for-web.md` 的 Part A 表**完全一致**（含大小写）；`keypoint` 是单类名，旧写法 `key point` 有兼容规则但已不推荐
3. `sync_notes.py` 的 callout 正则允许**内部空格**（`[!key point]` 能解析），但生成 `class` 时会带空格 → 只影响 `.callout` 的类名，CSS 靠 `data-callout` 匹配，所以不报错

**回滚方式**

```bash
# 旧版（Font Awesome 实现）备份在：
assets/css/obsidian-callouts.css.bak
# 或直接从 git 历史取：
git show f16830f:assets/css/obsidian-callouts.css > assets/css/obsidian-callouts.css
```

---

## 5. 常见故障排查

### 5.1 构建失败：`Nesting too deep`（Liquid 死循环）

**症状**

```
Liquid Exception: Liquid error (/github/workspace/_includes/xxx.html line N):
Nesting too deep included in /_layouts/note.html
```

**原因**：include 文件里出现了自己的名字。关键点 —— **HTML 注释里的 Liquid 照样会被执行**。
真实案例：`_includes/giscus.html` 的用法注释里写了一条 include 自己的 Liquid 标签，于是它自己 include 自己，无限递归。

**排查步骤**

1. 搜索 `_includes/*.html` 里所有 Liquid 标签（左花括号加百分号），看有没有自引用
2. 检查 A → B → A 的循环依赖
3. 在 include 里写示例语法时，**只能用纯文字或转义成 `&#123;%`**

**预防**：`_includes/` 里的注释不要出现任何 Liquid 标签；要举例就写「include 本文件」。

### 5.2 构建失败：其他原因

| 症状 | 排查方向 |
|---|---|
| `Liquid syntax error` | 布局里有未闭合的 if / for / unless 标签 |
| YAML front matter 报错 | title 含半角冒号必须加引号；`---` 必须闭合 |
| kramdown 报错 | 公式或代码块里有未转义的特殊字符 |
| 主题相关 | `remote_theme` 已锁 `@2.0`；若要跟上游完全一致，改成 `@dd114c3fef2d97adc1c6b6d46901e0d96ab83a7c`（main 当前提交） |

**看日志的地方**：仓库 → **Actions** → `pages build and deployment` → 最近一次失败的 run → `build` job 日志。

### 5.3 推送失败

```
fatal: unable to access 'https://github.com/...': Failed to connect ... :443
fatal: ... Recv failure: Connection was reset
```

**纯网络问题，不是代码问题。** 处理：开代理 / 切手机热点 / 稍后重试 `git push origin main`。
`deploy.ps1` 下次运行会自动补推积压的 commit。

### 5.4 线上样式没更新

1. `Ctrl + F5` 硬刷新
2. 用**无痕窗口**打开（排除本地缓存）
3. DevTools → Network → 看 CSS 的 `?v=...` 时间戳是否变了（没变说明还是旧 HTML）
4. 等 1–2 分钟（Pages 构建 + CDN 刷新）
5. 确认 `exclude` 生效（不该发布的文件却能被访问，说明 exclude 没生效）

### 5.5 开关位置不对

```js
// Console 验证，应输出：fixed 20px 20px
var s = getComputedStyle(document.querySelector('.theme-switch'));
console.log(s.position, s.top, s.right);
```

- 输出 `static` → CSS 还是旧版本（缓存）
- 输出 `fixed` 但位置偏了 → 检查有没有祖先元素带 `transform` / `filter` / `perspective`（会让 `fixed` 相对该元素定位）

### 5.6 Giscus 相关

| 症状 | 原因 |
|---|---|
| 评论区空白 | 仓库 Settings → Features → **Discussions 未开启**；或 giscus App 未授权该仓库 |
| 头像破图 | `avatars.githubusercontent.com` 被墙，**网络问题** |
| 切换主题评论框不变色 | iframe 还没加载（懒加载，需滚动到可见区）；或 postMessage 报错，看 Console |
| 留言板和文章评论串了 | 检查映射方式：主页必须 `specific + term`，文章必须 `pathname` |

---

## 附：目录速查

```
Personal-Website/
├── _config.yml              # 站点配置（remote_theme 已锁 @2.0）
├── Gemfile                  # 仅本地参考（本机无 ruby，不实际构建）
├── index.md                 # 主页内容（layout: homepage）
├── notes.md                 # 笔记列表片段（被 include_relative 引入）
├── notes/                   # ★ 脚本生成物，不要手改
├── origin/                  # ★ Obsidian 原始笔记（gitignore，不上传）
├── sync_notes.py            # 转换脚本
├── deploy.ps1               # 一键发布（PowerShell，UTF-8 BOM）
├── 发布博客.bat             # 双击发布（纯 ASCII 启动壳，调用 deploy.ps1）
├── TECH_GUIDE.md            # 本文档（exclude，不发布）
├── _layouts/                # homepage.html / note.html（两套独立整页布局）
├── _includes/               # giscus / mathjax / theme-head / theme-switch
├── _sass/                   # 主题样式副本（会覆盖 remote_theme 的同名文件）
├── assets/
│   ├── css/                 # style.scss、publications.css、notes.css、obsidian-callouts.css
│   ├── data/quotes.md       # 每日一言数据
│   ├── js/                  # favicon-switcher.js、scale.fix.js
│   └── img/                 # 头像、favicon、示意图
└── html_source_file/        # 旧版手写 HTML（exclude，不参与构建）
```

## 三条铁律

1. **`notes/` 里的文件全部由脚本生成** —— 要改内容请改 `origin/` 再跑脚本，直接改 `notes/` 会被下次同步覆盖
2. **`_includes/` 的注释里不能出现 Liquid 标签** —— HTML 注释挡不住 Liquid，会触发 `Nesting too deep`
3. **推送由本人手动执行** —— 脚本只负责 `commit`，`git push` 自己来
