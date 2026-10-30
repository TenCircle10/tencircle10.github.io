---
layout: note
title: "莱布尼茨记法"
slug: "lai-bu-ni-ci-ji-fa"
permalink: "/notes/lai-bu-ni-ci-ji-fa/"
public: false
generated_by: sync_notes.py
render_with_liquid: false
---

### 图1
**莱布尼茨记法**

核心 $\frac{d}{dx}$，表示对 $dx$ 的微分
来源于导数的算子本质
优点：直观，可类似“约分”

一阶导 $\frac{dy}{dx}$

二阶导 $\frac{d^2y}{dx^2} = \frac{d}{dx}\frac{dy}{dx} = \frac{d}{dx}\frac{d}{dx}y$

链式法则 $\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$

参数方程求导 $x = f(t) \quad y = g(t)$

$$
 \frac{d^2y}{dx^2} = \frac{d}{dx}\left(\frac{dy}{dx}\right) = \frac{\frac{d}{dt}\left(\frac{dy}{dx}\right)}{\frac{dx}{dt}} 
$$

重点还是“凑”

求 $f(x)$ 反函数的二阶导

$$
 \frac{d^2x}{dy^2} = \frac{d}{dy}\left(\frac{dx}{dy}\right) = \frac{d}{dx}\left(\frac{1}{\frac{dy}{dx}}\right) \cdot \frac{dx}{dy} 
$$

$$
 = \left(\frac{1}{f'(x)}\right)' \frac{1}{f'(x)} = \frac{-f''(x)}{(f'(x))^3} 
$$

---

### 图2
**隐函数求导** $x^2 + y^2 = 1$

$$
 \frac{d}{dx}(x^2 + y^2) = 0 
$$

$$
 2x + \frac{d(y^2)}{dx} = 0 
$$

$$
 2x + \frac{d(y^2)}{dy}\frac{dy}{dx} = 0 
$$

$$
 2x + 2y \cdot \frac{dy}{dx} = 0 
$$

$$
 \frac{dy}{dx} = -\frac{x}{y} 
$$

求二阶导：

$$
 \frac{d^2y}{dx^2} = ? 
$$

$$
 = \frac{d}{dx}\left(-\frac{x}{y}\right) 
$$

$$
 = -\frac{y - \frac{dy}{dx}x}{y^2} 
$$

$$
 = \frac{x \cdot (-\frac{x}{y}) - y}{y^2} 
$$

$$
 = -\frac{x^2 + y^2}{y^3} = -\frac{1}{y^3} 
$$
