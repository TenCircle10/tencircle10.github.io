---
layout: note
title: "子母矩阵秩的大小关系"
slug: "zi-mu-ju-zhen-zhi-de-da-xiao-guan-xi"
permalink: "/notes/zi-mu-ju-zhen-zhi-de-da-xiao-guan-xi/"
public: false
generated_by: sync_notes.py
render_with_liquid: false
---

29. 设 $A = [a_{ij}]&#95;{m \times n}$ , 令

$$
\boldsymbol {B} = \left[ \begin{array}{c c c c} a _ {i _ {1} j _ {1}} & a _ {i _ {1} j _ {2}} & \dots & a _ {i _ {1} j _ {t}} \\\\ a _ {i _ {2} j _ {1}} & a _ {i _ {2} j _ {2}} & \dots & a _ {i _ {2} j _ {t}} \\\\ \vdots & \vdots & & \vdots \\\\ a _ {i _ {s} j _ {1}} & a _ {i _ {s} j _ {2}} & \dots & a _ {i _ {s} j _ {t}} \end{array} \right],
$$

其中 $1 \leqslant i_{1} \lt{} i_{2} \lt{} \cdots \lt{} i_{s} \leqslant m, 1 \leqslant j_{1} \lt{} j_{2} \lt{} \cdots \lt{} j_{t} \leqslant n,$ 即 $\boldsymbol {B}$ 是 $\boldsymbol {A}$ 的一个 $s \times t$ 子矩阵. 证明: $\mathrm{r}(B) \leqslant \mathrm{r}(A)$ .

证明 通过互换行和互换列, 把 A 化为 $A'$ , 使 B 位于 $A'$ 的左上角:

$$
\boldsymbol {A} \longrightarrow \boldsymbol {A} ^ {\prime} = \left[ \begin{array}{c c c c} a _ {i _ {1} j _ {1}} & \dots & a _ {i _ {1} j _ {t}} & \dots \\\\ \vdots & & \vdots \\\\ a _ {i _ {s} j _ {1}} & \dots & a _ {i _ {s} j _ {t}} & \dots \\\\ \vdots & & \vdots \end{array} \right]
$$

根据把 B 化为相抵标准形的过程, 对 $A'$ 进行初等变换, 并进一步化为 $B'$ :

$$
\boldsymbol {B} ^ {\prime} = \left[ \begin{array}{c c c c c c c c c} 1 & \dots & 0 & 0 & \dots & 0 & 0 & \dots & 0 \\\\ \vdots & & \vdots & \vdots & & \vdots & \vdots & & \vdots \\\\ 0 & \dots & 1 & 0 & \dots & 0 & 0 & \dots & 0 \\\\ 0 & \dots & 0 & 0 & \dots & 0 & b _ {1 1} & \dots & b _ {1 t _ {1}} \\\\ \vdots & & \vdots & \vdots & & \vdots & \vdots & & \vdots \\\\ 0 & \dots & 0 & 0 & \dots & 0 & b _ {s _ {1} 1} & \dots & b _ {s _ {1} t _ {1}} \\\\ 0 & \dots & 0 & c _ {1 1} & \dots & c _ {1 t _ {2}} & d _ {1 1} & \dots & d _ {1 t _ {1}} \\\\ \vdots & & \vdots & \vdots & & \vdots & \vdots & & \vdots \\\\ 0 & \dots & 0 & c _ {s _ {2} 1} & \dots & c _ {s _ {2} t _ {2}} & d _ {s _ {2} 1} & \dots & d _ {s _ {2} t _ {1}} \end{array} \right] r \text {行}
$$

其中 $r = \mathrm{r}(\pmb{B})$ 

根据引理的结论, 可知

$$
\mathrm{r} \left(\boldsymbol {B} ^ {\prime}\right) = \mathrm{r} \left[ \begin{array}{l l l l} 1 & 0 & \dots & 0 \\\\ 0 & 1 & \dots & 0 \\\\ \vdots & \vdots & & \vdots \\\\ 0 & 0 & \dots & 1 \end{array} \right] + \mathrm{r} \left[ \begin{array}{c c c c c c} 0 & \dots & 0 & b _ {1 1} & \dots & b _ {1 t _ {1}} \\\\ \vdots & & \vdots & \vdots & & \vdots \\\\ 0 & \dots & 0 & b _ {s _ {1} 1} & \dots & b _ {s _ {1} t _ {1}} \\\\ c _ {1 1} & \dots & c _ {1 t _ {2}} & d _ {1 1} & \dots & d _ {1 t _ {1}} \\\\ \vdots & & \vdots & \vdots & & \vdots \\\\ c _ {s _ {2} 1} & \dots & c _ {s _ {2} t _ {2}} & d _ {s _ {2} 1} & \dots & d _ {s _ {2} t _ {1}} \end{array} \right]
$$

$$
\geqslant r (I _ {r}) = r
$$

于是

$$
\mathrm{r} (\boldsymbol {A}) = \mathrm{r} (\boldsymbol {A} ^ {\prime}) = \mathrm{r} (\boldsymbol {B} ^ {\prime}) \geqslant r = \mathrm{r} (\boldsymbol {B})
$$

---

<details class="callout note" data-callout="note" open>
<summary class="callout-title">引理</summary>
<div class="callout-content" markdown="block">

