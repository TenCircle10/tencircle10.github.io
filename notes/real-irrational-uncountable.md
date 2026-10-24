---
layout: note
title: "实数集与无理数集不可列证明"
slug: "real-irrational-uncountable"
permalink: "/notes/real-irrational-uncountable/"
render_with_liquid: false
---

<details class="callout theorem" data-callout="theorem" open>
<summary class="callout-title">Theorem</summary>
<div class="callout-content" markdown="block">

无理数集为**不可列集**

</div>
</details>

<details class="callout tip" data-callout="tip" open>
<summary class="callout-title">引理</summary>
<div class="callout-content" markdown="block">

实数集是**不可列集**

</div>
</details>

假设实数集是可列集。
由可列集性质，$(0, 1) \subset \mathbb{R}$
则 $(0, 1)$ 也为可列集。

假设可列为 $\\{a\_1, a\_2, \dots, a\_n, \dots\\}$
设
$a\_1 = 0.x\_{11} x\_{12} x\_{13} \dots x\_{1n} \dots$
$a\_2 = 0.x\_{21} x\_{22} x\_{23} \dots x\_{2n} \dots$
$x\_{ij}$ 为 $a\_i$ 的第 $j$ 位小数，且不允许 $a\_i$ 的最后无限位均为9。

给出一个构造：定义数 $b = 0.y\_1 y\_2 y\_3 \dots y\_n \dots$
其中 $y\_i \neq x\_{ii}, \forall i \in \mathbb{N}^\*$,且$y\_i \in \\{1,2,3,4,5,6,7,8\\}$
这使得 $\forall i \in \mathbb{N}^\*, b \neq a\_i$  #skill
这与 $(0, 1)$ 为可列集矛盾！
故$\mathbb{R}$ **不可列**

下证无理数集不可列。
我们已知 $\mathbb{Q}$ 可列，$\mathbb{R}$ 不可列
$\mathbb{R} = \mathbb{Q} \cup \mathbb{Q}^c$
则 $\mathbb{Q}^c$ 必不可列，否则 $\mathbb{R}$ 可列与引理矛盾！
故**无理数集不可列**

---
