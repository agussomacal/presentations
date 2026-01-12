# Gradient descent
Iteratively improve approximation by minimizing $L(\theta_k)$.

<div class="absolute left-325px bottom-20px">
<img src="./../figures/handmade/GD_Taylor.png" width="350">
</div>

**Taylor expansion** around current iterate $\theta_k$.


$$L(\theta) \approx L(\theta_k) + \langle \nabla_\theta L(\theta_k), \theta-\theta_k\rangle_{\R^p} \color{white}  + \frac{1}{2s} \rho(\theta, \theta_k)$$
