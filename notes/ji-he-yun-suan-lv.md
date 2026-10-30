---
layout: note
title: "集合运算律"
slug: "ji-he-yun-suan-lv"
permalink: "/notes/ji-he-yun-suan-lv/"
public: false
generated_by: sync_notes.py
render_with_liquid: false
---

设 $A,B,C\subseteq U$，$A^c$ 表示 $A$ 在全集 $U$ 中的补集，$\varnothing$ 为空集。

### 1. 交换律

$$
A\cup B=B\cup A,\qquad A\cap B=B\cap A,\qquad A\triangle B=B\triangle A
$$

### 2. 结合律

$$
(A\cup B)\cup C=A\cup(B\cup C)
$$

$$
(A\cap B)\cap C=A\cap(B\cap C)
$$

$$
(A\triangle B)\triangle C=A\triangle(B\triangle C)
$$

### 3. 分配律

$$
A\cup(B\cap C)=(A\cup B)\cap(A\cup C)
$$

$$
A\cap(B\cup C)=(A\cap B)\cup(A\cap C)
$$

$$
A\cap(B\triangle C)=(A\cap B)\triangle(A\cap C)
$$

### 4. 幂等律

$$
A\cup A=A,\qquad A\cap A=A
$$

### 5. 吸收律

$$
A\cup(A\cap B)=A,\qquad A\cap(A\cup B)=A
$$

常用推论：

$$
A\cup(A^c\cap B)=A\cup B,\qquad A\cap(A^c\cup B)=A\cap B
$$

### 6. 同一律与零律

$$
A\cup\varnothing=A,\qquad A\cap U=A
$$

$$
A\cup U=U,\qquad A\cap\varnothing=\varnothing
$$

### 7. 补集律

$$
A\cup A^c=U,\qquad A\cap A^c=\varnothing
$$

$$
(A^c)^c=A,\qquad U^c=\varnothing,\qquad \varnothing^c=U
$$

### 8. 德摩根律

$$
(A\cup B)^c=A^c\cap B^c
$$

$$
(A\cap B)^c=A^c\cup B^c
$$

一般形式：

$$
\left(\bigcup_{i\in I}A_i\right)^c=\bigcap_{i\in I}A_i^c,\qquad
\left(\bigcap_{i\in I}A_i\right)^c=\bigcup_{i\in I}A_i^c
$$

### 9. 差集常用恒等式

$$
A\setminus B=A\cap B^c
$$

$$
A\setminus(B\cup C)=(A\setminus B)\cap(A\setminus C)
$$

$$
A\setminus(B\cap C)=(A\setminus B)\cup(A\setminus C)
$$

$$
(A\cup B)\setminus C=(A\setminus C)\cup(B\setminus C)
$$

$$
(A\cap B)\setminus C=(A\setminus C)\cap(B\setminus C)
$$

### 10. 对称差常用恒等式

$$
A\triangle B=(A\setminus B)\cup(B\setminus A)=(A\cup B)\setminus(A\cap B)
$$

$$
A\triangle\varnothing=A,\qquad A\triangle U=A^c,\qquad A\triangle A=\varnothing
$$

$$
A\triangle B^c=(A\triangle B)^c
$$

### 11. 子集等价关系

$$
A\subseteq B
\iff A\cup B=B
\iff A\cap B=A
\iff A\setminus B=\varnothing
$$

这些运算律与布尔代数中的运算律一致，其中并 $\cup$ 对应“或”，交 $\cap$ 对应“且”，补 $^c$ 对应“非”。