---
layout: post
title: "Extensive Form Games"
tags:
  - extensive-form
---

In class today we spoke about extensive form games.

You can see a recording of this here: [https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=a1b89a57-d6f1-4092-a958-b11300c68136](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=a1b89a57-d6f1-4092-a958-b11300c68136).

In class I asked you to write down strategies for a play of the centipede game.

This required writing down an action to take at _every_ possible node of the
centipede game.

You can see a pdf with the scans of ever strategy [here]({{site.baseurl}}/)

There were essentially 3 strategies played:

- Take at the first opportunity -- Let write this as: TT.
- Pass at the first opportunity but take at the second -- Let us write this as
  PT
- Pass always -- Let us call this: PP

If we consider just these 3 actions then we can reformulate the game as a two
player game with the action sets: $A_1=A_2=\{\text{TT}, \text{PT},
\text{PP}\}$.

Using this we can now rewrite the utility functions for both players by reading
from the tree definition of the centipede game:

$$
A = \begin{pmatrix}
    2 & 2 & 2\\
    1 & 4 & 4\\
    1 & 3 & 4\\
    \end{pmatrix}
B = \begin{pmatrix}
    0 & 0 & 0\\
    3 & 2 & 2\\
    3 & 5 & 4\\
    \end{pmatrix}
$$

The Nash equilibria for this can then be computed:

```python
>>> import numpy as np
>>> import nashpy as nash
>>> A = np.array(
...     (
...         (2, 2, 2),
...         (1, 4, 4),
...         (1, 3, 4),
...     )
... )
>>> B = np.array(
...     (
...         (0, 0, 0),
...         (3, 2, 2),
...         (3, 5, 4),
...     )
... )
>>> game = nash.Game(A, B)
>>> list(game.vertex_enumeration()
[(array([1., 0., 0.]), array([1., 0., 0.]))]
```

This corresponds to both players picking to take at the first opportunity. If
both players do this: neither have a reason to change what they are doing.

This was not the exact game I wrote down at the end of the class where we also
included the strategy to take at the first node and hypothetically pass at the
second. Of course no one wrote that one down as it does not make immediate
sense. If I were to change how I play this game (perhaps I will do this next
year) I would not only randomise who is player 1 or player 2 but also randomise
the node at which to start playing.

You can find the notebook I used in class [here]({{site.baseurl}}/assets/2023-2024/nbs/2024-02-16.ipynb)
