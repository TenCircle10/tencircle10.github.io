---
layout: note
title: "callout-color-test"
slug: "callout-color-test"
permalink: "/notes/callout-color-test/"
render_with_liquid: false
---

# Callout 全量图标测试（24 种）

逐个渲染 `assets/css/obsidian-callouts.css` 里定义的全部类型，核对图标形状、主色与背景浓度（亮 0.08 / 暗 0.15）。

## 定理与推导类

<details class="callout theorem" data-callout="theorem" open>
<summary class="callout-title">Theorem · 定理</summary>
<div class="callout-content" markdown="block">

若 $f$ 在闭区间 $[a,b]$ 上连续，则 $f$ 在 $[a,b]$ 上有界。

</div>
</details>

<details class="callout definition" data-callout="definition" open>
<summary class="callout-title">Definition · 定义</summary>
<div class="callout-content" markdown="block">

设 $A$ 为 $m \times n$ 矩阵，若 $m = n$，称 $A$ 为 $n$ 阶方阵。

</div>
</details>

<details class="callout lemma" data-callout="lemma" open>
<summary class="callout-title">Lemma · 引理</summary>
<div class="callout-content" markdown="block">

设 $\lbrace{}a_n\rbrace{}$ 收敛于 $A \gt{} 0$，则存在 $N$，当 $n \gt{} N$ 时 $a_n \gt{} 0$。

</div>
</details>

<details class="callout corollary" data-callout="corollary" open>
<summary class="callout-title">Corollary · 推论</summary>
<div class="callout-content" markdown="block">

由 $r(AB) \le \min\lbrace{}r(A), r(B)\rbrace{}$ 立得：可逆矩阵乘任何矩阵不改变秩。

</div>
</details>

<details class="callout formula" data-callout="formula" open>
<summary class="callout-title">Formula · 公式</summary>
<div class="callout-content" markdown="block">

$$e = \sum_{n=0}^{\infty} \frac{1}{n!}$$

</div>
</details>

<details class="callout conclusion" data-callout="conclusion" open>
<summary class="callout-title">Conclusion · 结论</summary>
<div class="callout-content" markdown="block">

有限维方阵只要单侧可逆，另一侧自动成立：$AB = I \Rightarrow BA = I$。

</div>
</details>

## 提示与提醒类

<details class="callout keypoint" data-callout="keypoint" open>
<summary class="callout-title">Keypoint · 重点</summary>
<div class="callout-content" markdown="block">

抄错率最高的一步：$\sqrt{a_n} \to \sqrt{a}$ 证明里，分母要留上界 $\dfrac{\mid{}a_n - a\mid{}}{\sqrt a}$。

</div>
</details>

<details class="callout warning" data-callout="warning" open>
<summary class="callout-title">Warning · 警告</summary>
<div class="callout-content" markdown="block">

分母不能为 $0$：$\lim\limits_{x \to a} \dfrac{f(x)}{g(x)}$ 拆开前先确认 $B \neq 0$。

</div>
</details>

<details class="callout tip" data-callout="tip" open>
<summary class="callout-title">Tip · 提示</summary>
<div class="callout-content" markdown="block">

记法：**$M$、$N$ 取 $\max$，$\delta$ 取 $\min$。**

</div>
</details>

<details class="callout note" data-callout="note" open>
<summary class="callout-title">Note · 笔记</summary>
<div class="callout-content" markdown="block">

这一节的内容在 §4.2 会再用到一次。

</div>
</details>

<details class="callout info" data-callout="info" open>
<summary class="callout-title">Info · 信息</summary>
<div class="callout-content" markdown="block">

参考教材：李忠、方丽萍《数学分析教程》上册第三章。

</div>
</details>

<details class="callout question" data-callout="question" open>
<summary class="callout-title">Question · 问题</summary>
<div class="callout-content" markdown="block">

把 $A \gt{} B$ 换成 $A \ge B$，还能得到「存在 $N$，当 $n \gt{} N$ 时 $a_n \ge b_n$」吗？

</div>
</details>

<details class="callout abstract" data-callout="abstract" open>
<summary class="callout-title">Abstract · 摘要</summary>
<div class="callout-content" markdown="block">

本章主线：确界原理 → 单调有界 → 夹逼 → 两个重要极限 → $e$。

</div>
</details>

## 例子与状态类

<details class="callout example" data-callout="example" open>
<summary class="callout-title">Example · 示例</summary>
<div class="callout-content" markdown="block">

证明 $\mid{}x\mid{}$ 在 $0$ 处连续但不可导。

</div>
</details>

<details class="callout quote" data-callout="quote" open>
<summary class="callout-title">Quote · 引用</summary>
<div class="callout-content" markdown="block">

以直代曲，以慢为快。

</div>
</details>

<details class="callout todo" data-callout="todo" open>
<summary class="callout-title">Todo · 待办</summary>
<div class="callout-content" markdown="block">

补写 Stokes 公式的推导。

</div>
</details>

<details class="callout success" data-callout="success" open>
<summary class="callout-title">Success · 成功</summary>
<div class="callout-content" markdown="block">

第 3 章习题已全部做完。

</div>
</details>

<details class="callout failure" data-callout="failure" open>
<summary class="callout-title">Failure · 失败</summary>
<div class="callout-content" markdown="block">

这套放缩不成立：$(1/2)^{n/2}$ 作为上界太强。

</div>
</details>

<details class="callout danger" data-callout="danger" open>
<summary class="callout-title">Danger · 危险</summary>
<div class="callout-content" markdown="block">

不要在 $\mathbb{R}$ 上直接对 $\mathbb{Q}$ 的结论做极限运算。

</div>
</details>

## 风格类

<details class="callout idea" data-callout="idea" open>
<summary class="callout-title">Idea · 想法</summary>
<div class="callout-content" markdown="block">

把矩阵看成线性映射，秩就是像空间的维数——很多不等式一眼就出来了。

</div>
</details>

<details class="callout motivation" data-callout="motivation" open>
<summary class="callout-title">Motivation · 动机</summary>
<div class="callout-content" markdown="block">

为什么要区分「有界」和「有极限」？因为单调有界定理只保证后者存在。

</div>
</details>

<details class="callout context" data-callout="context" open>
<summary class="callout-title">Context · 背景</summary>
<div class="callout-content" markdown="block">

这条极限是整个数列分析的起点：$\lim\limits_{n \to \infty} \left(1 + \dfrac{1}{n}\right)^{n} = e$。

</div>
</details>

<details class="callout seealso" data-callout="seealso" open>
<summary class="callout-title">Seealso · 参见</summary>
<div class="callout-content" markdown="block">

证明细节见 [Stolz定理的证明](/notes/Stolz定理的证明/)。

</div>
</details>

<details class="callout understand" data-callout="understand" open>
<summary class="callout-title">Understand · 顿悟</summary>
<div class="callout-content" markdown="block">

确界「取一个不一定取到，但取一段一定包含」——想通这句话，闭区间套就不可怕了。

</div>
</details>
