07 Repeated games
=================

Corresponding chapters
----------------------

- `Repeated games <http://vknight.org/gt/chapters/08/>`_

Objectives
----------

- Define repeated games and strategies in repeated games
- Understand proof of theorem for sequence of stage Nash
- Understand that other equilibria exist

Notes
-----

Playing repeated games in pairs
*******************************

- Explain that we are about to play a game twice.
- Explain that this has to be done **SILENTLY**

In groups we are going to play:


.. math::

   A =
   \begin{pmatrix}
       \underline{12} & 6\\
       0 & \underline{24}\\
       \underline{12} & 23\\
   \end{pmatrix}
   \qquad
   B =
   \begin{pmatrix}
       \underline{2} & 1\\
       \underline{5} & 4\\
       \underline{0} & 0\\
   \end{pmatrix}

In pairs:

- Decide on row/column player (recall you don't care about your opponents
  reward).
- We are going to play the game TWICE and write down both players *cumulative*
  scores.
- Define a strategy and ask players to write down a strategy that must describe
  what they do in both stages by answering the following question:
  - What should the player do in the first stage?
  - What should the player do in the second stage given knowledge of what both
    players did in the first period?
- SILENTLY, after having written down a strategy: show each other your
  strategies and SILENTLY agree on the pair of utilities. If you are unable to
  agree on a utility this indicates that the strategies were not descriptive
  enough. SILENTLY start again :)

As a challenge: repeat this (so repeatedly play a repeated game, repeatedly
write down a new strategy) and make a note
when you arrive at an equilibria (where no one has a reason to write a different
strategy down)

**If anyone arrives at an equilibria where the row player scores more than 24
and the column player more than 4 stand up as a pair.**

Following this, assuming a pair has arrived at such an equilibrium discuss this.

Then work through the notes:

- Definition of a repeated game;
- Definition of a strategy;
- Theorem of sequence of stage Nash (relate this back to the utilities of our
  game):

  - :math:`(r_1r_1, c_1c_1)` with utility: (24, 4).
  - :math:`(r_1r_3, c_1c_1)` with utility: (24, 2).
  - :math:`(r_3r_1, c_1c_1)` with utility: (24, 2).
  - :math:`(r_3r_3, c_1c_1)` with utility: (24, 0).

Now discuss the potential of a different equilibrium:


1. For the row player:

   .. math::

      (\emptyset, \emptyset) \to r_2

   .. math::

      (r_2, c_1) \to r_3

   .. math::

      (r_2, c_2) \to r_1

2. For the column player:

   .. math::

      (\emptyset, \emptyset) \to c_2

   .. math::

      (r_1, c_2) \to c_1

   .. math::

      (r_2, c_2) \to c_1

   .. math::

      (r_3, c_2) \to c_1

This corresponds to the following scenario:

> Play :math:`(r_2, c_2)` in first stage and :math:`(r_1,c_1)` in second stage
unless the column player does not cooperate in which case play :math:`(r_3,
c_1)`.

This gives a utility of :math:`(36, 6)`. Is this an equilibrium?

1. If the row player deviates, they would do so in the first round and gain no
   utility.
2. If the column player deviates, they would only be rational to do so in the
   first stage, if they did they would gain 1 but lose 2 in the second round.

Thus this is Nash equilibrium.

- Discuss how to identify such an equilibria: which player has an incentive to
  build a reputation? (The column player want to prove to be trustworthy to gain
  2 in the final round).
- Mention how this shows how game theory studies the emergence of unexpected
  behaviour.
