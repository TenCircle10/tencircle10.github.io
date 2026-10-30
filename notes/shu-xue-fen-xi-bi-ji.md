---
layout: note
title: "数学分析笔记"
slug: "shu-xue-fen-xi-bi-ji"
permalink: "/notes/shu-xue-fen-xi-bi-ji/"
public: true
generated_by: sync_notes.py
render_with_liquid: false
---

# 数学分析

<details class="callout abstract" data-callout="abstract" open>
<summary class="callout-title">主线</summary>
<div class="callout-content" markdown="block">

思考：**无穷小分析** —— 用"要多小有多小"的语言（$\varepsilon$、$\delta$、$N$）把"趋势"写成可以逐条验证的不等式。

</div>
</details>

---

## 1 集合与数集

### 1.1 集合的基本概念

**集合**的三条性质：**互异性**（相同元素只算一个，如 $\lbrace{}1, 2, 1, 2\rbrace{} = \lbrace{}1, 2\rbrace{}$）、**无序性**（$\lbrace{}1, 2\rbrace{} = \lbrace{}2, 1\rbrace{}$）、**确定性**（任一对象要么属于、要么不属于）。

**例子**：$1 \in \lbrace{}1\rbrace{}$，而 $1 \neq \lbrace{}1\rbrace{}$（元素不等于集合）；$\varnothing \subseteq A$ 对任何集合 $A$ 成立（$A$ 允许为空集）。

<details class="callout keypoint" data-callout="keypoint" open>
<summary class="callout-title">一个容易混的符号</summary>
<div class="callout-content" markdown="block">

$\varnothing \subset A$ 里的符号要理解为"包含于"（$\subseteq$）；写成 $\subset$ 时也不排除 $A = \varnothing$ 的情形。

</div>
</details>

**性质**：$A \subset B,\ B \subset C \Rightarrow A \subset C$；$A = B \iff A \subset B$ 且 $B \subset A$。

### 1.2 集合运算与德摩根律

$A \cap B$ 交，$A \cup B$ 并，$A \setminus B = \lbrace{}x \mid x \in A \text{ 且 } x \notin B\rbrace{}$ 差，$A^{c}$ 补（相对于全集 $X$）。运算律（交换、结合、分配、幂等、吸收、补集、德摩根、差集与对称差恒等式）见 [集合运算律](/notes/ji-he-yun-suan-lv/)。

<details class="callout formula" id="de-morgan" data-callout="formula" open>
<summary class="callout-title">德摩根律（de Morgan）</summary>
<div class="callout-content" markdown="block">

$$(A \cup B)^{c} = A^{c} \cap B^{c}, \qquad (A \cap B)^{c} = A^{c} \cup B^{c}$$

一般形式：$\left(\bigcup_{i \in I} A_i\right)^{c} = \bigcap_{i \in I} A_i^{c}$，$\left(\bigcap_{i \in I} A_i\right)^{c} = \bigcup_{i \in I} A_i^{c}$。

</div>
</details>

### 1.3 笛卡尔积

<details class="callout definition" data-callout="definition" open>
<summary class="callout-title">笛卡尔积</summary>
<div class="callout-content" markdown="block">

$$A \times B = \{(x, y) \mid x \in A,\ y \in B\}$$

</div>
</details>

### 1.4 数集、数域与有序域

**数集对运算的封闭性**：$\mathbb{N}$ 对 $+,\times$ 封闭，对 $-, \div$ 不封闭；$\mathbb{Z}$ 对 $+,-,\times$ 封闭，对 $\div$ 不封闭；$\mathbb{Q}$ 对四则封闭（除数 $\neq 0$）；$\mathbb{R}$ 是 $\mathbb{Q}$ 添上无理数，四则封闭；$\mathbb{C}$ 四则封闭、还封闭开方，但不是有序域（见下）。

<details class="callout definition" id="number-field" data-callout="definition" open>
<summary class="callout-title">数域与有序域</summary>
<div class="callout-content" markdown="block">

**数域**：设 $\mathbb{F} \subset \mathbb{C}$，若 $\mathbb{F}$ 中任意两数的和、差、积、商（除数非零）仍属于 $\mathbb{F}$，且 $0, 1 \in \mathbb{F}$，则称 $\mathbb{F}$ 为数域。
**有序域**：域 $\mathbb{F}$ 上存在全序 $\le$ 且与运算相容 —— $a \le b \Rightarrow a + c \le b + c$；$0 \le a$ 且 $0 \le b \Rightarrow 0 \le ab$。

</div>
</details>

数域只需验证**封闭性**（及含 $0, 1$）：交换、结合、分配律从 $\mathbb{C}$ 继承，自动成立。

$\mathbb{Q}$、$\mathbb{R}$ 是有序域；$\mathbb{C}$ **不是**：相容的序下必有 $a^{2} \ge 0$，于是 $-1 = i^{2} \ge 0$ 与 $1 = 1^{2} \gt{} 0$ 相加得 $0 \ge 1$，矛盾。

---

## 2 可列集

### 2.1 定义

<details class="callout definition" id="countable-set" data-callout="definition" open>
<summary class="callout-title">可列集</summary>
<div class="callout-content" markdown="block">

若无限集 $A$ 的元素能按某种规律排成一个序列 $A = \lbrace{}a_1, a_2, \dots, a_n, \dots\rbrace{}$，则称 $A$ 为**可列集**（可数无限集）。

</div>
</details>

### 2.2 可列个可列集之并

<details class="callout theorem" id="countable-union" data-callout="theorem" open>
<summary class="callout-title">定理 1.0.1</summary>
<div class="callout-content" markdown="block">

可列个可列集之并也是可列集。

</div>
</details>

**证明思路（记）**：记 $A_n = \lbrace{}a_{n1}, a_{n2}, \dots, a_{nk}, \dots\rbrace{}$，沿对角线方向取

$$\bigcup_{n=1}^{\infty} A_n = \{a_{11},\ a_{21},\ a_{12},\ a_{31},\ a_{22},\ a_{13},\ \dots\}$$

即按 $i + j$ 递增的顺序枚举（重复元素跳过）：

$$
\begin{matrix}
 & 1 & 2 & 3 & 4 & \cdots \\\\
1 & a_{11} & a_{12} & a_{13} & a_{14} & \cdots \\\\
2 & a_{21} & a_{22} & a_{23} & a_{24} & \cdots \\\\
3 & a_{31} & a_{32} & a_{33} & a_{34} & \cdots \\\\
4 & a_{41} & a_{42} & a_{43} & a_{44} & \cdots \\\\
\vdots & \vdots & \vdots & \vdots & \vdots & \ddots
\end{matrix}
$$

### 2.3 $\mathbb{Q}$ 是可列集

