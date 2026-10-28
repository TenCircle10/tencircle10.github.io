---
layout: note
title: "线性代数笔记"
slug: "xian-xing-dai-shu-bi-ji"
permalink: "/notes/xian-xing-dai-shu-bi-ji/"
render_with_liquid: false
---

# 线性代数

<details class="callout abstract" data-callout="abstract" open>
<summary class="callout-title">学习路线</summary>
<div class="callout-content" markdown="block">

① **线性过程：先图式化，暂时抛弃形式化**，走"形象 $\to$ 抽象 $\to$ 结构"的路。两条腿：**严格**（写得出证明）、**直观**（画得出图式）。
② **独立解题时卡壳，是在做跳跃**；以慢为快。

</div>
</details>

**线性**：直线、"一次"，以直代曲。**代数**：用符号代表数，研究数。

---

## 1 从线性方程组到矩阵

### 1.1 一般 $n$ 元齐次线性方程组

$$
\begin{cases}
a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = 0\\
a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = 0\\
\quad \vdots\\
a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = 0
\end{cases}
$$

**两类解**：**零解（平凡解）** 指 $x_1 = x_2 = \cdots = x_n = 0$；**非零解** 指 $x_1, \dots, x_n$ 不全取 $0$。

### 1.2 解方程组的通法

<details class="callout keypoint" id="solve-procedure" data-callout="keypoint" open>
<summary class="callout-title">消元 → 阶梯形 → 回代</summary>
<div class="callout-content" markdown="block">

1. **消元**：初等行变换把矩阵 $A$ 化成阶梯形 $B$；
2. **判断**：看有没有 $0 = \text{非零}$ 这样的矛盾方程 —— 有则无解，没有则有解；
3. **定元**：确定**主元（未知数）**与**自由（未知数）**；
4. **回代**：自由未知数任取，主元随之唯一确定。

</div>
</details>

主元所在列的下方全为 $0$，故**自由元确定后，主元随之确定**。希望：

1. $0$ 越多越好；
2. 非零元尽量当主元；
3. **行简化阶梯形矩阵**（主元为 $1$，主元所在列其余元素为 $0$）。

### 1.3 初等变换

<details class="callout definition" id="elementary-ops" data-callout="definition" open>
<summary class="callout-title">初等变换的三种类型</summary>
<div class="callout-content" markdown="block">

- **倍乘**：某行（列）乘 $k$，要求 $k \neq 0$；
- **倍加**：某行（列）的 $k$ 倍加到另一行（列）；
- **对换**：交换两行（列）。

对方程组做的三种**同解变形**，正好对应矩阵的三种初等**行**变换。

</div>
</details>

初等变换是**可逆**的：每一种都能用同类的初等变换还原（倍乘用 $1/k$，倍加用 $-k$，对换再对换一次）。

<details class="callout warning" data-callout="warning" open>
<summary class="callout-title">为什么倍乘不允许乘 $0$</summary>
<div class="callout-content" markdown="block">

乘 $0$ 会把整行信息彻底抹掉、无法还原（$O$ 行变不回原来的行），初等变换就不再可逆，"等价 / 同解"的整条链就断了。所以定义里限定 $k \neq 0$。

</div>
</details>

### 1.4 记号约定

$a_{ij}$ 表示第 $i$ 行第 $j$ 列的元素；矩阵用大写 $A, B, C$，元素用小写 $a, b, a_{ij}$。只有一行称**行矩阵 / 行向量**，只有一列称**列矩阵 / 列向量**。注意**不同型的零矩阵不相等**：$O_{2 \times 3} \neq O_{3 \times 2}$。

---

## 2 矩阵运算

### 2.1 矩阵加法与阿贝尔群

同型矩阵对应元素相加，满足 $A + B = B + A$。

<details class="callout keypoint" data-callout="keypoint" open>
<summary class="callout-title">别把"交换律"算进群的公理</summary>
<div class="callout-content" markdown="block">

矩阵加法满足群的四条公理：**封闭、结合、有恒元（$O$）、有逆元（$-A$）** —— 这是一个**群**。再加上**交换律** $A + B = B + A$，才叫**阿贝尔群（交换群）**。

</div>
</details>

