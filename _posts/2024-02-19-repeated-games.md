---
layout: post
title: "Repeated games"
tags:
  - repeated-games
---

In class we spoke about repeated games.

You can see a recording of this here: [https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=f8ffef2b-2a36-4bf4-ae9f-b11600a56276](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=f8ffef2b-2a36-4bf4-ae9f-b11600a56276).

I asked you all to write strategies for the game **defined** by playing the
following **stage** game **twice**:

$$
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
$$

We discussed things at length and found 4 Nash equilibria which corresponds to
both players playing a strategy **that did not depend on actions of either
player**:

- \\((r_1r_1, c_1c_1)\\) with utility: (24, 4).
- \\((r_1r_3, c_1c_1)\\) with utility: (24, 2).
- \\((r_3r_1, c_1c_1)\\) with utility: (24, 2).
- \\((r_3r_3, c_1c_1)\\) with utility: (24, 0).

We then discussed the following strategy:

1. For the row player:

$$
\begin{array}
(\emptyset, \emptyset) \to r_2\\
(r_2, c_1) \to r_3\\
(r_2, c_2) \to r_1\\
\end{array}
$$

2. For the column player:

$$
\begin{array}
(\emptyset, \emptyset) \to c_2\\
(r_1, c_2) \to c_1\\
(r_2, c_2) \to c_1\\
(r_3, c_2) \to c_1
\end{array}
$$

This corresponds to the following scenario:

> Play \\((r_2, c_2)\\) in first stage and \\((r_1,c_1)\\) in second stage
> unless the column player does not cooperate in which case play \\((r_3, c_1)\\)

This gives a utility of \\((36, 6)\\). Is this an equilibrium?

We discussed the incentive either play might have to deviate from this: there is
none. No player has a reason to deviate so this is a Nash equilibrium.
