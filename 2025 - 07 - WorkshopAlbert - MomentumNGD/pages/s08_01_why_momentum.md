# Why we need momentum
Using momentum to **scape local minima** and **correct the biased step** of NGD.


<div class="grid grid-cols-2 gap-30">

<div>
<h3 style="text-align: center"> 

<span v-mark.square.green="-1"> Beyond $L^2$ loss </span>
</h3> 



<!-- ======== Classification ======== -->
<div class="grid grid-cols-2 gap-10">

$$\textbf{Classification} \\ \text{problem: KL-div}$$
$$\cL_u(\v) = \int \v(x) \log \frac{\v(x)}{\u(x)} \dd x$$
</div>

<div class="grid grid-cols-2 gap-10">

<!-- ======== Stochastic ======== -->
$$\text{\textbf{Stochastic} setting}\\ \text{empirical loss}$$
$$
\cL_u(\vk) = \|\u-\vk\|_m^2 \\
\frac{1}{2m} \sum_{i=1}^{m} (\u(x_{I^k_i})-\v(x_{I^k_i}))^2
$$
</div>

<div class="grid grid-cols-2 gap-10">

<!-- ======== PDE ======== -->
$$\text{\textbf{PDE} residual}$$
$$
\begin{aligned}
\cL(\v) &= \|R(\v)\|^2 \\
 &= \|-\epsilon \partial_{xx} \v+\partial_x \v-1\|^2
\end{aligned}
$$
</div>
</div>


<div>
<!-- ======== Local minima ======== -->
<br></br>
<h3 style="text-align: center"> 

<span v-mark.square.blue="-1"> Escape local minima </span>
</h3> 

<br></br>

$$\frac{\partial \vp}{\partial s} = -P_{\cT_k} \LossVGrad$$



<!-- ======== Non linear model ======== -->
<br></br>
<h3 style="text-align: center"> 

<span v-mark.square.red="-1"> Non-linear model </span>
</h3> 

<br></br>
$$\theta_{k+1} = \theta_k -sG_k^{-1} \nabla_\theta \cL(\theta_k)$$
$$\theta_{s} = \theta_k -\int_0^{s} G_k^{-1}(\theta_\ell) \nabla_\theta \cL(\theta_\ell)\dd \ell$$


</div>
</div>

