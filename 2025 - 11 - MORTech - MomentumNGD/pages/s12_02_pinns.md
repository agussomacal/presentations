# Physics informed learning.
Physics informed neural networks (PINNs) $\text{}\\$
$[$Schwencke N., Furtlehner C. (2024)$]$ $\text{}\\$
$[$Müller J., Zeinhofer M. (2024)$]$.


$$
\begin{aligned}
\cL(\v) &= \|R(\v)\|^2 \\
\cL(\v) &= \|-\epsilon \partial_{xx} v+\partial_x \v-1\|^2 \\
\cL(\vk) &= \frac{1}{2m} \sum_i^m (-\epsilon \partial_{xx} \v(x_{I_i^k})+\partial_x \v(x_{I_i^k})-1)^2
\end{aligned}
$$

<div class="grid grid-cols-2">
<img src="./../figures/PINN_ReactionDiffusion/approximations/NGDLineSearchSampling.png" alt="drawing" width="500" style="float: right">
<img src="./../figures/PINN_ReactionDiffusion/approximations/MPLGLineSearchSampling.png" alt="drawing" width="500" style="float: right">
</div>

::right::
<img src="./../figures/PINN_ReactionDiffusion/num_steps/LineSearchSampling.png" alt="drawing" width="300" style="float: right">
<img src="./../figures/PINN_ReactionDiffusion/num_steps_m/LineSearchSampling.png" alt="drawing" width="300" style="float: right">



