---
layout: post
title:  "Ambulance diversion and replicator dynamics"
tags:
    - replicator-dynamics
---

In class today [Michalis
Panayides](https://uk.linkedin.com/in/michalis-panayides) presented research
from his PhD. Michalis' work uses queuing theory to build a Normal Form Game
between two hospitals. This is used to identify a good set of incentives/targets
to help reduce ambulances being blocked outside of Accident and Emergency
departments.

Once the game is built, based on a specific set of incentives, an evolutionary
algorithm based on [Replicator
Dynamics](https://vknight.org/gt/topics/replicator-dynamics.html) is used to see
what would happen. This helps to understand the effects of the incentives.

You can see a recording of this here:
[cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=cb2afc49-e02a-4753-8f9e-afb900a56bca](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=cb2afc49-e02a-4753-8f9e-afb900a56bca)

Here is a publication if you would like to read more: [A game theoretic model of
the behavioural gaming that takes place at the EMS - ED
interface](https://www.sciencedirect.com/science/article/pii/S0377221722005549?via%3Dihub)

After this we discussed potential reasons for the emergence of the social
convention of riding on a particular site of the road (on the left in the UK for
example).

We used the following game to model this using [Replicator Dynamics](https://vknight.org/gt/topics/replicator-dynamics.html):

$$
A = \begin{pmatrix}
    1 & -1 \\
    -1 & 1\\
\end{pmatrix}
$$

This game is meant to model the interaction of individuals in a given population
who interact (by driving past each other). If both these individuals drive
according to the same convention then they get a utility of 1 but if not they
get a utility of -1.

We then model a given population using a vector \\(x=(x\_1, x\_2)\\) where \\(x\_1\\)
corresponds to the **proportion** of individuals driving according to the
first convention (say: the left) and \\(x_2=1-x_1\\) is the **proportion** driving
according to the second convention.

We can then compute the average utility of an individual who drives using the
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
\frac{dx_1}{dt} =& x_1 ((x_1 - x_2) - (x_1 - x_2) ^2)\\
\frac{dx_2}{dt} =& x_2 ((x_2 - x_1) - (x_1 - x_2) ^2)
\end{align}
$$

Substituting \\(x\_2=1-x\_1\\) we have:

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

The fact that this is **stable** mathematically (ie the derivaties are zero)
corresponds to the game theoretic fact that in these populations every type of
individual has the same fitness: **so no one behaviour has an evolutionary
advantage.**

With the final minutes of the class I showed how we could use
[Nashpy](https://nashpy.readthedocs.io/en/stable/how-to/use-replicator-dynamics.html)
to solve these equations numerically. You can find the notebook with that
[here]({{ site.baseurl }}/assets/2022-2023/nbs/2023-03-07-gt.ipynb).
