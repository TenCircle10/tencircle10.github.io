---
layout: note
title: "hell-math-test"
slug: "hell-math-test"
permalink: "/notes/hell-math-test/"
public: true
generated_by: sync_notes.py
render_with_liquid: false
---

# 地狱级公式测试

若 $p_n \gt{} 0$ 是正无穷大量，则 $\lim\limits_{n \to \infty}\left(1 + \dfrac{1}{p_n}\right)^{p_n} = e$。**证**：由 $\left(1+\frac1n\right)^n \to e$，$\exists N_1$ 使 $n \gt{} N_1$ 时 $\left\vert\left(1+\frac1n\right)^n - e\right\vert \lt{} \varepsilon$；又 $p_n \to +\infty$，$\exists N_2$ 使 $n \gt{} N_2$ 时 $p_n \gt{} N_1$，故 $n \gt{} N_2$ 时 $\left\vert\left(1+\frac{1}{p_n}\right)^{p_n} - e\right\vert \lt{} \varepsilon$。

## 附加极值用例

含裸尖括号：$a \lt{} b \gt{} c$、$x\lt{}0$、$y\gt{}1$。

含 HTML 样式的尖括号：$a \lt{}b\gt{} c$、$p\lt{}q$。

紧贴文字的公式：设$n\gt{}N$时$x\lt{}y$成立。

单字符公式：$a$、$\gt{}$、$\lt{}$。

含 & 的公式：$a & b$、$\begin{bmatrix} 1 & 0 \\\\ 0 & 1 \end{bmatrix}$。

## 跨仓双链测试

公开笔记指向隐藏笔记：[隐藏草稿](/notes/yin-cang-cao-gao/)（应解析为 `/notes/yin-cang-cao-gao/`）。
