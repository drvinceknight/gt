01 Strategies and utilities
===========================

Corresponding chapters
----------------------

- `Calculating utilities of strategies <http://vknight.org/gt/chapters/03/>`_
- `Rationalisation <http://vknight.org/gt/chapters/04/>`_


Objectives
----------

- Define mixed strategies
- Understand utility calculation for mixed strategies
- Understand utility calculation as a linear algebraic construct
- Be able to identify dominated strategies
- Understand notion of Common knowledge of granularity


Notes
-----

Utility calculations
********************

Use :download:`matching pennies
form<../assets/activities/matchingpennies.pdf>` have students play in pairs.
Following each game:

- Ask how many people won?
- Ask why they won?

Mixed strategies
****************

Look at definition for mixed strategies.

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
[0,1]_{\mathbb{R}}^{m}` to :math:`\mathbb{R}^2`: the utility space.

Equivalently, if :math:`S_r, S_c` are the strategy spaces of the row/column
player:

.. math::

   (A, B): S_r\times S_c \to \mathbb{R} ^2

We can use games defined in :code:`nashpy` in that way::

    >>> import nash
    >>> game = nash.Game(A, B)
    >>> game[sigma_r, sigma_c]
    array([ 0.08, -0.08])


Rationalisation of strategies
*****************************

Identify two volunteers and play a sequence of zero sum games where they play as
a team against me. The group is the row player.

.. math::

   A = \begin{pmatrix}
       1 & -1\\
       -1 & 2
   \end{pmatrix}

(No dominated strategy)

.. math::

   A = \begin{pmatrix}
       1 & 2\\
       -1 & 2
   \end{pmatrix}

(First column weakly dominates second column)

.. math::

   A = \begin{pmatrix}
       1 & -1\\
       -1 & -3
   \end{pmatrix}

(First row strictly dominates second row)
(Second column strictly dominates first column)

.. math::

   A = \begin{pmatrix}
       2 & 2\\
       -1 & 2
   \end{pmatrix}

(First row weakly dominates second row)
(First column weakly dominates second column)

.. math::

   A = \begin{pmatrix}
       -1 & 2 & 1\\
       -2 & -2 & 1\\
       1 & 1 & -1\\
   \end{pmatrix}

(First row dominates second row)
(First column dominates second column)

Now pit the two players against each other, the utilities represent the share of
the total amount of chocolates/sweets gathered so far:

.. math::

   A = \begin{pmatrix}
       1 & 0\\
       1.5 & .5
   \end{pmatrix}\qquad
   B = \begin{pmatrix}
       1 & 1.5\\
       0 & .5
   \end{pmatrix}


Capture all of the above (on the white board) and discuss each action and why
they were taken.


Iterated elimination of dominated strategies
********************************************

As a class work through the following example.

.. math::

   A = \begin{pmatrix}
   2 & 5 \\
   1 & 2 \\
   7 & 3
   \end{pmatrix}\qquad
   B = \begin{pmatrix}
   0 & 3 \\
   6 & 1 \\
   0 & 1
   \end{pmatrix}

1. First row dominates second row

   .. math::
      A = \begin{pmatrix}
      2 & 5 \\
      7 & 3
      \end{pmatrix}\qquad
      B = \begin{pmatrix}
      0 & 3 \\
      0 & 1
      \end{pmatrix}

2. Second column dominates first column

   .. math::
      A = \begin{pmatrix}
      2\\
      7
      \end{pmatrix}\qquad
      B = \begin{pmatrix}
      0\\
      0
      \end{pmatrix}

3. Second (third) row dominates first row. Thus the rationalised behaviour is
   :math:`(r_3, c_1)`.


Now return to the last example played as a pair:

.. math::

   A = \begin{pmatrix}
       -1 & 2 & 1\\
       -2 & -2 & 1\\
       1 & 1 & -1\\
   \end{pmatrix}\qquad
   B = \begin{pmatrix}
       1 & -2 & -1\\
       2 & 2 & -1\\
       -1 & -1 & 1\\
   \end{pmatrix}

1. The first row/column weakly dominate the second row/column:

   .. math::
      A = \begin{pmatrix}
      -1 & 1 \\
      1 & -1
      \end{pmatrix}\qquad
      B = \begin{pmatrix}
      1 & -1 \\
      -1 & 1
      \end{pmatrix}

There is nothing further that we can do here.
