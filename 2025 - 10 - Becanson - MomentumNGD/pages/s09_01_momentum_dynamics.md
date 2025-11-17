# Momentum dynamics
From gradient flow to momentum $[$Polyak, B.T. 1964$]$ $[$Nesterov, Yurii. 1983$]$.




<div class="grid grid-cols-2">

$$\frac{\partial \theta}{\partial s} = -\nabla_\theta \cL $$
$$\frac{\partial^2 \theta}{\partial s^2} = - \gamma \frac{\partial \theta}{\partial s} -\nabla_\theta \cL $$
</div>
<Arrow v-bind="{ x1:400, y1:185, x2:550, y2:185, color:'red', width:1.5}" />
<!-- <Arrow v-bind="{ x1:710, y1:220, x2:400, y2:250, color:'green', width:1.5}" />
<Arrow v-bind="{ x1:400, y1:185, x2:550, y2:185, color:'purple', width:1.5}" /> -->

___

<div class="grid grid-cols-2">

<div v-click="1">
<h3 style="text-align: center"> <span style="color: green">Heavy-ball</span></h3> 
</div>

<div v-click="2">
<h3 style="text-align: center"> <span style="color: purple">Nestorov</span></h3> 
</div>
</div>

<div class="grid grid-cols-2">

<div v-click="1">

$$
\begin{aligned}
\theta_{k+1} &= \theta_k + p_k\\
p_{k} &= \beta p_{k-1} -\alpha\nabla_\theta \cL_u(\theta_k)
\end{aligned}
$$
</div>

<div v-click="2">

$$
\begin{aligned}
y_{k} &= \theta_k + \beta(\theta_k - \theta_{k-1}) \\
\theta_{k+1} &= y_{k} - \alpha\nabla_\theta \cL_u(y_k)
\end{aligned}
$$
</div>
</div>

<div class="grid grid-cols-2">

<div v-click="3">

$$
\begin{aligned}
\theta_{k+1} &= \theta_k + \beta p_{k-1} -\alpha\nabla_\theta \cL_u(\theta_k)\\
             &= \theta_k + \beta (\theta_k - \theta_{k-1}) -\alpha\nabla_\theta \cL_u(\theta_k)
\end{aligned}
$$
</div>


<div v-click="4">

$$\theta_{k+1} = \theta_k + \beta(\theta_k - \theta_{k-1}) -\alpha\nabla_\theta \cL_u(y_k)$$
</div>
</div>