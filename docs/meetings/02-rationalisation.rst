02 Rationalisation
==================

Corresponding chapters
----------------------

- `Rationalisation <http://vknight.org/gt/chapters/03/>`_

**Duration**: 50 minutes


Objectives
----------

- Be able to identify dominated strategies
- Understand notion of Common knowledge of rationality


Notes
-----


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

- First row strictly dominates second row
- Second column strictly dominates first column

.. math::

   A = \begin{pmatrix}
       2 & 2\\
       -1 & 2
   \end{pmatrix}

- First row weakly dominates second row
- First column weakly dominates second column

.. math::

   A = \begin{pmatrix}
       -1 & 2 & 1\\
       -2 & -2 & 1\\
       1 & 1 & -1\\
   \end{pmatrix}

- First row dominates second row
- First column dominates second column

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

Ask students to repeat the game against each other in groups of two (use "days
of doing the dishes perhaps?").

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
      3\\
      1
      \end{pmatrix}

3. First row dominates third row. Thus the rationalised behaviour is
   :math:`(r_1, c_2)`.


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