<details class="callout understand" data-callout="understand" open>
<summary class="callout-title">理解</summary>
<div class="callout-content" markdown="block">

元 $\to$ 矩阵：各元相等 $\Rightarrow$ 矩阵相等；
点 $\to$ 轨迹：各点相等 $\Rightarrow$ 轨迹相等。

</div>
</details>

### 2.2 矩阵乘法

$$C_{ij} = \sum_{k=1}^{p} a_{ik} b_{kj}, \qquad A_{m \times p} \, B_{p \times n} = C_{m \times n}$$

也就是说：$A$ 的第 $i$ 行 $\times$ $B$ 的第 $j$ 列 $\Rightarrow C_{ij}$。

<details class="callout example" data-callout="example" open>
<summary class="callout-title">矩阵乘法（$3 \times 2$ 乘 $2 \times 4$ 得 $3 \times 4$）</summary>
<div class="callout-content" markdown="block">

$$
\begin{bmatrix} 3 & 2 \\ -2 & 1 \\ 0 & 1 \end{bmatrix}
\begin{bmatrix} 1 & 2 & 3 & 1 \\ 2 & 4 & 1 & 3 \end{bmatrix}
=
\begin{bmatrix} 7 & 14 & 11 & 9 \\ 0 & 0 & -5 & 1 \\ 2 & 4 & 1 & 3 \end{bmatrix}
$$

</div>
</details>

<details class="callout keypoint" data-callout="keypoint" open>
<summary class="callout-title">口诀</summary>
<div class="callout-content" markdown="block">

**对乘**（行对列逐位相乘）、**中间消，看两头**（求和指标 $k$ 被消掉，剩下的 $i, j$ 就是结果的指标）。

</div>
</details>

#### 2.2.1 结合律 $(AB)C = A(BC)$

<details class="callout theorem" id="associativity" data-callout="theorem" open>
<summary class="callout-title">矩阵乘法满足结合律</summary>
<div class="callout-content" markdown="block">

设 $A_{m \times p},\ B_{p \times q},\ C_{q \times n}$，则 $(AB)C = A(BC)$。

</div>
</details>

**左式**：把 $AB$ 的元素记为 $x_{ik} = \sum_{l=1}^{p} a_{il} b_{lk}$，则 $(AB)C$ 的 $(i,j)$ 元为

$$
y_{ij} = \sum_{k=1}^{q} x_{ik} c_{kj}
= \sum_{k=1}^{q}\left( \sum_{l=1}^{p} a_{il} b_{lk} \right) c_{kj}
= \sum_{l=1}^{p}\sum_{k=1}^{q} a_{il} b_{lk} c_{kj}
$$

**右式**：把 $BC$ 的元素记为 $x'&#95;{lj} = \sum_{k=1}^{q} b_{lk} c_{kj}$（内层求和指标是 $k$，走 $B$ 的列数 $q$），则 $A(BC)$ 的 $(i,j)$ 元为

$$
y'_{ij} = \sum_{l=1}^{p} a_{il} x'_{lj}
= \sum_{l=1}^{p} a_{il} \left( \sum_{k=1}^{q} b_{lk} c_{kj} \right)
= \sum_{l=1}^{p}\sum_{k=1}^{q} a_{il} b_{lk} c_{kj}
$$

**为什么两个求和相等**：两者都是 $p \times q$ 项有限和，项的形状都是 $a_{il}b_{lk}c_{kj}$；把左式 $(l,k)$ 与右式 $(l,k)$ 一一对应（取 $l_2 = l_1,\ k_2 = k_1$），对应项相同；有限和可交换次序。

<details class="callout keypoint" data-callout="keypoint" open>
<summary class="callout-title">这一步最容易写错</summary>
<div class="callout-content" markdown="block">

对应关系必须是 $l \leftrightarrow l$、$k \leftrightarrow k$。若写成"$l_2 = k_1,\ k_2 = l_1$"，就会把项错位成 $a_{ik} b_{kl} c_{lj}$，这不是同一个乘积，比较就失去依据了。

</div>
</details>

### 2.3 矩阵乘法的代价

<details class="callout keypoint" data-callout="keypoint" open>
<summary class="callout-title">三条"不能想当然"</summary>
<div class="callout-content" markdown="block">

