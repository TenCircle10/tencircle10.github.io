---
layout: note
title: "容错压力测试"
slug: "torture-test"
permalink: "/notes/torture-test/"
---

## 紧贴文字的标题

上一行是普通文字，紧接着下面是标题（没有空行）：

### 这个三级标题上面原本没有空行
标题下面的正文。

普通文字后面紧跟引用块（原本没有空行）：

> 这是一个紧贴文字的引用块
> 第二行
> 第三行

另一段文字后面紧跟另一个引用块：

> 第二条引用，也是紧贴的

带有全角空格和制表符的链接：[ 全角空格 中间还有 制表符 的文字](https://example.com)
图片也一样：![ 全角空格的 alt ](https://example.com/a.png)

公式与文字混杂：前面紧贴$\sqrt{n+1} - \sqrt{n}$后面也紧贴，接着

$$
a_1 * b_1 \quad \# x \quad \& y
$$

然后紧跟文字（原本没有空行）：
`$a_1 * b_1$` 这种行内代码要原样保留，`#标签` 也一样。

$\alpha + \beta$ 这种圆括号定界符要变成 `$ \alpha + \beta $`。

- ☐ 未完成
- ☑ 已完成

<mark>高亮文字</mark>

#标签 保持纯文本

<img src="/assets/img/obsidian/photo.png" width="300" /> 与 *(嵌入笔记：某笔记)* 与 [torture-test](/notes/torture-test/) 与 [文字](#abc123)

块 ID 独立一行：
<a id="abc123"></a>

代码块里全都不许动：

```
文字
> 引用
# 标题
$公式$
`行内代码`
%% 注释 %%
```
