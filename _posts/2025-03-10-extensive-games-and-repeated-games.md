---
layout: post
title: "Extensive Form Games and repeated games"
tags:
  - extensive-form
  - repeated-games
---

In class today we covered extensive form games as well as repeated games.

You can find a recording of the session [here](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=87f581d6-e8e9-41bf-84a2-b29401083e3d).

### Extensive Form Games

In class I asked you to write down strategies for a play of the centipede game.

This required writing down an action to take at _every_ possible node of the
centipede game.

We identified 4 strategies:

- Take at the first opportunity and either take or pass at the second.
- Take at the second opportunity and either take or pass at the second.

If we consider just these 3 actions then we can reformulate the game as a two
player game with the action sets: $A_1=A_2=\{\text{TT}, \text{PP}, \text{PT}, \text{TP}\}$.

Using this we can now rewrite the utility functions for both players by reading
from the tree definition of the centipede game:

$$
A = \begin{pmatrix}
    2 & 2 & 2 & 2\\
    1 & 4 & 3 & 1\\
    1 & 4 & 4 & 1\\
    2 & 2 & 2 & 2\\
    \end{pmatrix}
B = \begin{pmatrix}
    0 & 0 & 0 & 0\\
    3 & 4 & 5 & 3\\
    3 & 2 & 2 & 3\\
    0 & 0 & 0 & 0\\
    \end{pmatrix}
$$

The Nash equilibria for this can then be computed:

```python
>>> import numpy as np
>>> import nashpy as nash
>>> A = np.array(
>>> A = np.array(
...     (
...         (2, 2, 2, 2),
...         (1, 4, 3, 1),
...         (1, 4, 4, 1),
...         (2, 2, 2, 2),
...     )
... )
>>> B = np.array(
...     (
...         (0, 0, 0, 0),
...         (3, 4, 5, 3),
...         (3, 2, 2, 3),
...         (0, 0, 0, 0),
...     )
... )
>>> game = nash.Game(A, B)
>>> tuple(game.vertex_enumeration()
((array([1., 0., 0., 0.]), array([1., 0., 0., 0.])),
 (array([1., 0., 0., 0.]), array([0., 0., 0., 1.])),
 (array([0., 0., 0., 1.]), array([1., 0., 0., 0.])),
 (array([0., 0., 0., 1.]), array([0., 0., 0., 1.])))
```

These all correspond to both players picking to take at the first opportunity. If
both players do this: neither have a reason to change what they are doing.

### Repeated Games

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

We then discussed the following strategy (and I'm really sorry about my virtual board falling apart when I was doing this!):

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

We discussed the incentive either player might have to deviate from this: there is
none. No player has a reason to deviate so this is a Nash equilibrium.

