# Toy example
Gradient descent trajectory.


<div class="grid grid-cols-2">
<div>

$$
\u \in L^2([-1, 1]) \\
\cL_\u(\v) = \frac 1 2 \|\u-\v\|^2 \\
\begin{align*}
\vp(x) = {\colorM A(\theta)}(x) &= \theta^T{\colorV \Phi}(x)\\
&= \theta^T
 \begin{bmatrix}
\sin(2\pi x)\\
\cos(2\pi x)
\end{bmatrix}
\end{align*}
$$
</div>

<div>

$$
{\color{white}
\R^{p\times p} \ni B  = 
\begin{bmatrix}
1 & 0\\
0 & 0.2\\
\end{bmatrix}} \\
\dAdpi(\theta)(x) = {\colorV \Phi_i}(x) \\
G_{ij} = \int \left[{\colorV \Phi_i} {\colorV \Phi_j}\right](x)\dd x = \delta_{ij}
$$
</div>
</div>


<div class="absolute left-10px bottom-30px">
<div class="grid grid-cols-3 -pt-1 -mb-6">
<img src="./../figures/ExactSpaces/parameter_space/F01_GD.png" alt="drawing" width="300" style="float: center">
<img src="./../figures/ExactSpaces/functional_space/F01_GD.png" alt="drawing" width="300" style="float: center">
<img src="./../figures/ExactSpaces/convergence/F01_GD.png" alt="drawing" width="300" style="float: center">
</div>
</div>

