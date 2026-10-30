---
layout: note
title: "分块矩阵性质"
slug: "fen-kuai-ju-zhen-xing-zhi"
permalink: "/notes/fen-kuai-ju-zhen-xing-zhi/"
public: false
generated_by: sync_notes.py
render_with_liquid: false
---

关于分块矩阵的秩有一些（并不）显然的性质

$$
\mathbf {r} \left[ \begin{array}{c c} A & B \\\\ C & D \end{array} \right] \geq \mathbf {r} (A)\tag{1}
$$

$$
\mathbf {r} \left[ \begin{array}{c c} A & 0 \\\\ C & B \end{array} \right] \geq \mathbf {r} \left[ \begin{array}{c c} A & 0 \\\\ 0 & B \end{array} \right]\tag{2}
$$

$$
\mathbf {r} \left[ \begin{array}{c c} A & O \\\\ O & B \end{array} \right] = \mathbf {r} (A) + \mathbf {r} (B)
$$

$$
\mathbf {r} \left[ \begin{array}{l l} 0 & A \\\\ B & 0 \end{array} \right] = \mathbf {r} (A) + \mathbf {r} (B)
$$

定理 (1) 设 $A$ 与 $B$ 是同型矩阵, 则

$$
\mathbf {r} (A + B) \leq \mathbf {r} (A) + \mathbf {r} (B);
$$

(2) 设 A 是 $s \times n$ 矩阵，B 是 $n \times t$ 矩阵，则

$$
\mathbf {r} (A B) \geq \mathbf {r} (A) + \mathbf {r} (B) - n.
$$

推论 设A是 $s \times n$ 矩阵，B是 $n \times t$ 矩阵。若 $AB=0$，则

$$
\mathbf {r} (A) + \mathbf {r} (B) \leq n.
$$

---

# 学生作业：分块矩阵秩的性质证明整理

## 性质 (3) 证明
**待证**：$\mathbf{r}\begin{bmatrix} A & O \\\\ O & B \end{bmatrix} = \mathbf{r}(A) + \mathbf{r}(B)$

**学生证明过程**：

1. 将 $A$ 化为等价标准型 $I_A$（即 $\begin{bmatrix} I_r & O \\\\ O & O \end{bmatrix}$），将 $B$ 化为等价标准型 $I_B$。
2. 通过初等变换，原矩阵可化为：
   
$$ \begin{bmatrix} I_A & 0 & 0 & 0 \\\\ 0 & 0 & 0 & 0 \\\\ 0 & 0 & I_B & 0 \\\\ 0 & 0 & 0 & 0 \end{bmatrix} $$

3. 该矩阵中非零行（列）的总数为 $\mathbf{r}(I_A) + \mathbf{r}(I_B)$，即 $\mathbf{r}(A) + \mathbf{r}(B)$。
4. 由于初等变换不改变矩阵的秩，故原等式成立。
   
$$ \mathbf{r}\begin{bmatrix} A & 0 \\\\ 0 & B \end{bmatrix} = \mathbf{r}(A) + \mathbf{r}(B) $$

---

## 性质 (4) 证明
**待证**：$\mathbf{r}\begin{bmatrix} 0 & A \\\\ B & 0 \end{bmatrix} = \mathbf{r}(A) + \mathbf{r}(B)$

**学生证明过程**：

1. 对原矩阵进行分块列交换（相当于右乘置换矩阵），得到：
   
$$ \mathbf{r}\begin{bmatrix} 0 & A \\\\ B & 0 \end{bmatrix} = \mathbf{r}\begin{bmatrix} A & 0 \\\\ 0 & B \end{bmatrix} $$

2. 利用**性质 (3)** 的结论直接得出：
   
$$ \mathbf{r}\begin{bmatrix} 0 & A \\\\ B & 0 \end{bmatrix} = \mathbf{r}(A) + \mathbf{r}(B) $$

---

## 性质 (2) 证明
**待证**：$\mathbf{r}\begin{bmatrix} A & 0 \\\\ C & B \end{bmatrix} \ge \mathbf{r}\begin{bmatrix} A & 0 \\\\ 0 & B \end{bmatrix}$

**学生证明过程**：

1. 同样将 $A, B$ 化为等价标准型 $I_A, I_B$。设此时矩阵化为：
   
$$ \begin{bmatrix} I_A & 0 & 0 & 0 \\\\ C_1 & I_B & C_2 & 0 \\\\ C_3 & 0 & C_4 & 0 \\\\ 0 & 0 & 0 & 0 \end{bmatrix} $$

2. **行变换消元**：利用 $I_A$ 和 $I_B$ 所在的行，通过分块初等行变换消去 $C_1, C_3$，得到：
   
$$ \begin{bmatrix} I_A & 0 & 0 & 0 \\\\ 0 & I_B & C_2 & 0 \\\\ 0 & 0 & C_4 & 0 \\\\ 0 & 0 & 0 & 0 \end{bmatrix} $$

