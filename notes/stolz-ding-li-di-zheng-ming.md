---
layout: note
title: "Stolz定理的证明"
slug: "stolz-ding-li-di-zheng-ming"
permalink: "/notes/stolz-ding-li-di-zheng-ming/"
public: false
render_with_liquid: false
---

## Stolz 定理（施托尔茨定理）
**1. ∞/∞ 型**
设数列 $\lbrace{}b_n\rbrace{}$ 严格单调递增，且 $\lim_{n \to \infty} b_n = +\infty$。
若差商极限存在：

$$
\lim_{n \to \infty} \frac{a_{n+1} - a_n}{b_{n+1} - b_n} = L
$$

则原商极限也存在，且相等：

$$
\lim_{n \to \infty} \frac{a_n}{b_n} = L
$$

其中 $L$ 可以是有限实数，也可以是 $+\infty$ 或 $-\infty$。

---

**2. 0/0 型**
设 $a_n \to 0$，$b_n \to 0$，且 $\lbrace{}b_n\rbrace{}$ 严格单调（从而 $b_{n+1} - b_n \neq 0$）。
若差商极限存在：

$$
\lim_{n \to \infty} \frac{a_{n+1} - a_n}{b_{n+1} - b_n} = L
$$

则原商极限也存在，且相等：

$$
\lim_{n \to \infty} \frac{a_n}{b_n} = L
$$

其中 $L$ 可以是有限实数，也可以是 $+\infty$ 或 $-\infty$。

---

### 第一个证明：∞/∞ 型

$$
\Delta a_n = a_n - a_{n-1}
$$

定义 $a_0 = 0$

$$
\Delta b_n = b_n - b_{n-1}, \quad b_0 = 0
$$

$$
\exists N, \forall \varepsilon \gt{} 0, n \gt{} N, \left| \frac{\Delta a_n}{\Delta b_n} - L \right| \lt{} \varepsilon
$$

$$
a_n = \sum_{k=1}^n \Delta a_k
$$

$$
= \sum_{k=1}^N \Delta a_k + \sum_{k=N+1}^n \Delta a_k
$$

$$
= \sum_{k=N+1}^n \frac{\Delta a_k}{\Delta b_k} \Delta b_k + \sum_{k=1}^N \Delta a_k
$$

由 $\left\vert \frac{\Delta a_k}{\Delta b_k} - L \right\vert \lt{} \varepsilon$ 得：

$$
(L-\varepsilon)\Delta b_k \lt{} \Delta a_k \lt{} (L+\varepsilon)\Delta b_k
$$

$$
\sum_{k=N+1}^n (L-\varepsilon)\Delta b_k + a_N \lt{} a_n \lt{} \sum_{k=N+1}^n (L+\varepsilon)\Delta b_k + a_N
$$

$$
(L-\varepsilon)(b_n - b_N) + a_N \lt{} a_n \lt{} (L+\varepsilon)(b_n - b_N) + a_N
$$

两边除以 $b_n$（$b_n \to \infty$，故 $b_n \gt{} 0$）：

$$
\frac{(L-\varepsilon)(b_n - b_N)}{b_n} + \frac{a_N}{b_n} \lt{} \frac{a_n}{b_n} \lt{} \frac{(L+\varepsilon)(b_n - b_N)}{b_n} + \frac{a_N}{b_n}
$$

整理：

$$
(L-\varepsilon) - \frac{(L-\varepsilon)b_N}{b_n} + \frac{a_N}{b_n} \lt{} \frac{a_n}{b_n} \lt{} (L+\varepsilon) - \frac{(L+\varepsilon)b_N}{b_n} + \frac{a_N}{b_n}
$$

取极限（当 $n \to \infty$ 时，$\frac{1}{b_n} \to 0$）：

$$
L-\varepsilon \le \liminf_{n \to \infty} \frac{a_n}{b_n} \le \limsup_{n \to \infty} \frac{a_n}{b_n} \le L+\varepsilon
$$

由 $\varepsilon$ 的任意性，得：

$$
\lim_{n \to \infty} \frac{a_n}{b_n} = L
$$

---

### 第二个证明：0/0 型
已知 $a_n \to 0$，$b_n \to 0$（不妨设 $b_n$ 严格单调递减趋于 0，此时 $b_n \gt{} 0$，且 $b_k - b_{k+1} \gt{} 0$）。

$$
\Delta a_n = a_n - a_{n-1}
$$

定义 $a_0 = 0$

$$
\Delta b_n = b_n - b_{n-1}, \quad b_0 = 0
$$

$$
\exists N, \forall \varepsilon \gt{} 0, n \gt{} N, \left| \frac{\Delta a_n}{\Delta b_n} - L \right| \lt{} \varepsilon
$$

由于 $a_n \to 0$，把 $a_n$ 写成从 $n$ 开始的后缀和：

$$
a_n = a_n - a_\infty = \sum_{k=n}^{\infty} (a_k - a_{k+1})
$$

$$
= \sum_{k=n}^{\infty} \frac{a_k - a_{k+1}}{b_k - b_{k+1}} (b_k - b_{k+1})
$$

注意：

$$
\frac{a_k - a_{k+1}}{b_k - b_{k+1}} = \frac{a_{k+1} - a_k}{b_{k+1} - b_k} = \frac{\Delta a_{k+1}}{\Delta b_{k+1}}
$$

故当 $n \gt{} N$ 时，求和下标 $k \ge n \gt{} N$，有：

$$
L-\varepsilon \lt{} \frac{a_k - a_{k+1}}{b_k - b_{k+1}} \lt{} L+\varepsilon
$$

于是：

$$
(L-\varepsilon) \sum_{k=n}^{\infty} (b_k - b_{k+1}) \lt{} a_n \lt{} (L+\varepsilon) \sum_{k=n}^{\infty} (b_k - b_{k+1})
$$

而：

$$
\sum_{k=n}^{\infty} (b_k - b_{k+1}) = b_n - b_\infty = b_n
$$

所以：

$$
(L-\varepsilon) b_n \lt{} a_n \lt{} (L+\varepsilon) b_n
$$

两边除以 $b_n$（$b_n \gt{} 0$）：

$$
L-\varepsilon \lt{} \frac{a_n}{b_n} \lt{} L+\varepsilon
$$

由 $\varepsilon$ 的任意性，得：

$$
\lim_{n \to \infty} \frac{a_n}{b_n} = L
$$
