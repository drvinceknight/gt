01 Strategies and utilities
===========================

Corresponding chapters
----------------------

- `Calculating utilities of strategies <http://vknight.org/gt/chapters/02/>`_

**Duration**: 50 minutes

Objectives
----------

- Define strategies
- Understand utility calculation for strategies
- Understand utility calculation as a linear algebraic construct


Notes
-----

Utility calculations
********************

Use [matching pennies](../assets/activities/matchingpennies.pdf) have students play in pairs.
Following each game:

- Ask how many people won?
- Ask why they won?

Strategies
**********

Look at definition for strategies.

Consider:

.. math::

   A =
   \begin{pmatrix}
       2 & -2\\
       -1 & 1
   \end{pmatrix}\qquad
   B =
   \begin{pmatrix}
       -2 & 2\\
       1 & -1
   \end{pmatrix}

Let us assume we have :math:`\sigma_r=(.3, .7)` and :math:`\sigma_c=(.1, .9)`:


.. math::

   u_r(\sigma_r, \sigma_c) = 0.3 \times 0.1 \times 2 + 0.3 \times 0.9 \times
   (-2) + 0.7 \times 0.1 \times (-1) + 0.7 \times 0.9 \times 1 = 0.08

because the game is zero sum we immediately know:

.. math::
   u_c(\sigma_r, \sigma_c) = -0.08


This corresponds to the linear algebraic multiplication:

.. math::

   u_r(\sigma_r, \sigma_c) = \sigma_r A \sigma_c^T

.. math::

   u_c(\sigma_r, \sigma_c) = \sigma_r B \sigma_c^T

(Go through this on the board, make sure students are comfortable.)

This can be done straightforwardly using :code:`numpy`::

    >>> import numpy as np
    >>> A = np.array([[2, -2], [-1, 1]])
    >>> B = np.array([[-2, 2], [1, -1]])
    >>> sigma_r = np.array([.3, .7])
    >>> sigma_c = np.array([.1, .9])
    >>> np.dot(sigma_r, np.dot(A, sigma_c)), np.dot(sigma_r, np.dot(B, sigma_c))
    (0.079..., -0.079...)


Strategy profiles as coordinates on a game
******************************************

One way to thing of any game :math:`(A, B)\in{\mathbb{R}^{m \times n}}^2` is as
a mapping from the set of strategies :math:`[0,1]_{\mathbb{R}}^{m}\times
[0,1]_{\mathbb{R}}^{n}` to :math:`\mathbb{R}^2`: the utility space.

Equivalently, if :math:`S_r, S_c` are the strategy spaces of the row/column
player:

.. math::

   (A, B): S_r\times S_c \to \mathbb{R} ^2

We can use games defined in :code:`nashpy` in that way::

    >>> import nashpy as nash
    >>> game = nash.Game(A, B)
    >>> game[sigma_r, sigma_c]
    array([ 0.08, -0.08])