记 $A_n = [n, n+1] \cap \mathbb{Q}$（$n \in \mathbb{Z}$），则 $\bigcup_{n \in \mathbb{Z}} A_n = \mathbb{Q}$。这是**可列个**集合之并，由 [可列个可列集之并仍可列](#countable-union)，只需证 $A_0$ 可列：

$$A_0 = \Big\{0,\ 1,\ \tfrac{1}{2},\ \tfrac{1}{3},\ \tfrac{2}{3},\ \tfrac{1}{4},\ \tfrac{3}{4},\ \tfrac{1}{5},\ \tfrac{2}{5},\ \tfrac{3}{5},\ \tfrac{4}{5},\ \dots\Big\}$$

按"分母从小到大、同分母内按分子从小到大"枚举即可，故 $A_0$ 可列，进而 $\mathbb{Q}$ 可列。

### 2.4 注意点

- 所有可列集的元素个数都相同（同一基数 $\aleph_0$），见 [无限可列集等势证明](/notes/wu-xian-ke-lie-ji-deng-shi-zheng-ming/)；
- 有理数集与无理数集都**稠密**；
- 但稠密不等于可列：无理数集不可列，见 [实数集与无理数集不可列证明](/notes/shi-shu-ji-yu-wu-li-shu-ji-bu-ke-lie-zheng-ming/)。

---

## 3 实数的完备性

### 3.1 上确界与下确界

<details class="callout definition" id="sup-inf-def" data-callout="definition" open>
<summary class="callout-title">上确界与下确界</summary>
<div class="callout-content" markdown="block">

设 $E \subset \mathbb{R}$ 且 $E \neq \varnothing$。称 $M$ 为 $E$ 的**上确界**（记 $M = \sup E$），若

1. $M$ 是 $E$ 的上界：$\forall x \in E,\ x \le M$；
2. $M$ 是**最小**的上界：$\forall \varepsilon \gt{} 0$，$M - \varepsilon$ 都不是 $E$ 的上界。

**下确界**（记 $m = \inf E$）类似：$m$ 是下界，且 $\forall \varepsilon \gt{} 0$，$m + \varepsilon$ 不是 $E$ 的下界。

</div>
</details>

有上界就必有**无限多个**上界（上界往上都还是上界）；上确界是把"所有上界"压到最紧的那一个，**它不一定属于 $E$**。

<details class="callout understand" data-callout="understand" open>
<summary class="callout-title">理解</summary>
<div class="callout-content" markdown="block">

确界"取一个不一定取到，但取一段一定包含"：它是界的**边界**，未必落在集合里。

</div>
</details>

### 3.2 确界原理（完备性）

<details class="callout theorem" id="completeness" data-callout="theorem" open>
<summary class="callout-title">确界原理</summary>
<div class="callout-content" markdown="block">

$\mathbb{R}$ 的任一非空、有上界的子集必有上确界；非空、有下界的子集必有下确界。

</div>
</details>

对 $\mathbb{Q}$ 不成立：$S = \lbrace{}x \in \mathbb{Q} \mid x^{2} \lt{} 2\rbrace{}$ 在 $\mathbb{Q}$ 中**没有上确界**（"应该在"的那个位置 $\sqrt{2}$ 不在 $\mathbb{Q}$ 里）；而 $S' = \lbrace{}x \in \mathbb{R} \mid x^{2} \lt{} 2\rbrace{}$ 有界，且 $\sup S' = \sqrt{2}$。

<details class="callout understand" data-callout="understand" open>
<summary class="callout-title">理解</summary>
<div class="callout-content" markdown="block">

**实数集"充满"整个数轴**，对极限封闭。

</div>
</details>

有最值一定有界，有界不一定有最值（$(0,1)$ 有界但无最值）。

### 3.3 闭区间套定理

<details class="callout theorem" id="nested-intervals" data-callout="theorem" open>
<summary class="callout-title">闭区间套定理</summary>
<div class="callout-content" markdown="block">

若 $[a_{n+1}, b_{n+1}] \subset [a_n, b_n]$（$n = 1, 2, \dots$）且 $\lim\limits_{n \to \infty} (b_n - a_n) = 0$，则存在**唯一**的 $c \in \mathbb{R}$ 属于所有 $[a_n, b_n]$，且 $\lim\limits_{n \to \infty} a_n = \lim\limits_{n \to \infty} b_n = c$。

</div>
</details>

### 3.4 Bolzano–Weierstrass 定理

<details class="callout theorem" data-callout="theorem" open>
<summary class="callout-title">有界序列必有收敛子列（Bolzano–Weierstrass）</summary>
<div class="callout-content" markdown="block">

若 $a \le x_n \le b$（$n = 1, 2, \dots$），则 $\lbrace{}x_n\rbrace{}$ 有收敛子列。

</div>
</details>

**证明**：把 $[a, b]$ 等分成两个小区间，必有一个含 $\lbrace{}x_n\rbrace{}$ 的无穷多项（否则两边各只含有限项，合起来也只有有限项，矛盾），记为 $[a_1, b_1]$，并在其中取一项 $x_{n_1}$。再等分 $[a_1, b_1]$ 重复此过程，得到闭区间套 $\lbrace{}[a_k, b_k]\rbrace{}$ 与子列 $\lbrace{}x_{n_k}\rbrace{}$，满足 $x_{n_k} \in [a_k, b_k]$ 且下标严格递增。由 [闭区间套定理](#nested-intervals)，$a_k \to c \gets b_k$，夹逼得 $x_{n_k} \to c$。
<a id="bolzano-weierstrass"></a>

### 3.5 实数的小数表示

把实数按小数截断：$x_n = m + 0.a_1 a_2 \cdots a_n$，则 $0 \le x - x_n \lt{} \dfrac{1}{10^{n}}$。于是**任何实数（包括无理数）都是一列有理数的极限**：$\sqrt{2} = 1.4\cdots$ 就是 $1.4,\ 1.41,\ 1.414,\ \dots$ 的极限。
<a id="decimal-representation"></a>

---

## 4 数列极限

### 4.1 定义与记号

**数列**：按自然数 $1, 2, 3, \dots$ 编号依次排列的一列数 $x_1, x_2, x_3, \dots$，要点是 ① 无穷 ② 依次排列（即定义在 $\mathbb{N}^{&#42;}$ 上的函数）。**单调增**指 $x_n \le x_{n+1}$；**有界**指既有上界又有下界，等价地 $\exists M \gt{} 0,\ \forall n,\ \mid{}x_n\mid{} \le M$。

<details class="callout definition" id="sequence-limit" data-callout="definition" open>
<summary class="callout-title">数列极限</summary>
<div class="callout-content" markdown="block">

$\forall \varepsilon \gt{} 0$，$\exists N \in \mathbb{N}$，只要 $n \gt{} N$ 就有 $\mid{}a_n - l\mid{} \lt{} \varepsilon$，则称 $l$ 为 $\lbrace{}a_n\rbrace{}$ 的极限，记作 $\lim\limits_{n \to \infty} a_n = l$。
几何意义：$n \gt{} N$ 时 $a_n$ 全部落在 $l$ 的 **$\varepsilon$ 邻域** $U(l, \varepsilon) = (l - \varepsilon, l + \varepsilon)$ 内。

</div>
</details>

去掉有限项不改变敛散性，所以极限只约束**尾部**。

<details class="callout definition" id="limit-tail" data-callout="definition" open>
<summary class="callout-title">数列极限的等价刻画（"有限项"形式）</summary>
<div class="callout-content" markdown="block">

$\lim\limits_{n \to \infty} a_n = l \iff$ 对 $l$ 的任意 $\varepsilon$ 邻域 $U(l, \varepsilon)$，**只有有限项** $a_n \notin U(l, \varepsilon)$。

</div>
</details>

**如果把"只有有限项在邻域外"改成"有无穷项在邻域外"，对吗？** 不对，两者含义恰好相反：收敛数列对每个邻域外只有有限项（条件不必要）；而满足"有无穷项在外"的数列可以完全不收敛（条件不充分），连无界数列 $n$ 都满足它（取 $l = 1$、$\varepsilon = 1$，$n \gt{} 2$ 的项全在外）。

反例：$a_n = (-1)^{n} + \dfrac{1}{n}$，取 $l = 1$、$\varepsilon = \dfrac{1}{2}$。奇数项 $a_{2n-1} = -1 + \dfrac{1}{2n-1} \le 1 - \dfrac{1}{2}$ 全部落在邻域外，有无穷多项；但它不收敛 —— $a_{2n} \to 1$ 而 $a_{2n-1} \to -1$，由极限唯一性 $1 \neq -1$，矛盾。

<details class="callout keypoint" id="limit-negation" data-callout="keypoint" open>
<summary class="callout-title">"不以 $A$ 为极限"怎么写</summary>
<div class="callout-content" markdown="block">

$$\exists \varepsilon \gt{} 0,\ \forall N \in \mathbb{N},\ \exists n \gt{} N,\ |a_n - A| \ge \varepsilon$$

判断"不收敛"时不要拿 $(-1)^{n}/n$ 当反例 —— 它是**收敛**的（趋于 $0$）。

</div>
</details>

### 4.2 $\varepsilon – N$ 证明的实践

<details class="callout keypoint" data-callout="keypoint" open>
<summary class="callout-title">自己的经验（保留）</summary>
<div class="callout-content" markdown="block">

- $\varepsilon$ 尽量**放成一次的**，$N$ 才好找；
- 当"$n \gt{}$ 某值"时成立，**勿忘 $n \in \mathbb{N}$**（写 $N = \lceil \cdot \rceil$ 比写小数稳妥）；
- 证明里写清 $\mid{}a_n - a\mid{} \lt{} \varepsilon$ 的目标式，一步一步凑到它。

</div>
</details>

**例**：$\lim\limits_{n \to \infty} \dfrac{1}{n} = 0$。对 $\forall \varepsilon \gt{} 0$，取 $N = \left\lceil \dfrac{1}{\varepsilon} \right\rceil$，当 $n \gt{} N$ 时 $\left\vert \dfrac{1}{n} - 0 \right\vert = \dfrac{1}{n} \lt{} \varepsilon$。

<details class="callout formula" data-callout="formula" open>
<summary class="callout-title">该记住的常见极限</summary>
<div class="callout-content" markdown="block">

$$\lim_{n \to \infty} \sqrt[n]{n} = 1, \qquad \lim_{n \to \infty} \sqrt[n]{k} = 1\ (k \gt{} 0), \qquad \lim_{n \to \infty} \frac{n^{k}}{2^{n}} = 0$$

</div>
</details>

**思考**：若 $\lim\limits_{n \to \infty} a_n = a$，则 $\lim\limits_{n \to \infty} \dfrac{a_1 + a_2 + \cdots + a_n}{n} = a$。

### 4.3 极限的性质

<details class="callout theorem" id="sign-preserving" data-callout="theorem" open>
<summary class="callout-title">保号性</summary>
<div class="callout-content" markdown="block">

设 $\lbrace{}a_n\rbrace{}$ 收敛，$\lim\limits_{n \to \infty} a_n = A \gt{} 0$，则存在 $N$，当 $n \gt{} N$ 时 $a_n \gt{} 0$。

</div>
</details>

**证**：取 $\varepsilon = A$，存在 $N$，当 $n \gt{} N$ 时 $\mid{}a_n - A\mid{} \lt{} \varepsilon = A$，故 $a_n \gt{} A - \varepsilon = 0$。

**推论 1**：$\lbrace{}a_n\rbrace{}$ 收敛于 $A$，若存在 $N$ 使 $n \gt{} N$ 时 $a_n \ge 0$，则 $A \ge 0$。**推论 2**：$\lbrace{}a_n\rbrace{}$ 收敛于 $A \gt{} 0$，则存在 $N$，当 $n \gt{} N$ 时 $a_n \ge \dfrac{A}{2}$。

<details class="callout theorem" id="order-preserving" data-callout="theorem" open>
<summary class="callout-title">保序性</summary>
<div class="callout-content" markdown="block">

设 $\lbrace{}a_n\rbrace{}, \lbrace{}b_n\rbrace{}$ 收敛，极限分别为 $A, B$。若 $A \gt{} B$，则存在 $N$，当 $n \gt{} N$ 时 $a_n \gt{} b_n$。

</div>
</details>

**证**：取 $\varepsilon = \dfrac{A - B}{2} \gt{} 0$。由 $a_n \to A$ 得 $n \gt{} N_1$ 时 $a_n \gt{} A - \varepsilon = \dfrac{A + B}{2}$；由 $b_n \to B$ 得 $n \gt{} N_2$ 时 $b_n \lt{} B + \varepsilon = \dfrac{A + B}{2}$。取 $N = \max\lbrace{}N_1, N_2\rbrace{}$，当 $n \gt{} N$ 时 $b_n \lt{} \dfrac{A+B}{2} \lt{} a_n$。

**推论 3**：$\lbrace{}a_n\rbrace{}, \lbrace{}b_n\rbrace{}$ 收敛于 $A, B$，若存在 $N$ 使 $n \gt{} N$ 时 $a_n \le b_n$，则 $A \le B$。

**思考**：把 $A \gt{} B$ 换成 $A \ge B$，还能得到"存在 $N$，当 $n \gt{} N$ 时 $a_n \ge b_n$"吗？不能，反例 $a_n = 0,\ b_n = \dfrac{1}{n}$：此时 $A = B = 0$，但 $a_n \lt{} b_n$ 对一切 $n$ 成立。严格的大小关系在取极限后会被"抹平"。

<details class="callout keypoint" data-callout="keypoint" open>
<summary class="callout-title">$a_n \le b_n$ 推不出"$a_n \le B$"</summary>
<div class="callout-content" markdown="block">

已知 $a_n \le b_n\ (n \gt{} N)$、$\lbrace{}a_n\rbrace{} \to A$、$\lbrace{}b_n\rbrace{} \to B$，能得到的只有 $A \le B$；**得不到**"存在 $N$，当 $n \gt{} N$ 时 $a_n \le B$"。
反例：$a_n = b_n = \dfrac{1}{n}$，则 $A = B = 0$，但 $a_n = \dfrac{1}{n} \gt{} 0 = B$ 对一切 $n$ 成立。

</div>
</details>

### 4.4 四则运算与复合

<details class="callout theorem" id="limit-arithmetic" data-callout="theorem" open>
<summary class="callout-title">四则运算法则（何时能拆）</summary>
<div class="callout-content" markdown="block">

$\lim a_n = a$ 与 $\lim b_n = b$ **都存在**时才能拆开运算，而且只对**有限次**运算生效。

- $\lim\limits_{n \to \infty} (k_1 a_n + k_2 b_n) = k_1 a + k_2 b$（线性组合）
- $\lim\limits_{n \to \infty} a_n^{k} = a^{k}$（$k \in \mathbb{N}^{&#42;}$）
- $\lim\limits_{n \to \infty} f(a_n) = f(a)$，其中 $f$ 为多项式（即 $f$ 在 $a$ 处连续）

</div>
</details>

做法：构造一个新序列 $f(a_n)$，逐项用四则运算推（求和符号的运算律见 [∑求和运算律](/notes/qiu-he-yun-suan-lv/)）。

### 4.5 根式与幂的极限

<details class="callout lemma" id="sqrt-limit" data-callout="lemma" open>
<summary class="callout-title">开方保持极限</summary>
<div class="callout-content" markdown="block">

若 $a_n \ge 0$ 且 $\lim\limits_{n \to \infty} a_n = a \ge 0$，则 $\lim\limits_{n \to \infty} \sqrt{a_n} = \sqrt{a}$。

</div>
</details>

**证**：分两种情形。若 $a = 0$，由 $a_n \to 0$，$\forall \varepsilon \gt{} 0$ 当 $n$ 充分大时 $0 \le a_n \lt{} \varepsilon^{2}$，于是 $\sqrt{a_n} \lt{} \varepsilon$。若 $a \gt{} 0$，$n$ 充分大时 $a_n \gt{} \dfrac{a}{2} \gt{} 0$，且

$$|\sqrt{a_n} - \sqrt{a}| = \frac{|a_n - a|}{\sqrt{a_n} + \sqrt{a}} \le \frac{|a_n - a|}{\sqrt{a}} \to 0$$

注意别把取完极限的分母提前代入写成 $\dfrac{0 \cdot \mid{}a_n - a\mid{}}{2\sqrt a}$；要保留上界 $\dfrac{\mid{}a_n - a\mid{}}{\sqrt a}$，再由 $a_n \to a$ 得结论。

**两道"分母有理化"的题**：

<details class="callout example" data-callout="example" open>
<summary class="callout-title">例 1：分子分母同乘共轭</summary>
<div class="callout-content" markdown="block">

求 $\lim\limits_{n \to \infty} n\left(\sqrt{n^{2}+1} - \sqrt{n^{2}-1}\right)$。

</div>
</details>

**解**：

$$\lim_{n \to \infty} n\left(\sqrt{n^{2}+1} - \sqrt{n^{2}-1}\right) = \lim_{n \to \infty} \frac{2n}{\sqrt{n^{2}+1} + \sqrt{n^{2}-1}} = \lim_{n \to \infty} \frac{2}{\sqrt{1+\frac{1}{n^{2}}} + \sqrt{1-\frac{1}{n^{2}}}} = 1$$

<details class="callout example" data-callout="example" open>
<summary class="callout-title">例 2：同除最大底数 $5^{n}$</summary>
<div class="callout-content" markdown="block">

求 $\lim\limits_{n \to \infty} \dfrac{5^{n+1} - (-2)^{n}}{3 \times 5^{n} + 2 \times 3^{n}}$。

</div>
</details>

**解**：分子分母同除最大的底数 $5^{n}$，其余项都趋于 $0$：

$$\lim_{n \to \infty} \frac{5^{n+1} - (-2)^{n}}{3 \times 5^{n} + 2 \times 3^{n}} = \lim_{n \to \infty} \frac{5 - \left(-\frac{2}{5}\right)^{n}}{3 + 2\left(\frac{3}{5}\right)^{n}} = \frac{5}{3}$$

### 4.6 夹逼定理

<details class="callout theorem" id="squeeze" data-callout="theorem" open>
<summary class="callout-title">夹逼定理</summary>
<div class="callout-content" markdown="block">

若存在 $N$，当 $n \gt{} N$ 时 $c_n \le a_n \le b_n$，且 $\lim\limits_{n \to \infty} b_n = \lim\limits_{n \to \infty} c_n = l$，则 $\lim\limits_{n \to \infty} a_n = l$。

</div>
</details>

技巧：可以构造**常数列**来夹逼。常用结论（$a, b \gt{} 0$）：

$$\lim_{n \to \infty} \sqrt[n]{a^{n} + b^{n}} = \max\{a, b\}, \qquad \lim_{n \to \infty} \sqrt[n]{a^{n} + k b^{n}} = \max\{a, b\}\ \ (k \gt{} 0)$$

### 4.7 单调有界定理

<details class="callout theorem" id="monotone-bounded" data-callout="theorem" open>
<summary class="callout-title">单调有界定理</summary>
<div class="callout-content" markdown="block">

单调且有界的数列必有极限。具体地，$\lbrace{}x_n\rbrace{}$ 单调增且有上界时 $\lim\limits_{n \to \infty} x_n = \sup\lbrace{}x_n\rbrace{}$。

</div>
</details>

**证明**：设 $\lbrace{}x_n\rbrace{}$ 单调增且有上界，由 [上确界](#sup-inf-def) 与 [确界原理](#completeness)，记 $a = \sup\lbrace{}x_n\rbrace{}$。对任意 $\varepsilon \gt{} 0$，$a - \varepsilon$ 不再是上界，故存在 $N$ 使 $x_N \gt{} a - \varepsilon$。由单调性，当 $n \gt{} N$ 时 $a - \varepsilon \lt{} x_N \le x_n \le a \lt{} a + \varepsilon$，即 $\mid{}x_n - a\mid{} \lt{} \varepsilon$，故 $x_n \to a$。

<details class="callout understand" data-callout="understand" open>
<summary class="callout-title">直观记法</summary>
<div class="callout-content" markdown="block">

用小数表示看：$x_n = m_n + 0.a_1^{(n)} a_2^{(n)} \cdots$。单调增有上界保证整数部分 $m_n$ 最终不再变化；再看小数位，上一位一旦"锁定"，下一位只能从 $\lbrace{}0, 1, \dots, 9\rbrace{}$ 中取，于是逐位锁定出一个小数 —— 它就是上确界。

</div>
</details>

单调有界定理只保证极限存在，不给值 —— $\gamma$ 就是这类量。

<details class="callout example" data-callout="example" open>
<summary class="callout-title">例 1：Euler 常数 $\gamma$ 存在</summary>
<div class="callout-content" markdown="block">

证明 $\lim\limits_{n \to \infty}\left(1 + \dfrac{1}{2} + \cdots + \dfrac{1}{n} - \ln n\right)$ 存在。

</div>
</details>

**解**：记 $c_n = 1 + \dfrac{1}{2} + \cdots + \dfrac{1}{n} - \ln n$，用不等式 $\dfrac{1}{n+1} \lt{} \ln\!\left(1 + \dfrac{1}{n}\right) \lt{} \dfrac{1}{n}$：

- **单调减**：$c_{n+1} - c_n = \dfrac{1}{n+1} - \ln\!\left(1 + \dfrac{1}{n}\right) \lt{} 0$；
- **有下界**：$\ln n = \sum_{k=1}^{n-1} \ln\!\left(1 + \dfrac{1}{k}\right) \lt{} \sum_{k=1}^{n-1} \dfrac{1}{k} \lt{} 1 + \dfrac{1}{2} + \cdots + \dfrac{1}{n}$，故 $c_n \gt{} 0$。

由 [单调有界定理](#monotone-bounded)，$c_n$ 收敛，其极限记为 **Euler 常数 $\gamma$**。

<details class="callout example" data-callout="example" open>
<summary class="callout-title">例 2：$x_{n+1} = x_n(1 - x_n)$</summary>
<div class="callout-content" markdown="block">

设 $0 \lt{} x_1 \lt{} 1$，证明：(1) $\lbrace{}x_n\rbrace{}$ 收敛；(2) $\lim\limits_{n \to \infty} n x_n = 1$。

</div>
</details>

**解**：

(1) $0 \lt{} x_{n+1} \lt{} x_n \lt{} 1$（因 $0 \lt{} 1 - x_n \lt{} 1$），单调减且有下界 $0$，故收敛；设极限为 $a$，则 $a = a(1 - a) \Rightarrow a = 0$。

(2) 记 $y_n = \dfrac{1}{x_n}$，则 $y_{n+1} = \dfrac{y_n}{1 - x_n}$，于是 $y_{n+1} - y_n = \dfrac{1}{x_n}\left(\dfrac{1}{1 - x_n} - 1\right) = \dfrac{1}{1 - x_n} \longrightarrow 1$。由 [Stolz 定理](#stolz)，$\dfrac{y_n}{n} \to 1$，即 $n x_n \to 1$。

### 4.8 子列

<details class="callout lemma" id="subsequence" data-callout="lemma" open>
<summary class="callout-title">子列继承极限</summary>
<div class="callout-content" markdown="block">

若 $\lim\limits_{n \to \infty} a_n = L$，则 $\lbrace{}a_n\rbrace{}$ 的任何子列也收敛于 $L$。

</div>
</details>

更强的结论（用于"合并"）：

$$\begin{cases} \lim\limits_{n \to \infty} a_{2n} = A \\\\[4pt] \lim\limits_{n \to \infty} a_{2n-1} = A \end{cases} \Longrightarrow \lim_{n \to \infty} a_n = A$$

推广：若对 $r = 0, 1, \dots, p-1$ 都有 $\lim\limits_{n \to \infty} a_{pn+r} = A$，则 $\lim\limits_{n \to \infty} a_n = A$（即按模 $p$ 的完全剩余系分类）。它的逆否用法很实用：只要找到两个子列极限不同（或某个子列发散），就能断定原数列不收敛，见 <a href="#limit-tail">前面 $(-1)^n + 1/n$ 的反例</a>。

### 4.9 Stolz 定理

<details class="callout theorem" id="stolz" data-callout="theorem" open>
<summary class="callout-title">Stolz 定理（离散的洛必达法则）</summary>
<div class="callout-content" markdown="block">

设 $\lbrace{}y_n\rbrace{}$ 严格单调递增且 $\lim\limits_{n \to \infty} y_n = +\infty$。若 $\lim\limits_{n \to \infty} \dfrac{x_n - x_{n-1}}{y_n - y_{n-1}} = a$，则 $\lim\limits_{n \to \infty} \dfrac{x_n}{y_n} = a$，其中 $a$ 可以是有限数，也可以是 $+\infty$ 或 $-\infty$。

</div>
</details>

用差分形式表示 $x_n, y_n$ 凑出已知极限；用无穷大抵消"有限的累加项"。$0/0$ 型与两种证明见 [Stolz定理的证明](/notes/stolz-ding-li-di-zheng-ming/)。

**例**：

$$\lim_{n \to \infty} \frac{\sum_{i=1}^{n} i^{k}}{n^{k+1}} = \lim_{n \to \infty} \frac{(n+1)^{k}}{(n+1)^{k+1} - n^{k+1}} = \frac{1}{k+1}$$

因为分母 $(n+1)^{k+1} - n^{k+1} \sim (k+1)n^{k}$。

### 4.10 无穷小量与无穷大量

<details class="callout lemma" id="infinitesimal" data-callout="lemma" open>
<summary class="callout-title">有界 $\times$ 无穷小 $=$ 无穷小</summary>
<div class="callout-content" markdown="block">

若 $\lim\limits_{n \to \infty} a_n = 0$ 且 $\mid{}b_n\mid{} \le M$，则 $\lim\limits_{n \to \infty} a_n b_n = 0$。

</div>
</details>

同号无穷大量之和仍是无穷大量；无穷大量 $\pm$ 有界量仍是无穷大量（按 $\mid{}a_n\mid{} \to \infty$ 的意义；若 $a_n \to +\infty$ 则 $a_n + b_n \to +\infty$）。

<details class="callout keypoint" id="infinite-large" data-callout="keypoint" open>
<summary class="callout-title">无穷大量 $\neq$ 无界量</summary>
<div class="callout-content" markdown="block">

无穷大量要求 $\mid{}a_n\mid{} \to +\infty$（整条数列都跑向无穷），无界量只要求"没有界"。
例：$n$ 与 $\big((-1)^{n} + 1\big)n$。前者是无穷大量；后者无界（偶数项为 $0$，奇数项为 $2n$），但不是无穷大量。

</div>
</details>

### 4.11 三个"根号型"极限（补充）

<details class="callout example" data-callout="example" open>
<summary class="callout-title">三个"根号型"极限</summary>
<div class="callout-content" markdown="block">

求 $\lim\limits_{n \to \infty} \sqrt[n]{n}$、$\lim\limits_{n \to \infty} \sqrt[n]{n!}$、$\lim\limits_{n \to \infty} \dfrac{\sqrt[n]{n!}}{n}$。

</div>
</details>

**① $\lim\limits_{n \to \infty} \sqrt[n]{n} = 1$**：用 [AM–GM](#amgm)，取两个 $\sqrt{n}$ 与 $n - 2$ 个 $1$：

$$\sqrt[n]{n} = \sqrt[n]{\sqrt{n}\cdot\sqrt{n}\cdot 1 \cdots 1} \le \frac{2\sqrt{n} + (n - 2)}{n} = 1 + \frac{2(\sqrt{n} - 1)}{n} \to 1$$

又 $\sqrt[n]{n} \ge 1$，夹逼得极限为 $1$。

**② $\lim\limits_{n \to \infty} \sqrt[n]{n!} = +\infty$**：对 $k \gt{} \frac{n}{2}$ 有 $k \ge \frac{n}{2}$，这样的因子至少 $\frac{n}{2}$ 个，故

$$n! \ge \left(\frac{n}{2}\right)^{n/2} \quad \Longrightarrow \quad \sqrt[n]{n!} \ge \left(\frac{n}{2}\right)^{1/2} \to +\infty$$

**③ $\lim\limits_{n \to \infty} \dfrac{\sqrt[n]{n!}}{n} = \dfrac{1}{e}$**：取对数后用 [Stolz 定理](#stolz)，

$$
\lim_{n \to \infty} \frac{\ln n! - n\ln n}{n} \overset{\text{Stolz}}{=} \lim_{n \to \infty} (n-1)\ln\!\left(1 - \frac{1}{n}\right) = -1
$$

其中用了 $x_n - x_{n-1} = (n-1)\ln\!\left(1 - \dfrac{1}{n}\right)$（$x_n = \ln n! - n \ln n$）。故原极限 $= e^{-1}$。
<a id="radical-limits"></a>

---

## 5 重要极限：$e$

### 5.1 $(1 + \frac{1}{n})^{n}$ 单调有界

<details class="callout theorem" id="e-definition" data-callout="theorem" open>
<summary class="callout-title">$(1+\frac1n)^n$ 收敛</summary>
<div class="callout-content" markdown="block">

序列 $\left(1 + \dfrac{1}{n}\right)^{n}$ 单调递增且有上界，故收敛，记 $\lim\limits_{n \to \infty} \left(1 + \dfrac{1}{n}\right)^{n} = e$。

</div>
</details>

**① 单调增**：把两个序列都作二项式展开

$$\left(1 + \frac{1}{n}\right)^{n} = 1 + 1 + \sum_{k=2}^{n} \frac{1}{k!}\left(1 - \frac{1}{n}\right)\left(1 - \frac{2}{n}\right) \cdots \left(1 - \frac{k-1}{n}\right)$$

$$\left(1 + \frac{1}{n+1}\right)^{n+1} = 1 + 1 + \sum_{k=2}^{n} \frac{1}{k!}\left(1 - \frac{1}{n+1}\right)\cdots\left(1 - \frac{k-1}{n+1}\right) + \left(\frac{1}{n+1}\right)^{n+1}$$

逐项比对（因子满足 $1 - \frac{j}{n+1} \gt{} 1 - \frac{j}{n}$，且第二式还多了正项），得 $\left(1 + \frac{1}{n}\right)^{n} \lt{} \left(1 + \frac{1}{n+1}\right)^{n+1}$。

**② 有界**：

$$\left(1 + \frac{1}{n}\right)^{n} \lt{} 1 + 1 + \frac{1}{2!} + \frac{1}{3!} + \cdots + \frac{1}{n!} \lt{} 1 + 1 + \frac{1}{2!} + \frac{1}{3\times2} + \frac{1}{4\times3} + \cdots + \frac{1}{n(n-1)}$$

而 $1 + 1 + \dfrac{1}{2!} + \displaystyle\sum_{k=3}^{n} \frac{1}{k(k-1)} = 2 + \frac{1}{2} + \left(\frac{1}{2} - \frac{1}{n}\right) = 3 - \frac{1}{n} \lt{} 3$，故有上界。

由 [单调有界定理](#monotone-bounded)，极限存在，记为 $e$。

<details class="callout idea" data-callout="idea" open>
<summary class="callout-title">另一个"很惊人的注意力"</summary>
<div class="callout-content" markdown="block">

也可以直接看 $(1 + \frac{1}{n})^{n+1}$：它**单调递减**且有下界 $1$，所以也有极限。两条序列刚好从两侧逼近 $e$（见下）。

</div>
</details>

### 5.2 $e$ 的上下界

<details class="callout theorem" id="e-bounds" data-callout="theorem" open>
<summary class="callout-title">两侧夹住 $e$</summary>
<div class="callout-content" markdown="block">

$$\left(1 + \frac{1}{n}\right)^{n} \lt{} e \lt{} \left(1 + \frac{1}{n}\right)^{n+1}$$

$n$ 越大，所得的界越精确。

</div>
</details>

**证法一（拉格朗日中值定理）**：对 $0 \lt{} a \lt{} b$，$n \in \mathbb{N}^{&#42;}$，用 $f(x) = x^{n+1}$ 得 $(n+1)a^{n} \lt{} \dfrac{b^{n+1} - a^{n+1}}{b - a} \lt{} (n+1)b^{n}$；取 $a = 1 + \dfrac{1}{n+1}$、$b = 1 + \dfrac{1}{n}$ 即得。

**证法二（初等解法，AM–GM）**：

$$\sqrt[n+1]{\left(1 + \frac{1}{n}\right)^{n} \cdot 1} \le \frac{n\left(1 + \frac{1}{n}\right) + 1}{n+1} = \frac{n+2}{n+1} = 1 + \frac{1}{n+1}$$

两边取 $n+1$ 次方得 $\left(1 + \dfrac{1}{n}\right)^{n} \le \left(1 + \dfrac{1}{n+1}\right)^{n+1}$。对序列 $\left(1 + \dfrac{1}{n}\right)^{n+1}$ 先取倒数，再对 $\left(\dfrac{n}{n+1}\right)^{n+1}$ 用 AM–GM：

$$\sqrt[n+1]{\left(\frac{n}{n+1}\right)^{n+1} \cdot 1} \le \frac{\frac{n}{n+1}(n+1) + 1}{n+2} = \frac{n+1}{n+2}$$

即 $\left(1 + \dfrac{1}{n+1}\right)^{n+2} \ge \left(1 + \dfrac{1}{n}\right)^{n+1}$，说明 $(1+\frac1n)^{n+1}$ 单调减；两端合并就得到双边不等式。

### 5.3 $e$ 的级数表示

<details class="callout formula" id="e-series" data-callout="formula" open>
<summary class="callout-title">$e$ 的级数表示</summary>
<div class="callout-content" markdown="block">

$$e = \lim_{n \to \infty} \sum_{k=0}^{n} \frac{1}{k!}$$

</div>
</details>

**两边夹**：一方面，5.1 的 ② 已证 $\left(1 + \frac{1}{n}\right)^{n} \lt{} \sum_{k=0}^{n} \frac{1}{k!}$，故 $e \le \lim\limits_{n \to \infty} \sum\limits_{k=0}^{n} \frac{1}{k!}$。

另一方面，对**取定**的 $k$，

$$e = \lim_{n \to \infty}\left(1 + 1 + \sum_{i=2}^{n} \frac{1}{i!}\left(1 - \frac{1}{n}\right)\cdots\left(1 - \frac{i-1}{n}\right)\right) \ge \lim_{n \to \infty}\left(1 + 1 + \sum_{i=2}^{k} \frac{1}{i!}\left(1 - \frac{1}{n}\right)\cdots\left(1 - \frac{i-1}{n}\right)\right) = \sum_{i=0}^{k} \frac{1}{i!}$$

（最后一步：有限项的极限逐项算出，因子 $\left(1 - \frac{1}{n}\right)\cdots \to 1$。）对 $k$ 取极限并用 [夹逼定理](#squeeze)，得 $e = \sum\limits_{n=0}^{\infty} \dfrac{1}{n!}$。

### 5.4 $e$ 是无理数

<details class="callout theorem" id="e-irrational" data-callout="theorem" open>
<summary class="callout-title">$e$ 是无理数</summary>
<div class="callout-content" markdown="block">

$e$ 不能写成 $\dfrac{p}{q}$（$p, q \in \mathbb{N}$）。

</div>
</details>

**证（反证）**：设 $e = \dfrac{p}{q}$，$p, q \in \mathbb{N}$ 且互质。由 <a href="#e-series">$e$ 的级数表示</a>，

$$e \cdot q! = \underbrace{\left(1 + 1 + \frac{1}{2!} + \cdots + \frac{1}{q!}\right)q!}_{\text{整数}} + \underbrace{\lim_{n \to \infty}\left[\frac{1}{(q+1)!} + \frac{1}{(q+2)!} + \cdots + \frac{1}{(q+n)!}\right]}_{\text{记为 } r}$$

左边 $e\,q! = p\,(q-1)!$ 是整数，前一项也是整数，所以 $r$ 必须是整数。但

$$0 \lt{} r \lt{} \lim_{n \to \infty}\left[\frac{1}{q+1} + \left(\frac{1}{q+1}\right)^{2} + \cdots + \left(\frac{1}{q+1}\right)^{n}\right] \le \frac{1}{q}$$

又 $e \in (2, 3)$ 不是整数，故 $q \ge 2$，从而 $0 \lt{} r \lt{} \dfrac{1}{q} \le \dfrac{1}{2} \lt{} 1$，与"$r$ 是整数"矛盾。故 $e$ 为无理数。

### 5.5 与 $e$ 有关的几个极限

<details class="callout formula" data-callout="formula" open>
<summary class="callout-title">与 $e$ 有关的几个极限</summary>
<div class="callout-content" markdown="block">

若 $p_n \gt{} 0$ 是正无穷大量，则 $\lim\limits_{n \to \infty}\left(1 + \dfrac{1}{p_n}\right)^{p_n} = e$。

</div>
</details>

**证**：由 $\left(1+\frac1n\right)^n \to e$，$\exists N_1$ 使 $n \gt{} N_1$ 时 $\left\vert\left(1+\frac1n\right)^n - e\right\vert \lt{} \varepsilon$；又 $p_n \to +\infty$，$\exists N_2$ 使 $n \gt{} N_2$ 时 $p_n \gt{} N_1$，故 $n \gt{} N_2$ 时 $\left\vert\left(1+\frac{1}{p_n}\right)^{p_n} - e\right\vert \lt{} \varepsilon$。

- $\lim\limits_{n \to \infty}\left(1 + \dfrac{1}{n^{2} + n}\right)^{n} = \lim\limits_{n \to \infty}\left[\left(1 + \dfrac{1}{n^{2}+n}\right)^{n^{2}+n}\right]^{\frac{n}{n^{2}+n}} = e^{0} = 1$；
- $\lim\limits_{n \to \infty} a_n^{b_n} = a^{b}$（$\lim a_n = a \gt{} 0$，$\lim b_n = b$）：由 $\lim\limits_{n \to \infty} e^{b_n \ln a_n} = e^{b \ln a} = a^{b}$；
- $\lim\limits_{x \to \infty}\left(1 + \dfrac{\alpha}{x}\right)^{\beta x} = e^{\alpha\beta}$（函数版推广，见下章）。

---

## 6 几个典型函数

$X$ 是**定义域**，$f(X) = \lbrace{}f(x) \mid x \in X\rbrace{}$ 是**值域**，且 $f(X) \subset Y$（$Y$ 为陪域）。复合函数 $y = f(g(x))$ 需满足 $g$ 的值域落在 $f$ 的定义域内。

| 名称 | 定义 | 备注 |
| --- | --- | --- |
| 符号函数 | $\operatorname{sgn} x = 1\ (x\gt{}0),\ 0\ (x=0),\ -1\ (x\lt{}0)$ | 分段常值，$x = 0$ 处不连续 |
| Dirichlet 函数 | $D(x) = 1\ (x \in \mathbb{Q}),\ 0\ (x \in \mathbb{Q}^{c})$ | 每个有理数都是周期，无最小正周期 |
| 双曲正弦/余弦 | $\operatorname{sh} x = \dfrac{e^{x} - e^{-x}}{2}$，$\operatorname{ch} x = \dfrac{e^{x} + e^{-x}}{2}$ | $\operatorname{ch}^{2} x - \operatorname{sh}^{2} x = 1$；$\operatorname{ch}' x = \operatorname{sh} x$，$\operatorname{sh}' x = \operatorname{ch} x$ |

<details class="callout definition" id="periodic-function" data-callout="definition" open>
<summary class="callout-title">周期函数</summary>
<div class="callout-content" markdown="block">

若存在 $T \neq 0$，使 $\forall x \in X$ 都有 $x + T \in X$ 且 $f(x + T) = f(x)$，称 $f$ 为周期函数，$T$ 为一个周期。

</div>
</details>

**周期函数不一定有最小正周期** —— 上表里的 Dirichlet 函数就是现成的例子（$\forall q \in \mathbb{Q}$，$D(x + q) = D(x)$）。

---

## 7 函数极限

### 7.1 定义

<details class="callout definition" id="function-limit" data-callout="definition" open>
<summary class="callout-title">函数极限与去心邻域</summary>
<div class="callout-content" markdown="block">

**空心（去心）邻域**：$(x_0 - \delta, x_0 + \delta) \setminus \lbrace{}x_0\rbrace{}$，记 $U^{\circ}(x_0, \delta)$。
**极限**：$\forall \varepsilon \gt{} 0,\ \exists \delta \gt{} 0$，当 $0 \lt{} \mid{}x - x_0\mid{} \lt{} \delta$ 时 $\mid{}f(x) - L\mid{} \lt{} \varepsilon$，记 $\lim\limits_{x \to x_0} f(x) = L$。

- $\varepsilon$ 任选、$\delta$ 随 $\varepsilon$ 变动，动态地描述"要多小有多小"；
- **不要求 $f$ 在 $x_0$ 处有定义**。

</div>
</details>

**单侧极限**：在 $(x_0, x_0 + \delta)$ 或 $(x_0 - \delta, x_0)$ 上讨论，$\lim\limits_{x \to x_0} f(x) = L \iff \lim\limits_{x \to x_0^{+}} f(x) = \lim\limits_{x \to x_0^{-}} f(x) = L$。

**在无穷远处的极限**：设 $f$ 在 $(-\infty, A) \cup (B, +\infty)$ 上有定义，若 $\forall \varepsilon \gt{} 0,\ \exists M \gt{} 0$，当 $\mid{}x\mid{} \gt{} M$ 时 $\mid{}f(x) - L\mid{} \lt{} \varepsilon$，则记 $\lim\limits_{x \to \infty} f(x) = L$。

### 7.2 Heine 定理

<details class="callout theorem" id="heine" data-callout="theorem" open>
<summary class="callout-title">Heine（海涅）定理</summary>
<div class="callout-content" markdown="block">

$$\lim_{x \to a} f(x) = L \iff \text{对任意 } x_n \to a\ (x_n \neq a)\text{，都有 } \lim_{n \to \infty} f(x_n) = L$$

</div>
</details>

用途：反证极限不存在 —— 只要找出两条趋于 $a$ 的序列 $x_n, x_n'$ 使 $f(x_n)$ 与 $f(x_n')$ 极限不同即可。

### 7.3 性质

<details class="callout theorem" data-callout="theorem" open>
<summary class="callout-title">函数极限的基本性质</summary>
<div class="callout-content" markdown="block">

- **唯一性**：极限存在则唯一。
- **局部有界性**：在某点附近有界（不是整体有界，与 [有界性定理](#boundedness-theorem) 里的"整体有界"对照着看），即 $\exists \delta$，当 $x \in U^{\circ}(x_0, \delta)$ 时 $\mid{}f(x)\mid{} \le M$。
- **无穷小量**：$\lim\limits_{x \to a} f(x) = 0$ 时称 $f$ 为无穷小量，且 $\lim\limits_{x \to a} f(x) = L \iff \lim\limits_{x \to a} (f(x) - L) = 0$。
- **有界 $\times$ 无穷小 $=$ 无穷小**：$x \to a$ 时 $\alpha(x) \to 0$，$h(x)$ 有界，则 $\alpha(x)h(x) \to 0$。
- $\lim\limits_{x \to a} f(x) = \infty \iff \lim\limits_{x \to a} \dfrac{1}{f(x)} = 0$；若 $f(x) \neq 0$，则 $\lim\limits_{x \to a} f(x) = 0 \iff \lim\limits_{x \to a} \dfrac{1}{f(x)} = \infty$。

</div>
</details>

**无界 ≠ 无穷大（函数版）**：无界只说明"没有界"，不能说"趋于无穷大"（数列版的例子见 [无穷大量 ≠ 无界量](#infinite-large)）。例：$f(x) = \dfrac{1}{x}\sin\dfrac{1}{x}$（$x \to 0$）。取 $x = \dfrac{1}{2n\pi}$ 时 $f(x) = 0$，而取 $x = \dfrac{1}{2n\pi + \pi/2}$ 时 $\mid{}f(x)\mid{} \to +\infty$，所以它无界，但极限不是 $\infty$。

若 $\lim\limits_{x \to a} f(x) = A \neq 0$，则 $f$ 在 $a$ 的某去心邻域内与 $A$ **同号**（取 $B = \dfrac{A}{2}$）。

<details class="callout theorem" id="function-limit-props" data-callout="theorem" open>
<summary class="callout-title">函数极限的保号性与四则运算</summary>
<div class="callout-content" markdown="block">

- **保号性**：设 $\lim\limits_{x \to a} f(x) = A \gt{} B$，则存在 $\delta \gt{} 0$，当 $x \in U^{\circ}(a, \delta)$ 时 $f(x) \gt{} B$。
- **保序性**：在 $U^{\circ}(a, \delta)$ 上 $f(x) \ge g(x)$，若 $f \to A,\ g \to B$，则 $A \ge B$。
- **四则运算**：各自极限存在时才可拆开，且 $B \neq 0$ 时

$$\lim_{x \to a}(f \pm g) = A \pm B,\quad \lim_{x \to a}(f g) = AB,\quad \lim_{x \to a}\frac{f}{g} = \frac{A}{B}$$

</div>
</details>

**证（保号性）**：取 $\varepsilon = A - B \gt{} 0$，则存在 $\delta$，当 $x \in U^{\circ}(a, \delta)$ 时 $\mid{}f(x) - A\mid{} \lt{} A - B$，故 $f(x) \gt{} B$。

**例 1（多项式型）**：

$$\lim_{x \to 1} \frac{x^{n} - 1}{x^{m} - 1} = \lim_{x \to 1} \frac{x^{n-1} + x^{n-2} + \cdots + 1}{x^{m-1} + x^{m-2} + \cdots + 1} = \frac{n}{m}$$

<details class="callout example" data-callout="example" open>
<summary class="callout-title">例 2：$\varepsilon$–$\delta$ 模板</summary>
<div class="callout-content" markdown="block">

用定义证明 $\lim\limits_{x \to 2} x^{2} = 4$。

</div>
</details>

**解**：取 $\mid{}x - 2\mid{} \lt{} 1$，则 $\mid{}x + 2\mid{} \lt{} 5$，于是 $\mid{}x^{2} - 4\mid{} = \mid{}x - 2\mid{}\mid{}x + 2\mid{} \lt{} 5\mid{}x - 2\mid{}$；要它 $\lt{} \varepsilon$ 只需 $\mid{}x - 2\mid{} \lt{} \dfrac{\varepsilon}{5}$，故 $\delta = \min\left\lbrace{}1, \dfrac{\varepsilon}{5}\right\rbrace{}$。记法：**$M$、$N$ 取 $\max$，$\delta$ 取 $\min$。**

### 7.4 夹逼与单调收敛（函数版）

<details class="callout theorem" id="function-squeeze" data-callout="theorem" open>
<summary class="callout-title">函数版的夹逼</summary>
<div class="callout-content" markdown="block">

若在 $U^{\circ}(x_0, \delta)$ 上 $\varphi(x) \le f(x) \le \phi(x)$，且 $\lim\limits_{x \to x_0} \varphi(x) = \lim\limits_{x \to x_0} \phi(x) = A$，则 $\lim\limits_{x \to x_0} f(x) = A$。

</div>
</details>

**例**：$\lim\limits_{x \to \infty} \dfrac{[x]}{x} = 1$。由 $x - 1 \lt{} [x] \le x$，$x \gt{} 0$ 时 $1 - \dfrac{1}{x} \lt{} \dfrac{[x]}{x} \le 1$；$x \lt{} 0$ 时 $1 - \dfrac{1}{x} \gt{} \dfrac{[x]}{x} \ge 1$（除以负数，不等号反向）。两边取极限即得 $1$。

<details class="callout theorem" id="function-monotone" data-callout="theorem" open>
<summary class="callout-title">单调收敛（单侧）</summary>
<div class="callout-content" markdown="block">

$(a - \delta, a)$ 上单调有界 $\Rightarrow \lim\limits_{x \to a^{-}} f(x)$ 存在；$(a, a + \delta)$ 上单调有界 $\Rightarrow \lim\limits_{x \to a^{+}} f(x)$ 存在；$(a, +\infty)$ 上单调有界 $\Rightarrow \lim\limits_{x \to +\infty} f(x)$ 存在。

</div>
</details>

**注意**：双侧不行 —— $f$ 在 $(a - \delta, a + \delta)$ 内单调有界，$\lim\limits_{x \to a} f(x)$ **不一定存在**。例：$f(x) = x\ (0 \lt{} x \lt{} 1)$，$f(x) = 2x\ (1 \le x \lt{} 2)$，在 $x = 1$ 处左右极限分别是 $1$ 与 $2$。

### 7.5 复合函数与变量替换

<details class="callout theorem" id="composite-limit" data-callout="theorem" open>
<summary class="callout-title">复合函数极限</summary>
<div class="callout-content" markdown="block">

设 $\lim\limits_{x \to x_0} g(x) = u_0$，在 $x_0$ 的某去心邻域内 $g(x) \neq u_0$，且 $\lim\limits_{u \to u_0} f(u) = A$，则 $\lim\limits_{x \to x_0} f\big(g(x)\big) = A$。

</div>
</details>

若 $g(x) \equiv u_0$，相当于只求 $f(u_0)$，但极限的本质是去心邻域，此时不能直接代入。常见推论：

- $\lim\limits_{x \to \infty} \operatorname{sgn}\!\left(\dfrac{1}{x^{2}}\right) = \lim\limits_{u \to 0^{+}} \operatorname{sgn}(u) = 1$；
- $\lim\limits_{x \to x_0} f(x) = A \Rightarrow \lim\limits_{x \to x_0} e^{f(x)} = e^{A}$；若 $A \gt{} 0$，则 $\lim\limits_{x \to x_0} \ln f(x) = \ln A$；
- $\lim\limits_{x \to x_0} f(x)^{g(x)} = A^{B}$（$A \gt{} 0$）。

### 7.6 两个重要极限

<details class="callout formula" id="important-limits" data-callout="formula" open>
<summary class="callout-title">基本款</summary>
<div class="callout-content" markdown="block">

$$\lim_{x \to 0} \frac{\sin x}{x} = 1, \qquad \lim_{x \to \infty}\left(1 + \frac{1}{x}\right)^{x} = e$$

第二个就是数列 $e = \lim\limits_{n \to \infty}\left(1+\frac{1}{n}\right)^{n}$（见 [e 的定义](#e-definition)）的函数版。

</div>
</details>

由此导出的一串极限：

- $\lim\limits_{x \to 0} \dfrac{\arcsin x}{x} = 1$（令 $\arcsin x = t$，即 $x = \sin t$）；
- $\lim\limits_{x \to 0^{+}}\left(1 + \dfrac{1}{x}\right)^{x} = \lim\limits_{t \to +\infty} (1 + t)^{\frac{1}{t}} = e^{\lim\limits_{t \to +\infty} \frac{\ln(1+t)}{t}} = e^{0} = 1$；
- $\lim\limits_{x \to \infty} x^{\frac{1}{x}} = 1$，$\lim\limits_{x \to 0^{+}} x^{x} = 1$。

<details class="callout understand" data-callout="understand" open>
<summary class="callout-title">草稿</summary>
<div class="callout-content" markdown="block">

用 $\ln(1 + x) \lt{} x$ 与 $\ln(1 + t) = 2\ln\sqrt{1+t} \lt{} 2(\sqrt{1+t} - 1)$：

$$0 \le \frac{\ln(1+t)}{t} \le \frac{2(\sqrt{1+t} - 1)}{t} = \frac{2}{\sqrt{1+t} + 1} \to 0$$

</div>
</details>

---

## 8 闭区间上连续函数的性质

<details class="callout theorem" id="boundedness-theorem" data-callout="theorem" open>
<summary class="callout-title">有界性定理</summary>
<div class="callout-content" markdown="block">

闭区间 $[a, b]$ 上的连续函数必有界。

</div>
</details>

**证（反证）**：若无界，则对每个 $n$ 存在 $x_n \in [a, b]$ 使 $\mid{}f(x_n)\mid{} \gt{} n$。由 [Bolzano–Weierstrass 定理](#bolzano-weierstrass) 有子列 $x_{n_k} \to \xi \in [a, b]$，由连续性 $f(x_{n_k}) \to f(\xi)$ 有界，与 $\mid{}f(x_{n_k})\mid{} \gt{} n_k \to \infty$ 矛盾。

### 8.1 最值定理

设 $f$ 在 $[a, b]$ 上连续，则 $f([a, b])$ 有上、下确界。以最小值为例，设下确界为 $m$，由 [确界](#sup-inf-def) 的定义，存在 $\lbrace{}x_n\rbrace{} \subset [a, b]$ 使 $m \le f(x_n) \lt{} m + \dfrac{1}{n}$，故 $f(x_n) \to m$。

<details class="callout theorem" id="extreme-value" data-callout="theorem" open>
<summary class="callout-title">最值定理</summary>
<div class="callout-content" markdown="block">

闭区间上的连续函数可取到最大值与最小值。

</div>
</details>

**证**：接上，由 [Bolzano–Weierstrass 定理](#bolzano-weierstrass) 有收敛子列 $x_{n_k} \to \xi$，其中 $\xi \in [a, b]$（闭区间对极限封闭）。由连续性 $f(\xi) = \lim\limits_{k \to \infty} f(x_{n_k}) = m$，即最小值可以取到。上确界同理。

### 8.2 介值定理

<details class="callout theorem" id="intermediate-value" data-callout="theorem" open>
<summary class="callout-title">介值定理（零点存在定理）</summary>
<div class="callout-content" markdown="block">

若 $f$ 在 $[a, b]$ 上连续，$f(a)f(b) \lt{} 0$，则存在 $\xi \in (a, b)$ 使 $f(\xi) = 0$。

</div>
</details>

**证明思路**：二分法。不断把含变号的区间对半缩小，构造 [闭区间套](#nested-intervals)，公共点 $\xi$ 处由连续性得 $f(\xi) = 0$。

---

## 9 无穷小量的比较

### 9.1 三种关系

设 $\alpha(x) \to 0$，$\beta(x) \to 0$，且 $\beta(x) \neq 0$：

- $\lim \dfrac{\alpha}{\beta} = 0$：$\alpha$ 是比 $\beta$ **高阶**的无穷小量；
- $\lim \dfrac{\alpha}{\beta} = c \neq 0$：**同阶**无穷小量；
- $\lim \dfrac{\alpha}{\beta} = 1$：**等价**无穷小量，记 $\alpha \sim \beta$（等价关系，有传递性）。

<details class="callout definition" id="equivalent-infinitesimal" data-callout="definition" open>
<summary class="callout-title">等价的一个刻画</summary>
<div class="callout-content" markdown="block">

设存在小邻域使 $\beta(x) \neq 0$，则 $\alpha(x) \sim \beta(x) \iff \alpha(x) = \beta(x) + o(\beta(x))$。

</div>
</details>

### 9.2 常用等价无穷小（$x \to 0$）

<details class="callout formula" id="equivalent-infinitesimals" data-callout="formula" open>
<summary class="callout-title">背下来的一串</summary>
<div class="callout-content" markdown="block">

$$\sin x \sim x \sim \tan x \sim \arcsin x \sim \arctan x \sim e^{x} - 1 \sim \ln(1 + x)$$

$$1 - \cos x \sim \frac{1}{2}x^{2}, \qquad (1 + x)^{a} - 1 \sim ax\ (a \neq 0)$$

$$a^{x} - 1 \sim x\ln a\ (a \gt{} 0,\ a \neq 1), \qquad \log_a (1 + x) \sim \frac{x}{\ln a}, \qquad \ln\!\left(x + \sqrt{1 + x^{2}}\right) \sim x$$

</div>
</details>

### 9.3 替换的规则

<details class="callout keypoint" data-callout="keypoint" open>
<summary class="callout-title">等价替换只能在"相乘"时用</summary>
<div class="callout-content" markdown="block">

若 $\alpha \sim \beta$，且 $\alpha f$、$\beta f$ 的极限都存在，则 $\lim \alpha f = \lim \beta f$。
**只能在"相乘"时替换**（乘除因子可以换），加减法里替换会丢掉高阶项，出错。

</div>
</details>

### 9.4 $O$ 记号与阶

**$O$ 记号**：$\mid{}\alpha(x)\mid{} \le C\mid{}\beta(x)\mid{}$（$x$ 在某个范围里）记作 $\alpha(x) = O(\beta(x))$。

**$k$ 阶无穷小**：$x \to a$ 时若 $\alpha \sim (x - a)^{k}$，称 $\alpha$ 是 $k$ 阶无穷小。

**同阶的等价写法**：$\dfrac{\beta}{\alpha} \to k \neq 0 \iff \beta = k\alpha + o(\alpha)$。

- 必要：$\dfrac{\beta}{\alpha} \to k$ 时 $\dfrac{\beta - k\alpha}{\alpha} = \dfrac{\beta}{\alpha} - k \to 0$，即 $\beta - k\alpha = o(\alpha)$；
- 充分：$\beta = k\alpha + o(\alpha)$ 时 $\lim \dfrac{\beta}{\alpha} = \lim \dfrac{k\alpha + o(\alpha)}{\alpha} = k$。

---

## 10 常用工具与技巧

### 10.1 $\mathrm{AM} \ge \mathrm{GM}$（柯西归纳法）

<details class="callout theorem" data-callout="theorem" open>
<summary class="callout-title">$\mathrm{AM} \ge \mathrm{GM}$（柯西归纳法）</summary>
<div class="callout-content" markdown="block">

$$\frac{1}{n}\sum_{i=1}^{n} a_i \ \ge\ \sqrt[n]{\prod_{i=1}^{n} a_i} \qquad (a_i \ge 0)$$

</div>
</details>

**证**（对 $n$ 归纳：用"$n-1$ 成立 $\Rightarrow$ $n$ 成立"）：

- $n = 1$ 显然。
- 设 $n - 1$ 时成立。不妨设 $a_1 \le a_2 \le \cdots \le a_n$，记前 $n-1$ 个的算术平均为 $y = \dfrac{1}{n-1}\sum\limits_{i=1}^{n-1} a_i$。由归纳假设与"$a_n$ 最大"得 $a_n \ge y \ge \sqrt[n-1]{a_1 a_2 \cdots a_{n-1}}$。
- 于是

$$\left(\frac{1}{n}\sum_{i=1}^{n} a_i\right)^{n} = \left(y + \frac{a_n - y}{n}\right)^{n} \ge y^{n} + n\,y^{n-1}\frac{a_n - y}{n} = y^{n-1} a_n \ge \prod_{i=1}^{n} a_i$$

第一个不等号用二项式展开：因 $a_n - y \ge 0$，展开式其余各项都非负，只保留前两项。
<a id="amgm"></a>

### 10.2 放缩的经验

<details class="callout keypoint" data-callout="keypoint" open>
<summary class="callout-title">三条（保留自己的话）</summary>
<div class="callout-content" markdown="block">

① 抛弃常数项（$n \to \infty$ 时常数可忽略）；
② 抛弃"非决定项"（只留起决定作用的项）；
③ 常数 $1$ 是好用的垫脚石（凑 $\mathrm{AM}$–$\mathrm{GM}$、凑"$1$ 的变形"）。

</div>
</details>

### 10.3 综合例：$\dfrac{(n!)^{\alpha}}{n^{n}}$ 的极限

<details class="callout example" data-callout="example" open>
<summary class="callout-title">综合例：讨论 $\dfrac{(n!)^{\alpha}}{n^{n}}$ 的极限</summary>
<div class="callout-content" markdown="block">

分别求 $\alpha \gt{} 1$ 与 $\alpha \le 1$ 时的极限。

</div>
</details>

**当 $\alpha \gt{} 1$ 时，极限为 $+\infty$。** 看相邻两项之比：

$$\frac{\frac{((n+1)!)^{\alpha}}{(n+1)^{n+1}}}{\frac{(n!)^{\alpha}}{n^{n}}} = \frac{(n+1)^{\alpha-1}}{\left(1 + \frac{1}{n}\right)^{n}} \longrightarrow \frac{(n+1)^{\alpha-1}}{e} \longrightarrow +\infty$$

比值趋于 $+\infty$，故数列本身趋于 $+\infty$（$\alpha \gt{} 1$ 时分子是 $n$ 的正幂次，压过常数 $e$）。

**当 $\alpha \le 1$ 时，极限为 $0$。** 此时 $(n!)^{\alpha} \le n!$（因 $n! \ge 1$），故

$$0 \le \frac{(n!)^{\alpha}}{n^{n}} \le \frac{n!}{n^{n}}$$

其中 $\dfrac{n!}{n^{n}} = \displaystyle\prod_{k=1}^{n}\frac{k}{n}$，用**配对放缩**：把 $\frac{k}{n}$ 与 $\frac{n-k}{n}$ 配成一对，$\dfrac{k}{n}\cdot\dfrac{n-k}{n} = \dfrac{k(n-k)}{n^{2}} \le \dfrac{1}{4}$。所以 $\dfrac{n!}{n^{n}} \le \left(\dfrac{1}{4}\right)^{\lfloor n/2 \rfloor}$（$n$ 为奇数时中间那个因子 $\le 1$，可以丢掉）。由 [夹逼定理](#squeeze) 与非负性，极限为 $0$。

---

## 11 导数与微分

### 11.1 可导的定义

<details class="callout definition" id="derivative-definition" data-callout="definition" open>
<summary class="callout-title">导数</summary>
<div class="callout-content" markdown="block">

$f(x)$ 在 $x_0$ 处**可导** $\iff \lim\limits_{\Delta x \to 0} \dfrac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}$ 存在，记为 $f'(x_0)$。
这是一个**双侧**极限，故充要条件是左右导数相等：

$$\lim_{\Delta x \to 0^{+}} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x} = \lim_{\Delta x \to 0^{-}} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}$$

</div>
</details>

**可导的必要条件：连续**。$f$ 在 $x_0$ 处必须 ① 有定义；② $\lim\limits_{x \to x_0^{+}} f(x) = \lim\limits_{x \to x_0^{-}} f(x) = f(x_0)$。反之不成立（$\mid{}x\mid{}$ 在 $0$ 处连续但不可导）。

<details class="callout keypoint" id="derivative-continuity-warning" data-callout="keypoint" open>
<summary class="callout-title">导函数不保证连续</summary>
<div class="callout-content" markdown="block">

相对于原函数"变差"：$f$ 在 $[a, b]$ 上可导，**$f'(x)$ 不一定也在 $[a, b]$ 上连续**。所以不能默认"求完导还能再对 $f'$ 用连续性的结论"。

</div>
</details>

### 11.2 求导法则

<details class="callout theorem" id="derivative-rules" data-callout="theorem" open>
<summary class="callout-title">四则与链式</summary>
<div class="callout-content" markdown="block">

$$(f \pm g)' = f' \pm g', \qquad (fg)' = f'g + fg', \qquad \left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^{2}}$$

复合：$\dfrac{dy}{dx} = \dfrac{dy}{du}\cdot\dfrac{du}{dx}$，即 $(f(g(x)))' = f'(g(x))\,g'(x)$；多重复合 $\dfrac{dy}{dx} = \dfrac{dy}{du_n}\dfrac{du_n}{du_{n-1}}\cdots\dfrac{du_1}{dx}$（有限项）。

</div>
</details>

推广至有限项、线性组合。链式法则的严格写法需构造辅助函数

$$
\varphi(u(x)) = \begin{cases}
\dfrac{f(u(x)) - f(u(x_0))}{u(x) - u(x_0)}, & u(x) \neq u(x_0) \\\\[6pt]
f'(u(x_0)), & u(x) = u(x_0)
\end{cases}
$$

<details class="callout understand" data-callout="understand" open>
<summary class="callout-title">为什么如此构造</summary>
<div class="callout-content" markdown="block">

**防止在 $x_0$ 的邻域内 $u(x) - u(x_0)$ 的零点极多**。
比如对任意的 $x \in \mathbb{Q}$，$U(x)-U(x_0)=0$，则任取一个邻域必然有零点。
$x \to u$ 映射，$u \to y$ 映射，**由外向内逐层求导**。

</div>
</details>

由 $f^{-1}(f(x)) = x$ 两边对 $x$ 求导得 $\left(f^{-1}\right)'(f(x))\cdot f'(x) = 1$，即

<details class="callout formula" id="inverse-derivative" data-callout="formula" open>
<summary class="callout-title">反函数求导</summary>
<div class="callout-content" markdown="block">

设 $y = f(x) \iff x = f^{-1}(y)$，则

$$\left(f^{-1}\right)'(y) = \frac{1}{f'(x)} = \frac{1}{f'\big(f^{-1}(y)\big)}$$

</div>
</details>

最常见的例子是 $f(x) = e^{x}$ 与 $f^{-1}(x) = \ln x$。

<details class="callout keypoint" data-callout="keypoint" open>
<summary class="callout-title">反函数求导最常见的错</summary>
<div class="callout-content" markdown="block">

写成 $\varphi'(x)f'(x) = 1$ **不成立** —— 两边的自变量不是同一个点。正确形式是 $\varphi'(f(x))\,f'(x) = 1$，即"$\varphi'$ 要在 $f(x)$ 那一点取值"。

</div>
</details>

**隐函数求导**：设 $f(x, y) = 0$ 确定了 $x \mapsto y$ 的规则。当 $y$ 难以被 $x$ 显式表示时，把 $y$ 看成 $x$ 的函数、两边对 $x$ 求导，再解出 $y'$，就能研究 $y$ 的变化率。

**对数求导法 / 幂指函数**：对 $y = u(x)^{v(x)}$（$u \gt{} 0$，$u, v$ 可导），取对数 $\ln y = v\ln u$，两边求导得 $\dfrac{y'}{y} = v'\ln u + \dfrac{u'}{u}v$，即

$$y' = u^{v}\left(v'\ln u + \frac{u' v}{u}\right)$$

（等价写法：$y = e^{v \ln u}$，直接对指数求导。）
<a id="logarithmic-derivative"></a>

### 11.3 反三角函数的导数

以 $\arcsin$ 为例：$y = \arcsin x \iff x = \sin y$，

$$\frac{dy}{dx} = \frac{1}{\frac{dx}{dy}} = \frac{1}{\cos y} = \frac{1}{\cos(\arcsin x)}$$

由 $\sin(\arcsin x) = x$ 与 $\cos(\arcsin x) = \sqrt{1 - x^{2}}$（$y \in (-\pi/2, \pi/2)$ 上 $\cos y \gt{} 0$），得 $(\arcsin x)' = \dfrac{1}{\sqrt{1 - x^{2}}}$。

| 函数 | 导数 | 适用范围 |
| --- | --- | --- |
| $\arcsin x$ | $\dfrac{1}{\sqrt{1 - x^{2}}}$ | $\lvert x \rvert \lt{} 1$ |
| $\arccos x$ | $-\dfrac{1}{\sqrt{1 - x^{2}}}$ | $\lvert x \rvert \lt{} 1$ |
| $\arctan x$ | $\dfrac{1}{1 + x^{2}}$ | $x \in \mathbb{R}$ |
| $\operatorname{arccot} x$ | $-\dfrac{1}{1 + x^{2}}$ | $x \in \mathbb{R}$ |
| $\operatorname{arcsec} x$ | $\dfrac{1}{\lvert x \rvert\sqrt{x^{2} - 1}}$ | $\lvert x \rvert \gt{} 1$ |
| $\operatorname{arccsc} x$ | $-\dfrac{1}{\lvert x \rvert\sqrt{x^{2} - 1}}$ | $\lvert x \rvert \gt{} 1$ |

辅助式：$\cos(\operatorname{arcsec} x) = \dfrac{1}{x}$，$\sin(\operatorname{arcsec} x) = \dfrac{\sqrt{x^{2} - 1}}{\lvert x \rvert}$。三角恒等式备用：[积化和差 和差化积](/notes/ji-hua-he-cha-he-cha-hua-ji/)。
<a id="inverse-trig-derivatives"></a>

### 11.4 由两个重要极限导出的一组极限

<details class="callout formula" data-callout="formula" open>
<summary class="callout-title">由两个重要极限导出的一组极限</summary>
<div class="callout-content" markdown="block">

$\lim\limits_{x \to 0}\dfrac{\sin x}{x} = 1$（多项式与三角）导出

</div>
</details>

$$\lim_{x \to 0} \frac{\sin x}{x} = \lim_{x \to 0} \frac{\tan x}{x} = \lim_{x \to 0} \frac{\arcsin x}{x} = \lim_{x \to 0} \frac{\arctan x}{x} = 1, \qquad \lim_{x \to 0} \frac{1 - \cos x}{x^{2}} = \frac{1}{2}$$

$\lim\limits_{x \to \infty}\left(1 + \dfrac{1}{x}\right)^{x} = e$、$\lim\limits_{x \to 0}(1 + x)^{\frac{1}{x}} = e$（指数、对数、幂函数）导出

$$\lim_{x \to 0} \frac{\ln(1 + x)}{x} = \lim_{x \to 0}\ln(1 + x)^{\frac{1}{x}} = 1, \qquad \lim_{x \to 0} \frac{a^{x} - 1}{x} = \ln a, \qquad \lim_{x \to 0} \frac{(1 + x)^{a} - 1}{x} = a$$

后两式的算法是"凑"，统一变量至初等形式：

$$\frac{a^{x} - 1}{x} = \frac{e^{x\ln a} - 1}{x\ln a}\cdot\ln a \longrightarrow \ln a, \qquad \frac{(1 + x)^{a} - 1}{x} = \frac{(1 + x)^{a} - 1}{a\ln(1 + x)}\cdot\frac{a\ln(1 + x)}{x} \longrightarrow a$$

<a id="standard-derivative-limits"></a>

### 11.5 函数的连续

<details class="callout definition" id="continuity-definition" data-callout="definition" open>
<summary class="callout-title">连续的定义</summary>
<div class="callout-content" markdown="block">

$f$ 在 $x_0$ 处连续 $\iff \lim\limits_{x \to x_0} f(x) = f(x_0)$，即 $\forall \varepsilon \gt{} 0,\ \exists \delta \gt{} 0$，当 $\mid{}x - x_0\mid{} \lt{} \delta$ 时 $\mid{}f(x) - f(x_0)\mid{} \lt{} \varepsilon$。
三个条件：① $x_0$ 处有定义；② $\lim\limits_{x \to x_0} f(x)$ 存在；③ 二者相等。等价表述：$\lim\limits_{\Delta x \to 0} \Delta y = 0$。

</div>
</details>

连续时极限可入内：$\lim\limits_{x \to x_0} f(g(x)) = f\left(\lim\limits_{x \to x_0} g(x)\right)$。

区间上连续：在 $(a, b)$ 上连续指每一点连续；在 $[a, b]$ 上连续还要求 $a$ 处右连续、$b$ 处左连续。连续函数全体记

$$C[a, b] = \{f(x) \mid f(x) \text{ 在 } [a, b] \text{ 上连续}\}$$

**单调连续函数的反函数也是连续的**：若 $f$ 在 $(a, b)$ 上单调且连续，则 $f\big((a, b)\big) = (c, d)$，且反函数 $f^{-1}$ 在 $(c, d)$ 上连续。
<a id="monotone-inverse-continuity"></a>

---

## 12 微分

### 12.1 可微与微分

<details class="callout definition" id="differentiability" data-callout="definition" open>
<summary class="callout-title">可微与微分</summary>
<div class="callout-content" markdown="block">

记 $\Delta y = f(x_0 + \Delta x) - f(x_0)$。若存在**与 $\Delta x$ 无关**（只与 $x_0$ 有关）的 $A$，使

$$\Delta y = A\,\Delta x + o(\Delta x)\quad(\Delta x \to 0)$$

则称 $f$ 在 $x_0$ 处**可微**，$A\,\Delta x$ 称为 $f$ 在 $x_0$ 处的**微分**（线性主部），记 $dy\big\vert&#95;{x=x_0}$ 或 $df(x_0)$。
若 $f$ 在区间 $I$ 内处处可微，称 $f$ 为**可微函数**。

</div>
</details>

记 $dx = \Delta x$，但 $dy \neq \Delta y$：$\Delta y - dy = o(\Delta x)$。由定义立刻得到 $dy = f'(x)\,dx$，即 $\dfrac{dy}{dx} = f'(x)$。$A = f'(x_0) \neq 0$ 时 $dy \sim \Delta y$。

### 12.2 可导与可微

<details class="callout theorem" id="differentiable-iff-derivable" data-callout="theorem" open>
<summary class="callout-title">一元函数：可导 $\iff$ 可微</summary>
<div class="callout-content" markdown="block">

$f$ 在 $x_0$ 处可导 $\iff$ $f$ 在 $x_0$ 处可微；此时 $A = f'(x_0)$，$dy = f'(x_0)\,\Delta x$。

</div>
</details>

**证**。**可导 $\Rightarrow$ 可微**：$\dfrac{\Delta y}{\Delta x} \to f'(x_0)$，令 $\alpha = \dfrac{\Delta y}{\Delta x} - f'(x_0) \to 0$，则 $\Delta y = f'(x_0)\Delta x + \alpha \Delta x$，而 $\alpha \Delta x = o(\Delta x)$。
**可微 $\Rightarrow$ 可导**：$\Delta y = A\Delta x + o(\Delta x)$ 两边除以 $\Delta x$，得 $\dfrac{\Delta y}{\Delta x} = A + \dfrac{o(\Delta x)}{\Delta x} \to A$。

**多元不同**：可微 $\Rightarrow$ 可导（各偏导存在），反过来不成立。

### 12.3 微分法则与局部线性化

<details class="callout formula" id="differential-rules" data-callout="formula" open>
<summary class="callout-title">微分法则（同求导法则）</summary>
<div class="callout-content" markdown="block">

$$d(u \pm v) = du \pm dv, \qquad d(uv) = v\,du + u\,dv, \qquad d(Cu) = C\,du, \qquad d\!\left(\frac{u}{v}\right) = \frac{v\,du - u\,dv}{v^{2}}\quad(C \text{ 为常数})$$

</div>
</details>

**局部线性化**：$dy$ 代替 $\Delta y$，即 $y - y_0 = f'(x_0)(x - x_0)$。

**近似计算**：$\Delta y\big\vert&#95;{x=x_0} \approx dy\big\vert&#95;{x=x_0}$。

---

## 13 高阶导数与高阶微分

### 13.1 高阶导数

<details class="callout definition" id="higher-derivative" data-callout="definition" open>
<summary class="callout-title">高阶导数</summary>
<div class="callout-content" markdown="block">

$n \ge 2$ 时，$f^{(n)}(x) = \left(f^{(n-1)}(x)\right)'$，记 $\dfrac{d^{n}y}{dx^{n}}$。

</div>
</details>

$m$ 次多项式求 $m+1$ 阶导即得 $0$：$f(x) = a_m x^{m} + \cdots + a_1 x + a_0$ 时 $f^{(m+1)} \equiv 0$。

<details class="callout formula" id="nth-derivative-formulas" data-callout="formula" open>
<summary class="callout-title">常用 $n$ 阶导</summary>
<div class="callout-content" markdown="block">

$$(x^{\alpha})^{(n)} = \frac{\alpha!}{(\alpha-n)!}x^{\alpha-n} = \binom{\alpha}{n}n!\,x^{\alpha-n}$$

$$(\sin x)^{(n)} = \sin\left(x + \frac{n\pi}{2}\right), \qquad (\cos x)^{(n)} = \cos\left(x + \frac{n\pi}{2}\right)$$

$$(e^{ax})^{(n)} = a^{n}e^{ax}, \qquad (\sin bx)^{(n)} = b^{n}\sin\left(bx + \frac{n\pi}{2}\right)$$

$$y = e^{ax}\sin bx:\quad y^{(n)} = (a^{2} + b^{2})^{\frac{n}{2}}e^{ax}\sin(bx + n\varphi),\qquad \tan\varphi = \frac{b}{a}$$

</div>
</details>

$\alpha$ 为非负整数时 $\dfrac{\alpha!}{(\alpha-n)!} = \alpha(\alpha-1)\cdots(\alpha-n+1)$，$n \gt{} \alpha$ 时为 $0$。

### 13.2 Leibniz 公式

<details class="callout theorem" id="leibniz" data-callout="theorem" open>
<summary class="callout-title">Leibniz 公式</summary>
<div class="callout-content" markdown="block">

若 $f, g$ 都有 $n$ 阶导，则

$$[f(x)g(x)]^{(n)} = \sum_{k=0}^{n}\binom{n}{k}f^{(k)}(x)\,g^{(n-k)}(x)$$

</div>
</details>

类同二项式定理。若 $f$ 是 $m$ 次多项式，则 $k \gt{} m$ 时 $f^{(k)} \equiv 0$，和式只剩前 $m+1$ 项。求商的 $n$ 阶导时写 $\left[\dfrac{f}{g}\right]^{(n)} = \left[f\cdot\dfrac{1}{g}\right]^{(n)}$，把问题转成乘积。

<details class="callout example" data-callout="example" open>
<summary class="callout-title">例：$y = \arctan x$，求 $y^{(n)}(0)$</summary>
<div class="callout-content" markdown="block">

求 $y = \arctan x$ 在 $x = 0$ 处的 $n$ 阶导数。

</div>
</details>

**解**：$y' = \dfrac{1}{1 + x^{2}}$，即 $(1 + x^{2})y' = 1$。两边用 [Leibniz 公式](#leibniz) 求 $n$ 阶导 —— $1 + x^{2}$ 只有三项，得

$$(1 + x^{2})y^{(n+1)} + n\cdot 2x\,y^{(n)} + \frac{n(n-1)}{2}\cdot 2\,y^{(n-1)} = 0$$

令 $x = 0$：$y^{(n+1)}(0) = -n(n-1)\,y^{(n-1)}(0)$。由 $y(0) = 0$、$y'(0) = 1$，偶数阶导在 $0$ 处全为 $0$，奇数阶逐次递推得

$$y^{(2k+1)}(0) = (-1)^{k}(2k)!$$

<details class="callout understand" data-callout="understand" open>
<summary class="callout-title">理解：为何如此构造？</summary>
<div class="callout-content" markdown="block">

利用隐函数求导，去掉分式结构，找到递推。

</div>
</details>

### 13.3 高阶微分与形式不变性

**高阶微分**：$d^{n}y = d\left(d^{n-1}y\right)$。两种含义：$d(x^{n}) = nx^{n-1}dx$ 是求微分，$dx^{n} = (dx)^{n}$ 是微分的乘幂。

<details class="callout keypoint" id="higher-differential" data-callout="keypoint" open>
<summary class="callout-title">一阶有形式不变性，高阶没有</summary>
<div class="callout-content" markdown="block">

$dy = f'(x)dx$ 在 $x$ 为自变量时成立，在 $x = \varphi(t)$ 为中间变量时同样成立：$dy = f'(x)\varphi'(t)\,dt$。二阶起不成立，$d^{2}y = f''(x)(dx)^{2}$ 只在 $x$ 为自变量时对。

</div>
</details>

形式不变性的用处：① 积分变量替换；② 求复合微分。

### 13.4 反函数与参数方程

**反函数的高阶导**：$\dfrac{dx}{dy} = \dfrac{1}{f'(x)}$。再对 $y$ 求导时 $x$ 是 $y$ 的函数，要补一个 $\dfrac{dx}{dy}$：

$$\frac{d^{2}x}{dy^{2}} = \frac{d}{dy}\left(\frac{1}{f'(x)}\right) = \frac{d}{dx}\left(\frac{1}{f'(x)}\right)\cdot\frac{dx}{dy} = -\frac{f''(x)}{f'(x)^{3}}$$

**参数方程**：$x = x(t)$，$y = y(t)$ 时 $\dfrac{dy}{dx} = \dfrac{y'(t)\,dt}{x'(t)\,dt} = \dfrac{y'(t)}{x'(t)}$（$x'(t) \neq 0$）。
<a id="parametric-derivative"></a>

---

## 14 三个病态函数

| 函数 | 连续 | 可导 | 备注 |
| --- | --- | --- | --- |
| $f(x) = e^{-\frac{1}{x}}\ (x \gt{} 0)$，$0\ (x \le 0)$ | $\mathbb{R}$ 上连续 | $\mathbb{R}$ 上无穷次可导 | 各阶导在 $0$ 处为 $0$，但各阶导不恒为 $0$ |
| Dirichlet $D(x)$ | 处处不连续 | 处处不可导 | 非零有理数都是周期，无最小正周期 |
| Thomae $R(x)$ | 无理点连续、有理点不连续 | 处处不可导 | 周期 $1$；无理点处极限为 $0$ |

**$e^{-1/x}$**：$x \gt{} 0$ 时 $f^{(n)}(x) = P_n\!\left(\frac{1}{x}\right)e^{-\frac{1}{x}}$，$P_n$ 为多项式，$P_1(t) = t^{2}$，$P_{n+1}(t) = t^{2}\left(P_n(t) - P_n'(t)\right)$。$t^{m}e^{-t} \to 0$ 给出 $f^{(n)}(0) = 0$，于是它在 $0$ 处的泰勒级数恒为 $0$，与函数本身不符。通项与证明见 [e的负x分之一次方的无穷次可导性](/notes/e-de-fu-x-fen-zhi-yi-ci-fang-de-wu-qiong-ci-ke-dao-xing/)。

**Dirichlet 函数**：$D(x) = 1\ (x \in \mathbb{Q})$，$0\ (x \notin \mathbb{Q})$。$T \in \mathbb{Q}$、$T \neq 0$ 时 $D(x + T) = D(x)$，故每个非零有理数都是周期；**无理数不是周期**（$x$ 与 $x + T$ 的有理性相反）。任一点取有理数列与无理数列逼近，$D$ 的极限分别是 $1$ 与 $0$，故极限处处不存在。

**Thomae 函数**：$R(x) = \dfrac{1}{q}\ (x = \dfrac{p}{q}\ \text{既约},\ q \gt{} 0)$，$0\ (x \notin \mathbb{Q})$。分母越大值越小，所以有理点的稠密不破坏它在无理点收敛到 $0$。无理点处也不可导：差商沿无理方向为 $0$，沿有理方向无界。证明见 [Thomae 函数的连续性](/notes/thomae-han-shu-de-lian-xu-xing/)。

---

## 相关笔记

- 主线：[线性代数笔记](/notes/xian-xing-dai-shu-bi-ji/)
- 极限与证明细节：[Stolz定理的证明](/notes/stolz-ding-li-di-zheng-ming/)
- 集合、求和与三角工具：[集合运算律](/notes/ji-he-yun-suan-lv/)、[∑求和运算律](/notes/qiu-he-yun-suan-lv/)、[积化和差 和差化积](/notes/ji-hua-he-cha-he-cha-hua-ji/)
- 可列集专题：[无限可列集等势证明](/notes/wu-xian-ke-lie-ji-deng-shi-zheng-ming/)、[实数集与无理数集不可列证明](/notes/shi-shu-ji-yu-wu-li-shu-ji-bu-ke-lie-zheng-ming/)
- 病态函数：[e的负x分之一次方的无穷次可导性](/notes/e-de-fu-x-fen-zhi-yi-ci-fang-de-wu-qiong-ci-ke-dao-xing/)、[Thomae 函数的连续性](/notes/thomae-han-shu-de-lian-xu-xing/)
