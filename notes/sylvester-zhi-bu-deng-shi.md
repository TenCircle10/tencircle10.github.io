---
layout: note
title: "Sylvester 秩不等式"
slug: "sylvester-zhi-bu-deng-shi"
permalink: "/notes/sylvester-zhi-bu-deng-shi/"
public: false
generated_by: sync_notes.py
render_with_liquid: false
---

可以证明分块矩阵的秩有如下的性质:

(1) 

$$
\mathrm{r} \left(\left[ \begin{array}{l l} A & B \\\\ C & D \end{array} \right]\right) \geqslant \mathrm{r} (A), \quad \mathrm{r} \left(\left[ \begin{array}{l l} A & 0 \\\\ C & B \end{array} \right]\right) \geqslant \mathrm{r} \left(\left[ \begin{array}{l l} A & 0 \\\\ 0 & B \end{array} \right]\right);\tag{1.6.1}
$$

(2) 

$$
\mathrm{r} \left(\left[ \begin{array}{c c} {\boldsymbol {A}} & {\boldsymbol {0}} \\\\ {\boldsymbol {0}} & {\boldsymbol {B}} \end{array} \right]\right) = \mathrm{r} \left(\left[ \begin{array}{c c} {\boldsymbol {0}} & {\boldsymbol {A}} \\\\ {\boldsymbol {B}} & {\boldsymbol {0}} \end{array} \right]\right) = \mathrm{r} (\boldsymbol {A}) + \mathrm{r} (\boldsymbol {B});\tag{1.6.2}
$$

(3) 若 A, B 都满秩, 则分块矩阵 $\begin{bmatrix} A & 0 \\\\ C & B \end{bmatrix}$ , $\begin{bmatrix} A & C \\\\ 0 & B \end{bmatrix}$ 都满秩.
利用上述性质及定理1.6.1以及推论1.6.2,可以证明下面的重要结论.
定理 1.6.2 (1) 设 A、B 是两个同型矩阵, 则

$$
\mathrm{r} (\boldsymbol {A} + \boldsymbol {B}) \leqslant \mathrm{r} (\boldsymbol {A}) + \mathrm{r} (\boldsymbol {B});
$$

(2) 设 A 是 $s \times n$ 矩阵, B 是 $n \times t$ 矩阵, 则

$$
\mathrm{r} (\boldsymbol {A B}) \geqslant \mathrm{r} (\boldsymbol {A}) + \mathrm{r} (\boldsymbol {B}) - n.
$$

证 (1) 构造如下分块矩阵并对其作分块初等变换:

$$
\left[ \begin{array}{c c} {\boldsymbol {A}} & {\boldsymbol {0}} \\\\ {\boldsymbol {0}} & {\boldsymbol {B}} \end{array} \right] \xrightarrow {R _ {1} + R _ {2}} \left[ \begin{array}{c c} {\boldsymbol {A}} & {\boldsymbol {B}} \\\\ {\boldsymbol {0}} & {\boldsymbol {B}} \end{array} \right] \xrightarrow {C _ {1} + C _ {2}} \left[ \begin{array}{c c} {\boldsymbol {A} + \boldsymbol {B}} & {\boldsymbol {B}} \\\\ {\boldsymbol {B}} & {\boldsymbol {B}} \end{array} \right],
$$

由(1.6.2)式、推论1.6.2以及(1.6.1)式可得

$$
\mathrm{r} (A) + \mathrm{r} (B) = \mathrm{r} \left(\left[ \begin{array}{c c} A & 0 \\\\ 0 & B \end{array} \right]\right) = \mathrm{r} \left(\left[ \begin{array}{c c} A + B & B \\\\ B & B \end{array} \right]\right) \geqslant \mathrm{r} (A + B).
$$

(2) 构造如下分块矩阵并对其作分块初等变换:

$$
\left[ \begin{array}{c c} A & 0 \\\\ - I _ {n} & B \end{array} \right] \xrightarrow {R _ {1} + A R _ {2}} \left[ \begin{array}{c c} 0 & A B \\\\ - I _ {n} & B \end{array} \right] \xrightarrow {C _ {2} + C _ {1} B} \left[ \begin{array}{c c} 0 & A B \\\\ - I _ {n} & 0 \end{array} \right],
$$

由(1.6.2)式、推论1.6.2以及(1.6.1)式可得

$$
\mathrm{r} (\boldsymbol {A B}) + \mathrm{r} (- \boldsymbol {I} _ {n}) = \mathrm{r} \left(\left[ \begin{array}{c c} {\mathbf {0}} & {\boldsymbol {A B}} \\\\ {- \boldsymbol {I} _ {n}} & {\mathbf {0}} \end{array} \right]\right) = \mathrm{r} \left(\left[ \begin{array}{c c} {\boldsymbol {A}} & {\mathbf {0}} \\\\ {- \boldsymbol {I} _ {n}} & {\boldsymbol {B}} \end{array} \right]\right) \geqslant \mathrm{r} (\boldsymbol {A}) + \mathrm{r} (\boldsymbol {B}).
$$

即

$$
\mathrm{r} (\boldsymbol {A B}) \geqslant \mathrm{r} (\boldsymbol {A}) + \mathrm{r} (\boldsymbol {B}) - n.
$$

推论 1.6.3 设 A 是 $s \times n$ 矩阵, B 是 $n \times t$ 矩阵. 若 AB = 0, 则

$$
\mathrm{r} (\boldsymbol {A}) + \mathrm{r} (\boldsymbol {B}) \leqslant n.
$$

这是 Sylvester 秩不等式。设数域为 $\mathbb{F}$，下面给出一个**线性映射**版本的证明。

把矩阵看成线性映射：设

$$\varphi:\mathbb{F}^{t}\to \mathbb{F}^{n},\quad x\mapsto Bx, \qquad \psi:\mathbb{F}^{n}\to \mathbb{F}^{s},\quad y\mapsto Ay$$

则 $AB$ 对应复合映射 $\psi\circ\varphi:\mathbb{F}^{t}\to\mathbb{F}^{s}$。令 $U=\operatorname{Im}\varphi=\operatorname{Im}B$，则 $r(AB)=\dim\psi(U)$。由秩—零化度定理，

$$r(AB)=\dim U-\dim(U\cap\ker\psi)=r(B)-\dim(\operatorname{Im}B\cap\ker A)$$

又因为 $\operatorname{Im}B\cap\ker A\subseteq \ker A$，所以

$$\dim(\operatorname{Im}B\cap\ker A)\le \dim\ker A=n-r(A)$$

代回得 $r(AB)\ge r(B)-(n-r(A))=r(A)+r(B)-n$，即

$$\boxed{\,r(AB)\ge r(A)+r(B)-n\,}$$

几何意义：$B$ 的像空间落进 $A$ 的核空间的部分最多只有 $\dim\ker A=n-r(A)$ 维，因此复合映射损失的秩不超过 $n-r(A)$。

---

## 相关笔记

- 主线：[[线性代数笔记#^rank-further|秩的进一步结论]]
- 姊妹结论：[分块矩阵性质](/notes/fen-kuai-ju-zhen-xing-zhi/)、[子母矩阵秩的大小关系](/notes/zi-mu-ju-zhen-zhi-de-da-xiao-guan-xi/)