1. **一般 $AB \neq BA$**；甚至 $AB$ 有意义时 $BA$ 未必有意义（型不匹配）。
2. **$AB = AC$ 且 $A \neq O$ $\nRightarrow$ $B = C$**（没有消去律）。
3. **$A = B \Rightarrow CA = CB$ 且 $AD = BD$**；但 **$A = B \nRightarrow AC = CB$**（只能在同侧乘同一个矩阵）。

</div>
</details>

特例：数量矩阵与任何矩阵可交换，$kI \cdot A = kA = A \cdot kI$，$kIA = kA$。

<details class="callout example" id="zero-divisor" data-callout="example" open>
<summary class="callout-title">零因子：$A, B \neq O$ 却 $AB = O$</summary>
<div class="callout-content" markdown="block">

$$
A = \begin{bmatrix} 1 & 0 \\ 1 & 0 \end{bmatrix}, \qquad
B = \begin{bmatrix} 0 & 0 \\ 1 & 1 \end{bmatrix}
$$

甚至两个矩阵**都不含 $0$ 元素**也能乘出零矩阵，可见"零因子"与元素是否为 $0$ 无关：

$$
\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}
\begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}
= \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}
$$

</div>
</details>

### 2.4 转置

$$A = [a_{ij}]_{m \times n}, \qquad A^{T} = [a_{ji}]_{n \times m}$$

- $(A^{T})^{T} = A$，$(A + B)^{T} = A^{T} + B^{T}$；
- $(AB)^{T} = B^{T} A^{T}$。

**想法**：设 $A_{m \times p}, B_{p \times n}$。$AB$ 的 $(i,j)$ 元是 $\sum_k a_{ik} b_{kj}$，转置后它跑到第 $(j,i)$ 位；而 $B^{T}A^{T}$ 的 $(j,i)$ 元是 $\sum_k b_{kj} a_{ik}$ —— 同一个数。口诀：**前行乘后列，转置后行列互换**。推广得 $(A_1 A_2 \cdots A_m)^{T} = A_m^{T} \cdots A_2^{T} A_1^{T}$。

若 $A, B$ 同为 $m \times n$（保证 $AB^{T}$、$BA^{T}$ 是 $n$ 阶方阵），则

$$(AB^{T} + BA^{T})^{T} = B A^{T} + A B^{T} = AB^{T} + BA^{T}$$

所以 $AB^{T} + BA^{T}$ 一定是对称矩阵。
<a id="transpose"></a>

### 2.5 单位矩阵、方阵的幂与多项式

<details class="callout definition" data-callout="definition" open>
<summary class="callout-title">方阵与单位矩阵</summary>
<div class="callout-content" markdown="block">

- 若 $A_{m \times n}$ 中 $m = n$，称 $A$ 为 **$n$ 阶方阵**，$a_{ii}$ 称为**主对角元**。
- **单位矩阵** $I_n$（也写 $E_n$）：主对角元全为 $1$、其余全为 $0$ 的 $n$ 阶方阵，简记 $I$（或 $E$）。

</div>
</details>

单位矩阵是乘法的恒元：$A_{m \times n} I_n = A_{m \times n}$，$I_m A_{m \times n} = A_{m \times n}$；零矩阵则 $A_{m \times n} O_{n \times q} = O_{m \times q}$。

方阵的幂：$A^{k} A^{l} = A^{k+l}$，$(A^{k})^{l} = A^{kl}$，规定 $A^{0} = I$、$A^{1} = A$、$I^{k} = I$。多项式搬到矩阵上：$x \to A$，常数 $1 \to I$，

$$f(A) = a_n A^{n} + a_{n-1} A^{n-1} + \cdots + a_1 A + a_0 I$$

<details class="callout keypoint" id="matrix-polynomial" data-callout="keypoint" open>
<summary class="callout-title">为什么 $f(A) = g(A)h(A)$ 一定成立</summary>
<div class="callout-content" markdown="block">

因为同一个 $A$ 的各次幂彼此**可交换**（$A^{k}A^{l} = A^{l}A^{k} = A^{k+l}$），所以多项式乘法展开时不需要担心顺序。

</div>
</details>

---

## 3 特殊矩阵的幂：二项式定理与若尔当块

