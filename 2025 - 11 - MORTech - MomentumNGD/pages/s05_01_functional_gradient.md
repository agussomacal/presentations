# Functional gradient and geometric intuition
Some properties $[$Gruhlke, Robert, Anthony Nouy, and Philipp Trunschke. 2024$]$.


$${1|all}
\begin{aligned}
H_{ij}=\frac{\partial^2 L}{\partial \theta_i \partial \theta_j}
=\frac{\partial }{\partial \theta_i }\left[\dLdpj \right]
&=\frac{\partial }{\partial \theta_i }\left[\frac{\partial }{\partial \theta_j } (\cL_\u \circ A) \right] = \frac{\partial }{\partial \theta_i }\left[\int_\Omega {\color{blue}\nabla \cL_\u(\vp)}(x) \dAdpj(x) \dd \mu(x) \right] \\
&=\frac{\partial }{\partial \theta_i }\left[\Braket{ {\color{blue}\nabla \cL_\u}, \dAdpj }_V \right] \\
\end{aligned}
$$



<div class="grid grid-cols-2 -pt-1 -mb-6">

<div>
<img src="./../figures/handmade/NGDprojectionBest2.jpg" width="300" alt="drawing" style="margin: 0 auto; float: center">
</div>

<div>

<v-click>
<br></br>

$$\cL_\u(\v)=\frac 1 2 \|\u-\v\|^2_{L^2(\Omega)}$$
<br></br>
$$V \ni {\color{blue}\nabla \cL_\u}=\u-\v$$
</v-click>
</div>

</div>