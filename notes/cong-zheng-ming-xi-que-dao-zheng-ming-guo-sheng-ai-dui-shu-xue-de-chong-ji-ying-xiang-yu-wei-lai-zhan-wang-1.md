---
layout: note
title: 从“证明稀缺”到“证明过剩”：AI对数学的冲击、影响与未来展望-论文
aliases:
  - 证明过剩
  - AI与数学
  - 验证赤字
tags:
  - 论文
  - AI与数学
  - 形式化证明
  - 学术治理
  - Obsidian
created: 2026-10-20
status: 整理稿
slug: "cong-zheng-ming-xi-que-dao-zheng-ming-guo-sheng-ai-dui-shu-xue-de-chong-ji-ying-xiang-yu-wei-lai-zhan-wang-1"
permalink: "/notes/cong-zheng-ming-xi-que-dao-zheng-ming-guo-sheng-ai-dui-shu-xue-de-chong-ji-ying-xiang-yu-wei-lai-zhan-wang-1/"
public: true
render_with_liquid: false
---

# 从“证明稀缺”到“证明过剩”：AI对数学的冲击、影响与未来展望

<details class="callout abstract" data-callout="abstract" open>
<summary class="callout-title">摘要</summary>
<div class="callout-content" markdown="block">

本文以“证明稀缺—证明过剩”为分析框架，梳理 AI 介入数学研究的阶段性时间线，并讨论其结构性影响。本文认为，AI 数学能力的跃升并不只表现为解题能力提高，更关键的是形式化证明使证明逐步转化为机器可验证对象，从而显著降低验证的边际成本并推动证明批量生产。由此形成的核心矛盾不是“AI 能否做数学”，而是当证明产出速度超过学术共同体验证、理解、传播与吸收能力时，数学共同体将面临验证赤字与证明消化不良。纳维–斯托克斯争议、25 位菲尔兹奖得主声明与《莱顿宣言》表明，问题已从技术能力转向署名、溯源、评价制度与研究自主权等治理议题。本文据此提出形式化验证标准、证明溯源机制、分层评审与问题导向评价等制度回应方向。

</div>
</details>

**关键词：** AI 数学；形式化证明；验证赤字；证明消化不良；学术治理；莱顿宣言

**中图分类号：** O1-0；TP18  
**文献标识码：** A

---

## 1 引言

