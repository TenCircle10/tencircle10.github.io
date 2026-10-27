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

假设可列为 $\lbrace a_1, a_2, \dots, a_n, \dots\rbrace $
设
$a_1 = 0.x_{11} x_{12} x_{13} \dots x_{1n} \dots$
$a_2 = 0.x_{21} x_{22} x_{23} \dots x_{2n} \dots$
$x_{ij}$ 为 $a_i$ 的第 $j$ 位小数，且不允许 $a_i$ 的最后无限位均为9。

给出一个构造：定义数 $b = 0.y_1 y_2 y_3 \dots y_n \dots$
其中 $y_i \neq x_{ii}, \forall i \in \mathbb{N}^&#42;$,且$y_i \in \lbrace 1,2,3,4,5,6,7,8\rbrace $
这使得 $\forall i \in \mathbb{N}^&#42;, b \neq a_i$  #skill
这与 $(0, 1)$ 为可列集矛盾！
故$\mathbb{R}$ **不可列**

下证无理数集不可列。
我们已知 $\mathbb{Q}$ 可列，$\mathbb{R}$ 不可列
$\mathbb{R} = \mathbb{Q} \cup \mathbb{Q}^c$
则 $\mathbb{Q}^c$ 必不可列，否则 $\mathbb{R}$ 可列与引理矛盾！
故**无理数集不可列**

---
