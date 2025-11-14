---
layout: post
title: "Social Choice and Cooperative Games"
tags:
  - social-choice
  - cooperative-games
---

In class today we looked at [social choice](https://vknight.org/gtb/main-13/) and 
[cooperative games](https://vknight.org/gtb/main-14/).

You can see a recording of this [here](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=8ff7852e-a0f2-46bd-9da3-b392010b098b).

### Social Choice

For the purpose of studying social choice I asked you all to vote on which topic
from game theory you wanted us to revise on Monday.

Using the first past the post system: the Moran Process got 11 votes whilst the
other subjects got a total of 19.

Following this I used a different tool which uses more advanced social choice
methodology to get your decision. This site asked you to rank all your choices
and then gives a decision: it in fact resulted in the same outcome (but this is
not necessarily the case). You can see the results
[here](https://stablevoting.org/results/6915c031acad2cab93ca1ddc?oid=jsLVNa1q).

Following this I discussed the chapter on social choice highlighting:

- Arrow's impossibility theorem: there is no perfect system.
- Condorcet's method which might not always lead to a decision.
- Borda's scoring method which does always lead to a decision.

### Shapley Value

I then asked for 3 volunteers to try and land paper plans in a target.

You can find the results of this in the blue and red part of the so called
[characteristic function game](https://vknight.org/gtb/main-14/#definition-characteristic-function-game).

You can find the calculations we made on the board here:

![]({{site.baseurl}}/assets/2025-2026/boards/2025-11-14/main.jpg)

(Note that the value of Tom and Franks coalition in the blue game should be 6.)

At the very end of the class, after we computed the Shapley value for the red
game Tom asked an excellent question:

> Since I can get 3 alone and the Shapley value gets me 17/11 why would I act as
> part of the coalition?

**I made a mistake here, saying that something must be wrong.**

In fact the game is not [super additive](https://vknight.org/gtb/main-14/#sec-definition-of-superadditive-characteristic-function) and so the 
Shapley value here does not guarantee so called individual rationality.

Tom suggested a change to the characteristic function that would ensure it is
super additive that would ensure this.

You can find a Jupyter notebook
[here]({{site.baseurl}}/assets/2025-2026/nbs/shapley-value.ipnb) with code to
carry out the calculations for each other these scenarios.
