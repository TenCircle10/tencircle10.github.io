---
layout: note
title: "中文文件名测试笔记"
slug: "slug-demo"
permalink: "/notes/slug-demo/"
---

这篇笔记的源文件名是中文，靠 front matter 的 slug 决定输出文件名和 URL。

**Wikilink 解析**：

* 指向没有 slug 的笔记（回退用文件名）：[sync-test](/notes/sync-test/)
* 指向自己（源文件名是中文）：[中文文件名测试](/notes/slug-demo/)
* 用 title 作键并带显示文本：[测试笔记](/notes/slug-demo/)
* 指向不存在的笔记（应保持原样）：[不存在的笔记](/notes/不存在的笔记/)

**行内公式照常转义**：$A = \\{1, 2\\}$ 与 $\\{x \mid x \in A\\}$

**块级公式保持原样**：

$$
\{1\} | x
$$
