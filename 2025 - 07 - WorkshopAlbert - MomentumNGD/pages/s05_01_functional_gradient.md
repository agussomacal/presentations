# Functional gradient and geometric intuition
Some properties $[$Gruhlke, Robert, Anthony Nouy, and Philipp Trunschke. 2024$]$.


<div class="absolute right-300px top-290px">
<img src="./../figures/handmade/NGDprojectionBest.png" width="300">
</div>

$${1|all}
\begin{aligned}
H_{ij}=\frac{\partial^2 \cL}{\partial \theta_i \partial \theta_j}
=\frac{\partial }{\partial \theta_i }\left[\dLdpj \right]
&=\frac{\partial }{\partial \theta_i }\left[\frac{\partial }{\partial \theta_j } (\cL_\u \circ A) \right] = \frac{\partial }{\partial \theta_i }\left[\int_\Omega {\color{blue}\nabla \cL_\u(\vp)}(x) \dAdpj(x) \dd \mu(x) \right] \\
&=\frac{\partial }{\partial \theta_i }\left[\Braket{ {\color{blue}\nabla \cL_\u}, \dAdpj }_V \right] \\
\end{aligned}
$$

<v-click>


$$\cL_\u(\v)=\frac 1 2 \|\u-\v\|^2_{L^2(\Omega)}\quad \quad \quad \longrightarrow \quad \quad \quad V \ni {\color{blue}\nabla \cL_\u}=\u-\v$$

</v-click>