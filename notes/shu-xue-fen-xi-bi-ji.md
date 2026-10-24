---
layout: note
title: "数学分析笔记"
slug: "shu-xue-fen-xi-bi-ji"
permalink: "/notes/shu-xue-fen-xi-bi-ji/"
render_with_liquid: false
---

# 数学分析

<details class="callout abstract" data-callout="abstract" markdown="block" open>
<summary class="callout-title">主线（保留自己的话）</summary>
<div class="callout-content" markdown="block">

思考：**无穷小分析** —— 用"要多小有多小"的语言（$\varepsilon$、$\delta$、$N$）把"趋势"写成可以逐条验证的不等式。

</div>
</details>

---

## 1 集合与数集

### 1.1 集合的基本概念

**集合**的三条性质：

- **互异性**：相同元素只算一个，例如 $\\{1, 2, 1, 2\\} = \\{1, 2\\}$；
- **无序性**：$\\{1, 2\\} = \\{2, 1\\}$；
- **确定性**：任一对象要么属于、要么不属于该集合。

**例子**：

- $1 \in \\{1\\}$，而 $1 \neq \\{1\\}$（元素不等于集合）；
- $\varnothing \subseteq A$ 对任何集合 $A$ 成立（$A$ 允许为空集）。

<details class="callout warning" data-callout="warning" markdown="block" open>
<summary class="callout-title">一个容易混的点</summary>
<div class="callout-content" markdown="block">

$\varnothing \subset A$ 里的符号要理解为"包含于"（$\subseteq$）；写成 $\subset$ 时也不排除 $A = \varnothing$ 的情形。

</div>
</details>

**性质**：

- $A \subset B,\ B \subset C \Rightarrow A \subset C$；
- $A = B \iff A \subset B$ 且 $B \subset A$。

### 1.2 集合运算与德摩根律

- $A \cap B$：交；$A \cup B$：并；
- $A \setminus B$：差，$A \setminus B = \\{x \mid x \in A \text{ 且 } x \notin B\\}$；
- $A^{c}$：补集（相对于全集 $X$）。

运算律：交换律、结合律、分配律。

<details class="callout theorem" id="de-morgan" data-callout="theorem" markdown="block" open>
<summary class="callout-title">德摩根律（de Morgan）</summary>
<div class="callout-content" markdown="block">

$$(A \cup B)^{c} = A^{c} \cap B^{c}, \qquad (A \cap B)^{c} = A^{c} \cup B^{c}$$

</div>
</details>

### 1.3 笛卡尔积

$$A \times B = \{(x, y) \mid x \in A,\ y \in B\}$$

### 1.4 数集、数域与有序域

**数集对运算的封闭性**：

- $\mathbb{N}$：对 $+,\ \times$ 封闭，对 $-$、$\div$ 不封闭；
- $\mathbb{Z}$：对 $+,\ -,\ \times$ 封闭，对 $\div$ 不封闭；
- $\mathbb{Q}$：对 $+,\ -,\ \times,\ \div$ 封闭（除数 $\neq 0$）；
- $\mathbb{R}$：$\mathbb{Q}$ 添上无理数，四则封闭；
- $\mathbb{C}$：四则封闭，还封闭开方（但不是有序域，见下）。

<details class="callout definition" id="number-field" data-callout="definition" markdown="block" open>
<summary class="callout-title">数域</summary>
<div class="callout-content" markdown="block">

设 $\mathbb{F} \subset \mathbb{C}$，若 $\mathbb{F}$ 中任意两数的和、差、积、商（除数非零）仍属于 $\mathbb{F}$，且 $0, 1 \in \mathbb{F}$，则称 $\mathbb{F}$ 为一个**数域**。

</div>
</details>

<details class="callout warning" data-callout="warning" markdown="block" open>
<summary class="callout-title">数域的定义里不需要再验证运算律</summary>
<div class="callout-content" markdown="block">

交换律、结合律、分配律是从 $\mathbb{C}$ 继承下来的，**自动成立**，不用单独验证；真正要验证的只有**封闭性**（以及含 $0, 1$）。

</div>
</details>

<details class="callout definition" id="ordered-field" data-callout="definition" markdown="block" open>
<summary class="callout-title">有序域</summary>
<div class="callout-content" markdown="block">

域 $\mathbb{F}$ 若存在一个全序 $\le$，且与运算相容：

- $a \le b \Rightarrow a + c \le b + c$；
- $0 \le a$ 且 $0 \le b \Rightarrow 0 \le ab$，

则称 $\mathbb{F}$ 为**有序域**。

</div>
</details>

- $\mathbb{Q}$、$\mathbb{R}$ 是有序域。
- $\mathbb{C}$ **不是**有序域：相容的序下必有 $a^{2} \ge 0$，于是 $-1 = i^{2} \ge 0$ 与 $1 = 1^{2} \gt  0$ 相加得 $0 \ge 1$，矛盾。

---

## 2 可列集

### 2.1 定义

<details class="callout definition" id="countable-set" data-callout="definition" markdown="block" open>
<summary class="callout-title">可列集</summary>
<div class="callout-content" markdown="block">

若无限集 $A$ 的元素能按某种规律排成一个序列，即
$$A = \{a_1, a_2, \dots, a_n, \dots\}$$
则称 $A$ 为**可列集**（可数无限集）。

</div>
</details>

### 2.2 可列个可列集之并

<details class="callout theorem" id="f0fbb3" data-callout="theorem" markdown="block" open>
<summary class="callout-title">定理 1.0.1</summary>
<div class="callout-content" markdown="block">

可列个可列集之并也是可列集。

</div>
</details>

**证明思路（记）**：记 $A\_n = \\{a\_{n1}, a\_{n2}, \dots, a\_{nk}, \dots\\}$，沿对角线方向取

$$\bigcup_{n=1}^{\infty} A_n = \{a_{11},\ a_{21},\ a_{12},\ a_{31},\ a_{22},\ a_{13},\ \dots\}$$

即按 $i + j$ 递增的顺序枚举（重复元素跳过）：

$$
\begin{matrix}
 & 1 & 2 & 3 & 4 & \cdots \\
1 & a_{11} & a_{12} & a_{13} & a_{14} & \cdots \\
2 & a_{21} & a_{22} & a_{23} & a_{24} & \cdots \\
3 & a_{31} & a_{32} & a_{33} & a_{34} & \cdots \\
4 & a_{41} & a_{42} & a_{43} & a_{44} & \cdots \\
\vdots & \vdots & \vdots & \vdots & \vdots & \ddots
\end{matrix}
$$

### 2.3 $\mathbb{Q}$ 是可列集

记 $A\_n = [n, n+1] \cap \mathbb{Q}$（$n \in \mathbb{Z}$），则

$$\bigcup_{n \in \mathbb{Z}} A_n = \mathbb{Q}$$

