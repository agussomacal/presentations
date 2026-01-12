---
# You can also start simply with 'default'
theme: seriph
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
background: "./../figures/LagunaCreton.jpg"
# some information about your slides (markdown enabled)
title: Welcome to Slidev
info: |
  ## Momentum NGD
# apply unocss classes to the current slide
class: text-center
# https://sli.dev/features/drawing
drawings:
  persist: false
# slide transition: https://sli.dev/guide/animations.html#slide-transitions
transition: slide-left
# enable MDC Syntax: https://sli.dev/features/mdc
mdc: true

# open graph
# seoMeta:
#  ogImage: https://cover.sli.dev
---

# Natural gradient descent with momentum

Séminaire de mathématiques appliquées du LMJL, 2026 $\\$

**Agustín Somacal**

In collaboration with **Anthony Nouy** and **Joel Soffo**

École Centrale de Nantes

Laboratoire de Mathématiques Jean Leray

<!--
The last comment block of each slide will be treated as slide notes. It will be visible and editable in Presenter Mode along with the slide. [Read more in the docs](https://sli.dev/guide/syntax.html#notes)
-->

<!--
======== Outline ========
-->

---
src: ./pages/s01_outline.md
hide: false
transition: slide-left
---


<!-- ======== Problem formulation ======== -->
---
src: ./pages/s02_01_problem_formulation.md
hide: false
transition: none
---
---
src: ./pages/s02_02_problem_formulation.md
hide: false
transition: none
---
---
src: ./pages/s02_03_problem_formulation.md
hide: false
transition: slide-left
---


<!-- ======== Minimizatioin problem ======== -->
---
src: ./pages/s03_01_minimization_problem.md
hide: false
transition: none
---
---
src: ./pages/s03_02_minimization_problem.md
hide: false
transition: none
---
---
src: ./pages/s03_03_minimization_problem.md
hide: false
transition: slide-left
---


<!-- ======== Gradien descent ======== -->
---
src: ./pages/s04_01_gradient_descent.md
hide: false
transition: none
---
---
src: ./pages/s04_02_gradient_descent.md
hide: false
transition: none
---
---
src: ./pages/s04_03_gradient_descent.md
hide: false
transition: none
---
---
src: ./pages/s04_04_gradient_descent.md
hide: false
transition: none
---
---
src: ./pages/s04_05_gradient_descent.md
hide: false
transition: none
---
---
src: ./pages/s04_06_gradient_descent.md
hide: false
transition: none
---
---
src: ./pages/s04_07_newtons_method.md
hide: false
transition: slide-left
---


<!-- ======== Natural gradient ======== -->
---
src: ./pages/s05_01_functional_gradient.md
hide: false
transition: none
---


---
src: ./pages/s05_03_natural_gradient.md
hide: false
transition: slide-left
---

<!-- ======== Natural gradient flow ======== -->
---
src: ./pages/s06_01_natural_gradient_flow.md
hide: false
transition: none
---
---
src: ./pages/s06_02_natural_gradient_flow.md
hide: false
transition: slide-left
---


<!-- ======== Toy example ======== -->
---
src: ./pages/s07_01_toy_example_GD.md
hide: false
transition: none
---
---
src: ./pages/s07_02_toy_example_biasedGD.md
hide: false
transition: none
---
---
src: ./pages/s07_03_toy_example_NGD.md
hide: false
transition: none
---
---
src: ./pages/s07_04_toy_example_kernel.md
hide: false
transition: none
---
---
src: ./pages/s07_05_toy_example_NHGD.md
hide: false
transition: none
---
---
src: ./pages/s07_06_toy_example_Newton.md
hide: false
transition: none
---
---
src: ./pages/s07_07_toy_example_Quadratic.md
hide: false
transition: slide-left
---

<!-- ======== ROMs example ======== -->
---
src: ./pages/s08_01_ngd_rom.md
hide: false
transition: none
layout: two-cols
---

---
src: ./pages/s08_02_ngd_rom.md
hide: false
transition: none
---


<!-- ======== Why momentum ======== -->
---
src: ./pages/s08_01_why_momentum.md
hide: false
transition: slide-left
---

<!-- ======== Momentum dynamics ======== -->
---
src: ./pages/s09_01_momentum_dynamics.md
hide: false
transition: slide-up
---

---
src: ./pages/s09_02_momentum_dynamics.md
hide: false
transition: none
---

---
src: ./pages/s09_03_momentum_dynamics.md
hide: false
transition: slide-left
---


<!-- ======== Momentum example ======== -->
---
src: ./pages/s10_01_toy_example_local_minima.md
hide: false
transition: none
---


<!-- ======== Momentum real example ======== -->
---
src: ./pages/s11_01_pinns.md
hide: false
transition: none
layout: two-cols
---

---
src: ./pages/s12_01_pinns_nolin.md
hide: false
transition: none
layout: two-cols
---

---
src: ./pages/s13_01_xor.md
hide: false
transition: slide-left
layout: two-cols
---




- ======== Final slides ======== -->
---
hide: false
layout: default
---
# Conclusion
What is done, what is still to be done.

<br></br>

We saw how to build a **Natural inertial dynamics** for gradient optimization on non linear approximation manifolds.

<br></br>

Some directions

- Step-size adaptivity

- Theoretical questions: convergence? optimality?


<!-- ======== Final slides ======== -->
---
hide: false
layout: default
---

<h3 style="text-align: center"> Thank you! </h3>

<br></br>
<br></br>

<div class="grid grid-cols-2">
<div>

(2024) Schwencke N., Furtlehner C. $\text{}\\$
(2023) Müller J., Zeinhofer M. 

(2024) R. Gruhlke, A. Nouy, P. Trunschke.

(2020) J. Martens.

(2000) H. Park, S. Amari, K. Fukumizu.

(1998) S. Amari. 

(1983) Y. Nesterov.

(1964) B.T. Polyak.
</div>

<div>

<br></br>
NGD and PINNs.

NGD and optimal sampling.

NGD Review.

NGD Experiments.

NGD Initial paper.

Nestorov acceleration.

Heavy Ball acceleration.
</div>
</div>

<div style="text-align: center">  <PoweredBySlidev mt-10 /> </div>
