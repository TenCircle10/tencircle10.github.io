---
layout: note
title: "callout-color-test"
slug: "callout-color-test"
permalink: "/notes/callout-color-test/"
render_with_liquid: false
---

# Callout 12 色测试

逐个渲染 12 个数学类 Callout，核对主色、图标字形与背景不透明度（亮色 0.08 / 暗色 0.15）。

<details class="callout theorem" data-callout="theorem" open>
<summary class="callout-title">Theorem · 定理</summary>
<div class="callout-content" markdown="block">

若 $f$ 在闭区间 $[a,b]$ 上连续，则 $f$ 在 $[a,b]$ 上有界。

</div>
</details>

<details class="callout definition" data-callout="definition" open>
<summary class="callout-title">Definition · 定义</summary>
<div class="callout-content" markdown="block">

设 $A$ 为 $m \times n$ 矩阵，若 $m = n$，则称 $A$ 为 $n$ 阶方阵。

</div>
</details>

<details class="callout conclusion" data-callout="conclusion" open>
<summary class="callout-title">Conclusion · 结论</summary>
<div class="callout-content" markdown="block">

有限维方阵只要单侧可逆，另一侧自动成立：$AB = I \Rightarrow BA = I$。

</div>
</details>

<details class="callout corollary" data-callout="corollary" open>
<summary class="callout-title">Corollary · 推论</summary>
<div class="callout-content" markdown="block">

由 $r(AB) \le \min\lbrace r(A), r(B)\rbrace $ 立得：可逆矩阵乘任何矩阵不改变秩。

</div>
</details>

<details class="callout lemma" data-callout="lemma" open>
<summary class="callout-title">Lemma · 引理</summary>
<div class="callout-content" markdown="block">

设 $\lbrace a_n\rbrace $ 收敛于 $A \gt{} 0$，则存在 $N$，当 $n \gt{} N$ 时 $a_n \gt{} 0$。

</div>
</details>

<details class="callout formula" data-callout="formula" open>
<summary class="callout-title">Formula · 公式</summary>
<div class="callout-content" markdown="block">

$$e = \sum_{n=0}^{\infty} \frac{1}{n!}$$

</div>
</details>

<details class="callout context" data-callout="context" open>
<summary class="callout-title">Context · 背景</summary>
<div class="callout-content" markdown="block">

下面这条极限是整个数列分析的起点：$\lim\limits_{n \to \infty} \left(1 + \dfrac{1}{n}\right)^{n} = e$。

</div>
</details>

<details class="callout seealso" data-callout="seealso" open>
<summary class="callout-title">Seealso · 参见</summary>
<div class="callout-content" markdown="block">

证明细节见 [Stolz定理的证明](/notes/Stolz定理的证明/)。

</div>
</details>

<details class="callout idea" data-callout="idea" open>
<summary class="callout-title">Idea · 想法</summary>
<div class="callout-content" markdown="block">

把矩阵看成线性映射，秩就是像空间的维数——很多不等式一眼就出来了。

</div>
</details>

<details class="callout motivation" data-callout="motivation" open>
<summary class="callout-title">Motivation · 动机</summary>
<div class="callout-content" markdown="block">

为什么要区分"有界"和"有极限"？因为单调有界定理只保证后者存在，不告诉你是多少。

</div>
</details>

<details class="callout keypoint" data-callout="keypoint" open>
<summary class="callout-title">Keypoint · 重点</summary>
<div class="callout-content" markdown="block">

抄错率最高的一步：$\sqrt{a_n} \to \sqrt{a}$ 证明里，分母要留上界 $\dfrac{\mid{}a_n - a\mid{}}{\sqrt a}$，不能提前代入。

</div>
</details>

<details class="callout understand" data-callout="understand" open>
<summary class="callout-title">Understand · 顿悟</summary>
<div class="callout-content" markdown="block">

确界"取一个不一定取到，但取一段一定包含"——想通这句话，闭区间套就没什么可怕的了。

</div>
</details>
