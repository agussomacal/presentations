# Momentum dynamics in functional space
From momentum in parameter space to functional space.



<div class="grid grid-cols-2">

<h3 style="text-align: center"> Heavy-ball</h3> 
<h3 style="text-align: center"> Nestorov</h3> 
</div>

<div class="grid grid-cols-2">

$$\theta_{k+1} - \theta_k = \beta p_{k-1} -\alpha\nabla_\theta \cL_u(\theta_k)$$
$$\theta_{k+1} - \theta_k = \beta(\theta_k - \theta_{k-1}) -\alpha\nabla_\theta \cL_u(y_k)$$
</div>


<div class="grid grid-cols-2">

$$
\cT_k \ni {\colorT \dd v_k^{HB}} = P_{\cT_k}[\beta {\colorTprev p_{k-1}} -\alpha{\colorV\nabla  \cL}(\vk)]
$$
$$
\cT_k \ni {\colorT \dd v_k^N} = P_{\cT_k}[\beta (\vk - {\colorTprev v_{k-1}}) -\alpha{\colorV\nabla  \cL}({\color{teal} y_k})]
$$
</div>


<div class="grid grid-cols-3">

$$
P_{\cT_k} \LossVGrad(\vk)\\
$$
$$
P_{\cT_k}{\colorTprev p_{k-1}}\\
$$
$$
P_{\cT_k}(\vk - {\colorTprev v_{k-1}})\\
$$
</div>
