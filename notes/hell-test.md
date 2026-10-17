---
layout: note
title: "地狱级语法测试"
slug: "hell-test"
permalink: "/notes/hell-test/"
---

# 地狱级语法测试

## 1. 行内公式：全部雷区字符

- 宏参数：# 号：$f(\#1, \#2) = \#1 + \#2$
- 下标与星号：$a\_1 \* a\_2$ 与 $\mathbb{N}^\*$
- 花括号与竖线：$A = \\{1, 2\\}$，$\\{x \mid  x \in A\\}$
- 比较符：$a \lt  b$ 且 $b \gt  c$
- 对齐与百分号：$P(A \& B) = 50\%$
- 波浪号：$a \sim  b$
- 全混：$\#1\_2 \* \\{a\mid b\\} \lt  c \gt  d \& e \% f \sim  g$

## 2. 块级公式：矩阵对齐符 & 和下标 _ 必须原样

$$
\begin{matrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{matrix}
$$

$$
\int_0^1 x^2\,dx = \frac{1}{3}
$$

## 3. Callout 嵌套公式与块 ID

<details class="callout theorem" id="thm01" data-callout="theorem" markdown="block" open>
<summary class="callout-title">带公式的定理</summary>
<div class="callout-content" markdown="block">

设 $a\_1 \lt  b\_1$，则 $\\{a\_1\\} \subset \\{b\_1 \mid  b\_1 \gt  0\\}$。
并且 $\#1\_2 \* x$ 也要正常。

</div>
</details>

<details class="callout definition" data-callout="definition" markdown="block">
<summary class="callout-title">折叠的定义</summary>
<div class="callout-content" markdown="block">

定义 $f: A \to B$，其中 $x\_1 \* y\_1 \neq z\_1$。

</div>
</details>

<details class="callout note" data-callout="note" markdown="block" open>
<summary class="callout-title">普通 note 默认展开</summary>
<div class="callout-content" markdown="block">

这里没有公式。

</div>
</details>

## 4. 正文块 ID 与块引用

这是一个普通段落。 <a id="para01"></a>

回看：[定理](#thm01) 与 [这个段落](#para01)。

## 5. 链接与嵌入

- 内部链接：[hell-test](/notes/hell-test/) 与 [地狱测试](/notes/hell-test/)
- 带尺寸图片：<img src="/assets/img/obsidian/diagram.png" width="320" /> 与 <img src="/assets/img/obsidian/photo.png" width="200" height="150" />
- 普通图片：![pic.png](/assets/img/obsidian/pic.png)
- 笔记嵌入：*(嵌入笔记：某篇笔记)*

## 6. 其他语法

- 高亮：<mark>重要</mark> 与 <mark>第二处</mark>
- 待办：

- ☐ 未完成
- ☑ 已完成

- 标签：#数学 #attention_test 保持纯文本
- Emoji：😄 🚀

## 7. Dataview 与 Mermaid

<!-- Dataview query skipped -->

<div class="mermaid">
graph TD
A[开始] --> B{判断}
B -->|是| C[结束]
</div>

## 8. 代码块：所有符号必须原样保留

```text
$#1_2 * \{a|b\} < c > d & e % f ~ g$
> [!note] 不转换
[[hell-test]] ![[pic.png|300]] ==高亮== - [ ] 待办 #标签 :smile:
%% 注释 %%
```
