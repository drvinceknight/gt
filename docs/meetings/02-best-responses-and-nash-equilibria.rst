02 Best responses and Nash equilibrium
======================================

Corresponding chapters
----------------------

- `Nash equilibria <http://vknight.org/gt/chapters/05/>`_


Objectives
----------

- Define best responses
- Identify best responses in pure strategies
- Identify best responses against mixed strategies
- Theorem: best response condition
- Definition of Nash equilibria


Notes
-----

Best response against mixed strategies
**************************************

Use :download:`best responses against mixed
strategies<../assets/activities/bestresponsetomixedstrategies.pdf>` have
students play against a mixed strategy (sample using Python).

Discuss the definition of a best response. Identify best responses for the game
considered:

.. math::

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

Consider the best responses against a mixed strategy:

- Assume :math:`\sigma_r=(x, 1-x)`
- Assume :math:`\sigma_c=(y, 1-y)`

We have:

.. math::

   A\sigma_c^T = \begin{pmatrix}
   4y-2\\
   1-2y
   \end{pmatrix}\qquad
   \sigma_rB = \begin{pmatrix}
   1-3x & 3x-1
   \end{pmatrix}


Here is the code to do this calculation with :code:`sympy`::

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


Plot these two things::

   >>> import matplotlib.pyplot as plt
   >>> ys = [0, 1]
   >>> row_us = [[(A * sigma_c)[i].subs({y: val}) for val in ys] for i in range(2)]
   >>> plt.plot(ys, row_us[0], label="$(A\sigma_c^T)_1$")
   [<matplotlib...>]
   >>> plt.plot(ys, row_us[1], label="$(A\sigma_c^T)_2$")
   [<matplotlib...>]
   >>> plt.xlabel("$\sigma_c=(y, 1-y)$")
   <matplotlib...>
   >>> plt.title("Utility to player 1")
   <matplotlib...>
   >>> plt.legend();
   <matplotlib...>

   >>> xs = [0, 1]
   >>> row_us = [[(sigma_r * B)[j].subs({x: val}) for val in xs] for j in range(2)]
   >>> plt.plot(ys, row_us[0], label="$(\sigma_rB)_1$")
   [<matplotlib...>]
   >>> plt.plot(ys, row_us[1], label="$(\sigma_rB)_2$")
   [<matplotlib...>]
   >>> plt.xlabel("$\sigma_r=(x, 1-x)$")
   <matplotlib...>
   >>> plt.title("Utility to column player")
   <matplotlib...>
   >>> plt.legend();
   <matplotlib...>

Conclude:

.. math::

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


Some examples:

- If :math:`\sigma_r=(2/3, 1/3)` then :math:`\sigma_r^*=(0, 1)`.
- If :math:`\sigma_r=(1/3, 2/3)` then *any* strategy is a best response.


**Discuss best response condition theorem and proof.**

This gives a finite condition that needs to be checked. To find the best
response against :math:`\sigma_c` we **potentially** would need to check all
infinite possibilities alternatives to :math:`\sigma_r^*`. Now we simply need to
check the values of the pure strategies against :math:`sigma_c`:

- Either there will be a single **pure** best response;
- There will be multiple **pure** strategies for which the row player is
  indifferent.

Return to previous example:if :math:`\sigma_r=(1/3, 2/3)` then
:math:`(\sigma_rB)=(0, 0)` thus :math:`(\sigma_rB)_j = 0` for all :math:`j`.

:math:`(\sigma_r, \sigma_c) = ((1/3, 1/2), (1/2, 1/2))` is a pair of best
responses.

**Discuss definition of Nash equilibria**.

Explain how the best response condition theorem can be used to find NE.

- All possible supports (strategies that are played with positive probabilities)
  can be checked.
- All pure strategies must have maximum and equal payoff.