<details class="callout theorem" id="binomial-theorem" data-callout="theorem" open>
<summary class="callout-title">可交换情形的二项式定理</summary>
<div class="callout-content" markdown="block">

若 $A, B$ **同阶**且 $AB = BA$，则

$$(A+B)^{n} = \sum_{k=0}^{n} C_n^{k} A^{k} B^{n-k}$$

</div>
</details>

<details class="callout keypoint" data-callout="keypoint" open>
<summary class="callout-title">前提：可交换</summary>
<div class="callout-content" markdown="block">

否则 $(A+B)^{2} = A^{2} + AB + BA + B^{2} \neq A^{2} + 2AB + B^{2}$。

</div>
</details>

### 3.1 二阶若尔当块

$$
\begin{bmatrix} \lambda & 1 \\ 0 & \lambda \end{bmatrix}^{n}
= \begin{bmatrix} \lambda^{n} & n\lambda^{n-1} \\ 0 & \lambda^{n} \end{bmatrix}
$$

**做法**：拆成"对角 + 幂零"，就能用 [二项式定理](#binomial-theorem)。令

$$
A = \begin{bmatrix} \lambda & 0 \\ 0 & \lambda \end{bmatrix}, \qquad
B = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}, \qquad
\begin{bmatrix} \lambda & 1 \\ 0 & \lambda \end{bmatrix} = A + B
$$

$AB = BA = \begin{bmatrix} 0 & \lambda \\ 0 & 0 \end{bmatrix}$（可交换，定理可用）；$B^{2} = O$，$A^{n} = \begin{bmatrix} \lambda^{n} & 0 \\ 0 & \lambda^{n} \end{bmatrix}$。于是 $k \ge 2$ 的项全是 $O$：

$$
\begin{aligned}
(A+B)^{n} &= A^{n} + n A^{n-1}B \\
&= \begin{bmatrix} \lambda^{n} & 0 \\ 0 & \lambda^{n} \end{bmatrix} + n \begin{bmatrix} 0 & \lambda^{n-1} \\ 0 & 0 \end{bmatrix}
= \begin{bmatrix} \lambda^{n} & n\lambda^{n-1} \\ 0 & \lambda^{n} \end{bmatrix}
\end{aligned}
$$

<a id="jordan-block-2"></a>

### 3.2 三阶若尔当块（幂零块）

$$
A = \begin{bmatrix} \lambda & 1 & 0 \\ 0 & \lambda & 1 \\ 0 & 0 & \lambda \end{bmatrix}
= \lambda I + B, \qquad
B = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix},
\qquad
B^{2} = \begin{bmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix},
\qquad
B^{3} = O
$$

$B$ 是**三阶幂零块**（$B^{3} = O$）。仿照 [二阶的情形](#jordan-block-2)，二项式展开只剩前三项：

$$
A^{k} = (\lambda I + B)^{k}
= \lambda^{k} I + k\lambda^{k-1} B + \frac{k(k-1)}{2}\lambda^{k-2} B^{2}
$$

<a id="jordan-block-3"></a>

---

## 4 行/列视角与 $AX = b$

设 $A_{m \times n},\ B_{n \times t}$，记 $A_{i\cdot} = [a_{i1}\ a_{i2}\ \cdots\ a_{in}]$（行向量），$B_{\cdot j} = [b_{1j}\ b_{2j}\ \cdots\ b_{nj}]^{T}$（列向量）。

- **按行**：$AB$ 的第 $i$ 行 $= A_{i\cdot} B$，即 $AB = \begin{bmatrix} A_{1\cdot} B \\ A_{2\cdot} B \\ \vdots \\ A_{m\cdot} B \end{bmatrix}$；
- **按列**：$AB$ 的第 $j$ 列 $= A\, B_{\cdot j}$；
- 可乘条件：$A$ 的列数 $=$ $B$ 的行数。

<details class="callout definition" id="matrix-equation" data-callout="definition" open>
<summary class="callout-title">线性方程组的矩阵写法</summary>
<div class="callout-content" markdown="block">

$$
A = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ \vdots & \vdots & & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix},
\quad
x = \begin{bmatrix} x_1 \\ \vdots \\ x_n \end{bmatrix},
\quad
b = \begin{bmatrix} b_1 \\ \vdots \\ b_m \end{bmatrix}
$$

