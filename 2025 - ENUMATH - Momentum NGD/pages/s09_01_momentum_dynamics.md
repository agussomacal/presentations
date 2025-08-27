# Momentum dynamics
From gradient flow to momentum $[$Polyak, B.T. 1964$]$ $[$Nesterov, Yurii. 1983$]$.




<div class="grid grid-cols-2">

$$\frac{\dd \theta}{\dd s} = -\nabla_\theta \cL $$
$$\frac{\dd^2 \theta}{\dd s^2} = - \gamma \frac{\dd \theta}{\dd s} -\nabla_\theta \cL $$
</div>

<div class="grid grid-cols-2">

<h3 style="text-align: center"> Heavy-ball</h3> 
<h3 style="text-align: center"> Nestorov</h3> 
</div>

<div class="grid grid-cols-2">

$$
\begin{aligned}
\theta_{k+1} &= \theta_k + p_k\\
p_{k} &= \beta p_{k-1} -\alpha\nabla_\theta \cL_u(\theta_k)
\end{aligned}
$$
$$
\begin{aligned}
y_{k} &= \theta_k + \beta(\theta_k - \theta_{k-1}) \\
\theta_{k+1} &= y_{k} - \alpha\nabla_\theta \cL_u(y_k)
\end{aligned}
$$
</div>

<div class="grid grid-cols-2">

$$\theta_{k+1} = \theta_k + \beta p_{k-1} -\alpha\nabla_\theta \cL_u(\theta_k)$$
$$\theta_{k+1} = \theta_k + \beta(\theta_k - \theta_{k-1}) -\alpha\nabla_\theta \cL_u(y_k)$$
</div>