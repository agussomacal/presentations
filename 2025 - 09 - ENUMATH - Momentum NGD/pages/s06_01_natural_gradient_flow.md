# Natural gradient flow dynamics


$$
\begin{aligned}
\rho(\theta, \theta_k)=\|\theta-\theta_k\|_{G}^2 \quad \quad \quad \longrightarrow \quad \quad \quad
\theta = \theta_k-sG^{-1}\nabla\cL(\theta_k) 
\end{aligned}
$$
____

<div v-click="1">
<div class="grid grid-cols-2">

$$\text{Preconditioned gradient flow} \\ \text{in \textbf{parameter space}}$$

$$\frac{\partial \theta}{\partial s} = -M^{-1} \nabla_\theta \cL$$

</div>
</div>

<div v-click="2">

$${1|1,2|all}
\begin{aligned}
\frac{\partial \vp}{\partial s} = \frac{\partial \vp}{\partial \theta} \frac{\partial \theta}{\partial s}
=\dAdp^T M^{-1} \nabla_\theta \cL
&=-\dAdp^T M^{-1} \Braket{\LossVGrad, \dAdp}_V\\
&=-\left(G^{-\frac 1 2} \dAdp\right)^T G^{\frac 1 2} M^{-1}G^{\frac 1 2}  \Braket{\LossVGrad, G^{-\frac 1 2}\dAdp}_V \\
&=-{\colorT E}^T G^{\frac 1 2} M^{-1}G^{\frac 1 2}  \Braket{\LossVGrad, {\colorT E}}_V
\end{aligned}
$$
</div>


<div v-click="3">

$$
\begin{aligned}
\Braket{ {\colorT E}, {\colorT E}}_V &=\int_\Omega \left(G^{-\frac 1 2} \dAdp\right)^T\left(G^{-\frac 1 2} \dAdp\right) \dd\mu(x)
&=\int_\Omega \dAdp^TG^{-1} \dAdp \dd\mu(x)
&=I\\
\end{aligned}
$$
</div>


