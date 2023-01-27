07 Evolutionary game theory
===========================

Corresponding chapters
----------------------

- `Evolutionary game theory <http://vknight.org/gt/chapters/07/>`_

Objectives
----------

- Go over the logical progression from dynamics to games;
- Explain ESS

Notes
-----

Recall that there are *no* players: just strategies in a population.

Go over the notes, explaining the mathematics.

Now consider the Matching pennies game:

.. math::

   A = \begin{pmatrix}
   1 & -1\\
   -1 & 1\\
   \end{pmatrix}

This gives:

.. math::


   f_1 = x_1 - x_2\qquad f_2 = -x_1 + x_2


which is equivalent to:

.. math::

   f = A x =
   \begin{pmatrix}
       x_1 - x_2\\
       -x_1 + x_2
   \end{pmatrix}


and so:

.. math::

   phi = f x = x_1(x_1 - x_2) + x_2(x_2 - x_1) = (x_1 - x_2) ^ 2



thus:

.. math::

   \frac{dx}{dt} =
      \begin{pmatrix}
          x_1 ((x_1 - x_2) - (x_1 - x_2) ^2)\\
          x_2 ((x_2 - x_1) - (x_1 - x_2) ^2)
      \end{pmatrix}

.. math::

   \frac{dx}{dt} =
      \begin{pmatrix}
          x_1 (x_1 - x_2)(1 - (x_1 - x_2))\\
          x_2 (x_1 - x_2)(-1 - (x_1 - x_2))
      \end{pmatrix}

however recall that :math:`x_1 + x_2 = 1`:

.. math::

   \frac{dx_1}{dt} = x_1 (2x_1 - 1)2(1-x_1))

Verification of above calculations::

    >>> import sympy as sym
    >>> x_1, x_2 = sym.symbols("x_1, x_2")
    >>> f_1 = x_1 - x_2
    >>> f_2 = x_2 - x_1
    >>> phi = x_1 * f_1 + x_2 * f_2
    >>> dx_1 = x_1 * (f_1 - phi)
    >>> sym.factor(dx_1.subs({x_1: 1 - x_2}))
    2*x_2*(x_2 - 1)*(2*x_2 - 1)

We have the stable points as expected:

1. :math:`x_1 = 0`
2. :math:`x_1 = 1`
3. :math:`x_1 = 1 / 2`

Relate this to the notes and discuss notion of mutated population and stable ESS.

Show output of the following::

    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> from scipy.integrate import odeint
    >>> t = np.linspace(0, 10, 100)  # Obtain 100 time points
    >>> def dx(x, t, A):
    ...     """
    ...     Define the derivate of x.
    ...     """
    ...     f = np.dot(A, x)
    ...     phi = np.dot(f, x)
    ...     return x * (f - phi)

Slight deviation from :math:`x_1=0`::

    >>> A = np.array([[1, -1], [-1, 1]])
    >>> epsilon = 10 ** -1
    >>> xs = odeint(func=dx, y0=[epsilon, 1 - epsilon], t=t, args=(A,))
    >>> plt.plot(xs);
    [...

Slight deviation from :math:`x_1=1`::

    >>> xs = odeint(func=dx, y0=[1 - epsilon, epsilon], t=t, args=(A,))
    >>> plt.plot(xs);
    [...

Slight deviation from :math:`x_1=1/2`::

    >>> xs = odeint(func=dx, y0=[1 / 2 - epsilon, 1 / 2 + epsilon], t=t, args=(A,))
    >>> plt.plot(xs);
    [...


Look at theorem and discuss proof.

Carry out Nash equilibria computation (which corresponds to the above case)::

    >>> import nashpy as nash
    >>> game = nash.Game(A, A.transpose())
    >>> list(game.support_enumeration())
    [(array([1., 0.]), array([1., 0.])), (array([0., 1.]), array([0., 1.])), (array([0.5, 0.5]), array([0.5, 0.5]))]

Now look at cases:

1. :math:`x_1=0`: we are in the first case of the theorem so we have an
   ESS.
2. :math:`x_1=1`: we are in the first case of the theorem so we have an
   ESS.
3. :math:`x_1=1/2`: we now have the second case of the theorem :math:`u(x,
   y)=u(x, x)` (indeed the row strategy aims to make the column strategy
   indifferent - according to the best response condition).


To deal with this case we need to look at the next part of the second condition:

.. math::

   u(x, y) = 0

.. math::

   u(y, y) = y_1 ^2 + (1 - y_1) ^2 - 2(1-y_1)y_1 = (y_1 - (1 - y_1))^2 = (2y_1 - 1) ^ 2

And as long as :math:`y_1\ne x_1=1/2` then :math:`u(x, y) < u(y, y)` thus this
is *not* an ESS::

    >>> A = sym.Matrix(A)
    >>> y_1, y_2 = sym.symbols("y_1, y_2")
    >>> y = sym.Matrix([y_1, y_2])
    >>> sym.factor((y.transpose() * A * y)[0].subs({y_2: 1 - y_1}))
    1.0*(2.0*y_1 - 1.0)**2

Discuss the work John Maynard Smith in 1973 who formalised this work. Mention
that he was not actually aware of Nash equilibria at the time.
