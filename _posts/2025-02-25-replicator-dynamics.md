---
layout: post
title: "Replicator dynamics"
tags:
  - replicator-dynamics
---

In class we spoke about the replicator dynamics equation: a differential
equation that is a building block of evolutionary game theory.

You can see a recording of this [here](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=0afdd506-fee8-4a1f-9d47-b2890118f7a0).

I asked you all to suggest examples of social conventions. I then picked the
idea of asking "How are you?" and responding "Fine" as a socially
conventionally greeting to explore from an evolutionary game theoretic point of
view.

We used the following game to model this using [Replicator Dynamics](https://vknight.org/gt/topics/replicator-dynamics.html):

$$
A = \begin{pmatrix}
    2 & -1 \\
    0 & 2\\
\end{pmatrix}
$$

This assumes a population of two types of individuals:

- The first type \\(H\\): individuals who say "How are you?" and expect "Fine"
  to complete the greeting. These individuals get a utility of 2 when meeting
  each other and a utility of -1 when meeting someone who does not follow the
  convention.
- The second type \\(\bar H\\): individuals who use a different type of
  greeting. These individuals get a utility of 0 when meeting someone of type
  \\(H\\) and 2 when meeting someone of their own type.

We then model a given population using a vector \\(x=(x_1, x_2)\\) where \\(x_1\\)
corresponds to the **proportion** of individuals of the type \\(H\\) and
\\(x_2=1-x_1\\) is the **proportion** of the type \\(\bar H\\).

We can then compute the average fitness of individuals of each type:

$$
f_1 = 2x_1 - x_2
$$

The average fitness of the individuals of the second type are:

$$
f_2 = 0\times x_1 + 2x_2 = 2x_2
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
\frac{dx_1}{dt} =& x_1 (2x_1 - x_2 - x_1(2x_1 - x_2)-2x_2)\\
\frac{dx_2}{dt} =& x_2 (2x_2 - x_2 - x_1(2x_1 - x_2)-2x_2)
\end{align}
$$

which can be simplified to:

$$
\begin{align}
\frac{dx_1}{dt} =& x_{1} \left(- x_{1} \left(2 x_{1} - x_{2}\right) + 2 x_{1} - 2 x_{2}^{2} - x_{2}\right)\\
\frac{dx_2}{dt} =& x_{2} \left(- x_{1} \left(2 x_{1} - x_{2}\right) - 2 x_{2}^{2} + 2 x_{2}\right)
\end{align}
$$

Substituting \\(x_2=1-x_1\\) and factorising we have:

$$
\begin{align}
\frac{dx_1}{dt} =& - x_{1} \left(x_{1} - 1\right) \left(5 x_{1} - 3\right)\\
\frac{dx_2}{dt} =& x_{1} \left(x_{1} - 1\right) \left(5 x_{1} - 3\right)
\end{align}
$$

We note that \\(\frac{dx_1}{dt}=-\frac{dx_2}{dt}\\) which is expected as we have
\\(x_1+x_2=1\\).

And we see (setting the derivatives to be equal to 0) that there are 3 stable
populations:

- \\(x_1=0\\): No one uses "Hello how are you" as a greeting.
- \\(x_1=1\\): Everyone uses "Hello how are you" as a greeting.
- \\(x_1=3/5\\): 60% the population uses "Hello how are you" as a greeting.

The fact that this is **stable** mathematically (ie the derivatives are zero)
corresponds to the game theoretic fact that in these populations every type of
individual has the same fitness: **so no one behaviour has an evolutionary
advantage.**

The notebook you can find [here]({{site.baseurl}}/assets/2024-2025/nbs/asking-how-are-you.ipynb) (static html [here]({{site.baseurl}}/assets/2024-2025/nbs/asking-how-are-you.html)) includes the above calculations
but also includes some numerical solutions to the differential equations. This
is important as it shows not just what population is stable **but** how a
population can reach a stable population.
