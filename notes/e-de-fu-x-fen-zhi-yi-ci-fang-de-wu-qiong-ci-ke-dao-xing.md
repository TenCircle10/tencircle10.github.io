---
layout: note
title: "e的负x分之一次方的无穷次可导性"
slug: "e-de-fu-x-fen-zhi-yi-ci-fang-de-wu-qiong-ci-ke-dao-xing"
permalink: "/notes/e-de-fu-x-fen-zhi-yi-ci-fang-de-wu-qiong-ci-ke-dao-xing/"
public: false
render_with_liquid: false
---

# e 的负 x 分之一次方的无穷次可导性

<details class="callout abstract" data-callout="abstract" open>
<summary class="callout-title">断言</summary>
<div class="callout-content" markdown="block">

$f(x) = e^{-\frac{1}{x}}\ (x \gt{} 0)$，$f(x) = 0\ (x \le 0)$ 在 $\mathbb{R}$ 上无穷次可导，且 $f^{(n)}(0) = 0$ 对一切 $n$。

</div>
</details>

## 1 归结到 $x = 0$

$x \lt{} 0$ 时 $f \equiv 0$，常值；$x \gt{} 0$ 时 $f$ 是 $e^{u}$ 与 $u = -\frac{1}{x}$ 的复合，无穷次可导。只剩 $x = 0$。

## 2 $f^{(n)}$ 的形状与递推

<details class="callout theorem" id="smooth-derivative-form" data-callout="theorem" open>
<summary class="callout-title">$f^{(n)}$ 一定是"多项式 $\times e^{-1/x}$"</summary>
<div class="callout-content" markdown="block">

$$f^{(n)}(x) = \begin{cases} P_n\!\left(\frac{1}{x}\right)e^{-\frac{1}{x}}, & x \gt{} 0 \\\\[4pt] 0, & x \le 0 \end{cases}$$

其中 $P_n$ 为多项式，$P_1(t) = t^{2}$，且

$$P_{n+1}(t) = t^{2}\left(P_n(t) - P_n'(t)\right)$$

</div>
</details>

**推导**：$f'(x) = e^{-\frac{1}{x}}\cdot\dfrac{1}{x^{2}}$，故 $P_1(t) = t^{2}$。一般地

$$f^{(n+1)}(x) = \left(P_n\!\left(\tfrac{1}{x}\right)e^{-\frac{1}{x}}\right)' = e^{-\frac{1}{x}}\left(\frac{1}{x^{2}}P_n\!\left(\tfrac{1}{x}\right) - \frac{1}{x^{2}}P_n'\!\left(\tfrac{1}{x}\right)\right)$$

