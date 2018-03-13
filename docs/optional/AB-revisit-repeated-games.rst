AB - Revisiting Repeated games
==============================

Corresponding chapters
----------------------

- `Repeated games <https://vknight.org/gt/chapters/08/>`_

**Duration**: 50 minutes


Objectives
----------

- Re visit repeated games and ensure able to compute Nash equilibria for games
  that are not stage nash.


Notes
-----


Consider the :math:`(A,B)\in{\mathbb{R}^{2\times 2}}^2` game with :math:`T=2`:

.. math::

   A = \begin{pmatrix}
   200 & 4 & 3 \\
   1   & 0 & 2
   \end{pmatrix}
   \qquad
   B = \begin{pmatrix}
   0 & -3 & 0 \\
   -10 & 0 & -10
   \end{pmatrix}

**Ask students in pairs to:**

- Identify pure Nash equilibria of stage game:

.. math::

   A = \begin{pmatrix}
   \underline{200} & \underline{4} & \underline{3} \\
   1   & 0 & 2
   \end{pmatrix}
   \qquad
   B = \begin{pmatrix}
   \underline{0} & -3 & \underline{0} \\
   -10 & \underline{0} & -10
   \end{pmatrix}

- Identify repeated game Nash equilibria:

  - :math:`(r_1r_1, c_1c_1)` with utility: (400, 0).
  - :math:`(r_1r_1, c_1c_3)` with utility: (203, 0).
  - :math:`(r_1r_1, c_3c_1)` with utility: (203, 0).
  - :math:`(r_1r_1, c_3c_3)` with utility: (6, 0).


- Identify an equilibria that is not stage Nash:

  1. For the row player:

     .. math::

        (\emptyset, \emptyset) \to r_2

     .. math::

        (r_2, c_1) \to r_1

     .. math::

        (r_2, c_2) \to r_1

     .. math::

        (r_2, c_3) \to r_1

  2. For the column player:

     .. math::

        (\emptyset, \emptyset) \to c_2

     .. math::

        (r_2, c_1) \to c_1

     .. math::

        (r_1, c_3) \to c_1

  This corresponds to the following scenario:

  > Play :math:`(r_2, c_2)` in first stage and :math:`(r_1,c_1)` in second stage
  unless the row player does not cooperate in which case play :math:`(r_1,
  c_3)`.

  This gives a utility of :math:`(200, 0)`. Is this an equilibrium?

  1. If the row player deviares, they would only be rational to do so in the
       first state, if they did they would gain 4 but lose 197.
  2. If the column player deviates they would do so in the first round and gain
       no utility.

Potentially discuss how this repeated game framework can/does correspond to a
*normal* normal form game.

- Writing all strategies down;
- Obtaining large matrix (very large)
