# Toy example
Escaping local minima.


<div class="grid grid-cols-2">

<div>

$$
\begin{aligned}
\u&\in L^2([0, 1]) \\
\cL_u(\v) &= \frac 1 2 \|\u-\v\|_{\color{orange}K}^2 \\
\end{aligned}
$$
$$\vp(x) = \theta_1 {\color{red}b^T}{\colorV \Phi}(x) + \theta_1^2 {\color{red}b^{\perp T}} {\colorV \Phi}(x)$$
</div>

<div class="absolute right-120px top-125px">

$${\colorT \dd v_k^{HB}} = P_{\cT_k}[\beta {\colorTprev p_{k-1}} -\alpha{\colorV\nabla  \cL}(\vk)]$$
$${\colorT \dd v_k^{N}} = P_{\cT_k}[\beta (\vk - {\colorTprev v_{k-1}}) -\alpha{\colorV\nabla  \cL}({\colorM y_k})]$$
</div>
</div>

<div class="absolute left-30px bottom-7px">
<div class="grid grid-cols-3">
<img src="./../figures/ExactSpaces/parameter_space/F08_LocalMinima_0.png" alt="drawing" width="300" style="float: center">
<img src="./../figures/ExactSpaces/functional_space/F08_LocalMinima_0.png" alt="drawing" width="300" style="float: center">
<img src="./../figures/ExactSpaces/convergence/F08_LocalMinima_0.png" alt="drawing" width="300" style="float: center">
</div>
</div>

