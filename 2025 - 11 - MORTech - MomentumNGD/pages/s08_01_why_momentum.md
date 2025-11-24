# Why we need momentum
Using momentum to **scape local minima** and **correct the biased step** of NGD.


<div class="grid grid-cols-2 gap-30">
<div>

<!-- ========           ======== -->
<!-- ======== BEYOND L2 ======== -->
<!-- ========           ======== -->
<h3 style="text-align: center"> 

<span v-mark.square.green="-1"> Beyond $L^2$ loss </span>
</h3> 
<div class="grid grid-cols-2 gap-10">
<!-- ======== Classification ======== -->
<div>

$$\textbf{Classification} \\\text{KL-div}$$ 
$$\int \left[\v \log \frac{\v}{\u}\right](x) \dd x$$
</div>
<!-- ======== PDE ======== -->
<div>

$$\text{\textbf{PDE} residual}$$
$$
\begin{aligned}
\cL(\v) &= \|R(\v)\|^2 \\
 &= \|-\epsilon \partial_{xx} \v+\partial_x \v-1\|^2
\end{aligned}
$$
</div>
</div>

<!-- ========           ======== -->
<!-- ======== INACURATE ======== -->
<!-- ========           ======== -->
<h3 style="text-align: center"> 

<span v-mark.square.purple="-1"> Inacurate estimation of update </span>
</h3> 
<div class="grid grid-cols-2 gap-10">
<!-- ======== Stochastic ======== -->
<div>

$$\text{\textbf{Stochastic} setting}\\ \text{empirical loss}$$
$$
\cL_u(\vk) = \|\u-\vk\|_m^2
$$
</div>
<!-- ======== Inversion ======== -->
<div>

$$\text{\textbf{Solving} NGD system}$$
$$
G^{-1} 
\begin{cases}
\xrightarrow{Penrose} V(\Sigma_{\sigma>\varepsilon})^{-1}V^T \\
\xrightarrow{Tikhonov} (G+\varepsilon I)^{-1}
\end{cases}
$$
</div>
</div>
</div>


<div>
<!-- ========                  ======== -->
<!-- ======== Non linear model ======== -->
<!-- ========                  ======== -->
<h3 style="text-align: center"> 

<span v-mark.square.red="-1"> Non-linear model </span>
</h3> 

<br></br>
$$\theta_{k+1} = \theta_k -sG_k^{-1} \nabla_\theta L(\theta_k)$$
$$\theta_{s} = \theta_k -\int_0^{s} G_k^{-1}(\theta_\ell) \nabla_\theta L(\theta_\ell)\dd \ell$$
<br></br>

<!-- ========              ======== -->
<!-- ======== Local minima ======== -->
<!-- ========              ======== -->
<h3 style="text-align: center"> 

<span v-mark.square.blue="-1"> Escape local minima </span>
</h3> 

<br></br>

$$\frac{\partial \vp}{\partial s} = -P_{\cT_k} \LossVGrad$$
</div>
</div>

