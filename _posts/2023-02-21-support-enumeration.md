---
layout: post
title:  "A lengthy set of support enumeration calculations"
tags:
    - support-enumeration
---

In today's class we worked through the support enumeration algorithm. This
involved some discussions about what the algorithm is based on but also a bunch
of tedious linear equations.

A recording of the class is available [here](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=e408cec3-f6ec-42c1-b07e-afab00a5702f).

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
   (the column player only using Paper and Scissors). This lead to a
   contradiction (at step 3 of the above general idea) the row player would
   benefit from playing Scissors.

That is 2 of the 9 possible pairs of supports of size 2.

We then considered both players playing all 3 strategies which lead to [a Nash
equilibria](https://nashpy.readthedocs.io/en/stable/text-book/best-responses.html#definition-of-nash-equilibrium) of:

$$
\sigma_r = (1/3, 1/3, 1/3)
\qquad
\sigma_c = (1/3, 1/3, 1/3)
$$

Indeed in this case we have:

$$
\max(A\sigma_c) = \begin{pmatrix}0\\0\\0\end{pmatrix}
$$

(the important thing is not that the values are 0 but that they are all the
same)

and:

$$
\sigma_r A \sigma_c = \max(A\sigma_c)
$$

**and** there are no strategies outside of the support (because they're all
being played) that could do better.

This all corresponds to the [best response condition](https://nashpy.readthedocs.io/en/stable/text-book/best-responses.html#general-condition-for-a-best-response).

With a few more minutes, I wanted to show how to use support enumeration with
Nashpy, you can see the video describing this: "Using Python to find Nash
Equilibria with Nashpy - [YouTube](https://youtu.be/ggUp9EfkEo8)
[Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=a8d76a65-8772-44f8-b3bf-af9301104ebd)"

Here is some code to recreate everything we did today:

```python
import numpy as np
import nashpy as nash

A = np.array(
    (
        (0, -1, 1),
        (1, 0, -1),
        (-1, 1, 0),
    )
)
rps = nash.Game(A)
list(rps.support_enumeration())
```

A student come up to me after class and made a great point: "this seems
incredibly inefficient": this is absolutely correct. Support enumeration is
essentially a "from first principles" algorithm. It is robust **but** slow.
Some alternatives (that are not considered in the class but might be useful to
you in your group projects):

- [Vertex enumeration](https://nashpy.readthedocs.io/en/stable/text-book/vertex-enumeration.html).
- [Lemke Howson
  algorithm](https://nashpy.readthedocs.io/en/stable/text-book/lemke-howson.html):
  this is essentially state of the art and takes advantage of things computers
  can do very quickly. BUT it is not guaranteed to obtain **all** the
  equilibria.
