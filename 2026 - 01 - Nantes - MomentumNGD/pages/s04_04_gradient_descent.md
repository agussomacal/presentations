# Gradient descent
Iteratively improve approximation by minimizing $L(\theta_k)$.

**Taylor expansion** around current iterate $\theta_k$ plus <span style="color:blue">penalization on the distance</span> traveled on each step.

$$\frac 1 2 \nabla_\theta{\color{blue} \rho(\theta, \theta_k)} = -s\nabla_\theta L(\theta_k)$$