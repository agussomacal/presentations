# Mackey Glass
A less toy example $[$Park, H, S.-I Amari, and K Fukumizu (2000)$]$.


<div>

Mackey Glass caotic time series: 
- $z(t+1) = (1-b)z(t) + a \frac{z(t-\tau)}{1+z(t-\tau)^{10}}$
- Input: $z(t), z(t-6), z(t-12), z(t-18)$
- Output: $z(t+6)$

Model (shallow NN $10$ neurons): $\vp: \R^4 \to \R$ 

</div>

<div class="absolute left-110px bottom-10px">
<img src="./../figures/MackeyGlass/dataset_0.png" alt="drawing" width="250" style="float: center">
</div>

::right::

<div v-click="[0, 1]">
<div class="absolute right-20px bottom-10px">
<img src="./../figures/MackeyGlass/TrajectoriesMackeyGlass_ntrain500Test150_0.png" alt="drawing" width="500" style="float: right">
</div>
</div>

<div v-click="[1, 2]">
<div class="absolute right-20px bottom-10px">
<img src="./../figures/MackeyGlass/TrajectoriesMackeyGlass_ntrain500Test50_0.png" alt="drawing" width="500" style="float: right">
</div>
</div>

<div v-click="2">
<div class="absolute right-20px bottom-10px">
<img src="./../figures/MackeyGlass/TrajectoriesMackeyGlass_ntrain500Test500_0.png" alt="drawing" width="500" style="float: right">
</div>
</div>