则 $AX = b$ 就是原来的 $m$ 个方程。$A$ 称**系数矩阵**；注意 $b$ 的行数必须与 $A$ 的行数同为 $m$（不是 $n$）。

</div>
</details>

---

## 5 矩阵的秩

### 5.1 定义

<details class="callout definition" id="rank-definition" data-callout="definition" open>
<summary class="callout-title">秩与主元</summary>
<div class="callout-content" markdown="block">

一个矩阵经初等行变换化成阶梯形矩阵后，**非零行的数目是唯一确定的**，称之为矩阵的**秩**，记 $r(A)$。

- **主元**：阶梯形中每个非零行的首非零元；
- $r(A) = \text{主元个数} = \text{独立（有效）方程个数}$。

</div>
</details>

增广矩阵的秩与系数矩阵的秩只差一步：$r(A) \le r(\tilde{A}) \le r(A) + 1$（多出的一列最多贡献一个主元）。

### 5.2 性质

<details class="callout theorem" id="rank-properties" data-callout="theorem" open>
<summary class="callout-title">秩的基本性质</summary>
<div class="callout-content" markdown="block">

设 $A$ 是 $m \times n$ 矩阵，则

1. $r(A) = 0 \iff A = O$；若 $A \neq O$，则 $r(A) \ge 1$；
2. $r(A) \le \min\lbrace m, n\rbrace $；
3. 初等行变换不改变矩阵的秩。

</div>
</details>

性质 1：$A = O$ 时显然 $r(A) = 0$；$A \neq O$ 时至少有一个非零元，化阶梯形后至少有一个主元。

性质 2 的想法：$A$ 至多 $m$ 行，故非零行至多 $m$ 个 $\Rightarrow r(A) \le m$；又主元必须落在不同的列上，而只有 $n$ 列，故 $r(A) \le n$。直观记法：**秩不超过非零行数，也不超过非零列数**（零列一定出不了主元；非零列也可能只贡献自由元）。

<details class="callout keypoint" data-callout="keypoint" open>
<summary class="callout-title">两个容易写错的推论</summary>
<div class="callout-content" markdown="block">

- **单位矩阵 $\Rightarrow$ 满秩**（对）；反过来只能得到"**满秩 $\Rightarrow$ 经有限次初等行变换可化为 $I$**"，并不是"满秩 $\Rightarrow$ 本身就是 $I$"。
- $r(A) \ge 0$ 只是废话；有内容的是 $r(A) = 0 \iff A = O$。

</div>
</details>

### 5.3 初等行变换不改变秩

<details class="callout theorem" id="rank-invariance" data-callout="theorem" open>
<summary class="callout-title">初等行变换不改变秩</summary>
<div class="callout-content" markdown="block">

若 $B$ 由 $A$ 经有限次初等行变换得到，则 $r(A) = r(B)$。

</div>
</details>

