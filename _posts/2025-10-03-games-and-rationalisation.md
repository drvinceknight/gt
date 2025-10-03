---
layout: post
title: "The 2/3rds of the average game and playing against strategies"
tags:
  - games
  - rationalisation
---

In today's class we played the 2/3rds of the average game using that to define
what a game is in a mathematical sense, and also played against strategies to
start to understand the concept of rationalization.

You can find the recording of the class [here](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=f31d9532-ca76-4cb2-8ceb-b366010846ee).

In the two thirds of the average game we played twice:

1. The winning guess was Tom with a guess of 20.
2. After spending time discussing the fact that everyone would win with a guess
   of 0 the winning guess was much lower: 8.

You can see the board where I talked about the dominated actions for the game
here:

![]({{site.baseurl}}/assets/2025-2026/boards/2029-10-03/main.jpg)

I then went on to discuss the [Game Chapter](https://vknight.org/gtb/main-1/):

- I talked about the definition of [An Extensive Form Game](https://vknight.org/gtb/main-1/#definition-extensive-form-game) and how this did not apply to our case.
- We talked about the definition of [A Normal Form Game](https://vknight.org/gtb/main-1/#sec-normal-form-games) and how **this did** apply to the two thirds of the average game.
- We talked about what actions were (in the case of the 2 thirds of the average game this is the choice of integers from 0 to 100) and what the definition of a [Strategy](https://vknight.org/gtb/main-1/#sec-normal-form-games) was.

---

We started the second half of the class we played against 3 mixed strategies for
row player for the game you can find [here]({{site.baseurl}}/assets/activities/best_responses/main.pdf).
We played as the column player.

The main part of this was a lengthy discussion about the purpose of each matrix
and how it relates to the definition of a Normal Form Game.

This is an important conversation as it sets up for good foundations for these
objects that we will be using going forward.

After that we played against the computer picking actions using the specified
strategies. I used a Jupyter notebook for that that you can find
[here]({{site.baseurl}}/assets/nbs/rationalisation.ipynb).

We talked about "the best way of playing" against each strategy.

- Against \\((.2, .8)\\) we discussed that it was best to always pick the first
  column as we were more often than not in the last row.
- Against \\((.9, .1)\\) we discussed that it was best to always pick the second
  column as we were more often than not in the first row.
- Against \\((1/3, 2/3)\\) we had a slightly longer and perhaps non trivial
  conversation that in fact here there was no best option: this strategy had made
  us irrelevant.

This last point is in fact directly related to the first theorem of the course
which you can find [here](https://vknight.org/gtb/main-2/#thrm-best-response-condition). That chapter defines many important
notions such as dominance and best responses.

You can see the basic idea for calculating expected utilities I wrote on the
board here:

![]({{site.baseurl}}/assets/2025-2026/boards/2029-10-03/main_1.jpg)

This calculation is covered towards the end of [this section in the Games chapter](https://vknight.org/gtb/main-1/#definition-strategy-in-normal-form-games).