3. **列变换消元**：利用 $I_B$ 所在的列，通过分块初等列变换消去 $C_2$，得到：
   
$$ \begin{bmatrix} I_A & 0 & 0 & 0 \\\\ 0 & I_B & 0 & 0 \\\\ 0 & 0 & C_4 & 0 \\\\ 0 & 0 & 0 & 0 \end{bmatrix} $$

4. **得出秩**：该矩阵的秩为 $\mathbf{r}(A) + \mathbf{r}(B) + \mathbf{r}(C_4)$。因为矩阵的秩是非负的（$\mathbf{r}(C_4) \ge 0$），所以：
   
$$ \mathbf{r}\begin{bmatrix} A & 0 \\\\ C & B \end{bmatrix} = \mathbf{r}(A) + \mathbf{r}(B) + \mathbf{r}(C_4) \ge \mathbf{r}(A) + \mathbf{r}(B) $$

5. 结合性质 (3) 中 $\mathbf{r}\begin{bmatrix} A & 0 \\\\ 0 & B \end{bmatrix} = \mathbf{r}(A) + \mathbf{r}(B)$，原不等式得证。
   *(学生笔记旁注：$C_4$ 化为相应标准型，额外多出的秩由 $C_4$ 贡献)*

---

## 性质 (1) 证明
**待证**：$\mathbf{r}\begin{bmatrix} A & B \\\\ C & D \end{bmatrix} \ge \mathbf{r}(A)$

**学生证明过程**：

1. 将左上角的 $A$ 化为等价标准型 $I_A$。此时原矩阵通过初等变换化为：
   
$$ \begin{bmatrix} I_A & 0 & 0 & 0 \\\\ 0 & 0 & B_3 & B_4 \\\\ C_1 & C_2 & D_1 & D_2 \\\\ C_3 & C_4 & D_3 & D_4 \end{bmatrix} $$

2. 观察该矩阵，其左上角包含非零子块 $I_A$。
3. 因此，整体矩阵的秩至少包含 $I_A$ 的秩。即：
   
$$ \mathbf{r}\begin{bmatrix} A & B \\\\ C & D \end{bmatrix} \ge \mathbf{r}(I_A) = \mathbf{r}(A) $$

4. 证毕。

---

### 📝 整理者注（关于学生证明的点评）

*   **性质 (3)(4)**：学生的证明非常干净利落，直接利用标准型得出秩相加，思路满分。
*   **性质 (2)**：这是学生证明中最精彩的部分。他敏锐地发现了化为标准型后，无法被消去的残余子块 $C_4$，从而完美解释了为何是“大于等于”而不是“等于”。
*   **性质 (1)**：学生图3的推导略显繁琐（试图展开所有的块进行初等变换），但其实核心逻辑就是“整体包含子块 $I_A$，所以整体秩 $\ge$ 子块秩”。建议可以直接用“矩阵的秩 $\ge$ 其任意子矩阵的秩”这一结论，或者用分块初等变换消去 $B, C$ 块的方法来简化证明。

# 分块矩阵秩性质的严谨证明

**预备知识（引理）**：

1. 设 $\mathbf{r}(A) = r$，则存在可逆矩阵 $P, Q$，使得 $PAQ = \begin{bmatrix} I_r & O \\\\ O & O \end{bmatrix}$。
2. 初等变换不改变矩阵的秩。即若 $P, Q$ 可逆，则 $\mathbf{r}(PAQ) = \mathbf{r}(A)$。
3. 矩阵的秩等于其非零行（列）的最大个数，且矩阵的秩具有非负性。

为了记号简便，以下证明中统一假设 $A, B$ 为零矩阵或维数相匹配的矩阵，并记 $\mathbf{r}(A) = r$，$\mathbf{r}(B) = s$。

---

## 性质 (3) 证明
**待证**：$\mathbf{r}\begin{bmatrix} A & O \\\\ O & B \end{bmatrix} = \mathbf{r}(A) + \mathbf{r}(B)$

**证明**：
由引理1，存在可逆矩阵 $P_1, Q_1$ 和 $P_2, Q_2$，使得：

$$ P_1 A Q_1 = \begin{bmatrix} I_r & O \\\\ O & O \end{bmatrix}, \quad P_2 B Q_2 = \begin{bmatrix} I_s & O \\\\ O & O \end{bmatrix} $$

令 $P = \begin{bmatrix} P_1 & O \\\\ O & P_2 \end{bmatrix}$，$Q = \begin{bmatrix} Q_1 & O \\\\ O & Q_2 \end{bmatrix}$，显然 $P, Q$ 均可逆。
对原矩阵进行分块初等变换：

$$ P \begin{bmatrix} A & O \\\\ O & B \end{bmatrix} Q = \begin{bmatrix} P_1 A Q_1 & O \\\\ O & P_2 B Q_2 \end{bmatrix} = \begin{bmatrix} I_r & O & O & O \\\\ O & O & O & O \\\\ O & O & I_s & O \\\\ O & O & O & O \end{bmatrix} $$

