# Minimization problem
Objective: approximate $u\in V$ by $v\in\cM$.

<div class="grid grid-cols-2">

<h3 style="text-align: center">Continuous problem</h3>
<h3 style="text-align: center">Discrete problem</h3>
</div>

<div class="grid grid-cols-2">
$$
\begin{aligned}
\cL_\u(\v)&=\frac 1 2 \|\u-\v\|^2_V \\
&= \frac 1 2 \langle \u-\v, \u-\v\rangle_V \\
&= \frac 1 2 \int (\u(x)-\v(x))^2\dd\mu(x)
\end{aligned}
$$
$$
\begin{aligned}
\cL_\u(\v)&=\frac 1 2 \|\u-\v\|^2_m \\
&= \frac 1 2 \langle \u-\v, \u-\v\rangle_m \\
&= \frac{1}{2m} \sum_{i=1}^{m} (\u(x_i)-\v(x_i))^2
\end{aligned}
$$
</div>

___
___
___

<div class="grid grid-cols-2">

<h3 style="text-align: center">Functional perspective</h3>
<h3 style="text-align: center">Parameter perspective</h3>
</div>

<div class="grid grid-cols-2">
<div>

$$
\begin{aligned}
{\colorM v^*}&=\underset{\v\in\cM}{\argmin} \; \cL_\u(\v)
\end{aligned}
$$
</div>

<div>

$$
\begin{aligned}
\theta^*&=\underset{\theta\in\R^p}{\argmin} \; \cL_\u({\colorM A(\theta)}) \\
\end{aligned}
$$
$$
\cL_\u({\colorM A(\theta)})=(\cL_\u \circ A) (\theta) =: L(\theta) $$

</div>
</div>