**证明（反证）**。由 [初等变换](#elementary-ops) 不改变方程组的解集，齐次方程组 $AX = 0$ 与 $BX = 0$ **同解**。设 $r(A) = r_1 \lt{} r_2 = r(B)$。

1. 设 $B$ 有 $r_2$ 个主元未知数、$n - r_2$ 个自由未知数，把自由未知数的下标集合记为 $F$。
2. **在 $B$ 中**：令 $F$ 中所有自由未知数为 $0$，阶梯形方程组给出唯一解 —— 只能是**零解**。即 $BX = 0$ 在"$F$ 上取 $0$"的解只有零解。
3. **在 $A$ 中**：同样令 $F$ 中这 $n - r_2$ 个未知数为 $0$，剩下 $r_2$ 个未知数只受至多 $r_1$ 个独立方程约束。因为 $r_2 \gt{} r_1$（未知数多于有效方程），这个齐次方程组必有**非零解** $X_0$，且 $X_0$ 在 $F$ 上取 $0$。
4. $X_0$ 是 $A$ 的解，由同解性也是 $B$ 的解；但由第 2 步，$B$ 在 $F$ 上取 $0$ 的解只有零解，矛盾。

所以 $r_1 = r_2$，初等行变换不改变秩。

### 5.4 列变换与乘积的秩

<details class="callout theorem" id="rank-column-op" data-callout="theorem" open>
<summary class="callout-title">右乘满秩矩阵不改变秩</summary>
<div class="callout-content" markdown="block">

若 $Q$ 是 $n$ 阶满秩方阵，$A$ 为 $m \times n$，则 $r(AQ) = r(A)$。

</div>
</details>

<details class="callout lemma" data-callout="lemma" open>
<summary class="callout-title">阶梯形右乘不增加非零行</summary>
<div class="callout-content" markdown="block">

阶梯形矩阵 $T$（$r(T) = r$）右乘任何矩阵，非零行数不会增加 —— $T$ 有 $m - r$ 个零行，零行右乘仍是零行，故 $r(TQ) \le r$。

</div>
</details>

**证明**：设 $P_s \cdots P_1 A = T$（$P_i$ 为初等矩阵），则 $A = P_1^{-1} \cdots P_s^{-1} T$，于是

$$
r(AQ) = r(P_1^{-1} \cdots P_s^{-1} TQ) = r(TQ) \le r(T) = r(A) \qquad (\ast)
$$

（第一、二个等号用的是 [初等行变换不改变秩](#rank-invariance)，最后一个等号由 $r(T) = r(A)$ 得到。）由 $(\ast)$ 得 $r(AQP) \le r(AQ) \le r(A)$；取 $P = Q^{-1}$ 又得 $r(A) \le r(AQ) \le r(A)$，故 $r(AQ) = r(A)$。

<details class="callout corollary" data-callout="corollary" open>
<summary class="callout-title">$r(AB) \le \min\lbrace r(A),\, r(B)\rbrace $</summary>
<div class="callout-content" markdown="block">

矩阵乘法不增加信息，只可能减少信息。

</div>
</details>

### 5.5 相抵标准形与转置

<details class="callout definition" id="canonical-form" data-callout="definition" open>
<summary class="callout-title">相抵（等价）标准形</summary>
<div class="callout-content" markdown="block">

任何 $m \times n$ 矩阵 $A$ 都可经初等变换化为 $\begin{bmatrix} I_r & O \\ O & O \end{bmatrix}&#95;{m \times n}$（$r = r(A)$），称**相抵标准形**。它被 $r(A)$ **唯一确定**，于是同型矩阵之间

$$A \cong B \iff r(A) = r(B)$$

</div>
</details>

转置后相抵标准形的形状不变，只是型从 $m\times n$ 变成 $n\times m$：

<details class="callout theorem" id="rank-transpose" data-callout="theorem" open>
<summary class="callout-title">$r(A) = r(A^{T})$</summary>
<div class="callout-content" markdown="block">

设 $P_s \cdots P_1 A Q_1 \cdots Q_t = \begin{bmatrix} I_r & O \\ O & O \end{bmatrix}&#95;{m \times n}$，两边转置得

$$Q_t^{T} \cdots Q_1^{T} A^{T} P_1^{T} \cdots P_s^{T} = \begin{bmatrix} I_r & O \\ O & O \end{bmatrix}_{n \times m}$$

</div>
</details>

左边是"可逆矩阵乘 $A^{T}$ 再乘可逆矩阵"，不改变秩；右边的秩为 $r$，故 $r(A^{T}) = r(A) = r$。

### 5.6 秩的进一步结论（专题）

$r(A+B) \le r(A) + r(B)$。其余专题单开：

- **分块矩阵的秩**（$\begin{bmatrix} A & O \\ O & B\end{bmatrix}$ 的秩、$\begin{bmatrix} A & C \\ 0 & B\end{bmatrix}$ 的下界）：见 [分块矩阵性质](/notes/分块矩阵性质/)
- **Sylvester 秩不等式** $r(AB) \ge r(A) + r(B) - n$ 及其几何解释：见 [Sylvester 秩不等式](/notes/Sylvester 秩不等式/)
- **子矩阵的秩不超过原矩阵** $r(B) \le r(A)$：见 [子母矩阵秩的大小关系](/notes/子母矩阵秩的大小关系/)
- **加长向量组仍无关**（无关的向量组添上若干坐标后仍无关）：见 [向量组无关加元素仍无关](/notes/向量组无关加元素仍无关/)
<a id="rank-further"></a>

---

## 6 初等矩阵与矩阵等价

<details class="callout definition" id="elementary-matrix" data-callout="definition" open>
<summary class="callout-title">初等矩阵</summary>
<div class="callout-content" markdown="block">

对单位矩阵 $I$ 作**一次**初等变换得到的矩阵，按三种变换分为三型（变换本身见 [初等变换](#elementary-ops)）。

</div>
</details>

设 $i \neq j$，三型的元素特征与作用方式：

| 变换 | 初等矩阵 $E$ 的元素特征 | 作用方式 |
| --- | --- | --- |
| 第 $i$ 行（列）倍乘 $k \neq 0$ | $a_{ii} = k$，其余对角元为 $1$ | $EA$ 行变 / $AE$ 列变 |
| 第 $i$ 行（列）的 $k$ 倍加到第 $j$ 行（列） | $a_{ii} = a_{jj} = 1$，$a_{ji} = k$ | $EA$ 行变 / $AE$ 列变 |
| 对换 $i, j$ 两行（列） | $a_{ii} = a_{jj} = 0$，$a_{ij} = a_{ji} = 1$，其余对角元为 $1$ | $EA$ 行变 / $AE$ 列变 |

一次初等**行**变换 $=$ 左乘相应的 $m$ 阶初等矩阵（作用在 $A_{m \times n}$ 上）；一次初等**列**变换 $=$ 右乘相应的 $n$ 阶初等矩阵。**左行右列**：左乘则行变，右乘则列变（$I$ 中改动的位置固定）。

若 $A$ 可经**有限次**初等变换化为 $B$，记 $A \cong B$。它自反、对称、传递，是一个等价关系；同型矩阵之间 $A \cong B \iff r(A) = r(B)$（见 [相抵标准形](#canonical-form)）。
<a id="equivalence"></a>

---

## 7 满秩与可逆

<details class="callout theorem" id="full-rank-invertible" data-callout="theorem" open>
<summary class="callout-title">满秩 $\iff$ 可逆</summary>
<div class="callout-content" markdown="block">

设 $A$ 为 $n$ 阶方阵（[满秩](#rank-definition) 即 $r(A) = n$），则以下三条等价：

1. $r(A) = n$（满秩）；
2. $A$ 可表示为若干个初等矩阵的乘积；
3. 存在 $n$ 阶方阵 $B$，使 $AB = BA = I$（即 $A$ 可逆，且 $B = A^{-1}$）。

</div>
</details>

**思路**：满秩时可用有限次初等行变换把 $A$ 化成 $I$：$P_s \cdots P_1 A = I$，于是

$$
A = (P_s \cdots P_1)^{-1} = P_1^{-1} P_2^{-1} \cdots P_s^{-1}
$$

即 $A$ 是初等矩阵之积；初等矩阵都可逆，故 $A$ 可逆。反过来，初等矩阵都满秩，满秩方阵之积仍满秩。

初等矩阵都可逆；若 $P$ 可逆，则存在 $Q$ 使 $PQ = QP = I$，并且 $Q = P^{-1}$。可逆只对方阵有意义，但方阵未必可逆（$\iff$ 不满秩）。

<details class="callout corollary" data-callout="corollary" open>
<summary class="callout-title">单侧逆即双侧逆</summary>
<div class="callout-content" markdown="block">

若 $A, B$ 都是 $n$ 阶方阵且 $AB = I$，则 $BA = I$、$B = A^{-1}$（非方阵不成立）。

</div>
</details>

细节见 [满秩矩阵](/notes/满秩矩阵/)、[满秩方阵的单侧可逆蕴含双侧可逆](/notes/满秩方阵的单侧可逆蕴含双侧可逆/)。

### 7.1 逆矩阵的运算

<details class="callout formula" id="inverse-properties" data-callout="formula" open>
<summary class="callout-title">逆矩阵的运算</summary>
<div class="callout-content" markdown="block">

设 $A, B$ 可逆，则 $A^{-1}$、$A^{T}$、$AB$ 都可逆，且

$$(A^{-1})^{-1} = A, \qquad (A^{T})^{-1} = (A^{-1})^{T}, \qquad (AB)^{-1} = B^{-1} A^{-1}$$

若 $A, B, A+B$ 都可逆，则 $A^{-1}(A+B)B^{-1} = A^{-1}AB^{-1} + A^{-1}BB^{-1} = B^{-1} + A^{-1}$。
对角矩阵（$a_{ii} \neq 0$）：

$$
\begin{bmatrix} a_{11} & & & \\ & a_{22} & & \\ & & \ddots & \\ & & & a_{nn} \end{bmatrix}^{-1}
=
\begin{bmatrix} \frac{1}{a_{11}} & & & \\ & \frac{1}{a_{22}} & & \\ & & \ddots & \\ & & & \frac{1}{a_{nn}} \end{bmatrix}
$$

</div>
</details>

---

## 8 求逆矩阵

### 8.1 二阶公式

<details class="callout formula" id="inverse-formula-2x2" data-callout="formula" open>
<summary class="callout-title">二阶求逆公式</summary>
<div class="callout-content" markdown="block">

$$
A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}, \qquad
A^{-1} = \frac{1}{ad - bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}
\quad (ad - bc \neq 0)
$$

</div>
</details>

### 8.2 初等行变换法

$$(A \mid I) \xrightarrow{\ \text{只做初等行变换}\ } (I \mid A^{-1})$$

理由：若 $P_1 \cdots P_s A = I$，则 $P_1 \cdots P_s = A^{-1}$，故 $P_1 \cdots P_s I = A^{-1}$ —— 把 $A$ 化成 $I$ 的同一串行变换，作用在 $I$ 上即得 $A^{-1}$。

<details class="callout keypoint" id="inverse-algorithm" data-callout="keypoint" open>
<summary class="callout-title">别记错名字</summary>
<div class="callout-content" markdown="block">

$[A \mid I] \to [I \mid A^{-1}]$ 是**初等行变换法**；**伴随矩阵法**是 $A^{-1} = \dfrac{1}{\mid{}A\mid{}} A^{&#42;}$，两者不是一回事。

</div>
</details>

### 8.3 例题：由 $AX = A + 2X$ 反推可逆性

<details class="callout example" data-callout="example" open>
<summary class="callout-title">由 $AX = A + 2X$ 反推可逆性</summary>
<div class="callout-content" markdown="block">

设 $AX = A + 2X$，证明 $A - 2I$ 可逆并写出 $(A - 2I)^{-1}$，其中 $A = \begin{bmatrix} 4 & 2 & 3 \\ 1 & 1 & 0 \\ -1 & 2 & 3 \end{bmatrix}$。

</div>
</details>

**移项**：$AX - 2X = A$，即 $(A - 2I)X = A$，进而

$$(A - 2I)(X - I) = AX - A - 2X + 2I = A - A + 2I = 2I$$

所以 $(A - 2I) \cdot \frac{1}{2}(X - I) = I$，由 [满秩与可逆](#full-rank-invertible) 得 $\frac{1}{2}(X - I) = (A - 2I)^{-1}$。

**验证**：$A - 2I = \begin{bmatrix} 2 & 2 & 3 \\ 1 & -1 & 0 \\ -1 & 2 & 1 \end{bmatrix}$，$\mid{}A - 2I\mid{} = 2(-1) - 2(1) + 3(1) = -1 \neq 0$，故 $r(A - 2I) = 3$，确实可逆。
<a id="example-inverse"></a>

---

## 相关笔记

- 主线：[数学分析笔记](/notes/shu-xue-fen-xi-bi-ji/)
- 秩与不等式专题：[分块矩阵性质](/notes/分块矩阵性质/)、[Sylvester 秩不等式](/notes/Sylvester 秩不等式/)、[子母矩阵秩的大小关系](/notes/子母矩阵秩的大小关系/)、[向量组无关加元素仍无关](/notes/向量组无关加元素仍无关/)
- 满秩与可逆：[满秩矩阵](/notes/满秩矩阵/)、[满秩方阵的单侧可逆蕴含双侧可逆](/notes/满秩方阵的单侧可逆蕴含双侧可逆/)
- 工具：[∑求和运算律](/notes/∑求和运算律/)