设 $A$ 与 $B$ 是两个任意矩阵，证明：

$$
\mathrm{r}\left(\left[\begin{array}{cc}
\boldsymbol{A} & \boldsymbol{0}\\\\
\boldsymbol{0} & \boldsymbol{B}
\end{array}\right]\right)
= \mathrm{r}(\boldsymbol{A})+\mathrm{r}(\boldsymbol{B}); \tag{1}
$$

（2）

$$
\mathrm{r}\left(\left[\begin{array}{ll}
A & C\\\\
0 & B
\end{array}\right]\right)
\geqslant \mathrm{r}(A)+\mathrm{r}(B),
$$

其中 $C$ 是任一个满足分块要求的矩阵。

</div>
</details>

证明 设 $\mathbf{r}(\mathbf{A}) = r, \mathbf{r}(\mathbf{B}) = s$ .

先证第一式:由假设,A、B可分别用初等变换化为相抵标准形

$$
A \longrightarrow \left[ \begin{array}{l l} I _ {r} & 0 \\\\ 0 & 0 \end{array} \right], B \longrightarrow \left[ \begin{array}{l l} I _ {s} & 0 \\\\ 0 & 0 \end{array} \right]
$$

对分块矩阵

$$
\left[ \begin{array}{c c} \boldsymbol {A} & \boldsymbol {0} \\\\ \boldsymbol {0} & \boldsymbol {B} \end{array} \right]
$$

作相同的初等变换可得

$$
\left[ \begin{array}{l l} A & 0 \\\\ 0 & B \end{array} \right] \longrightarrow \left[ \begin{array}{c c c c} I _ {r} & 0 & 0 & 0 \\\\ 0 & 0 & 0 & 0 \\\\ 0 & 0 & I _ {r} & 0 \\\\ 0 & 0 & 0 & 0 \end{array} \right]
$$

$$
\longrightarrow \left[ \begin{array}{c c c c} I _ {r} & 0 & 0 & 0 \\\\ 0 & I _ {s} & 0 & 0 \\\\ 0 & 0 & 0 & 0 \\\\ 0 & 0 & 0 & 0 \end{array} \right] = \left[ \begin{array}{c c} I _ {r + s} & 0 \\\\ 0 & 0 \end{array} \right]
$$

最后一个矩阵是相抵标准形,秩为 $r + s$ ,于是由此得

$$
\mathrm{r} \left[ \begin{array}{c c} \boldsymbol {A} & \boldsymbol {0} \\\\ \boldsymbol {0} & \boldsymbol {B} \end{array} \right] = r + s = \mathrm{r} (\boldsymbol {A}) + \mathrm{r} (\boldsymbol {B})
$$

再证第二式:利用前面的假设,作初等变换

$$
\begin{array}{r l} & {\left[ \begin{array}{l l} A & C \\\\ 0 & B \end{array} \right] \longrightarrow \left[ \begin{array}{l l l l} I _ {r} & 0 & C _ {1} & C _ {2} \\\\ 0 & 0 & C _ {3} & C _ {4} \\\\ 0 & 0 & I _ {s} & 0 \\\\ 0 & 0 & 0 & 0 \end{array} \right]} \\\\ & {\longrightarrow \left[ \begin{array}{l l l l} I _ {r} & 0 & 0 & 0 \\\\ 0 & 0 & 0 & C _ {4} \\\\ 0 & 0 & I _ {s} & 0 \\\\ 0 & 0 & 0 & 0 \end{array} \right] \longrightarrow \left[ \begin{array}{l l l l} I _ {r} & 0 & 0 & 0 \\\\ 0 & I _ {s} & 0 & 0 \\\\ 0 & 0 & C _ {4} & 0 \\\\ 0 & 0 & 0 & 0 \end{array} \right]} \end{array}
$$

利用第一式可得

$$
\begin{array}{r l} \mathrm{r} \left[ \begin{array}{c c} \boldsymbol {A} & \boldsymbol {C} \\\\ \boldsymbol {0} & \boldsymbol {B} \end{array} \right] & = \mathrm{r} (\boldsymbol {I} _ {r}) + \mathrm{r} (\boldsymbol {I} _ {s}) + \mathrm{r} (\boldsymbol {C} _ {4}) \\\\ & \geqslant r + s = \mathrm{r} (\boldsymbol {A}) + \mathrm{r} (\boldsymbol {B}) = \mathrm{r} \left[ \begin{array}{c c} \boldsymbol {A} & \boldsymbol {0} \\\\ \boldsymbol {0} & \boldsymbol {B} \end{array} \right] \end{array}
$$

矩阵分块是实现矩阵运算和研究矩阵性质的重要工具,在很多情况下它已成为解决问题的关键.因此,在学有余力的情况下,应努力掌握分块矩阵的有关知识.

在引理例 15 中, 多次用到求矩阵的相抵标准形, 其中往往既用到矩阵的初等行变换, 也要用到初等列变换. 然而在处理求矩阵的秩、求可逆矩阵的逆矩阵以及解线性方程组时, 只用初等行变换即可达到目的, 并且解方程组更是只允许用行变换. 所以, 为了正确使用初等变换和便于记忆, 除了求相抵标准形外, 在其他场合可要求只使用初等行变换.

