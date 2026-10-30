---
layout: note
type: concept
course: "数学mathmatic"
tema: "通用"
created: "2026-10-24"
status: draft
aliases: ["满秩方阵", "非奇异矩阵"]
tags: [concept, 线性代数]
next_review: "2026-11-07"
title: "满秩矩阵"
slug: "man-zhi-ju-zhen"
permalink: "/notes/man-zhi-ju-zhen/"
public: false
generated_by: sync_notes.py
render_with_liquid: false
---

<details class="callout abstract" data-callout="abstract" open>
<summary class="callout-title">我的断言</summary>
<div class="callout-content" markdown="block">

**满秩**只对方阵说：$n$ 阶方阵 $A$ 满足 $r(A) = n$（秩等于阶数）时，称 $A$ 满秩。满秩 $\iff$ 可逆，$\iff$ 能写成若干个初等矩阵的乘积。

</div>
</details>

## 🧠 类比

- 满秩方阵是"**可还原的变换**"：$Ax = b$ 对任意 $b$ 有唯一解，且能原路退回（求逆）。不满秩就是"把信息压扁了"，回不去（[[线性代数笔记#^zero-divisor|零因子]]）。

## 📝 费曼讲解

- **定义**：$n$ 阶方阵 $A$ 满足 $r(A) = n$ 即满秩；等价说法是"行（列）向量组线性无关"。
- **初等变换**：满秩方阵能用有限次初等行变换化成 $I$：$P_s\cdots P_1 A = I$，于是

$$A = P_1^{-1}P_2^{-1}\cdots P_s^{-1}$$

即满秩方阵是**初等矩阵之积**；初等矩阵都满秩，满秩方阵之积仍满秩。

- **可逆**：满秩 $\iff$ 存在同阶方阵 $B$ 使 $AB = BA = I$。方阵只要单侧成立就够：$AB = I \Rightarrow BA = I$（见[满秩方阵的单侧可逆蕴含双侧可逆](/notes/man-zhi-fang-zhen-de-dan-ce-ke-ni-yun-han-shuang-ce-ke-ni/)）。
- **相抵标准形**：满秩方阵 $A \cong I_n$。
- （学过行列式：$A$ 满秩 $\iff \mid{}A\mid{} \neq 0$。）

<details class="callout warning" data-callout="warning" open>
<summary class="callout-title">常见误解</summary>
<div class="callout-content" markdown="block">

- "满秩"是**方阵**的专属说法；$m \times n$ 矩阵只有 $r(A) = \min\lbrace{}m, n\rbrace{}$ 这种"列满秩 / 行满秩"的说法，不叫满秩。
- 满秩 $\Rightarrow$ 能**化成** $I$，不是"满秩 $\Rightarrow$ 本身就是 $I$"。
- 满秩方阵之积仍满秩，但**和不一定**：$I$ 满秩，而 $I + (-I) = O$ 不满秩 —— 加法没有"保持秩"的性质。

</div>
</details>

**自测**：$A, B$ 都是 $n$ 阶方阵且 $AB = I$，能直接说"$A$ 满秩"吗？

能。$AB = I$ 满秩 $\Rightarrow r(AB) = n$，而 $r(AB) \le \min\lbrace{}r(A), r(B)\rbrace{} \le n$，故 $r(A) = r(B) = n$，进而可逆、$B = A^{-1}$，于是 $BA = I$。

## 🔗 出现在哪里

- [[线性代数笔记#^full-rank-invertible|满秩 ⟺ 可逆]]（主线第 7 节）
- [满秩方阵的单侧可逆蕴含双侧可逆](/notes/man-zhi-fang-zhen-de-dan-ce-ke-ni-yun-han-shuang-ce-ke-ni/)
- [子母矩阵秩的大小关系](/notes/zi-mu-ju-zhen-zhi-de-da-xiao-guan-xi/)、[Sylvester 秩不等式](/notes/sylvester-zhi-bu-deng-shi/)

```uni-loom-backlinks
```
