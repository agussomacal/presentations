# Toy example
Natural gradient and Newton method are equivalent for linear models.


<div class="grid grid-cols-2">
<div>

$$
\u \in L^2([0, 1]) \\
\cL_u(\v) = \frac 1 2 \|\u-\v\|_{\color{orange}K}^2 \\
\begin{align*}
\vp(x) = {\colorT A(\theta)}(x) &= \theta^T {\color{red}B} {\colorV \Phi}(x)\\
&= \theta^T {\color{red}B}
 \begin{bmatrix}
1\\
\sqrt{2}\sin(2\pi x)
\end{bmatrix}
\end{align*}
$$
</div>


<div>

$$
\R^{p\times p} \ni {\color{red}B}  = 
\begin{bmatrix}
1 & 0\\
0 & 0.2\\
\end{bmatrix} \\
\dAdpi(\theta)(x) = {\color{red}B_i}{\colorV \Phi}(x) \\
G_{ij} = \int \left[{\colorV \Phi^T} {\color{red}B_i^T{\color{orange}K}B_j} {\colorV \Phi} \right](x)\dd x = \color{red}B_i^T{\color{orange}K}B_j
$$
</div>
</div>


<div class="absolute left-10px bottom-7px">
<div class="grid grid-cols-3">
<img src="./../figures/experiments/ExactSpaces/parameter_space/F06_Newton_0.png" alt="drawing" width="300" style="float: center">
<img src="./../figures/experiments/ExactSpaces/functional_space/F06_Newton_0.png" alt="drawing" width="300" style="float: center">
<img src="./../figures/experiments/ExactSpaces/convergence/F06_Newton_0.png" alt="drawing" width="300" style="float: center">
</div>
</div>
