---
layout: post
title: "A lengthy set of support enumeration calculations and a Python speed run"
tags:
  - support-enumeration
  - python
---

On Friday we went over the support enumeration algorithm and on Monday I gave a
Python refresher:

- A recording of Friday's class on the support enumeration algorithm is available [here](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=c2ca8cb8-5bf5-49bd-b570-b27f010896f5).
- A recording of Monday's class going over the basics of Python is available [here](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=8aa84229-eded-4302-9de2-b2820108bb17).

### Support enumeration algorithm

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

We considered the supports of size 1: there are no single pairs of actions that
are pairs of best responses to each other.

We considered 2 pairs of supports of size 2:

1. \\(I = \\{R, P\\}\\) (the row player only using Rock and Paper) and \\(J=\\{R, P\\}\\)
   (the column player also only using Rock and Paper). This lead to a
   contradiction (at step 2 of the above general idea) where there would be no
   probabilities that work.
2. \\(I = \\{R, P\\}\\) (the row player only using Rock and Paper) and \\(J=\\{P, S\\}\\)
   (the column player only using Paper and Scissors). This lead to a contradiction (at step 3
   of the above general idea) where there was a best response outside of the support chosen.

That is 2 of the 9 possible pairs of supports of size 2.

### Python refresher

You can find the notebook I used [here]({{site.baseurl}}/assets/2024-2025/nbs/speed-run-of-python.ipynb).

I worked through the how to sections of these two chapters of [Python for Mathematics](https://vknight.org/pfm/):

- [Variables, conditionals and loops](https://vknight.org/pfm/building-tools/01-variables-conditionals-loops/introduction/main.html)
- [Functions and data structures](https://vknight.org/pfm/building-tools/02-functions-and-data-structures/introduction/main.html)
