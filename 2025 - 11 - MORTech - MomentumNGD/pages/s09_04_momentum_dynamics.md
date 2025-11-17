# Momentum dynamics in functional space
From momentum in parameter space to functional space.



<div class="grid grid-cols-2">

<h3 style="text-align: center"> <span style="color: black">Heavy-ball: "momentum variable"</span></h3> 
<h3 style="text-align: center"> <span style="color: black">Heavy-ball: iterates difference</span></h3> 
</div>

<div class="grid grid-cols-2">

$$\theta_{k+1} - \theta_k = \beta p_{k-1} -\alpha\nabla_\theta \cL_u(\theta_k)$$
$$\theta_{k+1} - \theta_k = \beta(\theta_k - \theta_{k-1}) -\alpha\nabla_\theta \cL_u(\theta_k)$$
</div>


<div class="grid grid-cols-2">

$$
\cT_k \ni {\colorT \dd v_k} = \beta P_{\cT_k}{\colorTprev p_{k-1}} -\alpha P_{\cT_k}^{H_{\cL}}{\colorV\nabla  \cL}(\vk)
$$
$$
\cT_k \ni {\colorT \dd v_k} = \beta P_{\cT_k}(\vk - {\colorMprev v_{k-1}}) -\alpha P_{\cT_k}^{H_{\cL}}{\colorV\nabla  \cL}(\vk)
$$
</div>



<div class="grid grid-cols-3">

<div>

$$
P_{\cT_k}^{H_{\cL}} \LossVGrad(\vk)\\
{\color{white}}\\
(G_k^{H_\cL})^{-1}\nabla_\theta \cL(\theta_k)\\
{\color{white}}\\
G_k^{H_\cL} = \int \left[ \dAdp H_{\cL} \dAdp \right](x)\dd x
$$
</div>

<div>

$$
P_{\cT_k}{\colorTprev p_{k-1}}\\
{\color{white}}\\
G_k^{-1}G_{k,k-1}p_{k-1}\\
{\color{white}}\\
G_{k,k-1} = \int \left[\left. \dAdp\right|_{\theta_k} \left. {\colorTprev \frac{\partial A}{\partial \theta}}\right|_{\theta_{k-1}} \right](x)\dd x
$$
</div>
<div>

$$
P_{\cT_k}(\vk - {\colorMprev v_{k-1}})\\
{\color{white}}\\
G_k^{-1}\int \left[\left.\dAdp\right|_{\theta_k} (\vk - {\colorMprev v_{k-1}})\right](x)\dd x
$$
</div>
</div>
