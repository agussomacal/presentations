# Physics informed learning.
Physics informed neural networks (PINNs) $\text{}\\$
$[$Müller J., Zeinhofer M. (2023)$]$ $\text{}\\$
$[$Schwencke N., Furtlehner C. (2024)$]$. 


$$
\begin{aligned}
\cL(\v) &= \|R(\v)\|^2 \\
\cL(\v) &= \|-\epsilon \partial_{xx} v+\partial_x \v-1\|^2
\end{aligned}
$$

<!-- 
\cL(\vk) &= \frac{1}{2m} \sum_i^m (-\epsilon \partial_{xx} \v(x_{I_i^k})+\partial_x \v(x_{I_i^k})-1)^2
 -->

<div class="absolute left-100px bottom-10px">
<img src="./../figures/PINNs/Reconstruction__optimizer_name_NaturalNestorov-m_1000.png" alt="drawing" width="350" style="float: right">
</div>

::right::
<div class="absolute right-20px bottom-10px">
<img src="./../figures/PINNs/Convergence__m_100-mu_0.1.png" alt="drawing" width="500" style="float: right">
</div>