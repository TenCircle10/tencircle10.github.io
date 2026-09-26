---
layout: note
title: 数学分析 by TenCircle10
permalink: /notes/mathematical-analysis-szy/
---



思考：无穷小分析

**集合**：
*   互异性（可表示为相同元素但不重复计入，e.g.$\{1,2,1,2\}=\{1,2\}$）
*   无序性
*   确定性

**例子**：
*   $1 \in \{1\}$
*   $1 \neq \{1\}$
*   $\varnothing \subset A$ (A可以为空)

**性质**：
*   $A \subset B, B \subset C \Rightarrow A \subset C$
*   $A=B \Leftrightarrow A \subset B \text{ 且 } B \subset A$

**集合运算**：
*   $A \cap B$ 交
*   $A \cup B$ 并
*   $A \setminus B$ 差 $\{x | x \in A \text{ 且 } x \notin B\}$
*   $A^c$ 补 (相对于全集 $X$)

**运算律**：
*   交换
*   分配
*   结合

**德摩根律 (de Morgan)**：
*   $(A \cup B)^c = A^c \cap B^c$
*   $(A \cap B)^c = A^c \cup B^c$

**笛卡尔积 (Descartes)**：
*   $A \times B = \{(x, y) | x \in A, y \in B\}$

---

**数集对运算的封闭性**：
*   $\mathbb{N}$ 对于 $+ \times$ 封闭，对 $- \div$ 不封闭
*   $\mathbb{Z}$ 对于 $+ - \times$ 封闭
*   $\mathbb{Q}$ 对于 $+ - \times \div$ 封闭
*   $\mathbb{R}$
*   $\mathbb{C}$

**数域定义**：
① 对 $+ - \times \div$ 封闭
② 满足交换、结合、分配律
$\Rightarrow$ 数域

**有序域**：
*   有大小关系，加法可传递 / 乘法 $\Rightarrow$ 有序域

**可列集定义**：
若一个无限集中元素可以按某种规律排成一个序列，即这个集合可表为 $\{a_1, a_2, \dots, a_n, \dots\}$

> [!note] 定理 1.0.1
>  可列个可列集之并也是可列集。
^f0fbb3

**证明思路（记）**：
记 $A_n = \{a_{n1}, a_{n2}, \dots, a_{nk}, \dots\}$
$\displaystyle \bigcup_{n=1}^{\infty} A_n = \{a_{11}, a_{21}, a_{12}, a_{31}, a_{22}, a_{13}, \dots\}$
沿对角线方向取
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


---

**$\mathbb{Q}$ 为可列集**：

记 $A_n = [n, n+1] \cap \mathbb{Q}, n \in \mathbb{Z}$，则 $$\bigcup_{n \in \mathbb{Z}} A_n = \mathbb{Q}$$由[[#^f0fbb3|定理1.0.1]]，只需证 $A_0$ 可列。
$A_0 = \{0, 1, \frac{1}{2}, \frac{1}{3}, \frac{2}{3}, \frac{1}{4}, \dots, \frac{k-1}{k}, \dots\}$
$\Rightarrow \mathbb{Q}$ 可列。

**注意点**：
*   所有可列集的元素个数相同，见[[无限可列集等势证明]]
*   有理数集与无理数集均具有稠密性
$f: A \to B$，A, B 有限集
*  无理数为何不可列?见[[实数集与无理数集不可列证明]]
**完备性**：
*   完备：对极限封闭。

**实数与极限**：
*   $x_n = m + 0.a_1a_2\dots a_n$
*   $0 \le x - x_n < \frac{1}{10^n}$
*   任何一个无理数是一个有理数列的极限。
*   $\sqrt{2} = 1.4\dots$

**上下界**：
*   有上界就有无限上界
*   上确界（最小上界）：
    $\alpha$ 是 $S$ 的上界；若 $\beta < \alpha$，则 $\beta$ 不为 $S$ 的上界。
    记为 $\alpha = \sup S$
*   下确界（最大下界）：
    记为 $\beta = \inf S$

---

*   数列是可列有序数组。
*   单调增：$x_n \le x_{n+1}$
*   $\{x_n\}$ 有上界、下界 $\Leftrightarrow$ $\{x_n\}$ 有界

**证明（单调有界定理相关证明思路）**：
设 $x_n$ 的小数...
$x_n = m_n + 0.a_1^{(n)}a_2^{(n)}\dots$
当上一位不再变化，下一位必从 $\{0, 1, \dots, 9\}$ 中取。
