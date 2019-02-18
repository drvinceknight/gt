05 Best response polytopes
==========================

Corresponding chapters
----------------------

- `Best response polytopes <http://vknight.org/gt/chapters/06/>`_

**Duration**: 100 minutes

Objectives
----------

- Define the best response polytopes (using both definitions: convex hull and
  halfspaces).
- Labelling of vertices
- Equivalence between equilibrium and fully labeled pair
- Vertex enumeration

Notes
-----

Defining best response polytopes
********************************

Discuss what an average is. Place this in the context of the line between two
points. Weighted averages of two points are just a line. So an average is just
a probability distribution.
Expand this notion to the average over **two points**. How would you take the
weighted average between three points :math:`x, y, z`:

.. math::

   \lambda_1 x + \lambda_2 y + \lambda_3 z

This corresponds to something like:

.. image:: ../assets/activities/triangular_convex_hull.png
   :width: 500px

Explain how another definition for that space would be to draw inequalities on
our variables.
Give definition of best response polytopes for a game. Illustrate this with
the battle of the sexes game (scaled):

.. math::

   A = \begin{pmatrix}
   3 & 1\\
   0 & 2\\
   \end{pmatrix}
   \qquad
   B = \begin{pmatrix}
   2 & 1\\
   0 & 3\\
   \end{pmatrix}

**Go over the definition of the best response polytopes**.

The *row* best response polytope is given by:

.. math::

   \mathcal{P} = \left\{x\in\mathbb{R}^{m}\;|\;x\geq 0; xB\leq 1\right\}

This corresponds to the following inequalities:

- :math:`x_1\geq 0`
- :math:`x_2\geq 0`
- :math:`2x_1\leq 1`
- :math:`x_1+3x_2\leq 1`

From this we can identify the vertices:

- :math:`(x_1, x_2)=(0,0)`
- :math:`(x_1, x_2)=(1/2,0)`
- :math:`(x_1, x_2)=(0,1/3)`
- :math:`(x_1, x_2)=(1/2,1/6)`

This can be confirmed using :code:`nashpy`::

    >>> import numpy as np
    >>> import nashpy as nash
    >>> B = np.array([[2, 1], [0, 3]])
    >>> halfspaces = nash.polytope.build_halfspaces(B.transpose())
    >>> for v, l in nash.polytope.non_trivial_vertices(halfspaces):
    ...     print(v)
    [ 0.5  0. ]
    [ 0.          0.333...]
    [ 0.5         0.166...]

The *column* best response polytope is given by:

.. math::

   \mathcal{Q} = \left\{y\in\mathbb{R}^{m}\;|\;Ay\leq 1; y\geq 0\right\}

This corresponds to the following inequalities:

- :math:`3y_1+y_2\leq 1`
- :math:`2y_2\leq 1`
- :math:`y_1\geq 0`
- :math:`y_2\geq 0`

From this we can identify the vertices:

- :math:`(y_1, y_2)=(0,0)`
- :math:`(y_1, y_2)=(1/3,0)`
- :math:`(y_1, y_2)=(0,1/2)`
- :math:`(y_1, y_2)=(1/6,1/2)`

Confirmed::

    >>> import numpy as np
    >>> A = np.array([[3, 1], [0, 2]])
    >>> halfspaces = nash.polytope.build_halfspaces(A)
    >>> for v, l in nash.polytope.non_trivial_vertices(halfspaces):
    ...     print(v)
    [ 0.333...  0.        ]
    [ 0.   0.5]
    [ 0.1666...  0.5       ]

Pair activity
*************

Ask everyone to draw these two polytopes.

Now describe how we label the vertices: **using the same ordering as the
inequalities** (starting at 0), a vertex has the label corresponding to that
inequality if it is a strict equality.

:math:`\mathcal{P}`:

.. image:: ../assets/activities/matching_pennies_row_best_response_polytope.png
   :width: 500px

:math:`\mathcal{Q}`:

.. image:: ../assets/activities/matching_pennies_col_best_response_polytope.png
   :height: 500px

Explain that what these polytopes represent is the scaled strategies when
players maximum utilities are 1. So given, the action of an opponent, if the
players' utility is 1 they are playing a best response.

Ask everyone to fill in a table for every vertex:

For :math:`\mathcal{P}`:

- :math:`(0, 1/3)`:

  - Labels: :math:`\{0, 3\}`
  - Strategy: :math:`(0, 1)`
  - Support: :math:`\{r_2\}`
  - Best response: :math:`\{c_2\}`

- :math:`(1/2, 1/6)`:

  - Labels: :math:`\{2, 3\}`
  - Strategy: :math:`(3/4, 1/4)`
  - Support: :math:`\{r_1, r_2\}`
  - Best response: :math:`\{c_1, c_2\}`

- :math:`(1/2, 0)`:

  - Labels: :math:`\{1, 2\}`
  - Strategy: :math:`(1, 0)`
  - Support: :math:`\{r_1\}`
  - Best response: :math:`\{c_1\}`

For :math:`\mathcal{Q}`:

- :math:`(0, 1/2)`:

  - Labels: :math:`\{1, 2\}`
  - Strategy: :math:`(0, 1)`
  - Support: :math:`\{c_2\}`
  - Best response: :math:`\{r_2\}`

- :math:`(1/6, 1/2)`:

  - Labels: :math:`\{0, 1\}`
  - Strategy: :math:`(1/4, 3/4)`
  - Support: :math:`\{c_1, c_2\}`
  - Best response: :math:`\{r_1, r_2\}`

- :math:`(1/3, 0)`:

  - Labels: :math:`\{0, 3\}`
  - Strategy: :math:`(1, 0)`
  - Support: :math:`\{c_1\}`
  - Best response: :math:`\{r_1\}`


Once they have filled in this table:

Ask students what is connection between:

- Support and labels?
- Best responses and labels?


Now identify strategies that are best responses to each other:

- :math:`\sigma_r=(0, 1)` and :math:`\sigma_r=(0,1)`
- :math:`\sigma_r=(3/4, 1/4)` and :math:`\sigma_r=(1/4,3/4)`
- :math:`\sigma_r=(1, 0)` and :math:`\sigma_r=(1, 0)`

Discuss how this relates to the labels.

Finally show how this is implemented in :code:`nashpy`::

    >>> A = np.array([[1, -1], [-1, 1]])
    >>> matching_pennies = nash.Game(A)
    >>> for eq in matching_pennies.vertex_enumeration():
    ...     print(eq)
    (array([ 0.5,  0.5]), array([ 0.5,  0.5]))

If there is time use support enumeration to compare.
