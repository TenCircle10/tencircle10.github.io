---
layout: note
title: "left-right-test"
slug: "left-right-test"
permalink: "/notes/left-right-test/"
public: true
generated_by: sync_notes.py
render_with_liquid: false
---

# left/right 定界符测试

行内测试：$\lim_{n \to \infty} \left( 1 + \frac{1}{p_n} \right)$

行内带左中括号：$\left[ a + b \right]$

行内带花括号：$\left\lbrace{} x \mid x \gt{} 0 \right\rbrace{}$

行内绝对值：$\left\vert x \right\vert$

块级测试：

$$
\lim_{n \to \infty} \left( 1 + \frac{1}{p_n} \right)^{p_n} = e
$$

块级带中括号：

$$
\left[ \left( a + b \right) \cdot c \right]^{2}
$$

块级绝对值与范数：

$$
\left| \frac{a}{b} \right| + \left\| x \right\|_{2}
$$

## 用户报告的真实公式（行内）

- $\lim\limits_{n \to \infty}\left(1 + \dfrac{1}{n^{2} + n}\right)^{n} = \lim\limits_{n \to \infty}\left[\left(1 + \dfrac{1}{n^{2}+n}\right)^{n^{2}+n}\right]^{\frac{n}{n^{2}+n}} = e^{0} = 1$；
- $\lim\limits_{n \to \infty} a_n^{b_n} = a^{b}$（$\lim a_n = a \gt{} 0$，$\lim b_n = b$）
- $\lim\limits_{x \to \infty}\left(1 + \dfrac{\alpha}{x}\right)^{\beta x} = e^{\alpha\beta}$