AE - Support enumeration
========================

Corresponding chapters
----------------------

- `Support enumeration <http://vknight.org/gt/chapters/05/>`_

**Duration**: 50 minutes

Objectives
----------

- Obtain the Nash equilibria of a game using support enumeration.

Notes
-----

Play a knockout RPSLS tournament
********************************

Tell students to works in pairs.

Invite students to obtain the Nash equilibria, using support enumeration for the
following game:

.. math::

   A = \begin{pmatrix}
   1 & -1\\
   -2  & 2\\
   \end{pmatrix}


Ask students to apply the support enumeration algorithm.

For supports of size one: there are no pairs of best response so now we only
consider :math:`k=2`. This implies the following pair of linear equations:


.. math::

   \begin{align*}
   -{\sigma_r}_1 + 2{\sigma_r}_2 &= {\sigma_r}_1 - 2{\sigma_r}_2\\
   {\sigma_r}_1 &= \frac{1}{2}{\sigma_r}_2
   \end{align*}

.. math::

   \begin{align*}
   {\sigma_c}_1 - {\sigma_c}_2 &= -2{\sigma_c}_1 + 2{\sigma_c}_2\\
   {\sigma_c}_1 &= {\sigma_c}_2
   \end{align*}


Setting this to be probability distributions gives the final result:


.. math::

   \begin{align*}
   {\sigma_r} &= (1/3, 2/3)\\
   {\sigma_c} &= (1/2, 1/2)
   \end{align*}

We don't need to really check the best response condition as the players have no
where to deviate to *but* we can:


.. math::
     A\sigma_c^T =  \begin{pmatrix}
                        0\\
                        0\\
                    \end{pmatrix}

Thus :math:`\sigma_r` is a best response to :math:`\sigma_c`.

  .. math::

     \sigma_rB =\sigma_r(-A) =  (0, 0)

Thus :math:`\sigma_c` is a best response to :math:`\sigma_r`.

We can confirm all of this using :code:`nashpy`::

    >>> import nashpy as nash
    >>> import numpy as np
    >>> A = np.array([[1, -1],
    ...               [-2, 2]])
    >>> game = nash.Game(A)
    >>> list(game.support_enumeration())
    [(array([0.666..., 0.333...]), array([0.5, 0.5]))]

As a second example consider:

.. math::
   A = \begin{pmatrix}
   0  & -2 & 2\\
   1  & 0 & -1\\
   -1  & 1 & 0\\
   \end{pmatrix}

1. We see there are no pairs of best response, so consider :math:`k\in\{2,3\}`.
2. We have the following set of utilities to consider:

   1. :math:`I=\{1, 2\}`
       1. :math:`J=\{1, 2\}`
       2. :math:`J=\{1, 3\}`
       3. :math:`J=\{2, 3\}`
   2. :math:`I=\{1, 3\}`
       1. :math:`J=\{1, 2\}`
       2. :math:`J=\{1, 3\}`
       3. :math:`J=\{2, 3\}`
   3. :math:`I=\{2, 3\}`
       1. :math:`J=\{1, 2\}`
       2. :math:`J=\{1, 3\}`
       3. :math:`J=\{2, 3\}`
   4. :math:`I=J=\{1, 2, 3\}`

The case for `k=2` leads to contradictions (let students identify some of
these).

   4. :math:`I=J=\{1, 2, 3\}`

      In this case we have:

      .. math::

         \begin{align*}
         -{\sigma_r}_2 + {\sigma_r}_3 &= 2{\sigma_r}_1 - {\sigma_r}_3\\
         2{\sigma_r}_1 - {\sigma_r}_3 &= -2{\sigma_r}_1 + {\sigma_r}_2\\
         \end{align*}

      which has solution:

      .. math::

         2{\sigma_r}_1 = {\sigma_r}_2 = {\sigma_r}_3

      Similarly:

      .. math::

         \begin{align*}
         -2{\sigma_c}_2 + 2{\sigma_c}_3 &= {\sigma_c}_1 - {\sigma_c}_3\\
         {\sigma_c}_1 - {\sigma_c}_3 &= -{\sigma_c}_1 + {\sigma_c}_2\\
         \end{align*}

      which has solution:

      .. math::

         {\sigma_c}_1 = {\sigma_c}_2 = {\sigma_c}_3

4. Now we consider which of those supports give valid mixed strategies:

   4. :math:`I=J=\{1, 2, 3\}`

          .. math::

             \begin{align*}
             {\sigma_r} &= (1/5, 2/5, 2/5)\\
             {\sigma_c} &= (1/3, 1/3, 1/3)
             \end{align*}

5. The final step is to check the best response condition:

   4. :math:`I=J=\{1, 2, 3\}`

          .. math::

             A\sigma_c^T =  \begin{pmatrix}
                                0\\
                                0\\
                                0\\
                            \end{pmatrix}

          Thus :math:`\sigma_r` is a best response to :math:`\sigma_c`.

          .. math::

             \sigma_rB =  (0, 0, 0)

          Thus :math:`\sigma_c` is a best response to :math:`\sigma_r`.


We can confirm all of this using :code:`nashpy`::

    >>> import nashpy as nash
    >>> A = np.array([[0, -2, 2],
    ...               [1, 0, -1],
    ...               [-1, 1, 0]])
    >>> rps = nash.Game(A)
    >>> list(rps.support_enumeration())
    [(array([0.2..., 0.4..., 0.4...]), array([0.333..., 0.333..., 0.333...]))]

Discuss with students about what happens when we have a 3 by 2 game?
