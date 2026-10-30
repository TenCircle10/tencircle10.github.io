---
layout: note
tags: [concept, 线性代数]
title: "向量组无关加元素仍无关"
slug: "xiang-liang-zu-wu-guan-jia-yuan-su-reng-wu-guan"
permalink: "/notes/xiang-liang-zu-wu-guan-jia-yuan-su-reng-wu-guan/"
public: false
render_with_liquid: false
---

# 向量组无关加元素仍无关

<details class="callout abstract" data-callout="abstract" open>
<summary class="callout-title">断言</summary>
<div class="callout-content" markdown="block">

一组**线性无关**的向量各自加长（后面添上同样的若干分量）后，仍然**线性无关**。简记：**无关加元素仍无关**。

</div>
</details>

设

$$
\alpha_1 = (a_{11}, a_{12}, a_{13}, \cdots, a_{1n}), \quad \dots, \quad
\alpha_s = (a_{s1}, a_{s2}, a_{s3}, \cdots, a_{sn})
$$

各自添上 $m$ 个分量，得到

$$
\beta_1 = (a_{11}, \cdots, a_{1n}, b_{11}, \cdots, b_{1m}), \quad \dots, \quad
\beta_s = (a_{s1}, \cdots, a_{sn}, b_{s1}, \cdots, b_{sm})
$$

若 $\alpha_1, \dots, \alpha_s$ 线性无关，则 $\beta_1, \dots, \beta_s$ 线性无关。

**证（反证）**：设 $\beta_1, \dots, \beta_s$ 线性**相关**，则有不全为零的 $k_1, \dots, k_s$ 使 $\sum_{i=1}^{s} k_i \beta_i = O$。**只看前 $n$ 个坐标**：

$$\sum_{i=1}^{s} k_i \alpha_i = 0$$

这与 $\alpha_1, \dots, \alpha_s$ 线性无关矛盾。故 $\beta_1, \dots, \beta_s$ 线性无关。

<details class="callout warning" data-callout="warning" open>
<summary class="callout-title">只需"看前 $n$ 个坐标"</summary>
<div class="callout-content" markdown="block">

$\sum k_i \beta_i = O$ 含两组等式（前 $n$ 个坐标、后 $m$ 个坐标），推矛盾**只用前一组**。关键是那组不全为零的系数在两个方程里**同一组**。

</div>
</details>

**逆否**：若加长后的 $\beta$ 组线性相关，则原来的 $\alpha$ 组也线性相关。这是 [子母矩阵秩的大小关系](/notes/zi-mu-ju-zhen-zhi-de-da-xiao-guan-xi/) 的向量版。

---

## 相关笔记

- 主线上位概念：[线性代数笔记](/notes/xian-xing-dai-shu-bi-ji/)
- 姊妹结论：[子母矩阵秩的大小关系](/notes/zi-mu-ju-zhen-zhi-de-da-xiao-guan-xi/)
