# Natural gradient flow dynamics


$$
\begin{aligned}
\rho(\theta, \theta_k)=\|\theta-\theta_k\|_{G}^2 \quad \quad \quad \longrightarrow \quad \quad \quad
\theta = \theta_k-sG^{-1}\nabla L(\theta_k) 
\end{aligned}
$$
____

<div class="grid grid-cols-2">

$$\text{Preconditioned gradient flow} \\ \text{in \textbf{parameter space}} \\ {\color{white} a} \\
\text{Preconditioned gradient flow} \\ \text{in \textbf{functional space}}$$
$$\frac{\partial \theta}{\partial s} = -M^{-1} \nabla_\theta  L \\ {\color{white} a} \\
\frac{\partial \vp}{\partial s} = -{\colorT E}^T G^{\frac 1 2} M^{-1}G^{\frac 1 2}  \Braket{\LossVGrad, {\colorT E}}_V$$

</div>



<!-- ======== Gradient Descent ======== -->
<div v-click="[1, 2]">
<div v-motion
  :initial="{ y: -30, x: 0 }"
>
<div class="grid grid-cols-2">


$$\text{Gradient descent } M=I \\ \text{in \textbf{functional space}}\\{\color{white} a} \\
\frac{\partial \vp}{\partial s} = -{\colorT E}^T G^{\frac 1 2} I^{-1}G^{\frac 1 2}  \Braket{\LossVGrad, {\colorT E}}_V$$

</div>
</div>
</div>

<div v-click="[2, 3]">
<div v-motion
  :initial="{ y: -220.6, x: 0 }"
>
<div class="grid grid-cols-2">


$$\text{Gradient descent } M=I \\ \text{in \textbf{functional space}}\\{\color{white} a} \\
\frac{\partial \vp}{\partial s} = -{\colorT E}^T G  \Braket{\LossVGrad, {\colorT E}}_V$$

</div>
</div>
</div>


<!-- ======== Natural Gradient ======== -->
<div v-click="[3, 4]">
<div v-motion
  :initial="{ y: -410.6, x: 0 }"
>

<div class="grid grid-cols-2">


$$\text{Gradient descent } M=I \\ \text{in \textbf{functional space}}\\{\color{white} a} \\
\frac{\partial \vp}{\partial s} = -{\colorT E}^T G  \Braket{\LossVGrad, {\colorT E}}_V$$
$$\text{Natural gradient } M=G \\ \text{in \textbf{functional space}}\\{\color{white} a} \\
\frac{\partial \vp}{\partial s} = -{\colorT E}^T G^{\frac 1 2} G^{-1}G^{\frac 1 2}  \Braket{\LossVGrad, {\colorT E}}_V$$

</div>
</div>
</div>

<div v-click="[4, 5]">
<div v-motion
  :initial="{ y: -600.6, x: 0 }"
>

<div class="grid grid-cols-2">


$$\text{Gradient descent } M=I \\ \text{in \textbf{functional space}}\\{\color{white} a} \\
\frac{\partial \vp}{\partial s} = -{\colorT E}^T G  \Braket{\LossVGrad, {\colorT E}}_V$$
$$\text{Natural gradient } M=G \\ \text{in \textbf{functional space}}\\{\color{white} a} \\
\frac{\partial \vp}{\partial s} = -{\colorT E}^T  \Braket{\LossVGrad, {\colorT E}}_V$$

</div>
</div>
</div>

<div v-click="5">
<div v-motion
  :initial="{ y: -790.6, x: 0 }"
>

<div class="grid grid-cols-2">


$$\text{Gradient descent } M=I \\ \text{in \textbf{functional space}}\\{\color{white} a} \\
\frac{\partial \vp}{\partial s} = -{\colorT E}^T G  \Braket{\LossVGrad, {\colorT E}}_V$$
$$\text{Natural gradient } M=G \\ \text{in \textbf{functional space}}\\{\color{white} a} \\
\frac{\partial \vp}{\partial s} = -P_{\cT_k} \LossVGrad$$

</div>
</div>
</div>