---
layout: class-notes
title: "Best responses"
tag: best-responses
---

**Duration**: 100 minutes

## Objectives

- Define best responses
- Identify best responses in pure strategies
- Identify best responses against mixed strategies
- Theorem: best response condition
- Definition of Nash equilibria

## Notes

Discuss best response in pure strategies.

### Best response against mixed strategies

Use [best responses]({{site.baseurl}}/assets/activities/best_responses/main.pdf) have students play against a mixed strategy:

    >>> import random
    >>> random.seed(0)  # Don't seed in class
    >>> ["r_2", "r_1"][random.random() < 0.8]  # 80 percent chance of r_2
    'r_2'

Discuss the definition of a best response. Identify best responses for
the game considered:

$$
\begin{aligned}
A=
\begin{pmatrix}
    \underline{2} & -2\\
    -1 & \underline{1}\\
\end{pmatrix}
\qquad
B=
\begin{pmatrix}
    -2 & \underline{2}\\
    \underline{1} & -1\\
\end{pmatrix}
\end{aligned}
$$

Consider the best responses against a mixed strategy:

- Assume $\sigma_r=(x, 1-x)$
- Assume $\sigma_c=(y, 1-y)$

We have:

$$
\begin{aligned}
A\sigma_c^T = \begin{pmatrix}
4y-2\\
1-2y
\end{pmatrix}\qquad
\sigma_rB = \begin{pmatrix}
1-3x & 3x-1
\end{pmatrix}
\end{aligned}
$$

Here is the code to do this calculation with `sympy`:

    >>> import sympy as sym
    >>> import numpy as np
    >>> x, y = sym.symbols('x, y')
    >>> A = sym.Matrix([[2, -2], [-1, 1]])
    >>> B = - A
    >>> sigma_r = sym.Matrix([[x, 1-x]])
    >>> sigma_c = sym.Matrix([y, 1-y])
    >>> A * sigma_c, sigma_r * B
    (Matrix([
    [ 4*y - 2],
    [-2*y + 1]]), Matrix([[-3*x + 1, 3*x - 1]]))

Plot these two things:

    >>> import matplotlib.pyplot as plt
    >>> ys = [0, 1]
    >>> row_us = [[(A * sigma_c)[i].subs({y: val}) for val in ys] for i in range(2)]
    >>> plt.plot(ys, row_us[0], label="$(A\sigma_c^T)_1$")
    [<matplotlib...>]
    >>> plt.plot(ys, row_us[1], label="$(A\sigma_c^T)_2$")
    [<matplotlib...>]
    >>> plt.xlabel("$\sigma_c=(y, 1-y)$")  # doctest: +SKIP
    >>> plt.title("Utility to player 1")  # doctest: +SKIP
    >>> plt.legend(); # doctest: +SKIP


    >>> xs = [0, 1]
    >>> row_us = [[(sigma_r * B)[j].subs({x: val}) for val in xs] for j in range(2)]
    >>> plt.plot(ys, row_us[0], label="$(\sigma_rB)_1$")
    [<matplotlib...>]
    >>> plt.plot(ys, row_us[1], label="$(\sigma_rB)_2$")
    [<matplotlib...>]
    >>> plt.xlabel("$\sigma_r=(x, 1-x)$")  # doctest: +SKIP
    >>> plt.title("Utility to column player")  # doctest: +SKIP
    >>> plt.legend();  # doctest: +SKIP

Conclude:

$$
\begin{aligned}
\sigma_r^* =
\begin{cases}
    (1, 0),&\text{ if } y > 1/2\\
    (0, 1),&\text{ if } y < 1/2\\
    \text{indifferent},&\text{ if } y = 1/2
\end{cases}
\qquad
\sigma_c^* =
\begin{cases}
    (0, 1),&\text{ if } x > 1/3\\
    (1, 0),&\text{ if } x < 1/3\\
    \text{indifferent},&\text{ if } x = 1/3
\end{cases}
\end{aligned}
$$

Some examples:

- If $\sigma_r=(2/3, 1/3)$ then $\sigma_c^*=(0, 1)$.
- If $\sigma_r=(1/3, 2/3)$ then _any_ strategy is a best response.

**Discuss best response condition theorem and proof.**

This gives a finite condition that needs to be checked. To find the best
response against $\sigma_c$ we **potentially** would need to check all
infinite possibilities alternatives to $\sigma_r^*$. Now we simply need
to check the values of the pure strategies against $\sigma_c$:

- Either there will be a single **pure** best response;
- There will be multiple **pure** strategies for which the row player
  is indifferent.

Return to previous <example:if> $\sigma_r=(1/3, 2/3)$ then
$(\sigma_rB)=(0, 0)$ thus $(\sigma_rB)_j = 0$ for all $j$.

$(\sigma_r, \sigma_c) = ((1/3, 1/2), (1/2, 1/2))$ is a pair of best
responses.

**Discuss definition of Nash equilibria**.

Explain how the best response condition theorem can be used to find NE.

- All possible supports (strategies that are played with positive
  probabilities) can be checked.
- All pure strategies must have maximum and equal payoff.