这是**可列个**集合之并，由 [定理 1.0.1](#f0fbb3)，只需证 $A\_0$ 可列：

$$A_0 = \Big\{0,\ 1,\ \tfrac{1}{2},\ \tfrac{1}{3},\ \tfrac{2}{3},\ \tfrac{1}{4},\ \tfrac{3}{4},\ \tfrac{1}{5},\ \tfrac{2}{5},\ \tfrac{3}{5},\ \tfrac{4}{5},\ \dots\Big\}$$

按"分母从小到大、同分母内按分子从小到大"枚举，就排成了一个序列。于是 $A\_0$ 可列，进而 $\mathbb{Q}$ 可列。

### 2.4 注意点

- 所有可列集的元素个数都相同，见 [无限可列集等势证明](/notes/infinite-countable-equivalence/)；
- 有理数集与无理数集都**稠密**；
- 但稠密不等于可列：无理数集不可列，见 [实数集与无理数集不可列证明](/notes/real-irrational-uncountable/)。

---

## 3 实数的完备性

### 3.1 上确界与下确界

<details class="callout definition" id="sup-inf-def" data-callout="definition" markdown="block" open>
<summary class="callout-title">上确界（最小上界）</summary>
<div class="callout-content" markdown="block">

设 $E \subset \mathbb{R}$ 且 $E \neq \varnothing$。称 $M$ 为 $E$ 的**上确界**，若

1. $M$ 是 $E$ 的上界：$\forall x \in E,\ x \le M$；
2. $M$ 是**最小**的上界：$\forall \varepsilon \gt  0$，$M - \varepsilon$ 都不是 $E$ 的上界。

记 $M = \sup E = \alpha$。**下确界（最大下界）**类似：$m$ 是下界，且 $\forall \varepsilon \gt  0$，$m + \varepsilon$ 不是 $E$ 的下界，记 $m = \inf E = \beta$。

</div>
</details>

- 有上界就必有**无限多个**上界（上界往上都还是上界）。
- 上确界是把"所有上界"压到最紧的那一个；**它不一定属于 $E$**。

<details class="callout key point" data-callout="key point" markdown="block" open>
<summary class="callout-title">一句话理解（保留自己的话）</summary>
<div class="callout-content" markdown="block">

确界"取一个不一定取到，但取一段一定包含"：它是界的**边界**，未必落在集合里。例如 $\sup(0, 1) = 1 \notin (0, 1)$，但任何含 $1$ 的开区间都与 $(0,1)$ 相交。

</div>
</details>

### 3.2 确界原理（完备性）

<details class="callout theorem" id="completeness" data-callout="theorem" markdown="block" open>
<summary class="callout-title">确界原理</summary>
<div class="callout-content" markdown="block">

$\mathbb{R}$ 的任一非空、有上界的子集必有上确界；非空、有下界的子集必有下确界。

</div>
</details>

- 直观：**实数集"充满"整个数轴**，没有"洞"，对极限封闭。
- 对 $\mathbb{Q}$ 不成立：$S = \\{x \in \mathbb{Q} \mid x^{2} \lt  2\\}$ 在 $\mathbb{Q}$ 中**没有上确界**（"应该在"的那个位置 $\sqrt{2}$ 不在 $\mathbb{Q}$ 里）；而 $S' = \\{x \in \mathbb{R} \mid x^{2} \lt  2\\}$ 有界，且 $\sup S' = \sqrt{2}$。
- 有最值一定有界，有界不一定有最值（$(0,1)$ 有界但无最值）。

### 3.3 闭区间套定理

<details class="callout theorem" id="nested-intervals" data-callout="theorem" markdown="block" open>
<summary class="callout-title">闭区间套定理</summary>
<div class="callout-content" markdown="block">

若 $[a\_{n+1}, b\_{n+1}] \subset [a\_n, b\_n]$（$n = 1, 2, \dots$）且 $\lim\limits\_{n \to \infty} (b\_n - a\_n) = 0$，则存在**唯一**的 $c \in \mathbb{R}$ 属于所有 $[a\_n, b\_n]$，且
$$\lim_{n \to \infty} a_n = \lim_{n \to \infty} b_n = c$$

</div>
</details>

### 3.4 Bolzano–Weierstrass 定理

<details class="callout theorem" id="bolzano-weierstrass" data-callout="theorem" markdown="block" open>
<summary class="callout-title">有界序列必有收敛子列</summary>
<div class="callout-content" markdown="block">

若 $a \le x\_n \le b$（$n = 1, 2, \dots$），则 $\\{x\_n\\}$ 有收敛子列。

</div>
</details>

**证明**：把 $[a, b]$ 等分成两个小区间，必有一个含 $\\{x\_n\\}$ 的无穷多项（否则两边各只含有限项，合起来也只有有限项，矛盾），记为 $[a\_1, b\_1]$，并在其中取一项 $x\_{n\_1}$。

再等分 $[a\_1, b\_1]$，重复此过程，得到闭区间套 $\\{[a\_k, b\_k]\\}$ 与子列 $\\{x\_{n\_k}\\}$，满足 $x\_{n\_k} \in [a\_k, b\_k]$，且下标可以取得严格递增。由 [闭区间套定理](#nested-intervals)，$a\_k \to c \leftarrow b\_k$，于是

$$a_k \le x_{n_k} \le b_k \quad \Longrightarrow \quad \lim_{k \to \infty} x_{n_k} = c$$

### 3.5 实数的小数表示

- 把实数按小数截断：$x\_n = m + 0.a\_1 a\_2 \cdots a\_n$，则

$$0 \le x - x_n < \frac{1}{10^{n}}$$

- 于是**任何实数（包括无理数）都是一列有理数的极限**：$\sqrt{2} = 1.4\cdots$ 就是 $1.4,\ 1.41,\ 1.414,\ \dots$ 的极限；
- 这也是"$\mathbb{Q}$ 在 $\mathbb{R}$ 中稠密"的定量版本。
<a id="decimal-representation"></a>

---

## 4 数列极限

### 4.1 定义与记号

**数列**：按自然数 $1, 2, 3, \dots$ 编号依次排列的一列数 $x\_1, x\_2, x\_3, \dots$，称为无穷数列，简称数列。要点是 ① 无穷 ② 依次排列（即定义在 $\mathbb{N}^{\*}$ 上的函数，可列且有序）。

- **单调增**：$x\_n \le x\_{n+1}$（严格单调增则成立 $\lt $）；
- **有界**：既有上界又有下界，等价地 $\exists M \gt  0,\ \forall n,\ \mid x\_n\mid  \le M$。

<details class="callout definition" id="sequence-limit" data-callout="definition" markdown="block" open>
<summary class="callout-title">数列极限</summary>
<div class="callout-content" markdown="block">

$\forall \varepsilon \gt  0$，$\exists N \in \mathbb{N}$，只要 $n \gt  N$ 就有 $\mid a\_n - l\mid  \lt  \varepsilon$，
则称 $l$ 为 $\\{a\_n\\}$ 的极限，记作 $\lim\limits\_{n \to \infty} a\_n = l$ 或 $a\_n \to l\ (n \to \infty)$。

</div>
</details>

**几何意义**：当 $n \gt  N$ 时，$a\_n$ 全部落在 $(l - \varepsilon, l + \varepsilon)$ 内，称为 $l$ 的 **$\varepsilon$ 邻域**，记 $U(l, \varepsilon)$。

<details class="callout note" id="limit-tail" data-callout="note" markdown="block" open>
<summary class="callout-title">等价的"尾巴"说法</summary>
<div class="callout-content" markdown="block">

$\lim\limits\_{n \to \infty} a\_n = l \iff$ 对 $l$ 的任意 $\varepsilon$ 邻域 $U(l, \varepsilon)$，**只有有限项** $a\_n \notin U(l, \varepsilon)$。
关键在"只有有限项"：极限只约束**最终**的行为，前面任意有限项都可以乱来。

</div>
</details>

<details class="callout question" data-callout="question" markdown="block" open>
<summary class="callout-title">如果把"只有有限项在邻域外"改成"有无穷项在邻域外"，对吗？</summary>
<div class="callout-content" markdown="block">

不对。这句话把"最终落进邻域"换成了"反复跑到邻域外"，两者含义恰好相反：

- 收敛数列对每个邻域外**只有有限项**，所以它根本不满足这个条件（条件不必要）；
- 反过来，满足这个条件的数列可以完全不收敛（条件不充分）。连无界数列 $n$ 都满足它：取 $l = 1$、$\varepsilon = 1$，则 $n \gt  2$ 的项全在邻域外。

**反例**：$a\_n = (-1)^{n} + \dfrac{1}{n}$，取 $l = 1$，$\varepsilon = \dfrac{1}{2}$。奇数项
$$a_{2n-1} = -1 + \frac{1}{2n-1} \le 1 - \frac{1}{2}$$
全部落在邻域外，有无穷多项；但这个数列根本不收敛：

- $a\_{2n} = 1 + \dfrac{1}{2n} \to 1$；
- $a\_{2n-1} = -1 + \dfrac{1}{2n-1} \to -1$。

由极限唯一性，$1 \neq -1$，矛盾。所以"有无穷项在邻域外"既不是收敛的充分条件，也与收敛的定义相冲突。

</div>
</details>

<details class="callout note" id="limit-negation" data-callout="note" markdown="block" open>
<summary class="callout-title">"不以 $A$ 为极限"怎么写</summary>
<div class="callout-content" markdown="block">

$$\exists \varepsilon > 0,\ \forall N \in \mathbb{N},\ \exists n > N,\ |a_n - A| \ge \varepsilon$$
判断"不收敛"时不要拿 $(-1)^{n}/n$ 当反例 —— 它是**收敛**的（趋于 $0$）。

</div>
</details>

### 4.2 $\varepsilon$–$N$ 证明的实践

<details class="callout tip" data-callout="tip" markdown="block" open>
<summary class="callout-title">自己的经验（保留）</summary>
<div class="callout-content" markdown="block">

- $\varepsilon$ 尽量**放成一次的**，$N$ 才好找；
- 当"$n \gt $ 某值"时成立，**勿忘 $n \in \mathbb{N}$**（写 $N = \lceil \cdot \rceil$ 比写小数稳妥）；
- 证明里写清 $\mid a\_n - a\mid  \lt  \varepsilon$ 的目标式，一步一步凑到它。

</div>
</details>

**例**：$\lim\limits\_{n \to \infty} \dfrac{1}{n} = 0$。对 $\forall \varepsilon \gt  0$，取 $N = \left\lceil \dfrac{1}{\varepsilon} \right\rceil$，当 $n \gt  N$ 时

$$\left| \frac{1}{n} - 0 \right| = \frac{1}{n} < \varepsilon$$

<details class="callout key point" data-callout="key point" markdown="block" open>
<summary class="callout-title">该记住的常见极限</summary>
<div class="callout-content" markdown="block">

$$\lim_{n \to \infty} \sqrt[n]{n} = 1, \qquad \lim_{n \to \infty} \sqrt[n]{k} = 1\ (k > 0), \qquad \lim_{n \to \infty} \frac{n^{k}}{2^{n}} = 0$$
直观：$n$ 次根会把幂次压平，而指数增长压过任何多项式。

**思考**：若 $\lim\limits\_{n \to \infty} a\_n = a$，则 $\lim\limits\_{n \to \infty} \dfrac{a\_1 + a\_2 + \cdots + a\_n}{n} = a$ —— 算术平均也收敛到同一个值（注意外层必须写 $\lim$，否则左边是个随 $n$ 变化的量，不能等于常数 $a$）。

</div>
</details>

### 4.3 极限的性质

<details class="callout theorem" id="sign-preserving" data-callout="theorem" markdown="block" open>
<summary class="callout-title">保号性</summary>
<div class="callout-content" markdown="block">

设 $\\{a\_n\\}$ 收敛，$\lim\limits\_{n \to \infty} a\_n = A \gt  0$，则存在 $N$，当 $n \gt  N$ 时 $a\_n \gt  0$。

**证**：取 $\varepsilon = A$，存在 $N$，当 $n \gt  N$ 时 $\mid a\_n - A\mid  \lt  \varepsilon = A$，故 $a\_n \gt  A - \varepsilon = 0$。

</div>
</details>

- **推论 1**：$\\{a\_n\\}$ 收敛于 $A$，若存在 $N$ 使 $n \gt  N$ 时 $a\_n \ge 0$，则 $A \ge 0$。
- **推论 2**：$\\{a\_n\\}$ 收敛于 $A \gt  0$，则存在 $N$，当 $n \gt  N$ 时 $a\_n \ge \dfrac{A}{2}$。

<details class="callout theorem" id="order-preserving" data-callout="theorem" markdown="block" open>
<summary class="callout-title">保序性（性质 4）</summary>
<div class="callout-content" markdown="block">

设 $\\{a\_n\\}, \\{b\_n\\}$ 收敛，极限分别为 $A, B$。若 $A \gt  B$，则存在 $N$，当 $n \gt  N$ 时 $a\_n \gt  b\_n$。

**证**：取 $\varepsilon = \dfrac{A - B}{2} \gt  0$。由 $a\_n \to A$，存在 $N\_1$，当 $n \gt  N\_1$ 时
$$|a_n - A| < \varepsilon \ \Rightarrow\ a_n > A - \varepsilon = \frac{A + B}{2}$$
由 $b\_n \to B$，存在 $N\_2$，当 $n \gt  N\_2$ 时
$$|b_n - B| < \varepsilon \ \Rightarrow\ b_n < B + \varepsilon = \frac{A + B}{2}$$
取 $N = \max\\{N\_1, N\_2\\}$，当 $n \gt  N$ 时 $b\_n \lt  \dfrac{A+B}{2} \lt  a\_n$，得证。

</div>
</details>

<details class="callout question" data-callout="question" markdown="block" open>
<summary class="callout-title">把 $A \gt  B$ 换成 $A \ge B$，还能得到"存在 $N$，当 $n \gt  N$ 时 $a\_n \ge b\_n$"吗？</summary>
<div class="callout-content" markdown="block">

不能。反例：$a\_n = 0$，$b\_n = \dfrac{1}{n}$，此时 $A = B = 0$，但 $a\_n = 0 \lt  b\_n$ 对一切 $n$ 成立。严格的大小关系在取极限后会被"抹平"。

</div>
</details>

- **推论 3**：$\\{a\_n\\}, \\{b\_n\\}$ 收敛于 $A, B$，若存在 $N$ 使 $n \gt  N$ 时 $a\_n \le b\_n$，则 $A \le B$。

<details class="callout danger" data-callout="danger" markdown="block" open>
<summary class="callout-title">注意：$a\_n \le b\_n$ 推不出"$a\_n \le B$"</summary>
<div class="callout-content" markdown="block">

已知 $a\_n \le b\_n\ (n \gt  N)$，$\\{a\_n\\} \to A$，$\\{b\_n\\} \to B$，能得到的只有 $A \le B$；
**得不到**"存在 $N$，当 $n \gt  N$ 时 $a\_n \le B$"。
反例：$a\_n = b\_n = \dfrac{1}{n}$，则 $A = B = 0$，但 $a\_n = \dfrac{1}{n} \gt  0 = B$ 对一切 $n$ 成立。

</div>
</details>

### 4.4 四则运算与复合

<details class="callout note" id="limit-arithmetic" data-callout="note" markdown="block" open>
<summary class="callout-title">什么时候能拆</summary>
<div class="callout-content" markdown="block">

$\lim a\_n = a$ 与 $\lim b\_n = b$ **都存在**时才能拆开运算，而且只对**有限次**运算生效。

- $\lim\limits\_{n \to \infty} (k\_1 a\_n + k\_2 b\_n) = k\_1 a + k\_2 b$（线性组合）
- $\lim\limits\_{n \to \infty} a\_n^{k} = a^{k}$（$k \in \mathbb{N}^{\*}$）
- $\lim\limits\_{n \to \infty} f(a\_n) = f(a)$，其中 $f$ 为多项式函数（即 $f$ 在 $a$ 处连续）
$$f(x) = b_m x^{m} + b_{m-1} x^{m-1} + \cdots + b_1 x + b_0$$
做法：构造一个新序列 $f(a\_n)$，逐项用四则运算推。

</div>
</details>

### 4.5 根式与幂的极限

<details class="callout theorem" id="sqrt-limit" data-callout="theorem" markdown="block" open>
<summary class="callout-title">开方保持极限</summary>
<div class="callout-content" markdown="block">

若 $a\_n \ge 0$ 且 $\lim\limits\_{n \to \infty} a\_n = a \ge 0$，则 $\lim\limits\_{n \to \infty} \sqrt{a\_n} = \sqrt{a}$。

**证**：分两种情形。

- $a = 0$：由 $a\_n \to 0$，$\forall \varepsilon \gt  0$，当 $n$ 充分大时 $0 \le a\_n \lt  \varepsilon^{2}$，于是 $\sqrt{a\_n} \lt  \varepsilon$。
- $a \gt  0$：$n$ 充分大时 $a\_n \gt  \dfrac{a}{2} \gt  0$，且
$$|\sqrt{a_n} - \sqrt{a}| = \frac{|a_n - a|}{\sqrt{a_n} + \sqrt{a}} \le \frac{|a_n - a|}{\sqrt{a}} \to 0$$

（常见错误：把取完极限的分母提前代入，写成 $\dfrac{0 \cdot \mid a\_n - a\mid }{2\sqrt a}$。正确做法是保留上界 $\dfrac{\mid a\_n - a\mid }{\sqrt a}$，再由 $a\_n \to a$ 得到结论。）

</div>
</details>

<details class="callout example" data-callout="example" markdown="block" open>
<summary class="callout-title">两道"分母有理化"的题</summary>
<div class="callout-content" markdown="block">

$$\lim_{n \to \infty} n\left(\sqrt{n^{2}+1} - \sqrt{n^{2}-1}\right) = \lim_{n \to \infty} n \cdot \frac{2}{\sqrt{n^{2}+1} + \sqrt{n^{2}-1}} = \lim_{n \to \infty} \frac{2}{\sqrt{1+\frac{1}{n^{2}}} + \sqrt{1-\frac{1}{n^{2}}}} = 1$$

$$\lim_{n \to \infty} \frac{5^{n+1} - (-2)^{n}}{3 \times 5^{n} + 2 \times 3^{n}} = \lim_{n \to \infty} \frac{5 - \left(-\frac{2}{5}\right)^{n}}{3 + 2\left(\frac{3}{5}\right)^{n}} = \frac{5}{3}$$

（第二题的想法：分子分母同除最大的底数 $5^{n}$，其余项都趋于 $0$。）

</div>
</details>

### 4.6 夹逼定理

<details class="callout theorem" id="squeeze" data-callout="theorem" markdown="block" open>
<summary class="callout-title">夹逼定理</summary>
<div class="callout-content" markdown="block">

若存在 $N$，当 $n \gt  N$ 时 $c\_n \le a\_n \le b\_n$，且 $\lim\limits\_{n \to \infty} b\_n = \lim\limits\_{n \to \infty} c\_n = l$，则 $\lim\limits\_{n \to \infty} a\_n = l$。

</div>
</details>

- 技巧：可以构造**常数列**来夹逼。
- 常用结论（$a, b \gt  0$）：

$$\lim_{n \to \infty} \sqrt[n]{a^{n} + b^{n}} = \max\{a, b\}, \qquad \lim_{n \to \infty} \sqrt[n]{a^{n} + k b^{n}} = \max\{a, b\}\ \ (k > 0)$$

### 4.7 单调有界定理

<details class="callout theorem" id="monotone-bounded" data-callout="theorem" markdown="block" open>
<summary class="callout-title">单调有界定理</summary>
<div class="callout-content" markdown="block">

单调且有界的数列必有极限。具体地，$\\{x\_n\\}$ 单调增且有上界时
$$\lim_{n \to \infty} x_n = \sup\{x_n\}$$

</div>
</details>

**严格证明**：设 $\\{x\_n\\}$ 单调增且有上界，由 [上确界](#sup-inf-def) 与 [确界原理](#completeness)，记 $a = \sup\\{x\_n\\}$。对任意 $\varepsilon \gt  0$，$a - \varepsilon$ 不再是上界，故存在 $N$ 使 $x\_N \gt  a - \varepsilon$。由单调性，当 $n \gt  N$ 时

$$a - \varepsilon < x_N \le x_n \le a < a + \varepsilon$$

即 $\mid x\_n - a\mid  \lt  \varepsilon$，故 $x\_n \to a$。

<details class="callout tip" data-callout="tip" markdown="block" open>
<summary class="callout-title">直观记法（保留自己的话）</summary>
<div class="callout-content" markdown="block">

用小数表示看：$x\_n = m\_n + 0.a\_1^{(n)} a\_2^{(n)} \cdots$。单调增有上界保证整数部分 $m\_n$ 最终不再变化；再看小数位，上一位一旦"锁定"，下一位只能从 $\\{0, 1, \dots, 9\\}$ 中取，于是逐位锁定出一个小数 —— 它就是上确界。

</div>
</details>

<details class="callout example" data-callout="example" markdown="block" open>
<summary class="callout-title">应用：Euler 常数 $\gamma$ 存在</summary>
<div class="callout-content" markdown="block">

证明 $\lim\limits\_{n \to \infty} \left(1 + \dfrac{1}{2} + \cdots + \dfrac{1}{n} - \ln n\right)$ 存在，该极限记为 **Euler 常数 $\gamma$**。

记 $c\_n = 1 + \dfrac{1}{2} + \cdots + \dfrac{1}{n} - \ln n$，用不等式 $\dfrac{1}{n+1} \lt  \ln\!\left(1 + \dfrac{1}{n}\right) \lt  \dfrac{1}{n}$：

- **单调减**：$c\_{n+1} - c\_n = \dfrac{1}{n+1} - \ln\!\left(1 + \dfrac{1}{n}\right) \lt  0$；
- **有下界**：$\ln n = \sum\_{k=1}^{n-1} \ln\!\left(1 + \dfrac{1}{k}\right) \lt  \sum\_{k=1}^{n-1} \dfrac{1}{k} \lt  1 + \dfrac{1}{2} + \cdots + \dfrac{1}{n}$，故 $c\_n \gt  0$。

由 [单调有界定理](#monotone-bounded)，$c\_n$ 收敛。

</div>
</details>

<details class="callout example" data-callout="example" markdown="block" open>
<summary class="callout-title">应用：$x\_{n+1} = x\_n(1 - x\_n)$</summary>
<div class="callout-content" markdown="block">

设 $0 \lt  x\_1 \lt  1$，$x\_{n+1} = x\_n(1 - x\_n)$。证明：(1) $\\{x\_n\\}$ 收敛；(2) $\lim\limits\_{n \to \infty} n x\_n = 1$。

(1) $0 \lt  x\_{n+1} \lt  x\_n \lt  1$（因 $0 \lt  1 - x\_n \lt  1$），单调减且有下界 $0$，故收敛；设极限为 $a$，则 $a = a(1 - a) \Rightarrow a = 0$。
(2) 记 $y\_n = \dfrac{1}{x\_n}$，则 $y\_{n+1} = \dfrac{y\_n}{1 - x\_n}$，于是
$$y_{n+1} - y_n = \frac{1}{x_n}\left(\frac{1}{1 - x_n} - 1\right) = \frac{1}{1 - x_n} \longrightarrow 1$$
由 [Stolz 定理](#stolz)，$\dfrac{y\_n}{n} \to 1$，即 $n x\_n \to 1$。

</div>
</details>

### 4.8 子列

<details class="callout theorem" id="subsequence" data-callout="theorem" markdown="block" open>
<summary class="callout-title">子列继承极限</summary>
<div class="callout-content" markdown="block">

若 $\lim\limits\_{n \to \infty} a\_n = L$，则 $\\{a\_n\\}$ 的任何子列也收敛于 $L$。

</div>
</details>

<details class="callout key point" data-callout="key point" markdown="block" open>
<summary class="callout-title">更强的结论（用于"合并"）</summary>
<div class="callout-content" markdown="block">

$$\begin{cases} \lim\limits_{n \to \infty} a_{2n} = A \\[4pt] \lim\limits_{n \to \infty} a_{2n-1} = A \end{cases} \Longrightarrow \lim_{n \to \infty} a_n = A$$
推广：若对 $r = 0, 1, \dots, p-1$ 都有 $\lim\limits\_{n \to \infty} a\_{pn+r} = A$，则 $\lim\limits\_{n \to \infty} a\_n = A$（即按模 $p$ 的完全剩余系分类）。

</div>
</details>

它的逆否用法很实用：只要找到两个子列极限不同（或某个子列发散），就能断定原数列不收敛，见 [前面  SYNC\_MATH\_385  的反例](#limit-tail)。

### 4.9 Stolz 定理

<details class="callout theorem" id="stolz" data-callout="theorem" markdown="block" open>
<summary class="callout-title">Stolz 定理（离散的洛必达法则）</summary>
<div class="callout-content" markdown="block">

设 $\\{y\_n\\}$ 严格单调递增且 $\lim\limits\_{n \to \infty} y\_n = +\infty$。若
$$\lim_{n \to \infty} \frac{x_n - x_{n-1}}{y_n - y_{n-1}} = a$$
则 $\lim\limits\_{n \to \infty} \dfrac{x\_n}{y\_n} = a$。其中 $a$ 可以是有限数，也可以是 $+\infty$ 或 $-\infty$。

</div>
</details>

- 用差分形式去表示 $x\_n$、$y\_n$，凑出已知极限；
- 用无穷大去抵消"有限的累加项"。

<details class="callout example" data-callout="example" markdown="block" open>
<summary class="callout-title">例：幂和与 $n^{k+1}$</summary>
<div class="callout-content" markdown="block">

$$\lim_{n \to \infty} \frac{\sum_{i=1}^{n} i^{k}}{n^{k+1}} = \lim_{n \to \infty} \frac{(n+1)^{k}}{(n+1)^{k+1} - n^{k+1}} = \frac{1}{k+1}$$
因为分母 $(n+1)^{k+1} - n^{k+1} \sim (k+1)n^{k}$。

</div>
</details>

### 4.10 无穷小量与无穷大量

<details class="callout theorem" id="infinitesimal" data-callout="theorem" markdown="block" open>
<summary class="callout-title">有界 $\times$ 无穷小 $=$ 无穷小</summary>
<div class="callout-content" markdown="block">

若 $\lim\limits\_{n \to \infty} a\_n = 0$ 且 $\mid b\_n\mid  \le M$，则 $\lim\limits\_{n \to \infty} a\_n b\_n = 0$。

</div>
</details>

<details class="callout warning" id="infinite-large" data-callout="warning" markdown="block" open>
<summary class="callout-title">无穷大量 $\neq$ 无界量</summary>
<div class="callout-content" markdown="block">

无穷大量要求 $\mid a\_n\mid  \to +\infty$（整条数列都跑向无穷），无界量只要求"没有界"。
例：$n$ 与 $\big((-1)^{n} + 1\big)n$。前者是无穷大量；后者无界（偶数项为 $0$，奇数项为 $2n$），但不是无穷大量。

</div>
</details>

- 同号无穷大量之和仍是无穷大量；
- 无穷大量 $\pm$ 有界量仍是无穷大量（按 $\mid a\_n\mid  \to \infty$ 的意义；若 $a\_n \to +\infty$ 则 $a\_n + b\_n \to +\infty$）。

---

## 5 重要极限：$e$

### 5.1 $(1 + \frac{1}{n})^{n}$ 单调有界

<details class="callout theorem" id="e-definition" data-callout="theorem" markdown="block" open>
<summary class="callout-title">单调增 + 有上界</summary>
<div class="callout-content" markdown="block">

序列 $\left(1 + \dfrac{1}{n}\right)^{n}$ 单调递增且有上界，故收敛，记
$$\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^{n} = e$$

</div>
</details>

**① 单调增**：把两个序列都作二项式展开

$$\left(1 + \frac{1}{n}\right)^{n} = 1 + 1 + \sum_{k=2}^{n} \frac{1}{k!}\left(1 - \frac{1}{n}\right)\left(1 - \frac{2}{n}\right) \cdots \left(1 - \frac{k-1}{n}\right)$$

$$\left(1 + \frac{1}{n+1}\right)^{n+1} = 1 + 1 + \sum_{k=2}^{n} \frac{1}{k!}\left(1 - \frac{1}{n+1}\right)\cdots\left(1 - \frac{k-1}{n+1}\right) + \left(\frac{1}{n+1}\right)^{n+1}$$

逐项比对（每一项的因子 $1 - \frac{j}{n+1} \gt  1 - \frac{j}{n}$，而且第二式还多了正项），得

$$\left(1 + \frac{1}{n}\right)^{n} < \left(1 + \frac{1}{n+1}\right)^{n+1}$$

**② 有界**：

$$\left(1 + \frac{1}{n}\right)^{n} < 1 + 1 + \frac{1}{2!} + \frac{1}{3!} + \cdots + \frac{1}{n!} < 1 + 1 + \frac{1}{2!} + \frac{1}{3\times2} + \frac{1}{4\times3} + \cdots + \frac{1}{n(n-1)}$$

而 $1 + 1 + \dfrac{1}{2!} + \displaystyle\sum\_{k=3}^{n} \frac{1}{k(k-1)} = 2 + \frac{1}{2} + \left(\frac{1}{2} - \frac{1}{n}\right) = 3 - \frac{1}{n} \lt  3$，故有上界。

由 [单调有界定理](#monotone-bounded)，极限存在，记为 $e$。

<details class="callout tip" data-callout="tip" markdown="block" open>
<summary class="callout-title">另一个"很惊人的注意力"（保留）</summary>
<div class="callout-content" markdown="block">

也可以直接看 $(1 + \frac{1}{n})^{n+1}$：它是**单调递减**的且有下界 $1$，所以也有极限。两条序列刚好从两侧逼近 $e$（见下）。

</div>
</details>

### 5.2 $e$ 的上下界

<details class="callout key point" id="e-bounds" data-callout="key point" markdown="block" open>
<summary class="callout-title">两侧夹住 $e$</summary>
<div class="callout-content" markdown="block">

$$\left(1 + \frac{1}{n}\right)^{n} < e < \left(1 + \frac{1}{n}\right)^{n+1}$$
$n$ 越大，所得的界越精确。

</div>
</details>

**证法一（拉格朗日中值定理）**：对 $0 \lt  a \lt  b$，$n \in \mathbb{N}^{\*}$，用 $f(x) = x^{n+1}$ 得

$$(n+1)a^{n} < \frac{b^{n+1} - a^{n+1}}{b - a} < (n+1)b^{n}$$

取 $a = 1 + \dfrac{1}{n+1}$、$b = 1 + \dfrac{1}{n}$ 即得。

**证法二（初等解法，AM–GM）**：

$$\sqrt[n+1]{\left(1 + \frac{1}{n}\right)^{n} \cdot 1} \le \frac{n\left(1 + \frac{1}{n}\right) + 1}{n+1} = \frac{n+2}{n+1} = 1 + \frac{1}{n+1}$$

两边取 $n+1$ 次方得 $\left(1 + \dfrac{1}{n}\right)^{n} \le \left(1 + \dfrac{1}{n+1}\right)^{n+1}$。

对序列 $\left(1 + \dfrac{1}{n}\right)^{n+1}$ 先取倒数，再对 $\left(\dfrac{n}{n+1}\right)^{n+1}$ 用 AM–GM：

$$\sqrt[n+1]{\left(\frac{n}{n+1}\right)^{n+1} \cdot 1} \le \frac{\frac{n}{n+1}(n+1) + 1}{n+2} = \frac{n+1}{n+2}$$

即 $\left(1 + \dfrac{1}{n+1}\right)^{n+2} \ge \left(1 + \dfrac{1}{n}\right)^{n+1}$，说明 $(1+\frac1n)^{n+1}$ 单调减；两端合并就得到上面的双边不等式。

### 5.3 $e$ 的级数表示

<details class="callout theorem" id="e-series" data-callout="theorem" markdown="block" open>
<summary class="callout-title">$e = \sum\limits\_{n=0}^{\infty} \frac{1}{n!}$</summary>
<div class="callout-content" markdown="block">

$$e = \lim_{n \to \infty} \sum_{k=0}^{n} \frac{1}{k!}$$

</div>
</details>

**两边夹**：

- 由 5.1 的 ② 已证 $\left(1 + \frac{1}{n}\right)^{n} \lt  \sum\_{k=0}^{n} \frac{1}{k!}$，故 $e \le \lim\limits\_{n \to \infty} \sum\limits\_{k=0}^{n} \frac{1}{k!}$；
- 反过来，对**取定**的 $k$，

$$e = \lim_{n \to \infty}\left(1 + 1 + \sum_{i=2}^{n} \frac{1}{i!}\left(1 - \frac{1}{n}\right)\cdots\left(1 - \frac{i-1}{n}\right)\right) \ge \lim_{n \to \infty}\left(1 + 1 + \sum_{i=2}^{k} \frac{1}{i!}\left(1 - \frac{1}{n}\right)\cdots\left(1 - \frac{i-1}{n}\right)\right) = \sum_{i=0}^{k} \frac{1}{i!}$$

（最后一步：有限项的极限逐项算出，因子 $\left(1 - \frac{1}{n}\right)\cdots \to 1$。）

- 对 $k$ 取极限并用 [夹逼定理](#squeeze)，得 $e = \sum\limits\_{n=0}^{\infty} \dfrac{1}{n!}$。

### 5.4 $e$ 是无理数

<details class="callout theorem" id="e-irrational" data-callout="theorem" markdown="block" open>
<summary class="callout-title">$e$ 是无理数</summary>
<div class="callout-content" markdown="block">

**证（反证）**：设 $e = \dfrac{p}{q}$，$p, q \in \mathbb{N}$ 且互质。由 [ SYNC\_MATH\_446  的级数表示](#e-series)，
$$e \cdot q! = \underbrace{\left(1 + 1 + \frac{1}{2!} + \cdots + \frac{1}{q!}\right)q!}_{\text{整数}} + \underbrace{\lim_{n \to \infty}\left[\frac{1}{(q+1)!} + \frac{1}{(q+2)!} + \cdots + \frac{1}{(q+n)!}\right]}_{\text{记为 } r}$$
左边 $e\,q! = p\,(q-1)!$ 是整数，前一项也是整数，所以 $r$ 必须是整数。但
$$0 < r < \lim_{n \to \infty}\left[\frac{1}{q+1} + \left(\frac{1}{q+1}\right)^{2} + \cdots + \left(\frac{1}{q+1}\right)^{n}\right] \le \frac{1}{q}$$
又 $e \in (2, 3)$ 不是整数，故 $q \ge 2$，从而 $0 \lt  r \lt  \dfrac{1}{q} \le \dfrac{1}{2} \lt  1$，与"$r$ 是整数"矛盾。

故假设不成立，$e$ 为无理数。

</div>
</details>

### 5.5 与 $e$ 有关的几个极限

- 若 $p\_n \gt  0$ 是正无穷大量，则 $\lim\limits\_{n \to \infty}\left(1 + \dfrac{1}{p\_n}\right)^{p\_n} = e$。
  **证**：由 $\left(1+\frac1n\right)^n \to e$，$\exists N\_1$ 使 $n \gt  N\_1$ 时 $\left\mid \left(1+\frac1n\right)^n - e\right\mid  \lt  \varepsilon$；又 $p\_n \to +\infty$，$\exists N\_2$ 使 $n \gt  N\_2$ 时 $p\_n \gt  N\_1$，故 $n \gt  N\_2$ 时 $\left\mid \left(1+\frac{1}{p\_n}\right)^{p\_n} - e\right\mid  \lt  \varepsilon$。

- $\lim\limits\_{n \to \infty}\left(1 + \dfrac{1}{n^{2} + n}\right)^{n} = \lim\limits\_{n \to \infty}\left[\left(1 + \dfrac{1}{n^{2}+n}\right)^{n^{2}+n}\right]^{\frac{n}{n^{2}+n}} = e^{0} = 1$。
- $\lim\limits\_{n \to \infty} a\_n^{b\_n} = a^{b}$（$\lim a\_n = a \gt  0$，$\lim b\_n = b$）：

$$\lim_{n \to \infty} e^{b_n \ln a_n} = e^{b \ln a} = a^{b}$$

- $\lim\limits\_{x \to \infty}\left(1 + \dfrac{\alpha}{x}\right)^{\beta x} = e^{\alpha\beta}$（函数版推广）。

---

## 6 几个典型函数

- $X$ 是**定义域**，$f(X) = \\{f(x) \mid x \in X\\}$ 是**值域**，且 $f(X) \subset Y$（$Y$ 为陪域）。

<details class="callout definition" id="sign-function" data-callout="definition" markdown="block" open>
<summary class="callout-title">符号函数</summary>
<div class="callout-content" markdown="block">

$$\operatorname{sgn} x = \begin{cases} 1, & x > 0 \\ 0, & x = 0 \\ -1, & x < 0 \end{cases}$$

</div>
</details>

<details class="callout definition" id="periodic-function" data-callout="definition" markdown="block" open>
<summary class="callout-title">周期函数</summary>
<div class="callout-content" markdown="block">

若存在 $T \neq 0$，使 $\forall x \in X$ 都有 $x + T \in X$ 且 $f(x + T) = f(x)$，则称 $f$ 为**周期函数**，$T$ 为一个周期。
注意：周期函数**不一定有最小正周期**。

</div>
</details>

<details class="callout example" id="dirichlet-function" data-callout="example" markdown="block" open>
<summary class="callout-title">Dirichlet 函数</summary>
<div class="callout-content" markdown="block">

$$D(x) = \begin{cases} 1, & x \in \mathbb{Q} \\ 0, & x \in \mathbb{Q}^{c} \end{cases}$$

- 由 [周期函数](#periodic-function) 的定义：$\forall q \in \mathbb{Q}$，$D(x + q) = D(x)$ —— **每个有理数都是它的周期**；
- 于是它没有最小正周期，正是"周期可以不设最小正周期"的现成例子。

</div>
</details>

<details class="callout note" id="hyperbolic" data-callout="note" markdown="block" open>
<summary class="callout-title">双曲函数</summary>
<div class="callout-content" markdown="block">

$$\operatorname{sh} x = \frac{e^{x} - e^{-x}}{2}, \qquad \operatorname{ch} x = \frac{e^{x} + e^{-x}}{2}$$

- $\operatorname{ch}^{2} x - \operatorname{sh}^{2} x = 1$；
- $\operatorname{ch}' x = \operatorname{sh} x$，$\operatorname{sh}' x = \operatorname{ch} x$。

</div>
</details>

- **复合函数**：$y = f(g(x))$，需满足 $g$ 的值域落在 $f$ 的定义域内。

---

## 7 函数极限

### 7.1 定义

<details class="callout definition" id="punctured-neighborhood" data-callout="definition" markdown="block" open>
<summary class="callout-title">空心（去心）邻域</summary>
<div class="callout-content" markdown="block">

$$(x_0 - \delta, x_0 + \delta) \setminus \{x_0\} = (x_0 - \delta, x_0) \cup (x_0, x_0 + \delta)$$
简记为 $U^{\circ}(x\_0, \delta)$ 或 $U^{\circ}(x\_0)$。

</div>
</details>

<details class="callout definition" id="function-limit" data-callout="definition" markdown="block" open>
<summary class="callout-title">函数极限</summary>
<div class="callout-content" markdown="block">

$\forall \varepsilon \gt  0,\ \exists \delta \gt  0$，当 $0 \lt  \mid x - x\_0\mid  \lt  \delta$ 时 $\mid f(x) - L\mid  \lt  \varepsilon$，则记 $\lim\limits\_{x \to x\_0} f(x) = L$。

- $\varepsilon$ 任选、$\delta$ 随 $\varepsilon$ 变动，动态地描述"要多小有多小"；
- $\triangle$ **不要求 $f$ 在 $x\_0$ 处有定义**。

</div>
</details>

- **单侧极限**：在 $(x\_0, x\_0 + \delta)$ 或 $(x\_0 - \delta, x\_0)$ 上讨论；

$$\lim_{x \to x_0} f(x) = L \iff \lim_{x \to x_0^{+}} f(x) = \lim_{x \to x_0^{-}} f(x) = L$$

- **在无穷远处的极限**：设 $f$ 在 $(-\infty, A) \cup (B, +\infty)$ 上有定义，若 $\forall \varepsilon \gt  0,\ \exists M \gt  0$，当 $\mid x\mid  \gt  M$ 时 $\mid f(x) - L\mid  \lt  \varepsilon$，则记 $\lim\limits\_{x \to \infty} f(x) = L$。

### 7.2 Heine 定理

<details class="callout theorem" id="heine" data-callout="theorem" markdown="block" open>
<summary class="callout-title">Heine（海涅）定理</summary>
<div class="callout-content" markdown="block">

$$\lim_{x \to a} f(x) = L \iff \text{对任意 } x_n \to a\ (x_n \neq a)\text{，都有 } \lim_{n \to \infty} f(x_n) = L$$

</div>
</details>

用途：反证极限不存在 —— 只要找出两条趋于 $a$ 的序列 $x\_n, x\_n'$ 使 $f(x\_n)$ 与 $f(x\_n')$ 极限不同即可。

### 7.3 性质

- **唯一性**：极限存在则唯一。
- **局部有界性**：在某点附近有界（不是整体有界，与 [有界性定理](#boundedness-theorem) 里的"整体有界"对照着看）。即 $\exists \delta$，当 $x \in (x\_0 - \delta, x\_0 + \delta)$ 时 $\mid f(x)\mid  \le M \in \mathbb{R}\_{+}$。
- **无穷小量**：$\lim\limits\_{x \to a} f(x) = 0$，称 $x \to a$ 时 $f$ 为无穷小量；

$$\lim_{x \to a} f(x) = L \iff \lim_{x \to a} (f(x) - L) = 0$$

- 有界 $\times$ 无穷小 $=$ 无穷小：$x \to a$ 时 $\alpha(x) \to 0$，$h(x)$ 有界，则 $\alpha(x)h(x) \to 0$。
- $\lim\limits\_{x \to a} f(x) = \infty \iff \lim\limits\_{x \to a} \dfrac{1}{f(x)} = 0$；若 $f(x) \neq 0$，则 $\lim\limits\_{x \to a} f(x) = 0 \iff \lim\limits\_{x \to a} \dfrac{1}{f(x)} = \infty$。

<details class="callout warning" data-callout="warning" markdown="block" open>
<summary class="callout-title">无界 ≠ 无穷大（函数版）</summary>
<div class="callout-content" markdown="block">

无界只说明"没有界"，不能说"趋于无穷大"（数列版的例子见 [无穷大量 ≠ 无界量](#infinite-large)）。
例：$f(x) = \dfrac{1}{x}\sin\dfrac{1}{x}$（$x \to 0$）。取 $x = \dfrac{1}{2n\pi}$ 时 $f(x) = 0$，而取 $x = \dfrac{1}{2n\pi + \pi/2}$ 时 $\mid f(x)\mid  \to +\infty$，所以它无界，但极限不是 $\infty$。

</div>
</details>

<details class="callout theorem" id="function-limit-props" data-callout="theorem" markdown="block" open>
<summary class="callout-title">函数极限的保号性与四则运算</summary>
<div class="callout-content" markdown="block">

- **保号性**：$\lim\limits\_{x \to a} f(x) = A \gt  B$，取 $\varepsilon = A - B$，则存在 $\delta$，当 $x \in U^{\circ}(a, \delta)$ 时 $\mid f(x) - A\mid  \lt  A - B$，故 $f(x) \gt  B$。
- **保序性**：在 $U^{\circ}(a, \delta)$ 上 $f(x) \ge g(x)$，若 $f \to A,\ g \to B$，则 $A \ge B$。
- **四则运算**：各自极限存在时才可拆开，且 $B \neq 0$ 时
$$\lim_{x \to a}(f \pm g) = A \pm B,\quad \lim_{x \to a}(f g) = AB,\quad \lim_{x \to a}\frac{f}{g} = \frac{A}{B}$$

</div>
</details>

<details class="callout example" data-callout="example" markdown="block" open>
<summary class="callout-title">例：多项式型的技巧</summary>
<div class="callout-content" markdown="block">

$$\lim_{x \to 1} \frac{x^{n} - 1}{x^{m} - 1} = \lim_{x \to 1} \frac{x^{n-1} + x^{n-2} + \cdots + 1}{x^{m-1} + x^{m-2} + \cdots + 1} = \frac{n}{m}$$

</div>
</details>

<details class="callout example" data-callout="example" markdown="block" open>
<summary class="callout-title">$\varepsilon$–$\delta$ 的模板：证明 $\lim\limits\_{x \to 2} x^{2} = 4$</summary>
<div class="callout-content" markdown="block">

先用 $\delta$ 把 $x$ 限制在一个范围内，把"含 $x$ 的因子"放大成常数，再让剩下的部分 $\lt  \varepsilon$。

先限定 $\mid x - 2\mid  \lt  1$，则 $\mid x + 2\mid  \lt  5$，于是
$$|x^{2} - 4| = |x - 2|\,|x + 2| < 5|x - 2|$$
要让它 $\lt  \varepsilon$，只需 $\mid x - 2\mid  \lt  \dfrac{\varepsilon}{5}$。故取
$$\delta = \min\left\{1, \frac{\varepsilon}{5}\right\}$$

记法：**$M$、$N$ 取 $\max$，$\delta$ 取 $\min$。**

</div>
</details>

### 7.4 夹逼与单调收敛（函数版）

<details class="callout theorem" id="function-squeeze" data-callout="theorem" markdown="block" open>
<summary class="callout-title">函数版的夹逼</summary>
<div class="callout-content" markdown="block">

若在 $U^{\circ}(x\_0, \delta)$ 上 $\varphi(x) \le f(x) \le \phi(x)$，且 $\lim\limits\_{x \to x\_0} \varphi(x) = \lim\limits\_{x \to x\_0} \phi(x) = A$，则 $\lim\limits\_{x \to x\_0} f(x) = A$。

</div>
</details>

**例**：$\lim\limits\_{x \to \infty} \dfrac{[x]}{x} = 1$。由 $x - 1 \lt  [x] \le x$ 得

- $x \gt  0$ 时 $1 - \dfrac{1}{x} \lt  \dfrac{[x]}{x} \le 1$；
- $x \lt  0$ 时 $1 - \dfrac{1}{x} \gt  \dfrac{[x]}{x} \ge 1$（除以负数，不等号反向）。

两边取极限即得 $1$。

<details class="callout theorem" id="function-monotone" data-callout="theorem" markdown="block" open>
<summary class="callout-title">单调收敛（单侧）</summary>
<div class="callout-content" markdown="block">

- $(a - \delta, a)$ 上单调有界 $\Rightarrow \lim\limits\_{x \to a^{-}} f(x)$ 存在；
- $(a, a + \delta)$ 上单调有界 $\Rightarrow \lim\limits\_{x \to a^{+}} f(x)$ 存在；
- $(a, +\infty)$ 上单调有界 $\Rightarrow \lim\limits\_{x \to +\infty} f(x)$ 存在。

</div>
</details>

<details class="callout warning" data-callout="warning" markdown="block" open>
<summary class="callout-title">$\triangle$ 双侧不行</summary>
<div class="callout-content" markdown="block">

$f$ 在 $(a - \delta, a + \delta)$ 内单调有界，$\lim\limits\_{x \to a} f(x)$ **不一定存在**。
例：$f(x) = \begin{cases} x, \& 0 \lt  x \lt  1 \\ 2x, \& 1 \le x \lt  2 \end{cases}$，在 $x = 1$ 处左右极限分别是 $1$ 与 $2$。

</div>
</details>

### 7.5 复合函数与变量替换

<details class="callout theorem" id="composite-limit" data-callout="theorem" markdown="block" open>
<summary class="callout-title">复合函数极限</summary>
<div class="callout-content" markdown="block">

设 $\lim\limits\_{x \to x\_0} g(x) = u\_0$，在 $x\_0$ 的某去心邻域内 $g(x) \neq u\_0$，且 $\lim\limits\_{u \to u\_0} f(u) = A$，则
$$\lim_{x \to x_0} f\big(g(x)\big) = A$$
若 $g(x) \equiv u\_0$，相当于只求 $f(u\_0)$，但极限的本质是去心邻域，此时不能直接代入。

</div>
</details>

- 例：$\lim\limits\_{x \to \infty} \operatorname{sgn}\!\left(\dfrac{1}{x^{2}}\right) = \lim\limits\_{u \to 0^{+}} \operatorname{sgn}(u) = 1$。
- $\lim\limits\_{x \to x\_0} f(x) = A \Rightarrow \lim\limits\_{x \to x\_0} e^{f(x)} = e^{A}$；若 $A \gt  0$，则 $\lim\limits\_{x \to x\_0} \ln f(x) = \ln A$。
- $\lim\limits\_{x \to x\_0} f(x)^{g(x)} = A^{B}$（$A \gt  0$）。

### 7.6 两个重要极限

<details class="callout key point" id="important-limits" data-callout="key point" markdown="block" open>
<summary class="callout-title">基本款</summary>
<div class="callout-content" markdown="block">

$$\lim_{x \to 0} \frac{\sin x}{x} = 1 \iff \lim_{x \to 0^{-}}\frac{\sin x}{x} = \lim_{x \to 0^{+}}\frac{\sin x}{x} = 1, \qquad \lim_{x \to \infty}\left(1 + \frac{1}{x}\right)^{x} = e$$
第二个就是数列 $e = \lim\limits\_{n \to \infty}\left(1+\frac{1}{n}\right)^{n}$（见 [e 的定义](#e-definition)）的函数版。

</div>
</details>

- $\lim\limits\_{x \to 0} \dfrac{\arcsin x}{x} = 1$（令 $\arcsin x = t$，即 $x = \sin t$）；
- $\lim\limits\_{x \to 0^{+}}\left(1 + \dfrac{1}{x}\right)^{x} = \lim\limits\_{t \to +\infty} (1 + t)^{\frac{1}{t}} = e^{\lim\limits\_{t \to +\infty} \frac{\ln(1+t)}{t}} = e^{0} = 1$；
- $\lim\limits\_{x \to \infty} x^{\frac{1}{x}} = 1$，$\lim\limits\_{x \to 0^{+}} x^{x} = 1$。

<details class="callout example" data-callout="example" markdown="block" open>
<summary class="callout-title">草稿：极限 $\ln(1+t)/t \to 0$ 的放缩</summary>
<div class="callout-content" markdown="block">

用 $\ln(1 + x) \lt  x$ 与 $\ln(1 + t) = 2\ln\sqrt{1+t} \lt  2(\sqrt{1+t} - 1)$：
$$0 \le \frac{\ln(1+t)}{t} \le \frac{2(\sqrt{1+t} - 1)}{t} = \frac{2}{\sqrt{1+t} + 1} \to 0$$
所以 $e^{0} = 1$。

</div>
</details>

---

## 8 闭区间上连续函数的性质

<details class="callout theorem" id="boundedness-theorem" data-callout="theorem" markdown="block" open>
<summary class="callout-title">有界性定理</summary>
<div class="callout-content" markdown="block">

闭区间 $[a, b]$ 上的连续函数必有界。
**证（反证）**：若无界，则对每个 $n$ 存在 $x\_n \in [a, b]$ 使 $\mid f(x\_n)\mid  \gt  n$。由 [Bolzano–Weierstrass 定理](#bolzano-weierstrass) 有子列 $x\_{n\_k} \to \xi \in [a, b]$，由连续性 $f(x\_{n\_k}) \to f(\xi)$ 有界，与 $\mid f(x\_{n\_k})\mid  \gt  n\_k \to \infty$ 矛盾。

</div>
</details>

<details class="callout theorem" id="extreme-value" data-callout="theorem" markdown="block" open>
<summary class="callout-title">最值定理</summary>
<div class="callout-content" markdown="block">

闭区间上的连续函数可取到最大值与最小值。

</div>
</details>

**证明思路**：设 $f$ 在 $[a, b]$ 上连续，则 $f([a, b])$ 有上、下确界。以最小值为例，设下确界为 $m$，由 [确界](#sup-inf-def) 的定义，存在 $\\{x\_n\\} \subset [a, b]$ 使

$$m \le f(x_n) < m + \frac{1}{n}$$

故 $f(x\_n) \to m$。又 $x\_n \in [a, b]$，由 [Bolzano–Weierstrass 定理](#bolzano-weierstrass) 有收敛子列 $x\_{n\_k} \to \xi$，其中 $\xi \in [a, b]$（闭区间的极限点还在区间内，注意这一点）。由连续性

$$f(\xi) = \lim_{k \to \infty} f(x_{n_k}) = m$$

即最小值可以取到。上确界同理。

<details class="callout theorem" id="intermediate-value" data-callout="theorem" markdown="block" open>
<summary class="callout-title">介值定理（零点存在定理）</summary>
<div class="callout-content" markdown="block">

若 $f$ 在 $[a, b]$ 上连续，$f(a)f(b) \lt  0$，则存在 $\xi \in (a, b)$ 使 $f(\xi) = 0$。

</div>
</details>

**证明思路**：二分法。不断把含变号的区间对半缩小，构造[闭区间套](#nested-intervals)，化归、不断缩小讨论范围，公共点 $\xi$ 处由连续性得 $f(\xi) = 0$。

---

## 9 无穷小量的比较

### 9.1 三种关系

设 $\alpha(x) \to 0$，$\beta(x) \to 0$，且 $\beta(x) \neq 0$：

- $\lim \dfrac{\alpha}{\beta} = 0$：$\alpha$ 是比 $\beta$ **高阶**的无穷小量；
- $\lim \dfrac{\alpha}{\beta} = c \neq 0$：**同阶**无穷小量；
- $\lim \dfrac{\alpha}{\beta} = 1$：**等价**无穷小量，记 $\alpha \sim \beta$（等价关系，有传递性）。

<details class="callout note" id="equivalent-infinitesimal" data-callout="note" markdown="block" open>
<summary class="callout-title">等价的一个刻画</summary>
<div class="callout-content" markdown="block">

设存在小邻域使 $\beta(x) \neq 0$，则
$$\alpha(x) \sim \beta(x) \iff \alpha(x) = \beta(x) + o(\beta(x))$$

</div>
</details>

### 9.2 常用等价无穷小（$x \to 0$）

<details class="callout key point" id="equivalent-infinitesimals" data-callout="key point" markdown="block" open>
<summary class="callout-title">背下来的一串</summary>
<div class="callout-content" markdown="block">

$$\sin x \sim x \sim \tan x \sim \arcsin x \sim \arctan x \sim e^{x} - 1 \sim \ln(1 + x)$$
$$1 - \cos x \sim \frac{1}{2}x^{2}, \qquad (1 + x)^{a} - 1 \sim ax\ (a \neq 0)$$
$$a^{x} - 1 \sim x\ln a\ (a > 0,\ a \neq 1), \qquad \log_a (1 + x) \sim \frac{x}{\ln a}, \qquad \ln\!\left(x + \sqrt{1 + x^{2}}\right) \sim x$$

</div>
</details>

### 9.3 替换的规则

- 若 $\alpha \sim \beta$，且 $\alpha f$、$\beta f$ 的极限都存在，则 $\lim \alpha f = \lim \beta f$；
- **只能在"相乘"时替换**（乘除因子可以换），加减法里替换会丢掉高阶项，出错。

---

## 10 常用工具与技巧

### 10.1 $\mathrm{AM} \ge \mathrm{GM}$（柯西归纳法）

$$\frac{1}{n}\sum_{i=1}^{n} a_i \ \ge\ \sqrt[n]{\prod_{i=1}^{n} a_i} \qquad (a_i \ge 0)$$

**证**（对 $n$ 归纳：用"$n-1$ 成立 $\Rightarrow$ $n$ 成立"）：

- $n = 1$ 显然。
- 设 $n - 1$ 时成立。不妨设 $a\_1 \le a\_2 \le \cdots \le a\_n$，记前 $n-1$ 个的算术平均为

$$y = \frac{1}{n-1}\sum_{i=1}^{n-1} a_i$$

由归纳假设与"$a\_n$ 最大"：

$$a_n \ge y \ge \sqrt[n-1]{a_1 a_2 \cdots a_{n-1}}$$

- 于是

$$\left(\frac{1}{n}\sum_{i=1}^{n} a_i\right)^{n} = \left(y + \frac{a_n - y}{n}\right)^{n} \ge y^{n} + n\,y^{n-1}\frac{a_n - y}{n} = y^{n-1} a_n \ge \prod_{i=1}^{n} a_i$$

第一个不等号用二项式展开：因 $a\_n - y \ge 0$，展开式其余各项都非负，只保留前两项。
<a id="amgm"></a>

### 10.2 放缩的经验

<details class="callout key point" data-callout="key point" markdown="block" open>
<summary class="callout-title">三条（保留自己的话）</summary>
<div class="callout-content" markdown="block">

① 抛弃常数项（$n \to \infty$ 时常数可忽略）；
② 抛弃"非决定项"（只留起决定作用的项）；
③ 常数 $1$ 是好用的垫脚石（凑 $\mathrm{AM}$–$\mathrm{GM}$、凑"$1$ 的变形"）。

</div>
</details>

### 10.3 综合例：$\dfrac{(n!)^{\alpha}}{n^{n}}$ 的极限

<details class="callout example" data-callout="example" markdown="block" open>
<summary class="callout-title">$\alpha \gt  1$ 时发散到 $+\infty$</summary>
<div class="callout-content" markdown="block">

$$\lim_{n \to \infty} \frac{(n!)^{\alpha}}{n^{n}} = +\infty$$
看相邻两项之比：
$$\frac{\frac{((n+1)!)^{\alpha}}{(n+1)^{n+1}}}{\frac{(n!)^{\alpha}}{n^{n}}} = \frac{(n+1)^{\alpha-1}}{\left(1 + \frac{1}{n}\right)^{n}} \to \frac{(n+1)^{\alpha-1}}{e} \to +\infty$$
比值趋于 $+\infty$，故数列本身趋于 $+\infty$（$\alpha \gt  1$ 时分子是 $n$ 的正幂次，压过常数 $e$）。

</div>
</details>

<details class="callout example" data-callout="example" markdown="block" open>
<summary class="callout-title">$\alpha \le 1$ 时趋于 $0$</summary>
<div class="callout-content" markdown="block">

此时 $(n!)^{\alpha} \le n!$（因 $n! \ge 1$），故
$$0 \le \frac{(n!)^{\alpha}}{n^{n}} \le \frac{n!}{n^{n}}$$
其中 $\dfrac{n!}{n^{n}} = \displaystyle\prod\_{k=1}^{n}\frac{k}{n}$，用**配对放缩**：把 $\frac{k}{n}$ 与 $\frac{n-k}{n}$ 配成一对，
$$\frac{k}{n}\cdot\frac{n-k}{n} = \frac{k(n-k)}{n^{2}} \le \frac{1}{4}$$
所以 $\dfrac{n!}{n^{n}} \le \left(\dfrac{1}{4}\right)^{\lfloor n/2 \rfloor}$（$n$ 为奇数时中间那个因子 $\le 1$，可以丢掉）。
由 [夹逼定理](#squeeze) 与非负性，$\lim\limits\_{n \to \infty} \dfrac{(n!)^{\alpha}}{n^{n}} = 0$。

</div>
</details>

---

## 相关笔记

- [线性代数笔记](/notes/xian-xing-dai-shu-bi-ji/)
