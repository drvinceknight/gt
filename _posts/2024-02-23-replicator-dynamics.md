---
layout: post
title: "Replicator dynamics"
tags:
  - replicator-dynamics
---

In class we spoke about the replicator dynamics equation: a differential
equation that is a building block of evolutionary game theory.

You can see a recording of this here:
[https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=5cc70927-0793-4dd5-9690-b11a00c682d0](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=5cc70927-0793-4dd5-9690-b11a00c682d0).

After this we discussed potential reasons for the emergence of the social
convention of walking on a particular site of the road (on the left in the UK for
example).

We used the following game to model this using [Replicator Dynamics](https://vknight.org/gt/topics/replicator-dynamics.html):

$$
A = \begin{pmatrix}
    1 & -1 \\
    -1 & 1\\
\end{pmatrix}
$$

This game is meant to model the interaction of individuals in a given population
who interact (by walking past each other). If both these individuals walk
according to the same convention then they get a utility of 1 but if not they
get a utility of -1.

We then model a given population using a vector \\(x=(x_1, x_2)\\) where \\(x_1\\)
corresponds to the **proportion** of individuals walking according to the
first convention (say: the left) and \\(x_2=1-x_1\\) is the **proportion**
walking
according to the second convention.

We can then compute the average utility of an individual who walks using the
first convention (we can refer to this as the **first type** and to utility as
**fitness**). They will interact with another individual of the first type
\\(x_1\\) of the time getting a fitness of \\(1\\) and an individual of the
second type \\(x_2\\) of the time getting a fitness of \\(-1\\). The average
utility is then:

$$
f_1 = x_1 - x_2
$$

The average utility of the individuals of the second type are:

$$
f_2 = - x_1 + x_2
$$

The average utility over the entire population is then given by:

$$\phi=x_1f_1+x_2f_2$$

In the [notes on Replicator
Dynamics](https://nashpy.readthedocs.io/en/stable/text-book/replicator-dynamics.html#)
you can find linear algebraic expressions of these quantities \\(f\\) and
\\(\phi\\) that extend naturally to populations with more than just 2 types.

The **actual** Replicator Dynamics equation is then given by:

$$
\frac{dx_i}{dt} = x_i(f_i-\phi)\text{ for all}i
$$

In the case of our game this corresponds to:

$$
\begin{align}
\frac{dx_1}{dt} =& x_1 (x_1 - x_2 - x_1(x_1 - x_2)+x_2(x_2 - x_1))\\
\frac{dx_2}{dt} =& x_2 (-x_1 + x_2 - x_1(x_1 - x_2)+x_2(x_2 - x_1))
\end{align}
$$

which can be simplified to:

$$
\begin{align}
\frac{dx_1}{dt} =& x_1 ((x_1 - x_2) - (x_1 - x_2) ^2)\\
\frac{dx_2}{dt} =& x_2 ((x_2 - x_1) - (x_1 - x_2) ^2)
\end{align}
$$

Substituting \\(x_2=1-x_1\\) we have:

$$
\begin{align}
\frac{dx_1}{dt} =& x_1 (2x_1 - 1)2(1-x_1))\\
\frac{dx_2}{dt} =& -x_1 (2x_1 - 1)2(1-x_1))
\end{align}
$$

And we see (setting the derivatives to be equal to 0) that there are 3 stable
populations:

- \\(x_1=0\\): Everyone drives on the right.
- \\(x_1=1\\): Everyone drives on the left.
- \\(x_1=1/2\\): Half the population drives on the left and half on the right.

The fact that this is **stable** mathematically (ie the derivatives are zero)
corresponds to the game theoretic fact that in these populations every type of
individual has the same fitness: **so no one behaviour has an evolutionary
advantage.**
