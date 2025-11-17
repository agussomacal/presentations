
# Problem formulation
Objective: approximate target function $u\in V$ by $v\in\cM\subset V$

<div class="absolute right-90px bottom-5px">
<img src="./../figures/handmade/settingmanifold.png" width="350">
</div>

<div class="absolute left-90px bottom-20px">
<img src="./../figures/FunctionApproximation.png" width="300">
</div>

<div class="grid grid-cols-3 -pt-1 -mb-6">

$$\text{Target function}$$
$$\u:\R^d\to\R\in V$$
$$\text{Hilbert space}\\L^2(\Omega), H^1(\Omega),\dots$$
</div>

<div class="grid grid-cols-3 -pt-1 -mb-6">

$$\text{Approximation} \\ \text{manifold}$$
<div>

$$\cM :=\{\vp(x)={\colorM A(\theta)}(x);\; \theta\in\R^p\}$$

$$
\begin{aligned}
{\colorM A(\theta)}(x) &= \theta_1 {\colorV \phi_1}(x) + \dots + \theta_p {\colorV \phi_p}(x) \\
&= \theta^T {\colorV \mathbf{\Phi}}(x)
\end{aligned}
$$
</div>

<div>

$$\text{Linear model\color{white},} \\  \color{white}\text{Neural network,}\\...$$
</div>

</div>



