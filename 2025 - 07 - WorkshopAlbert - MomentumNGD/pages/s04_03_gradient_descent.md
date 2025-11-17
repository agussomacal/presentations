# Gradient descent
Iteratively improve approximation by minimizing $\cL(\theta_k)$.

<div class="absolute left-325px bottom-20px">
<img src="./../figures/handmade/GD_TaylorQuadraticMinimum.png" width="350">
</div>

**Taylor expansion** around current iterate $\theta_k$ plus <span style="color:blue">penalization on the distance</span> traveled on each step.

$$0 = \nabla_\theta \left[\cL(\theta_k) + \langle \nabla_\theta\cL(\theta_k), \theta-\theta_k\rangle_{\R^p} + \frac{1}{2s} {\color{blue} \rho(\theta, \theta_k)} \right]$$

