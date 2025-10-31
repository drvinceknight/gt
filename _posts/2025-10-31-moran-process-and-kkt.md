---
layout: post
title: "Hawks, Doves and Dice"
tags:
  - moran-process
---

In class today we looked at the [Moran
Process](https://nashpy.readthedocs.io/en/stable/text-book/moran-process.html) and the 
[Karush-Kuhn-Tucker conditions](https://vknight.org/gtb/main-17/). We did this by
considering the [Hawk Dove game](https://vknight.org/gtb/main-8/#inknuM1ypp).

You can see a recording of this [here](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=724c904c-da51-40e8-a34b-b38200d6c839).

**The Moran Process**

The Moran process is a game theoretic model of evolution. One of the differences
from the [Replicator Dynamics equation]({{ site.baseurl
}}/topics/replicator-dynamics.html) is that the population is assumed to be
**finite**: so we assumed there is a finite population of \\(N\\) individuals
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

In class we used dice to simulate the above and obtained a
probability of 47% of the Hawk taking over.

[Here]({{site.baseurl}}/assets/2025-2026/nbs/hawks-doves.ipynb) is a notebook with some numeric simulations of the probabilities. If you
look through the notes you can see approaches for calculating exact fixation
probabilities.


**KKT Conditions**

After that we spoke about the [Karush-Kuhn-Tucker Condition](https://vknight.org/gtb/main-17/) which I described
as a rigorous mathematical set of rules for a simple idea of where optima might
be on a constrained region.

You can find the notebook I used to draw the function we looked at
[here]({{site.baseurl/assets/2025-2026/nbs/coffee-doughnuts.ipynb}}).
