---
layout: post
title: "A lengthy set of support enumeration calculations"
tags:
  - support-enumeration
---

In today's class we worked through the support enumeration algorithm. This
involved some discussions about what the algorithm is based on but also a bunch
of tedious linear equations.

A recording of the class is available [here](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=8a374aba-b055-49e3-b6e7-b10c00d6f400).

We applied the algorithm described
[here](https://nashpy.readthedocs.io/en/stable/text-book/support-enumeration.html#the-support-enumeration-algorithm)
to the zero sum game defined by:

$$
A = \begin{pmatrix}
0 & -1 & 1\\
1 & 0 & -1\\
-1 & 1 & 0
\end{pmatrix}
$$

The basic idea behind the algorithm is as follows:

1. Assume what actions are played by both players (this is called the [supports
   of the strategies](https://nashpy.readthedocs.io/en/stable/text-book/strategies.html#definition-of-support-of-a-strategy)
2. Identify the strategies that ensure that indeed all actions of the chosen
   supports will be played: this only happens if all actions in the support
   itself have the same expected utility.
3. Check that there is no better outside of the supports chosen.

**Note** We did not actually get to part 3 today.

We considered the supports of size 1: there are no single pairs of actions that
are pairs of best responses to each other.

We considered 2 pairs of supports of size 2:

1. \\(I = \\{R, P\\}\\) (the row player only using Rock and Paper) and \\(J=\\{R, P\\}\\)
   (the column player also only using Rock and Paper). This lead to a
   contradiction (at step 2 of the above general idea) where there would be no
   probabilities that work.
2. \\(I = \\{R, P\\}\\) (the row player only using Rock and Paper) and \\(J=\\{P, S\\}\\)
   (the column player only using Paper and Scissors).
   We did not finish this in class but it leads to a
   contradiction (at step 3 of the above general idea) the row player would
   benefit from playing Scissors. I will finish this in class on Monday.

That is 2 of the 9 possible pairs of supports of size 2.
