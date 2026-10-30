---
layout: note
title: "∑求和运算律"
slug: "qiu-he-yun-suan-lv"
permalink: "/notes/qiu-he-yun-suan-lv/"
public: false
generated_by: sync_notes.py
render_with_liquid: false
---

求和符号 $\sum$（Sigma）的运算律，常见如下。

### 1. 定义

$$
\sum_{i=m}^{n} a_i=a_m+a_{m+1}+\cdots+a_n
$$

### 2. 线性律

$$
\sum_{i=1}^{n}(\alpha a_i+\beta b_i)
=
\alpha\sum_{i=1}^{n}a_i+\beta\sum_{i=1}^{n}b_i
$$

特别地：

$$
\sum_{i=1}^{n}c a_i=c\sum_{i=1}^{n}a_i
$$

### 3. 可加性 / 拆分律

$$
\sum_{i=1}^{n}a_i
=
\sum_{i=1}^{k}a_i+\sum_{i=k+1}^{n}a_i
$$

更一般地：

$$
\sum_{i=m}^{n}a_i
=
\sum_{i=m}^{k}a_i+\sum_{i=k+1}^{n}a_i
$$

### 4. 常数求和

$$
\sum_{i=1}^{n}c=nc
$$

$$
\sum_{i=m}^{n}c=(n-m+1)c
$$

### 5. 指标平移 / 换元

$$
\sum_{i=m}^{n}a_i
=
\sum_{j=m+r}^{n+r}a_{j-r}
$$

例如：

$$
\sum_{i=1}^{n}a_i=\sum_{j=0}^{n-1}a_{j+1}
$$

### 6. 双重求和交换
有限项时恒成立：

$$
\sum_{i=1}^{m}\sum_{j=1}^{n}a_{ij}
=
\sum_{j=1}^{n}\sum_{i=1}^{m}a_{ij}
$$

无限项时，通常需要绝对收敛才能随意交换。

### 7. 乘积分离

$$
\sum_{i=1}^{m}\sum_{j=1}^{n}a_i b_j
=
\left(\sum_{i=1}^{m}a_i\right)
\left(\sum_{j=1}^{n}b_j\right)
$$

### 8. 重排律
有限项：

$$
\sum_{i=1}^{n}a_i=\sum_{i=1}^{n}a_{\sigma(i)}
$$

其中 $\sigma$ 是 $1,\dots,n$ 的任意排列。

无限项：

- 绝对收敛：可任意重排；
- 条件收敛：不能随意重排。

### 9. 三角不等式

$$
\left|\sum_{i=1}^{n}a_i\right|
\le
\sum_{i=1}^{n}|a_i|
$$

### 10. 常用求和公式

$$
\sum_{i=1}^{n}1=n
$$

$$
\sum_{i=1}^{n}i=\frac{n(n+1)}{2}
$$

$$
\sum_{i=1}^{n}i^2=\frac{n(n+1)(2n+1)}{6}
$$

$$
\sum_{i=1}^{n}i^3=\left(\frac{n(n+1)}{2}\right)^2
$$

$$
\sum_{i=0}^{n}r^i=\frac{1-r^{n+1}}{1-r}\qquad (r\ne 1)
$$

---

如果是指集合的 $\sigma$-并、$\sigma$-交或 $\sigma$-代数，其核心运算律是：

$$
\left(\bigcup_{i=1}^{\infty}A_i\right)^c
=
\bigcap_{i=1}^{\infty}A_i^c
$$

$$
\left(\bigcap_{i=1}^{\infty}A_i\right)^c
=
\bigcup_{i=1}^{\infty}A_i^c
$$

以及 $\sigma$-代数对可数并、可数交、补集封闭。