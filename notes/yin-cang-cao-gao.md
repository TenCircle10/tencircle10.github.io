---
layout: note
title: "隐藏草稿"
slug: "yin-cang-cao-gao"
permalink: "/notes/yin-cang-cao-gao/"
public: false
generated_by: sync_notes.py
render_with_liquid: false
---

# 隐藏草稿

这是一篇放在 `origin/hidden/` 里的笔记，用来验证「分仓」功能：

- 它**不会**出现在主页的笔记列表里（front matter 是 `public: false`）；
- 但依然可以通过 URL 直接访问（不是密码保护，只是「不在列表里」）；
- 它和 `origin/public/` 里的笔记共享同一套双链映射，所以这里的
  [数学分析笔记](/notes/shu-xue-fen-xi-bi-ji/) 依然能正确指向 `/notes/shu-xue-fen-xi-bi-ji/`。

<details class="callout note" data-callout="note" open>
<summary class="callout-title">写作中</summary>
<div class="callout-content" markdown="block">

这篇还在起草，等写完了再移回 `origin/public/`。

</div>
</details>
