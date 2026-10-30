---
summary: "Personal-Website 项目的长期要点"
read_when:
  - 接手本项目的脚本 / 样式 / 发布相关改动时
---

# Personal-Website 长期要点

**权威文档是 `TECH_GUIDE.md`** —— 改任何东西之前先读对应章节，改完同步更新它。
本文件只记录「不看文档也必须知道」的东西。

## 流水线

`origin/{public,hidden}/*.md` → `sync_notes.py` → `notes/*.md` → Jekyll（GitHub Pages）。

- `origin/` 被 `.gitignore` 忽略，源笔记零泄漏；`notes/` 才是入库的产物。
- 目录归属决定可见性：`public/` → `public: true`（进主页列表），
  `hidden/` → `public: false`（不进主页但 URL 仍可访问）。**目录是权威来源**，
  源文件里手写的 `public:` 会被覆盖。
- permalink 恒为 `/notes/<slug>/`，分仓不改变旧链接。
- 生成前会自动清理 `notes/` 里的上一轮产物（换仓/改名/删源文件不再残留），
  靠 `generated_by: sync_notes.py` 标记区分「脚本产物」与「手写页面」；
  测试稿（文件名含 test/测试/demo/torture/sample）与白名单文件永不删除。

## 反复踩的坑（别再犯）

- **MathJax v3 的 `GetCS()` 只吃 ASCII 字母**作为命令名 →
  `\left\vertx` 会变成未定义命令 `\vertx`，报
  "Missing or unrecognized delimiter for \left"。
  多字母定界符命令后面紧跟字母时必须补空分组 `{}` 切断。
  **合法定界符全集里没有 `\mid`**（只能当关系符）。
- **kramdown 会把行内公式里的 `|` 当表格列分隔符** → 行内公式里的竖线必须换成
  `\vert` / `\mid{}`；块级 `$$...$$` 原样透传。
- `\{` 不能写成 `\\{`（`\\` 是换行）→ 用 `\lbrace{}` / `\rbrace{}`。
- 下划线/星号用 HTML 实体（`&#95;` / `&#42;`）而不是 LaTeX 转义，
  且只在真的会触发 Markdown 强调时才替换。
- `math_engine: ~`（显式 null）—— kramdown 的 math 引擎会转成 MathJax 2 的
  `<script type="math/tex">`，而站点加载的是 MathJax 3，不认那个标签。
- 块级公式里的 `&` 是对齐符，绝不能转义。

## 交付约定

改完脚本**直接提交**，不做上线效果验证（不装引擎、不做模拟渲染、不写一次性校验脚本），
push 由 szy 本人做。详见 `TECH_GUIDE.md` 2.4。

**提交信息用中文**，写清根因与改动要点。
