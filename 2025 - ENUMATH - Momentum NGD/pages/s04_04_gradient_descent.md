# Gradient descent
Iteratively improve approximation by minimizing $\cL(\theta_k)$.

**Taylor expansion** around current iterate $\theta_k$ plus <span style="color:blue">penalization on the distance</span> traveled on each step.

$$\frac 1 2 \nabla_\theta{\color{blue} \rho(\theta, \theta_k)} = -s\nabla_\theta\cL(\theta_k)$$