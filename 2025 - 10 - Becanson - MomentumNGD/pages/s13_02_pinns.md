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
<img src="./../figures/PINNs/Reconstruction__optimizer_name_NaturalGradientDescent-m_100.png" alt="drawing" width="500" style="float: right">
<img src="./../figures/PINNs/Reconstruction__optimizer_name_NaturalHeavyBall-m_100.png" alt="drawing" width="500" style="float: right">
</div>

::right::
<img src="./../figures/PINNs/TimeComplexity__m_100-mu_0.1.png" alt="drawing" width="280" style="float: right">
<img src="./../figures/PINNs/TimeComplexity__m_200-mu_0.1.png" alt="drawing" width="280" style="float: right">


