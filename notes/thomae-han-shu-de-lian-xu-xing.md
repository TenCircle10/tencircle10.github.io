---
layout: note
title: "Thomae 函数的连续性"
slug: "thomae-han-shu-de-lian-xu-xing"
permalink: "/notes/thomae-han-shu-de-lian-xu-xing/"
public: false
generated_by: sync_notes.py
render_with_liquid: false
---

# Thomae 函数的连续性

<details class="callout abstract" data-callout="abstract" open>
<summary class="callout-title">断言</summary>
<div class="callout-content" markdown="block">

$R(x)$ 在**无理点连续**、在**有理点不连续**；周期 $1$，没有最小正周期。

</div>
</details>

分母越大值越小 —— 这条最简单的事实决定了后面所有结论。

<details class="callout definition" id="thomae" data-callout="definition" open>
<summary class="callout-title">Thomae（黎曼）函数</summary>
<div class="callout-content" markdown="block">

$$R(x) = \begin{cases} \dfrac{1}{q}, & x = \dfrac{p}{q} \in \mathbb{Q},\ (p, q) = 1,\ q \gt{} 0 \\\\[6pt] 0, & x \in \mathbb{R} \setminus \mathbb{Q} \end{cases}$$

$x = 0$ 约定 $R(0) = 1$（写成立约形式 $\frac{0}{1}$）。

</div>
</details>

<details class="callout theorem" id="thomae-continuity" data-callout="theorem" open>
<summary class="callout-title">无理点处连续</summary>
<div class="callout-content" markdown="block">

若 $x_0 \in \mathbb{R} \setminus \mathbb{Q}$，则 $\lim\limits_{x \to x_0} R(x) = 0 = R(x_0)$。

</div>
</details>

**证**：任给 $\varepsilon \gt{} 0$，取 $N \in \mathbb{N}&#95;{+}$ 使 $\dfrac{1}{N} \lt{} \varepsilon$。分母不超过 $N$ 的有理数只有有限个：

$$F_N = \left\{\frac{p}{q} \;\middle|\; 1 \le p \le q,\ 1 \le q \le N\right\}$$

（不妨设 $x_0 \in [0, 1]$，此时 $0 \lt{} \frac{p}{q} \le 1$ 必有 $p \le q$。）$F_N$ 有限且不含 $x_0$，所以

$$\delta = \min\{|x - x_0| : x \in F_N\} \gt{} 0$$

当 $0 \lt{} \mid{}x - x_0\mid{} \lt{} \delta$ 时：若 $x \notin \mathbb{Q}$，$R(x) = 0$；若 $x = \frac{p}{q}$ 既约，则 $x \notin F_N$ 迫使 $q \gt{} N$，于是

$$R(x) = \frac{1}{q} \lt{} \frac{1}{N} \lt{} \varepsilon$$

两种情形都给出 $\mid{}R(x) - 0\mid{} \lt{} \varepsilon$，故 $\lim\limits_{x \to x_0} R(x) = 0$。
<a id="thomae-proof"></a>

**有理点处不连续**：设 $x_0 = \dfrac{p}{q}$ 既约，则 $R(x_0) = \dfrac{1}{q} \gt{} 0$。取无理数列 $x_n \to x_0$，则 $R(x_n) = 0 \to 0 \neq R(x_0)$，故 $R$ 在 $x_0$ 处不连续。

<details class="callout understand" data-callout="understand" open>
<summary class="callout-title">重点</summary>
<div class="callout-content" markdown="block">

重点是如何想到以 $\frac{1}{q}$ 作为距离用 $\delta$ 约束。

</div>
</details>

**这一步的支点是"有限"**：$\delta$ 能取正，靠的是 $F_N$ 有限且不含 $x_0$；只写 $\delta \lt{} \frac{1}{N}$ 卡不住分母 $\le N$ 的那些点，它们可以任意接近 $x_0$。

---

## 无理点处不可导

$x_0 \notin \mathbb{Q}$ 时 $R(x_0) = 0$，差商为

$$\frac{R(x_0 + h) - R(x_0)}{h} = \frac{R(x_0 + h)}{h}$$

$h \notin \mathbb{Q}$ 时差商为 $0$；$h = \dfrac{p}{q} - x_0$ 时差商为 $\dfrac{1/q}{p/q - x_0}$。

**有理逼近**：记 $\Vert{}x\Vert{} = \min\lbrace{}\mid{}x - n\mid{} : n \in \mathbb{Z}\rbrace{}$。对无理数 $x_0$，存在无穷多个既约 $\dfrac{p}{q}$ 使 $\left\vert{}x_0 - \dfrac{p}{q}\right\vert \lt{} \dfrac{1}{q^{2}}$。

**证**：$0, \lbrace{}x_0\rbrace{}, \lbrace{}2x_0\rbrace{}, \dots, \lbrace{}Nx_0\rbrace{}$ 共 $N + 1$ 个数落在 $[0, 1)$ 的 $N$ 个等分区间内，存在 $k \ne l$ 使 $\Vert{}(k - l)x_0\Vert{} \lt{} \dfrac{1}{N}$。取 $q = \mid{}k - l\mid{} \le N$，$p$ 为离 $qx_0$ 最近的整数，则

$$\left|x_0 - \frac{p}{q}\right| = \frac{\|qx_0\|}{q} \lt{} \frac{1}{qN} \le \frac{1}{q^{2}}$$

$q$ 无界：若 $q \le Q$，则某个 $q$ 对无穷多个 $N$ 满足 $\Vert{}qx_0\Vert{} \lt{} \dfrac{1}{N}$，得 $qx_0 \in \mathbb{Z}$，与 $x_0$ 无理矛盾。约分后 $q' \le q \le N$，$\left\vert{}x_0 - \dfrac{p'}{q'}\right\vert \lt{} \dfrac{1}{qN} \le \dfrac{1}{q'^{2}}$ 仍成立，以下写作既约 $\dfrac{p}{q}$。

于是 $\left\vert\dfrac{1/q}{p/q - x_0}\right\vert \gt{} q$ 无界，差商极限不存在，$R$ 在无理点不可导。
<a id="thomae-nondiff"></a>

---

## 相关笔记

- 主线：[数学分析笔记](/notes/shu-xue-fen-xi-bi-ji/)
- 同期病态函数：[e的负x分之一次方的无穷次可导性](/notes/e-de-fu-x-fen-zhi-yi-ci-fang-de-wu-qiong-ci-ke-dao-xing/)
- 极限与连续：[[数学分析笔记#^heine|Heine 定理]]、[[数学分析笔记#^continuity-definition|连续的定义]]
