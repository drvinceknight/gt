AF- Revisiting Evolutionary Game Theory
=======================================

Corresponding chapters
----------------------

- `Lemke Howson algorithm <https://vknight.org/gt/chapters/11/>`_

**Duration**: 50 minutes


Objectives
----------

- Re visit evolutionary game theory.


Notes
-----


Consider the following matrix:

.. math::

   A = \begin{pmatrix}
   2 & 0 \\
   0 & 1
   \end{pmatrix}

**Ask students in pairs to obtain all potential candidates for evolutionary
stable strategies**

This corresponds to finding the symmetric (where both players do the same thing)
Nash equilibria of the corresponding game :math:`(A, A^T)`.

We have two pure symmetric NE:

.. math::

    ((1, 0), (1, 0))\qquad ((0, 1), (0, 1))

The mixed NE is found by solving the indifference equations:

.. math::

   \begin{align*}
   u_r((1, 0), (y, 1- y)) & = u_r((0, 1), (y, 1 - y))\\
                       2y & = (1 - y)\\
                        y & = 1 / 3
   \end{align*}

Similarly for the row player:

.. math::

   \begin{align*}
   u_c((x, 1- x), (1, 0)) & = u_c((x, 1 - x), (0, 1))\\
                       2x & = (1 - x)\\
                        x & = 1 / 3
   \end{align*}

Some code to check this::

    >>> import nashpy as nash
    >>> import numpy as np
    >>> A = np.array([[2, 0],
    ...               [0, 1]])
    >>> rps = nash.Game(A, A.T)
    >>> list(rps.support_enumeration())
    [(array([1., 0.]), array([1., 0.])), (array([0., 1.]), array([0., 1.])), (array([0.333..., 0.666...]), array([0.333..., 0.666...]))]


The first two pure NEs immediately obey the first condition of the theorem from
the notes.

**Ask students to verify this.**

**Then ask students to check the condition for the final NE:**

Let us consider the conditions for the final NE:

.. math::

    \begin{align*}
    u((1/3, 2/3), (1/3, 2/3)) &= 2/3\\
    u((y,(1-y)), (1/3, 2/3)) &= 2y/3+(1-y)2/3=2/3\\
    u((1/3, 2/3), (y, (1-y)) &= 2y/3+(1-y)2/3=2/3\\
    u((y,1-y), (y, (1-y)) &= 2y^2+(1-y)^2\\
    \end{align*}


We see that the final condition needs to be checked, :math:`(1/3, 2/3)` is an
ESS iff :math:`u((1/3, 2/3), (y, 1-y))>u((y, 1-y), (y, 1-y))`.


.. math::

    \begin{align*}
    u((1/3, 2/3), (y, 1-y)) - u(y,1-y) &= 2/3-2y^2-1+2y-y^2\\
                                       &=-3y^2+2y-1/3
                                       &=-1/3(9y^2-6y+1)
                                       &=-1/3(3y-1)^2
                                       &<0
    \end{align*}

Thus :math:`u((1/3, 2/3), (y, 1-y))<u(y,1-y)`. Thus this is not an ESS.

Some code to verify this::

    >>> from scipy.integrate import odeint
    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> t = np.linspace(0, 4, 100)  # Obtain 100 time points
    >>> def dx(x, t, A):
    ...     """
    ...     Define the derivate of x.
    ...     """
    ...     f = np.dot(A, x)
    ...     phi = np.dot(f, x)
    ...     return x * (f - phi)
    >>> A = np.array([[2, 0], [0, 1]])
    >>> np.random.seed(0)
    >>> plt.figure()
    >>> for epsilon in np.random.random(20):
    ...     xs = odeint(func=dx, y0=[1 - epsilon, epsilon], t=t, args=(A,))
    ...     plt.plot(xs)
    >>> plt.ylim(0,1);
    ...
