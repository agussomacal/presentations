# *Online learning* in Reduced Order Modelling
Natural Gradient for *online learning* in non-linear Reduced Order Modelling.

_____

<div style="text-align: center">
 
#### Korteweg-de Vries (KdV) equation  

$$\frac{\partial \u}{\partial t}+4\u\frac{\partial \u}{\partial x}+\frac{\partial^3 \u}{\partial x^3}$$
</div>

_____

<div>


</div>

$${\colorM v_{\text{lin}}}(x) = \sum_{i=1}^n \theta_i{\colorV \phi_i}(x)$$
$${\colorM v_{\text{non-lin}}}(x) = \sum_{i=1}^n \theta_i{\colorV \phi_i}(x) + \sum_{j=n+1}^N \mathcal{NN}(\theta)_j{\colorV \phi_j}(x)$$


::right::
<div class="absolute top-100px left-500px">
<img src="./../figures/ROMs/reconstruction_nb_points128_gt.png" alt="drawing" width="450" style="float: center">
</div>

<v-click>
<div class="absolute top-100px left-500px">
<img src="./../figures/ROMs/reconstruction_nb_points128_linear.png" alt="drawing" width="450" style="float: right">
</div>
</v-click>

<v-click>
<div class="absolute top-100px left-500px">
<img src="./../figures/ROMs/reconstruction_nb_points128_non_linear.png" alt="drawing" width="450" style="float: right">
</div>
</v-click>

<v-click>
<div class="absolute top-100px left-500px">
<img src="./../figures/ROMs/reconstruction_nb_points20.png" alt="drawing" width="450" style="float: right">
</div>
</v-click>

<v-click>
<div class="absolute top-100px left-500px">
<img src="./../figures/ROMs/reconstruction_nb_points20_GD.png" alt="drawing" width="450" style="float: right">
</div>
</v-click>

<v-click>
<div class="absolute top-100px left-500px">
<img src="./../figures/ROMs/reconstruction_nb_points20_NGD.png" alt="drawing" width="450" style="float: right">
</div>
</v-click>
