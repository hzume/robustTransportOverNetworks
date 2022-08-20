---
marp: true
theme: mytheme
math: katex
---
<!-- 
paginate: true 
_class: top
-->

# 研究会 5/31

---

# 背景 1/2

## グラフ上の輸送問題

$$
\begin{align*}
\text{directed graph}\ \ &\mathcal{G} = (\mathcal{V}, \mathcal{E}) \\
\text{nodes}\ \ &\mathcal{V}=\{1,2,\dots, n\}\\
\text{edges}\ \ &\mathcal{E}\sub \mathcal{V}\times\mathcal{V}\\
\text{cost}\ \ &C:\mathcal{E}\rightarrow \mathbb{R}_{\geq0}
\end{align*}
$$
重み付きグラフに対し1からnへ単位質量を輸送するとき、総コストを最小となるようなパスを求める問題を(グラフ上の)最適輸送問題という。

---

# 背景 2/2

これはFord-Fulkersonのアルゴリズムによりフローの問題として解くことができる。
しかし最適なパスのみを用いて輸送するため、パス上のnode,edgeを通れなくなると質量の100%が輸送できなくなる。

Shroding Bridge Problemを用いた手法により、利用可能なパス全てに分散し、かつ最適なパスに最大確率を割り当てるような輸送計画を求めることができる。

---

# 発表の流れ

- 基礎
  - 離散Schrodinger Bridge Problem
  - 時間的一様な解
  - Ruelle-Bwoens random walk
- 応用
  - case1: 強連結,重みなしの場合
  - case2: 強連結でなく,重み付きの場合

---

# 離散Schrodinger Bridge Problem

---

# case1: 強連結,重みなしの場合

隣接行列$A$の要素はすべて非負であり、強連結性から$A^n$の要素はすべて正
$$
A^Tu = \lambda_A u,\ \ Av = \lambda_A v\\
u^Tv = 1\\
\nu_{RB}(i) = u_i v_i
$$
