# Natural gradient from Newton's method
$[$Amari, Shun-ichi. 1998$]$ $[$Martens, James 2020$]$.

$${1,2,3|all}
\begin{aligned}
H_{ij}=\frac{\partial^2 L}{\partial \theta_i \partial \theta_j}
=\frac{\partial }{\partial \theta_i }\left[\dLdpj \right]
&=\frac{\partial }{\partial \theta_i }\left[\frac{\partial }{\partial \theta_j } (\cL_\u \circ A) \right] = \frac{\partial }{\partial \theta_i }\left[\int_\Omega {\color{blue}\nabla \cL_\u(\vp)}(x) \dAdpj(x) \dd \mu(x) \right] \\
&=\frac{\partial }{\partial \theta_i }\left[\Braket{ {\color{blue}\nabla \cL_\u}, \dAdpj }_V \right] \\

&=\Braket{ H_V \cL \dAdpi, \dAdpj } _V+ \Braket{ {\color{blue}\nabla \cL_\u}, \frac{\partial^2 A}{\partial \theta_i \partial \theta_j} }_V \notag \\
&= G^{H_\cL} + \Braket{ {\color{blue}\nabla \cL_\u}, H_A}_V
\end{aligned}
$$


<v-click>

$$G_{ij}^{H_\cL} = \int \dAdpi(x) [H_V\cL(\v)](x) \dAdpj(x)\dd \mu(x).$$
</v-click>

<v-click>

$$\cL_\u(\v)=\frac 1 2 \|\u-\v\|^2_{L^2(\Omega)}\quad \quad \quad \longrightarrow \quad \quad \quad H_V\cL(\v)(x)=1$$

</v-click>

<v-click>

$$G_{ij} = \int \left[\dAdpi \dAdpj \right](x)\dd x$$
</v-click>

<v-click>
<div v-motion
  :initial="{ y: -257, x: 357 }"
>
  ________________
</div>


<div v-motion
  :initial="{ y: -259, x: 540 }"
>
  <span v-mark.circle.orange="4"> Model linearization </span> 

</div>


</v-click>