令 $t = \dfrac{1}{x}$，即得 $P_{n+1}(t) = t^{2}\left(P_n(t) - P_n'(t)\right)$。

取极限：

$$\lim_{x \to 0^{+}} f^{(n)}(x) = \lim_{t \to +\infty} P_n(t)e^{-t} = 0$$

（多项式增长慢于指数：$t^{m}e^{-t} \to 0$。）

## 3 通项

<details class="callout formula" id="smooth-pn-formula" data-callout="formula" open>
<summary class="callout-title">$P_n$ 的通项</summary>
<div class="callout-content" markdown="block">

$$P_n(t) = \sum_{k=1}^{n}(-1)^{n-k}\binom{n-1}{k-1}\frac{n!}{k!}\,t^{n+k}$$

最高次为 $2n$，所以 $P_n\!\left(\frac{1}{x}\right)$ 可写成 $a_n\left(\frac{1}{x}\right)^{2n} + \cdots + a_1\left(\frac{1}{x}\right) + a_0$。

</div>
</details>

**验证**（对 $n$ 归纳）。设上式对 $n$ 成立，看 $P_{n+1}$ 中 $t^{n+1+k}$ 的系数。它有两个来源：

- $t^{2}P_n$ 的 $t^{n+(k-1)}$ 项：$(-1)^{n-k+1}\dbinom{n-1}{k-2}\dfrac{n!}{(k-1)!}$；
- $-t^{2}P_n'$ 的 $t^{n+k-1}$ 项：$-(n+k)(-1)^{n-k}\dbinom{n-1}{k-1}\dfrac{n!}{k!}$。

提出公因子 $(-1)^{n+1-k}\dfrac{n!}{k!}$，待证式化为

$$(n+k)\binom{n-1}{k-1} + k\binom{n-1}{k-2} = (n+1)\binom{n}{k-1}$$

右边用 Pascal 公式拆成 $(n+1)\left[\dbinom{n-1}{k-1} + \dbinom{n-1}{k-2}\right]$；左边用 $\dbinom{n-1}{k-1} = \dfrac{n-k+1}{k-1}\dbinom{n-1}{k-2}$ 统一成 $\dbinom{n-1}{k-2}$：

$$\left[(n+k)\frac{n-k+1}{k-1} + k\right]\binom{n-1}{k-2} = \frac{n(n+1)}{k-1}\binom{n-1}{k-2} = (n+1)\binom{n}{k-1}$$

（分子 $(n+k)(n-k+1) + k(k-1) = n(n+1)$。）

边界情形：$k = 1$ 时第二项取 $\dbinom{n-1}{-1} = 0$；$k = n+1$ 时第一项取 $\dbinom{n-1}{n} = 0$。

## 4 在 $x = 0$ 处的各阶导数

**证**：$f^{(n)}(0) = 0$ 对 $n$ 归纳。$n = 0$ 时 $f(0) = 0$。设 $f^{(n)}(0) = 0$，则

$$f^{(n+1)}(0) = \lim_{\Delta x \to 0}\frac{f^{(n)}(\Delta x) - f^{(n)}(0)}{\Delta x}$$

$\Delta x \lt{} 0$ 时 $f^{(n)}(\Delta x) = 0$，商为 $0$；$\Delta x \gt{} 0$ 时商为 $\dfrac{1}{\Delta x}P_n\!\left(\dfrac{1}{\Delta x}\right)e^{-\frac{1}{\Delta x}} = t\,P_n(t)e^{-t}$（$t = \frac{1}{\Delta x} \to +\infty$）。于是

$$\lim_{\Delta x \to 0^{+}}\frac{f^{(n)}(\Delta x) - f^{(n)}(0)}{\Delta x} = \lim_{t \to +\infty} t\,P_n(t)e^{-t} = 0$$

左右极限都是 $0$，故 $f^{(n+1)}(0) = 0$。归纳完毕：$f$ 在 $\mathbb{R}$ 上无穷次可导。

<details class="callout keypoint" id="smooth-nonconstant" data-callout="keypoint" open>
<summary class="callout-title">这里 $f^{(n)}$ 不是常值函数（相当好的性质）</summary>
<div class="callout-content" markdown="block">

$x \gt{} 0$ 上 $f^{(n)}(x) = P_n(1/x)e^{-1/x}$ 随 $x$ 变化，$P_n \not\equiv 0$。所以"各阶导在 $0$ 处都为 $0$"并不等于"各阶导恒为 $0$"。

</div>
</details>

## 5 泰勒展开

$f^{(n)}(0) = 0$ 对一切 $n$，所以 $f$ 在 $0$ 处的泰勒级数恒等于 $0$，而 $f$ 在 $x \gt{} 0$ 上并不为 $0$。

<details class="callout understand" data-callout="understand" open>
<summary class="callout-title">插个眼</summary>
<div class="callout-content" markdown="block">

不展开了，能力不够，插个眼先。

</div>
</details>

---

## 相关笔记

- 主线：[数学分析笔记](/notes/shu-xue-fen-xi-bi-ji/)
- 同期病态函数：[Thomae 函数的连续性](/notes/thomae-han-shu-de-lian-xu-xing/)
- 用到的求导法则：[[数学分析笔记#^derivative-rules|四则与链式]]
