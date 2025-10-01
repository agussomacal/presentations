# Toy example
Not $L^2$ loss.


<div class="grid grid-cols-2">
<div>

$$
\begin{aligned}
\u&\in L^2([0, 1]) \\
\cL_u(\v) &= \frac 1 2 \|f(\u)-f(\v)\|_{\color{blue}K}^2 \\
f(\v)&= (1+\omega \|\v-{\colorV q}\|^2)(\v-{\colorV q}) + {\colorV q} \\
{\colorV q}&= R_\varphi(\u-\v) + \v
\end{aligned}
$$
</div>


<div class="absolute right-120px top-70px">

$${\colorT \dd v_k^{HB}} = P_{\cT_k}[\beta {\colorTprev p_{k-1}} -\alpha{\colorV\nabla  \cL}(\vk)]$$
$${\colorT \dd v_k^{N}} = P_{\cT_k}[\beta (\vk - {\colorTprev v_{k-1}}) -\alpha{\colorV\nabla  \cL}(\vk)]$$
</div>
</div>



<div class="absolute right-120px bottom-5px">
<h3 style="color: white; text-align: center">Ghost</h3>
<img src="./../figures/ExactSpaces/convergence/F08_TwistedLoss_0.png" alt="drawing" width="400" style="float: center">
<h3 style="color: white; text-align: center">Ghost</h3>
</div>


<div class="absolute left-80px bottom-5px">
<img src="./../figures/handmade/TwistedLoss.png" width="350">
</div>