由于初等变换不改变矩阵的秩，且右侧矩阵的非零行（列）总数为 $r + s$，故：

$$ \mathbf{r}\begin{bmatrix} A & O \\\\ O & B \end{bmatrix} = r + s = \mathbf{r}(A) + \mathbf{r}(B) $$

**证毕。**

---

## 性质 (4) 证明
**待证**：$\mathbf{r}\begin{bmatrix} 0 & A \\\\ B & 0 \end{bmatrix} = \mathbf{r}(A) + \mathbf{r}(B)$

**证明**：
对原矩阵进行分块列交换（相当于右乘一个可逆的置换矩阵 $\begin{bmatrix} 0 & I \\\\ I & 0 \end{bmatrix}$）：

$$ \begin{bmatrix} 0 & A \\\\ B & 0 \end{bmatrix} \begin{bmatrix} 0 & I \\\\ I & 0 \end{bmatrix} = \begin{bmatrix} A & 0 \\\\ 0 & B \end{bmatrix} $$

因为初等变换不改变矩阵的秩，所以：

$$ \mathbf{r}\begin{bmatrix} 0 & A \\\\ B & 0 \end{bmatrix} = \mathbf{r}\begin{bmatrix} A & 0 \\\\ 0 & B \end{bmatrix} $$

结合**性质 (3)** 的结论，直接可得：

$$ \mathbf{r}\begin{bmatrix} 0 & A \\\\ B & 0 \end{bmatrix} = \mathbf{r}(A) + \mathbf{r}(B) $$

**证毕。**

---

## 性质 (2) 证明
**待证**：$\mathbf{r}\begin{bmatrix} A & 0 \\\\ C & B \end{bmatrix} \ge \mathbf{r}\begin{bmatrix} A & 0 \\\\ 0 & B \end{bmatrix}$

**证明**：
同性质(3)，利用可逆矩阵 $P, Q$ 将 $A, B$ 化为等价标准型。此时原矩阵化为：

$$ \begin{bmatrix} I_r & O & O & O \\\\ O & O & O & O \\\\ C_1 & C_2 & I_s & O \\\\ C_3 & C_4 & O & O \end{bmatrix} $$

利用分块初等变换（行变换消去 $C_1, C_2, C_3$，列变换消去 $C_2$），将矩阵进一步化简为：

$$ \begin{bmatrix} I_r & O & O & O \\\\ O & I_s & O & O \\\\ O & O & C_4 & O \\\\ O & O & O & O \end{bmatrix} $$

该矩阵的秩为 $r + s + \mathbf{r}(C_4)$。
由于矩阵的秩具有非负性，即 $\mathbf{r}(C_4) \ge 0$，因此：

$$ \mathbf{r}\begin{bmatrix} A & 0 \\\\ C & B \end{bmatrix} = \mathbf{r}(A) + \mathbf{r}(B) + \mathbf{r}(C_4) \ge \mathbf{r}(A) + \mathbf{r}(B) $$

又由性质(3)知 $\mathbf{r}\begin{bmatrix} A & 0 \\\\ 0 & B \end{bmatrix} = \mathbf{r}(A) + \mathbf{r}(B)$，故原不等式得证。
**证毕。**
*(注：当且仅当 $C_4 = O$ 时，等号成立。)*

---

## 性质 (1) 证明
**待证**：$\mathbf{r}\begin{bmatrix} A & B \\\\ C & D \end{bmatrix} \ge \mathbf{r}(A)$

**证明**（化标准型法）：
设 $P_1, Q_1$ 为可逆矩阵，使得 $P_1 A Q_1 = \begin{bmatrix} I_r & O \\\\ O & O \end{bmatrix}$。
构造可逆分块矩阵 $P = \begin{bmatrix} P_1 & O \\\\ O & I \end{bmatrix}$，$Q = \begin{bmatrix} Q_1 & O \\\\ O & I \end{bmatrix}$。
对原矩阵进行分块初等变换：

$$ P \begin{bmatrix} A & B \\\\ C & D \end{bmatrix} Q = \begin{bmatrix} P_1 A Q_1 & P_1 B \\\\ C Q_1 & D \end{bmatrix} = \begin{bmatrix} I_r & O & B_1 \\\\ O & O & B_2 \\\\ C_1 & C_2 & D \end{bmatrix} $$

观察变换后的矩阵，其左上角包含一个 $r$ 阶单位阵 $I_r$，这意味着该矩阵中至少存在 $r$ 个线性无关的行（或列）。
因此，变换后矩阵的秩至少为 $r$。由初等变换不改变矩阵的秩可知：

$$ \mathbf{r}\begin{bmatrix} A & B \\\\ C & D \end{bmatrix} \ge r = \mathbf{r}(A) $$

**证毕。**
*(另解：矩阵的任意子矩阵的秩不超过原矩阵的秩，而 $A$ 是原矩阵的子矩阵，故直接可得结论。)*