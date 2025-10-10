---
layout: post
title: "Subgame Perfection"
tags:
  - subgame-perfection
---

In class today we spoke returned to the notion of extensive form games.

You can see a recording of this [here](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=c3fdc573-3c94-4d0d-94b4-b36d01084629).

In class I asked you to write down strategies for a play of the centipede game.

This required writing down an action to take at _every_ possible node of the
centipede game. This is what is dictated by the [definition of a strategy in an
extensive form game](https://vknight.org/gtb/main-1/#definition-strategy-in-extensive-form-games)

We identified 4 strategies:

- Take at the first opportunity and either take or pass at the second.
- Pass at the second opportunity and either take or pass at the second.

If we consider just these 3 actions then we can reformulate the game as a two
player game with the action sets: \\(A_1=A_2=\{\text{TT}, \text{PP}, \text{PT}, \text{TP}\}\\).

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

We can look at the [best response in actions](https://vknight.org/gtb/main-2/#exam-predicted-behaviour-through-best-responses-in-the-action-space) to identify 4 Nash Equilibrium:

$$
A = \begin{pmatrix}
    \underline{2} & 2 & 2 & \underline{2}\\
    1 & \underline{4} & 3 & 1\\
    1 & \underline{4} & \underline{4} & 1\\
    \underline{2} & 2 & 2 & \underline{2}\\
    \end{pmatrix}
B = \begin{pmatrix}
    \unsderline{0} & \underline{0} & \underline{0} & \underline{0}\\
    3 & 4 & \underline{5} & 3\\
    \underline{3} & 2 & 2 & \underline{3}\\
    \underline{0} & \underline{0} & \underline{0} & \underline{0}\\
    \end{pmatrix}
$$

We see 4 pairs of best responses that correspond to:

$$\{\text{TT}, \text{TT}\}\qquad \{\text{TT}, \text{TP}\} \qquad \{\text{TP}, \text{TT}\}\qquad \{\text{TP}, \text{TP}\}$$

This all give the same outcome **but** only 1 of them is a Nash equilibrium no
matter **where we start in the game** which is the one we obtained using
[backwards induction](https://vknight.org/gtb/main-5/#definition-backward-induction). This is by definition a subgame perfect
Nash equilibrium which is the [topic of the corresponding chapter](https://vknight.org/gtb/main-5/).
