06 Lemke Howson Algorithm
=========================

Corresponding chapters
----------------------

- `The Lemke Howson algorithm <http://vknight.org/gt/chapters/07/>`_

Objectives
----------

- Describe the Lemke Howson algorithm graphically
- Describe integer pivoting

**Duration**: 50 minutes

Notes
-----

Describe the Lemke Howson algorithm
***********************************

Using the polytopes for the matching pennies game:

:math:`\mathcal{P}`:

.. image:: ../assets/activities/matching_pennies_row_best_response_polytope.png
   :width: 500px

:math:`\mathcal{Q}`:

.. image:: ../assets/activities/matching_pennies_col_best_response_polytope.png
   :height: 500px

illustrate the Lemke Howson algorithm:

- :math:`((0, 0), (0, 0))` have labels :math:`\{0, 1\}, \{2, 3\}`. Drop
  :math:`0` in :math:`\mathcal{P}`.
- :math:`\to ((1/2, 0), (0, 0))` have labels :math:`\{1, 2\}, \{2, 3\}`. Drop
  :math:`2` in :math:`\mathcal{Q}`.
- :math:`\to ((1/2, 0), (1/3, 0))` have labels :math:`\{1, 2\}, \{0, 3\}`. Have
  an equilibria.

Try varying other initial labels. Is it possible to arrive at the mixed nash
equilibrium?

Work through integer pivoting
*****************************

Consider Rock Paper Scissors:

.. math::

   A = \begin{pmatrix}
        0 & -1 &  1\\
        1 &  0 & -1\\
       -1 &  1 &  0\\
   \end{pmatrix}\qquad
   B = \begin{pmatrix}
        0 &  1 & -1\\
       -1 &  0 &  1\\
        1 & -1 &  0\\
   \end{pmatrix}\qquad


We see that drawing this would be a pain. Let us build the tableaux, but let us
first scale our payoffs so that all variables are positive (let us add 2 to all
the utilities):

.. math::

   A = \begin{pmatrix}
        2 & 1 & 3\\
        3 & 2 & 1\\
        1 & 3 & 2\\
   \end{pmatrix}\qquad
   B = \begin{pmatrix}
        2 & 3 & 1\\
        1 & 2 & 3\\
        3 & 1 & 2\\
   \end{pmatrix}\qquad

This gives the following tableaux:

.. math::

   T_r = \begin{pmatrix}
       2 &  1 &  3 & 1 & 0 & 0 & 1\\
       3 &  2 &  1 & 0 & 1 & 0 & 1\\
       1 &  3 &  2 & 0 & 0 & 1 & 1\\
   \end{pmatrix}


Following along in :code:`numpy`::

    >>> import numpy as np
    >>> row_tableau = np.array([[2, 1, 3, 1, 0, 0, 1],
    ...                         [3, 2, 1, 0, 1, 0, 1],
    ...                         [1, 3, 2, 0, 0, 1, 1]])

and:

.. math::

   T_c = \begin{pmatrix}
       1 & 0 & 0 &  2 &  1 &  3 & 1\\
       0 & 1 & 0 &  3 &  2 &  1 & 1\\
       0 & 0 & 1 &  1 &  3 &  2 & 1\\
   \end{pmatrix}

Following along in :code:`numpy`::

    >>> col_tableau = np.array([[1, 0, 0, 2, 1, 3, 1],
    ...                         [0, 1, 0, 3, 2, 1, 1],
    ...                         [0, 0, 1, 1, 3, 2, 1]])


The labels of :math:`T_r` are :math:`\{0, 1, 2\}` and the labels of :math:`T_c`
are :math:`\{3, 4, 5\}`.

Let us drop label :math:`0`, so we pivot the first column of :math:`T_r`. The
minimum ratio test gives: :math:`1/3<1/2<1/1` so we pivot on the second row
giving:

.. math::

   T_r = \begin{pmatrix}
       0 &  -1 &  7 & 3 & -2 & 0 & 1\\
       3 &  2  &  1 & 0 & 1  & 0 & 1\\
       0 &  7  &  5 & 0 & -1 & 3 & 2\\
   \end{pmatrix}

Code::

    >>> import nashpy as nash
    >>> dropped_label = nash.integer_pivoting.pivot_tableau(row_tableau,
    ...                                                     column_index=0)
    >>> row_tableau
    array([[ 0, -1,  7,  3, -2,  0,  1],
           [ 3,  2,  1,  0,  1,  0,  1],
           [ 0,  7,  5,  0, -1,  3,  2]])

This has labels :math:`\{1, 2, 4\}` so we need to drop label :math:`4` by
pivoting the fifth column of :math:`T_c`. The minimum ratio test implies that we
pivot on the third row.

