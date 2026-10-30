---
layout: note
title: "无限可列集等势证明"
slug: "wu-xian-ke-lie-ji-deng-shi-zheng-ming"
permalink: "/notes/wu-xian-ke-lie-ji-deng-shi-zheng-ming/"
public: false
render_with_liquid: false
---

<details class="callout theorem" data-callout="theorem" open>
<summary class="callout-title">Theorem</summary>
<div class="callout-content" markdown="block">

所有可列无限集都等势，它们具有相同的基数 $\aleph_0$

</div>
</details>

对于可列集 $A = \lbrace{}a_1, a_2, \dots, a_n, \dots\rbrace{}$，$B = \lbrace{}b_1, b_2, \dots, b_n, \dots\rbrace{}$
其中 $\forall i, j \in N^&#42;$，$i \neq j$，有 $a_i \neq a_j$，$b_i \neq b_j$。

定义映射 $f: A \to B$，
$f(a_i) = b_i$。

对于 $\forall i \in N^&#42;$，对于 $b_i$，总可以在 $A$ 中找到原像 $a_i$，故 $f$ 为满射。

假设 $b_i$ 有两个原像 $a_x, a_y$ ($x \neq y$)，
则 $f(a_x) = f(a_y) = b_x = b_y = b_i$。
矛盾！故假设不成立（$f$ 为单射）。

综上，$f$ 为双射。
故 $A$ 与 $B$ 等势