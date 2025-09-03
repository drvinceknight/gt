---
layout: class-notes
title: "integer-pivoting"
tag: integer-pivoting
---

## Activity (20 minutes)

Draw the Polytope from the [motivating example of the integer pivoting
appendix](https://vknight.org/gtb/main-18/#sec-motivating-example-two-views-of-a-polytope) as an intersection of halfspaces:

$$
\begin{align*}
x_1 + 3x_2 &\leq 1\\
3x_1 + x_2 &\leq 1\\
\end{align*}
$$

Ask how the following "table of numbers" corresponds to it:

$$
\begin{pmatrix}
1 & 3 & 0 & 1 & 1\\
3 & 0 & 1 & 0 & 1\\
\end{pmatrix}
$$

Ask how the follow "table of numbers" corresponds to it:

$$
\begin{pmatrix}
0 & 8 & 3 & -1 & 2\\
3 & -1 & 0 & 1 & 1\\
\end{pmatrix}
$$

Aim to have a discussion about how setting non-basic variables to 0 gives a
vertex.

Aim to have a discussion about how to make a non-basic variable become basic.
Show how this corresponds to

## Discussion (20 minutes)

Discussion point: **After showing notes, ask students how to decide how to
move?**

Hopefully some students will talk about the simplex algorithm. Make a note that
here we are not touching that an in fact how you move depends on what you are
trying to do. We will in fact see one approach when we look at the next chapter.
