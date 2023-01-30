AD - Moran process
==================

**Duration**: 25 minutes


Objectives
----------

- Compute the probability of fixation in the Hawk Dove game using the formula.

Notes
-----

For:

.. math::

   A = \begin{pmatrix}
       0 & 3\\
       1 & 2
   \end{pmatrix}

Ask students to work in pairs, using the formula to compute :math:`x_1`.

This is given by:

.. math::

   \begin{align}
       f_{1i} &= \frac{3(N-i)}{N - 1}=3\frac{N-i}{N-1}\\
       f_{2i} &= \frac{i+2(N - i -1)}{N - 1}=\frac{2N-2-i}{N - 1}\\
   \end{align}

This gives (for :math:`N=4`):

+------------------+--------------+--------------+--------------+
|                  | :math:`i=1`  | :math:`i=2`  | :math:`i=3`  |
+==================+==============+==============+==============+
| :math:`f_{1i}`   |      3       |       2      |       1      |
+------------------+--------------+--------------+--------------+
| :math:`f_{2i}`   |      5/3     |       4/3    |       1      |
+------------------+--------------+--------------+--------------+
| :math:`\gamma_i` |      5/9     |       2/3    |       1      |
+------------------+--------------+--------------+--------------+

Thus:

.. math::

  x_1 = \frac{1}{1 + 5/9 + 5/9\times2/3 +5/9\times2/3\times1}=\frac{1}{62/27}=\frac{27}{62}\approx.44
