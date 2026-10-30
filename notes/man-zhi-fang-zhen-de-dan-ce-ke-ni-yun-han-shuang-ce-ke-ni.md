---
layout: note
concepts:
  - "[[满秩矩阵]]"
tags: [concept, 线性代数]
title: "满秩方阵的单侧可逆蕴含双侧可逆"
slug: "man-zhi-fang-zhen-de-dan-ce-ke-ni-yun-han-shuang-ce-ke-ni"
permalink: "/notes/man-zhi-fang-zhen-de-dan-ce-ke-ni-yun-han-shuang-ce-ke-ni/"
public: false
generated_by: sync_notes.py
render_with_liquid: false
---

<details class="callout theorem" id="one-sided-inverse" data-callout="theorem" open>
<summary class="callout-title">定理：满秩方阵的单侧可逆蕴含双侧可逆</summary>
<div class="callout-content" markdown="block">

设 $A, B$ 均为 $n$ 阶满秩方阵（即 [满秩矩阵](/notes/man-zhi-ju-zhen/)），若已知 $AB = I$，则 $BA = I$，从而 $B = A^{-1}$。

</div>
</details>

## 错误证法

只用结合律：

$$B(AB)A = B I A = BA \quad \Longrightarrow \quad (BA)^{2} = BA \quad \Longrightarrow \quad BA(BA - I) = O$$

接着写"$BA \neq O \Rightarrow BA - I = O$"，**没有依据**。

## 为什么不能直接消去

矩阵乘法有 [零因子](/notes/xian-xing-dai-shu-bi-ji/#zero-divisor)，与实数不同：

- 实数：$a(a - 1) = 0 \iff a = 0$ 或 $a = 1$；
- 矩阵：$M(M - I) = O$ **推不出** $M = O$ 或 $M = I$。

反例：

$$
\begin{bmatrix} \frac{1}{2} & \frac{1}{2} \\\\[2pt] \frac{1}{2} & \frac{1}{2} \end{bmatrix}
\begin{bmatrix} -\frac{1}{2} & \frac{1}{2} \\\\[2pt] \frac{1}{2} & -\frac{1}{2} \end{bmatrix}
=
\begin{bmatrix} 0 & 0 \\\\ 0 & 0 \end{bmatrix}
$$

## 证法一：先证 $BA$ 满秩

由 $AB = I$ 知 $AB$ 满秩。假设 $A$ 不满秩，则用 [初等变换](/notes/xian-xing-dai-shu-bi-ji/#elementary-ops) 可把 $A$ 化成阶梯形：

$$P_s \cdots P_1 A = A_1$$

因为 $A$ 不满秩，阶梯形 $A_1$ 必然存在零行。又由 $AB = I$ 两边左乘 $P_s \cdots P_1$ 得

$$A_1 B = P_s \cdots P_1$$

此时等式左侧 $A_1 B$ 有零行，而右侧是初等矩阵之积、满秩（无零行），**矛盾**。故 $A$ 必然满秩，同理 $B$ 满秩，于是 $BA$ 也满秩（可逆）。

回到上面那个式子 $BA(BA - I) = O$：既然 $BA$ 满秩，两边同乘 $(BA)^{-1}$，立刻得 $BA - I = O$，即 $BA = I$。

<details class="callout warning" data-callout="warning" open>
<summary class="callout-title">要点</summary>
<div class="callout-content" markdown="block">

不是"$M^2 = M \Rightarrow M = I$"，而是**先证 $BA$ 可逆**，才有资格消去 $BA$。

</div>
</details>

## 证法二：直接用逆矩阵

前提已保证 $A$ 可逆，在 $AB = I$ 两边左乘 $A^{-1}$：

$$A^{-1}AB = A^{-1}I \quad \Longrightarrow \quad B = A^{-1}$$

于是 $AB = AA^{-1} = I$ 且 $BA = A^{-1}A = I$。

<details class="callout tip" data-callout="tip" open>
<summary class="callout-title">记法</summary>
<div class="callout-content" markdown="block">

**"单侧逆即双侧逆"只对有限维方阵成立**。非方阵反例：$A = [1\ \ 0]$（$1 \times 2$）、$B = [1;\ 0]$（$2 \times 1$），则 $AB = [1] = I_1$，但 $BA = \begin{bmatrix} 1 & 0 \\\\ 0 & 0\end{bmatrix} \neq I_2$。

</div>
</details>

---

## 相关笔记

- 概念：[满秩矩阵](/notes/man-zhi-ju-zhen/)
- 主线：[线性代数笔记](/notes/xian-xing-dai-shu-bi-ji/)
