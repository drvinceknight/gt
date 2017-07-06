07 Prisoners Dilemma
====================

Corresponding chapters
----------------------

- `Prisoners Dilemma <http://vknight.org/gt/chapters/09/>`_

Objectives
----------

- Explore the Iterated Prisoners Dilemma

Notes
-----

Playing team based Iterated Prisoner's Dilemma
**********************************************

Show this video: https://www.youtube.com/watch?v=p3Uos2fzIJ0

Ask class to form 4 teams of equal size.

Write the following on the board:

+---------+------------------+-------------------------------+-------------------------------+
|  Name   | Score vs 1st opp | :math:`\sum` score vs 2nd opp | :math:`\sum` score vs 3rd opp |
+=========+==================+===============================+===============================+
|         |                  |                               |                               |
+---------+------------------+-------------------------------+-------------------------------+
|         |                  |                               |                               |
+---------+------------------+-------------------------------+-------------------------------+
|         |                  |                               |                               |
+---------+------------------+-------------------------------+-------------------------------+
|         |                  |                               |                               |
+---------+------------------+-------------------------------+-------------------------------+

Explain that teams will play the iterated Prisoners dilemma:

.. math::

   A =
   \begin{pmatrix}
       3 & 0\\
       5 & 1
   \end{pmatrix}\qquad
   B =
   \begin{pmatrix}
       3 & 5\\
       0 & 1
   \end{pmatrix}

Discuss NE of stage game.

Discuss "Cooperation" versus "Defection" and explain that goal is to maximise
overall score (not necessarily beat direct opponent).

For every dual write the following on the board (assuming 5 turns):

+---------+-------+--------------------+--------------------+--------------------+--------------------+
|  Name   | Score | :math:`\sum` score | :math:`\sum` score | :math:`\sum` score | :math:`\sum` score |
+=========+=======+====================+====================+====================+====================+
|         |       |                    |                    |                    |                    |
+---------+-------+--------------------+--------------------+--------------------+--------------------+
|         |       |                    |                    |                    |                    |
+---------+-------+--------------------+--------------------+--------------------+--------------------+

Instructions for a dual:

- Give both teams copies of a :download:`C and a D <../assets/activities/C_and_D_cards.pdf>`.
- In your teams: discuss plans for a strategy.
- Before every stage invite both teams to talk to each other.
- Get teams to "face away", after a count down "show" (either a C or a D).


After the tournament:

- Discuss winning strategy and other interesting strategies.
  Discuss potential coalitions that arose.
- Discuss how teams had more information that usual.
- Invite the possibility of modifications (prob end, noise and lack of information).
