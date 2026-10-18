---
layout: note
title: "无限可列集等势证明"
slug: "infinite-countable-equivalence"
permalink: "/notes/infinite-countable-equivalence/"
render_with_liquid: false
---

<details class="callout theorem" data-callout="theorem" markdown="block" open>
<summary class="callout-title">Theorem</summary>
<div class="callout-content" markdown="block">

所有可列无限集都等势，它们具有相同的基数 $\aleph\_0$

</div>
</details>

对于可列集 $A = \\{a\_1, a\_2, \dots, a\_n, \dots\\}$，$B = \\{b\_1, b\_2, \dots, b\_n, \dots\\}$
其中 $\forall i, j \in N^\*$，$i \neq j$，有 $a\_i \neq a\_j$，$b\_i \neq b\_j$。

定义映射 $f: A \to B$，
$f(a\_i) = b\_i$。

对于 $\forall i \in N^\*$，对于 $b\_i$，总可以在 $A$ 中找到原像 $a\_i$，故 $f$ 为满射。

假设 $b\_i$ 有两个原像 $a\_x, a\_y$ ($x \neq y$)，
则 $f(a\_x) = f(a\_y) = b\_x = b\_y = b\_i$。
矛盾！故假设不成立（$f$ 为单射）。

综上，$f$ 为双射。
故 $A$ 与 $B$ 等势