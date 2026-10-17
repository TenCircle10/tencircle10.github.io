---
layout: note
title: "final-torture-test"
slug: "final-torture-test"
permalink: "/notes/final-torture-test/"
---

## 漏打空格的标题测试

### 这是三级标题（漏空格，应被修复）
#这是单井号标签（应保持原样，不能变成 H1）

正文紧贴列表：

- 列表第一项
- 列表第二项

正文紧贴水平线：

---

正文紧贴另一个水平线：

***

链接测试：[包含 ｜ 竖线的文字](https://example.com) 以及 [带有\*星号\*和\_下划线\_的文字](https://example.com/b)

空链接测试： 和 只有文字

独占一行的链接（上下应有空行）：

[独占行的链接](https://example.com/c)
紧贴图片：<img src="/assets/img/obsidian/photo.png" width="300" />

公式空格测试：$a + b$ 与 $x\_1 \* y\_1$

HTML 实体公式：$a \lt  b \& c$

连续定界符：
$$

$$

嵌套 Callout（应降级为普通引用块并告警）：

> > [!note] 嵌套的 callout
> > 这一层不会被转换

普通 Callout（正常转换）：
<details class="callout tip" data-callout="tip" markdown="block" open>
<summary class="callout-title">正常的 callout</summary>
<div class="callout-content" markdown="block">

这一层应该正常转成 details

</div>
</details>

列表紧贴文字（上方应补空行）：

1. 有序列表第一项
2. 有序列表第二项

#标签 和 #tag/subtag 都应保持纯文本
