# Momentum dynamics in functional space
From momentum in parameter space to functional space.



<div class="grid grid-cols-2">

<h3 style="text-align: center"> <span style="color: black">Heavy-ball: "momentum variable"</span></h3> 
<h3 style="text-align: center"> <span style="color: black">Heavy-ball: iterates difference</span></h3> 
</div>

<div class="grid grid-cols-2">

$$\theta_{k+1} - \theta_k = \beta p_{k-1} -\alpha\nabla_\theta  L(\theta_k)$$
$$\theta_{k+1} - \theta_k = \beta(\theta_k - \theta_{k-1}) -\alpha\nabla_\theta  L(\theta_k)$$
</div>

<v-click>
<div class="grid grid-cols-2">

$$
\cT_k \ni {\colorT \dd v_k} = P_{\cT_k}[\beta {\colorTprev p_{k-1}} -\alpha{\colorV\nabla  \cL}(\vk)]
$$
$$
\cT_k \ni {\colorT \dd v_k} = P_{\cT_k}[\beta (\vk - {\colorMprev v_{k-1}}) -\alpha{\colorV\nabla  \cL}(\vk)]
$$
</div>
</v-click>


<v-click>
<div class="grid grid-cols-3">

$$
P_{\cT_k} \LossVGrad(\vk)\\
$$
$$
P_{\cT_k}{\colorTprev p_{k-1}}\\
$$
$$
P_{\cT_k}(\vk - {\colorMprev v_{k-1}})\\
$$
</div>
</v-click>
