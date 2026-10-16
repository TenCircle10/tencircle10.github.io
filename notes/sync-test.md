---
layout: note
title: "sync-test"
---

这是用来验证 sync_notes.py 的测试笔记，覆盖 Callout、公式、Wikilink、图片与代码块。

<details class="callout note" data-callout="note" markdown="block">
<summary class="callout-title">定理 1.0.1</summary>
<div class="callout-content" markdown="block">

可列个可列集之并也是可列集。

</div>
</details>

<a id="abc123"></a>

引用上面的定理：[定理1.0.1](#abc123)

**公式转义（只应作用于行内 $...$）**：

* 集合写法 $A = \\{1, 2, 3\\}$
* 竖线写法 $\\{x \mid x \in A\\}$
* 已经转义过的写法 $B = \\{1, 2\\}$ 不应该被再次转义

**块级公式（块内必须原样保留，不做任何转义）**：

$$
\begin{matrix}
\{1\} & \{x | x \in A\} \\
\$100 & 4
\end{matrix}
$$

块级公式之后的行内公式 $C = \\{1\\} \mid \\{2\\}$ 仍然应该被转义。

**Wikilink**：

* [数学分析](/notes/数学分析/)
* [数学分析笔记](/notes/数学分析/)

**图片**：![demo.png](/assets/img/obsidian/demo.png)

**Callout 折叠标记**：

<details class="callout tip" data-callout="tip" markdown="block" open>
<summary class="callout-title">默认展开</summary>
<div class="callout-content" markdown="block">

这一行应该在展开状态。

</div>
</details>

<details class="callout warning" data-callout="warning" markdown="block">
<summary class="callout-title">默认折叠</summary>
<div class="callout-content" markdown="block">

点开才看到这一行。

</div>
</details>

**代码块里的内容必须原样保留**：

```
> [!note] 不转换
$A = \{1,2\}$ 和 [[不存在的笔记]] 以及 ![[demo.png]] 都保持原样
```
