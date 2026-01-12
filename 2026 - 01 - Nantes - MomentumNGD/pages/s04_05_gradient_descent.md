# Gradient descent
Iteratively improve approximation by minimizing $L(\theta_k)$.

**Taylor expansion** around current iterate $\theta_k$ plus <span style="color:blue">penalization on the distance</span> traveled on each step.

$$\frac 1 2 \nabla_\theta{\color{blue} \rho(\theta, \theta_k)} = -s\nabla_\theta L(\theta_k)$$

<div class="grid grid-cols-2 gap-5 pt-4 -mb-4">

<h3 style="text-align: center">Gradient descent</h3>
<h3 style="color: white; text-align: center">Ghost</h3>
</div>

<div class="grid grid-cols-2 gap-5 pt-4 -mb-4">

<div>

$${\color{blue} \rho(\theta, \theta_k)}=\|\theta-\theta_k\|_{\R^p}^2$$

$$\nabla_\theta {\color{blue} \rho(\theta, \theta_k)}= 2(\theta-\theta_k)$$
<br></br>
$$\theta = \theta_k-s\nabla_\theta L(\theta_k)$$
</div>

</div>
