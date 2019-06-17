09 Evolutionary dynamics
========================

Corresponding chapters
----------------------

- `Evolutionary dynamics <http://vknight.org/gt/chapters/10/>`_

Objectives
----------

- Go over basic differential models for population dynamics.

Notes
-----

Explain difference from games so far:

- Players were discrete entities (and we only consider 2 player games);
- Now there are *no* players: just strategies in a population.

Our population will be *stand* ers or *sit* ers.

Say we are going to use the following differential equation to denote the rate
at which people stand:

.. math::

   \frac{dx}{dt} = 2 x

Use seconds (artificially) as a time unit, :math:`\frac{dx}{dt}` corresponds to
the speed with which people stand up. We will instead consider it as *the rate
at which people become standing up*. Using a continuous population these two
things are equivalent.

Get one student to stand up.

The speed at which other individuals are becoming *standing up* is at that exact
point 2. Get someone to slowly stand up ... until they become stood up etc...

Note how we will run out of people very quickly as the solution to our equation
is:

.. math::

   x(t) = x_0e^{2t}

Show how we can use Python to solve this differential equation numerically::

   >>> import numpy as np
   >>> from scipy.integrate import odeint
   >>> t = np.linspace(0, 10, 100)  # Obtain 100 time points
   >>> def dx(x, t, a):
   ...     """Define the derivate of x"""
   ...     return a * x
   >>> a = 10
   >>> xs = odeint(func=dx, y0=1, t=t, args=(a,))
   >>> xs
   array([[1.000...


Now consider population of two individuals (see notes) (:math:`x`: standers and
:math:`y` sitting on desk).
What happens over time:

.. math::

   \frac{dx}{dt} = 2 x \qquad \frac{dy}{dt} = 3 y

This means that the we would very quickly run out of sitters and desk sitters but
what would happen to the limit of the ratio? (Go over mathematics in notes)

Now, finally consider a constant population:

Consider .5 population standing and .5 sitting.

What must we have for our rates?

One population increases at a rate of 2 and the other increases at a rate of 3.

So our population source also, somehow decrease by 5.

Ask students to suggest how this can be done. Have a discussion.

Solution: share this between both populations:

- One populations "increases" at a rate of 2 - 2.5 = -0.5
- One populations "increases" at a rate of 3 - 2.5 = 0.5

Go over notes.

Discuss what happens at following starting conditions:

- x=1, y=0
- x=0, y=1
- x=0.5, y=0.5 but changes rates to be equal.

Show how can obtain this numerically::

    >>> def dxy(xy, t, a, b):
    ...     """
    ...     Define the derivate of x and y.
    ...     It takes `xy` as a vector
    ...     """
    ...     x, y = xy
    ...     phi = a * x + b * y
    ...     return x * (a - phi), y * (b - phi)
    >>> a, b = 10, 5
    >>> xys = odeint(func=dxy, y0=[.5, .5], t=t, args=(a, b))
    >>> xys
    array([[ 5.00000000e-01,  5.000...


Discuss how this basic notion of fitness will now be extended to consider game
theoretic models where the fitness comes out game theoretic models.