.. math::

   T_c = \begin{pmatrix}
       3 & 0 & -1 &  5 &  0 &  7 & 2\\
       0 & 3 & -2 &  7 &  0 &  -1 & 1\\
       0 & 0 & 1  &  1 &  3 &  2 & 1\\
   \end{pmatrix}

Code::

    >>> dropped_label = nash.integer_pivoting.pivot_tableau(col_tableau,
    ...                                                     column_index=4)
    >>> col_tableau
    array([[ 3,  0, -1,  5,  0,  7,  2],
           [ 0,  3, -2,  7,  0, -1,  1],
           [ 0,  0,  1,  1,  3,  2,  1]])

This has labels :math:`\{2, 3, 5\}` so we need to drop :math:`2` by pivoting the
third row of :math:`T_r`. The minimum ratio test implies that we pivot on the
first row:

.. math::

   T_r = \begin{pmatrix}
       0 &  -1 &  7 & 3   & -2 & 0  & 1\\
      21 &  15 &  0 & -3  &  9 & 0  & 6\\
       0 &  54 &  0 & -15 &  3 & 21 & 9\\
   \end{pmatrix}

Code::

    >>> dropped_label = nash.integer_pivoting.pivot_tableau(row_tableau,
    ...                                                     column_index=2)
    >>> row_tableau
    array([[  0,  -1,   7,   3,  -2,   0,   1],
           [ 21,  15,   0,  -3,   9,   0,   6],
           [  0,  54,   0, -15,   3,  21,   9]])

This has labels :math:`\{1, 3, 4\}` so we need to drop :math:`3` by pivoting the
fourth column of :math:`T_c`. The minimum ratio test implies that we pivot on
the second row:

.. math::

   T_c = \begin{pmatrix}
       21 & -15 & 3  &  0 &  0  &  54 & 9\\
       0  & 3   & -2 &  7 &  0  &  -1 & 1\\
       0  & -3  & 9  &  0 &  21 &  15 & 6\\
   \end{pmatrix}

Code::

    >>> dropped_label = nash.integer_pivoting.pivot_tableau(col_tableau,
    ...                                                     column_index=3)
    >>> col_tableau
    array([[ 21, -15,   3,   0,   0,  54,   9],
           [  0,   3,  -2,   7,   0,  -1,   1],
           [  0,  -3,   9,   0,  21,  15,   6]])

This has labels :math:`\{1, 2, 5\}` so we need to drop :math:`1` by pivoting the
second column of :math:`T_r`. The minimum ratio test implies that we pivot on
the third row:

.. math::

   T_r = \begin{pmatrix}
       0 &  0  &  378 & 147   & -105 & 21  & 63\\
      1134 &  0 &  0 & 63  &  441 & -315  & 189\\
       0 &  54 &  0 & -15 &  3 & 21 & 9\\
   \end{pmatrix}


Code::

    >>> dropped_label = nash.integer_pivoting.pivot_tableau(row_tableau,
    ...                                                     column_index=1)
    >>> row_tableau
    array([[   0,    0,  378,  147, -105,   21,   63],
           [1134,    0,    0,   63,  441, -315,  189],
           [   0,   54,    0,  -15,    3,   21,    9]])

This has labels :math:`\{3, 4, 5\}` so we need to drop :math:`5` by pivoting the
sixth column of :math:`T_c`. The minimum ratio test implies that we pivot on
the first row:

.. math::

   T_c = \begin{pmatrix}
       21 & -15  & 3  &  0 &  0  &  54 & 9\\
       21  & 147 & -105 &  378 &  0  &  0 & 63\\
       -315  & 63   & 441  &  0 &  1134 &  0 & 189\\
   \end{pmatrix}

Code::

    >>> dropped_label = nash.integer_pivoting.pivot_tableau(col_tableau,
    ...                                                     column_index=5)
    >>> col_tableau
    array([[  21,  -15,    3,    0,    0,   54,    9],
           [  21,  147, -105,  378,    0,    0,   63],
           [-315,   63,  441,    0, 1134,    0,  189]])

This has labels :math:`\{0, 1, 2\}` so we have a Nash equilibrium with vertices:

.. math::

   \left((189/1134, 9/54, 63/378), (63/378, 189/1134, 9/54)\right) = \left((1/6, 1/6, 1/6), (1/6, 1/6, 1/6)\right)

Which in turn corresponds to the expected equilibrium:

.. math::

   \left((1/3, 1/3, 1/3, (1/3, 1/3, 1/3)\right)


- Mention how different pivoting methods are fine, doing it this way ensures
  everything is an integer which is also more efficient for a computer.
