---
layout: note
title: "math-bug-test"
slug: "math-bug-test"
permalink: "/notes/math-bug-test/"
render_with_liquid: false
---

# 公式转义 Bug 测试

绝对值公式：已知 $f(x)$ 连续，且 $\left| f(x) - A \right| \lt{} \varepsilon$。

含有大于小于的公式：当 $n \gt{} N_1$ 且 $x \lt{} 0$ 时。

行内多个公式同段：设 $a \lt{} b$，则 $f(a) \left| x \right| g(b) \gt{} h$，其中 $p \neq q$。

嵌套括号：$f\left( \left| x \right| \right) = \left[ \left( a + b \right) \right]^{2}$。

范数：$\left\| x \right\|&#95;{2} + \left| y \right|$.

下标与上标：$x_{n+1} = x_n^{2} + a_{ij}^{(k)}$。

块级绝对值：

$$
\left| f(x) - A \right| \lt{} \varepsilon
$$

块级大于小于：

$$
n \gt{} N_1 \quad \text{且} \quad x \lt{} 0
$$

