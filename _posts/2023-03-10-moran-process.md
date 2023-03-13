---
layout: post
title:  "Hawks, Doves and Dice"
tags:
    - moran-process
---

In class today we looked at the [Moran
Process](https://vknight.org/gt/topics/moran-processes.html). We did this by
considering the [Hawk Dove game](https://nashpy.readthedocs.io/en/stable/text-book/normal-form-games.html#hawk-dove-game).

You can see a recording of this here:
[cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=f41045d7-ff4b-4e0d-8adb-afbc00d6f23c](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=f41045d7-ff4b-4e0d-8adb-afbc00d6f23c)

The Moran process is a game theoretic model of evolution. One of the differences
from the [Replicator Dynamics equation]({{ site.baseurl
}}/topics/replicator-dynamics.html) is that the population is assumed to be
**finite**: so we assumed there is a finite population of \\(N\)) individuals
that can be of any of the types that correspond to actions of the underlying
Norma Form Game.

In the example of the Hawk Dove game that we played in class we assumed there
were \\(N=3\\) individuals and the question we attempted to understand was: _if
we introduce a Hawk in to a population of Doves, what will happen?_


---

The Moran process then follows the following:

1. Calculate the fitness of all individuals: everyone in the population plays
   the Normal Form game against everyone else. Their utility (or fitness)
   is given by their type and the type of the individual they play with.
2. Randomly select an individual for copying proportional to their fitness.
3. Randomly select an individual for removal (all individuals are equally likely
   to be removed).
4. Create a new individual of the same type as the one selected in step 2.
5. Remove the individual selected in step 3.

Repeat that process until there is a single type of individual in the
population.

---

In class we used dice to simulate the above. We were a bit short on time at the
end so not everyone got to complete a simulation. We did still find a
probability of 67% of the Hawk taking over.

I ran two other numerical simulation (the last one using
[Nashpy](https://nashpy.readthedocs.io/en/stable/how-to/use-moran-processes.html))
and found a good approximation around 55%.

In class on Tuesday we will discuss how we can calculate the theoretic value.

You can find a notebook with the various numerical simulations
[here]({{ site.baseurl }}/assets/2022-2023/nbs/2023-03-10-gt.ipynb).

Note that while the game we used here assumes only two type, this is not a
constraint of the Moran process.
