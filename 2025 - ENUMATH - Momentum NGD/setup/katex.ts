import { defineKatexSetup } from '@slidev/types'

export default defineKatexSetup(() => {
  return {
    maxExpand: 2000,
    macros: {
    "\\cL": "\\mathcal{L}",
    "\\cT": "\\mathcal{T}",
    "\\cM": "\\mathcal{M}",
    "\\cK": "\\mathcal{K}",
    "\\R": "\\mathbb{R}",
    "\\Q": "\\mathbb{Q}",
    "\\N": "\\mathbb{N}",
    "\\Z": "\\mathbb{Z}",
    "\\dd": "\\mathrm{d}",
    "\\be": "\\begin{equation}",
    "\\ee": "\\end{equation}",
    "\\dist": "{\\text{dist}}",
    "\\span": "{\\text{span}}",
    "\\argmin": "{\\text{arg}\\,\\text{min}}",
    "\\colorV": "\\color{blue}",
    "\\colorM": "\\color{red}",
    "\\colorT": "\\color{green}",
    "\\colorTprev": "\\color{purple}",
    "\\u": "{\\colorV u}",
    "\\params": "\\theta",
    "\\v": "{\\colorM v}",
    "\\vp": "{\\colorM v_{\\params}}",
    "\\vk": "{\\colorM v_{k}}",
    "\\vkprev": "{\\colorTprev v_{k-1}}",
    "\\dLdpj": "\\frac{\\partial \\cL}{\\partial \\params_j}",
    "\\dAdpi": "{\\colorT \\frac{\\partial A}{\\partial \\params_i}}",
    "\\dAdpj": "{\\colorT \\frac{\\partial A}{\\partial \\params_j}}",
    "\\dAdp": "{\\colorT \\frac{\\partial A}{\\partial \\params}}",
    "\\GradP": "\\nabla_\\params",
    "\\LossGrad": "\\GradP \\cL",
    "\\LossVGrad": "{\\colorV \\nabla \\cL}",
    "\\kettheta": "|\\theta \\rangle",
    "\\bratheta": "\\langle \\theta",
    "\\ketthetai": "|\\theta_i \\rangle",
    "\\brathetai": "\\langle \\theta_i",
    "\\ketu": "|u \\rangle",
    "\\brau": "\\langle u"
  }
  }
})