AI 与数学的关系在过去两年多内经历了从“竞赛选手”到“研究参与者”再到“争议中心”的转变。本文所讨论的“证明过剩”，并非指数学证明在绝对数量上已经无用，而是指 AI 批量生成证明的速度已远超学术共同体验证、消化和吸收的能力，形成结构性 [验证赤字](#verification-deficit)。在此意义上，AI 对数学的冲击不只是“能否给出答案”，而是“答案如何被验证、理解、归因与纳入知识体系”。

本文的核心问题是：当 AI 使证明生产从稀缺走向相对过剩时，数学作为人类集体事业的组织方式将发生何种变化？为此，本文基于所给材料，采用时间线分析与机制分析相结合的方法，先梳理三阶段演进，再讨论验证成本、评价制度与治理争议，最后给出未来展望。

<details class="callout warning" data-callout="warning" open>
<summary class="callout-title">材料说明</summary>
<div class="callout-content" markdown="block">

本文所述时间线包含原文所列 2026 年事件与链接。本文不将其视为已独立核验的事实，而将其作为分析“AI 数学冲击”的文本材料。引用处尽量保留原文链接。

</div>
</details>

## 2 分析框架与材料

本文使用两个核心概念。第一，形式化证明：在 Lean 等形式化环境中，证明步骤可由内核自动检查，从而压缩“看起来正确”与“确实正确”之间的模糊地带。 <a id="formal-proof"></a>

第二，验证赤字：当证明产出速度超过人类共同体验证与理解速度时，学术系统出现结构性积压。 <a id="verification-deficit"></a>

与之相关的还有陶哲轩提出的“证明消化不良”，即共同体难以在短时间内消化大量新证明。 <a id="proof-indigestion"></a>

材料上，本文依据所给文本及其外部链接，按“竞赛突破—研究前沿—千禧年难题与反弹”三阶段整理。分析方法为文本时间线分析与机制归纳，不涉及独立数学验证。

## 3 三阶段时间线

### 3.1 第一阶段：竞赛突破与形式化工具成熟（2024—2025）

2024 年 7 月，Google DeepMind 的 AlphaProof 与 AlphaGeometry 2 在 IMO 中解出 6 题中的 4 题，达到银牌水平。AlphaProof 的关键在于在 Lean 中运行强化学习，使生成步骤可被内核自动检查[1]。2024 年 11 月，Epoch AI 发布 FrontierMath 基准，初始顶尖模型解决率不足 2%。2025 年 7 月，多个模型在 IMO 中解出 6 题中的 5 道，Gemini Deep Think 达到金牌水平。2025 年 11 月，AlphaProof 技术细节在《Nature》发表，标志形式化数学 AI 的学术定型。2025 年 12 月，Axiom 模型在无人干预下完成埃尔德什问题第 481 号和 124 号猜想的形式化证明。

这一阶段的关键变化不是“AI 会做题”，而是数学证明开始被系统转化为机器可验证对象；一旦证明可自动检查，“批量生产”即成为可能。

### 3.2 第二阶段：从竞赛题到研究前沿（2026 年上半年）

2026 年 2 月，“首次证明”挑战赛要求参赛者一周内用 AI 解决 10 个研究级问题。2026 年 5 月 20 日，OpenAI 宣布其内部模型自主推翻悬置近 80 年的埃尔德什平面单位距离猜想：模型发现新的无限点集构造，使单位距离点对数量在多项式意义上超过网格构造上界。证明将代数数论工具用于离散几何问题，Timothy Gowers 评价为“AI 数学中的重要里程碑”，并称其达到最强数学期刊期望标准；证明由包括 Noga Alon 和 Timothy Gowers 的外部数学家小组独立验证、简化和阐释[2]。2026 年 8 月 1 日，OpenAI 一次发布十项数学与理论计算机科学成果，其中三项涉及埃尔德什问题，并附无未证明步骤的 Lean 4 证书；GPT-6 Astra 在 FrontierMath Tier 4 上得分达 97.6%。

### 3.3 第三阶段：千禧年难题与学术共同体反弹（2026 年 9 月）

2026 年 9 月 4 日，Anthropic 宣布 Claude 在基本自主运行 11 天后完成费马大定理的首个端到端、计算机验证形式化证明。需明确：Claude 并未重新发现 Wiles 的数学证明，而是将既有证明转化为约 1300 万行 Lean 代码，证明约 29,500 个中间定理。9 月 5 日前后，OpenAI 系统围绕纳维–斯托克斯问题组织约 10,000 个并发 AI 智能体，9 月 8 日发布 166 页论文与 Lean 验证代码，针对千禧年难题官方表述中的命题 C 和 D 方向[3]。随后争议爆发：纽约大学数学家 Tristan Buckmaster 质疑其与 Levent Alpöge 的相近工作是否被模型接触；OpenAI 回应未接触其成果，但“不能完全排除相关产品数据曾以某种方式参与训练”。

2026 年 9 月 9 日，陶哲轩提出“[证明消化不良](#proof-indigestion)”。

“好问题将比好答案更稀缺。” <a id="good-questions-scarcity"></a>

9 月 11 日，包括陶哲轩、邓煜、Peter Scholze、Martin Hairer、Maryna Viazovska 在内的 25 位菲尔兹奖得主联合发表《人工智能在数学中的严重错位》，核心论点是：AI 公司将重大开放问题当作模型能力基准，与数学研究追求概念理解和洞见的目标错位[5]。9 月 13 日，《[莱顿宣言](#leiden-declaration)》签名达 4,013 人；该宣言获国际数学联盟背书，指出虚假证明、署名版权、技术依赖与不平等、过度炒作、研究自主权丧失等五大威胁，并提出 23 条建议[4]。9 月 24 日，丘成桐等人在 arXiv 提交微分几何预印本，致谢 ChatGPT 6 Astra 与 Claude Pro 在部分证明策略与计算上的帮助，同时声明作者对人工验证与阐述负责[6]。10 月 7 日，OpenAI 在 GitHub 公开一批内部模型数学结果，首版目录 722 份手稿、372 个结果家族[7][8]。

<details class="callout note" data-callout="note" open>
<summary class="callout-title">时间线要点</summary>
<div class="callout-content" markdown="block">

第一阶段的主题是“可验证化”；第二阶段的主题是“原创研究接受度”；第三阶段的主题是“验证—理解—传播—引用链条的制度压力”。

</div>
</details>

## 4 机制分析：从证明稀缺到证明过剩

### 4.1 自动验证降低边际验证成本

[形式化证明](#formal-proof)使证明检查从依赖专家阅读转向机器内核检查。其直接效应是降低单个证明的验证边际成本，但间接效应更强：当验证可自动化，证明生产就可批量化；当生产批量化，共同体面对的就不再是“证明太少”，而是“待处理证明太多”。

### 4.2 验证赤字与证明消化不良

[验证赤字](#verification-deficit)不是数量绝对过剩，而是验证能力相对不足。[证明消化不良](#proof-indigestion)则强调理解与吸收的滞后：即使证明正确，共同体仍需时间总结方法、建立概念联系、评估意义。AI 批量产出会压缩这一时间窗口，导致“正确但未被消化”的证明积压。

### 4.3 评价制度的错位

25 位菲尔兹奖得主声明指出，AI 公司将重大开放问题当作模型基准，与数学研究追求概念理解的目标错位。换言之，AI 评价以“是否解出”为中心，数学共同体则以“是否形成洞见、方法是否可传播、署名是否可追溯”为中心。二者不完全一致，因而产生制度摩擦。

### 4.4 先到达与可追溯性

所谓验证—理解—传播—引用链条，指学术共同体从证明检查到概念吸收、方法传播与引用积累的完整流程。 <a id="validation-chain"></a>

纳维–斯托克斯争议之所以敏感，不在于争议本身是否成立，而在于它触及 [验证—理解—传播—引用链条](#validation-chain) 中最脆弱的一环：谁先到达、到达过程是否可追溯、训练数据与用户数据边界是否可信。 <a id="navier-stokes-controversy"></a>

这已不是单纯 AI 技术问题，而是数学作为人类集体事业的组织问题。

## 5 争议、治理与制度回应

《莱顿宣言》系统列出五类威胁：似是而非的虚假证明、署名与版权、技术依赖与不平等、过度炒作、研究自主权丧失，并提出面向个体数学家、数学组织与资助方、政策制定者的 23 条建议[4]。 <a id="leiden-declaration"></a>

25 位菲尔兹奖得主声明则进一步将问题概括为“严重错位”：AI 公司以开放问题为基准，可能压缩验证、方法总结与学术交流时间，并引发署名和抄袭问题[5]。

治理上，至少需要三类机制：其一，形式化验证与人工审阅结合，避免“机器通过”替代“数学理解”；其二，建立证明溯源与数据隔离机制，记录模型、数据、用户会话与人工贡献边界；其三，改革评价制度，从“答案数量”转向“问题质量、方法贡献与可消化性”。

## 6 未来展望

第一，建设公共形式化验证基础设施，使 Lean 证书成为可审计的标准附件。第二，建立 AI 参与证明的贡献声明规范，区分“策略建议”“计算辅助”“形式化转换”“独立发现”。第三，采用分层评审：机器初筛、专家定向审阅、社区消化并行，以缓解 [验证赤字](#verification-deficit)。第四，强化问题导向评价，回应“[好问题将比好答案更稀缺](#good-questions-scarcity)”的判断。第五，推动国际数学组织、资助方与 AI 公司共同制定数据使用与溯源准则，降低 [纳维–斯托克斯争议](#navier-stokes-controversy)类信任风险。

## 7 结论

本文认为，AI 对数学的冲击可概括为：从“证明稀缺”走向“证明过剩”，其本质是证明生产速度超过共同体验证与消化能力，形成结构性 [验证赤字](#verification-deficit)。AlphaProof 解决“证明能否自动检查”，埃尔德什猜想推翻解决“AI 能否做出被顶级期刊接受的原创新结果”，而纳维–斯托克斯争议与 25 位菲尔兹奖得主声明暴露 [验证—理解—传播—引用链条](#validation-chain) 的制度压力。未来数学共同体的关键任务，不是阻止 AI 生产证明，而是重建可验证、可追溯、可消化的学术基础设施，使 AI 成为数学集体事业的工具而非评价体系的错位驱动者。

---

## 参考文献

[1] 36氪. 刚刚，DeepMind 再登 Nature：AlphaProof 首夺国际数学奥林匹克银牌[EB/OL]. https://36kr.com/p/3550989555513221.  
[2] OpenAI. OpenAI 模型推翻了离散几何领域的核心猜想[EB/OL]. https://openai.com/zh-Hans-CN/index/model-disproves-discrete-geometry-conjecture/.  
[3] OpenAI. 关于纳维–斯托克斯千禧年大奖难题[EB/OL]. https://openai.com/zh-Hans-CN/index/navier-stokes-solution/.  
[4] Leiden Declaration on Artificial Intelligence and Mathematics[EB/OL]. https://leidendeclaration.ai/.  
[5] Tao T. A Severe Misalignment of AI in Mathematics[EB/OL]. https://terrytao.wordpress.com/2026/09/11/a-severe-misalignment-of-ai-in-mathematics/.  
[6] 网易. 丘成桐论文致谢 AI，77 岁数学泰斗，也逃不过“真香定律”？[EB/OL]. https://www.163.com/dy/article/L80QJMJD05118O92.html.  
[7] OpenAI. openai/math[EB/OL]. https://github.com/openai/math.  
[8] OpenAI. 分享 AI 在数学领域的进展[EB/OL]. https://openai.com/zh-Hans-CN/index/sharing-ai-progress-in-mathematics/.