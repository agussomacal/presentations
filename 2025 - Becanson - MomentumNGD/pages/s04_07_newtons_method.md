# Newton's method
Iteratively improve approximation by minimizing $\cL(\theta_k)$.

**Taylor expansion** around current iterate $\theta_k$ plus <span style="color:blue">penalization on the distance</span> traveled on each step.

$$\frac 1 2 \nabla_\theta{\color{blue} \rho(\theta, \theta_k)} = -s\nabla_\theta\cL(\theta_k)$$

<div class="grid grid-cols-2 gap-5 pt-4 -mb-4">

<h3 style="text-align: center">Gradient descent</h3>
<h3 style="text-align: center">Newton's method</h3>
</div>

<div class="grid grid-cols-2 gap-5 pt-4 -mb-4">

<div>

$${\color{blue} \rho(\theta, \theta_k)}=\|\theta-\theta_k\|_{\R^p}^2$$

$$\nabla_\theta {\color{blue} \rho(\theta, \theta_k)}= 2(\theta-\theta_k)$$
<br></br>
$$\theta = \theta_k-s\nabla_\theta\cL(\theta_k)$$
</div>

<div>

$${\color{blue} \rho(\theta, \theta_k)}=\|\theta-\theta_k\|_H^2$$

$$\nabla_\theta {\color{blue} \rho(\theta, \theta_k)}= 2H(\theta-\theta_k)$$
<br></br>
$$\theta = \theta_k-sH^{-1}\nabla_\theta\cL(\theta_k)$$
</div>
</div>
