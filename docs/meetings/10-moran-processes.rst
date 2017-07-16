10 Moran Processes
==================

Corresponding chapters
----------------------

- `Moran Processes <http://vknight.org/gt/chapters/12/>`_

Objectives
----------

- Play a class activity of a Moran process;
- Define a Moran process;
- Prove theorem for formula of fixation probabilities;
- Numeric calculations.

Activity
--------

Ask students to form groups of 4: this is a population.

Explain that players/individuals are either Hawks or Doves and that they will
play the Hawk-Dove game with row matrix:


.. math::

   A = \begin{pmatrix}
       0 & 3\\
       1 & 2
   \end{pmatrix}

Recall, this corresponds to sharing of 4 resources:

- Two hawks both get nothing;
- A hawk meeting a dove gets 3 out of 4.
- A dove meeting a hawk gets 1 out of 4.
- A dove meeting a dove gets 2 out of 4.


Hand out a 10 and 20 sided dice to each group.

Explain that one student is to be a Hawk and the others Doves.

Every student players each other and write down their total scores:

- The Hawk gets: 9 (:math:`3\times 3`).
- The Doves all get: 5 (:math:`1\times 1 + 2 \times 2=5`).

One of the individuals is chosen to reproduce:

.. math::

   P(H) = \frac{9}{24}=3/8 \qquad
   P(D) = \frac{9}{24}=5/24

Use the dice (invite the students to figure out a way to do this, various
different ways - ignore none throws etc...).

Then randomly choose a player to eliminate: **this can be the same player chosen
to reproduce** (life can suck).

Now recalculate the fitness (every player plays everyone else).

Repeat until all players are of the same type.

Count from groups to obtain mean fixation rate of a Hawk.

Depending on time, potentially repeat this using Doves.

**Now work through the notes: culminating in the proof of the theorem for the
absorption probabilities of a birth death process.**

Discuss and use code from chapter to show the fixation with the Hawk Dove game::

    >>> import numpy as np
    >>> A = np.array([[0, 3], [1, 2]])

Calculate theoretic value using formula from theorem:

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


- Discuss work of Maynard smith but that this actually used Hawk Dove game in
  infinite population games.
- Discussion possibility for using a utility model on top of fitness.
