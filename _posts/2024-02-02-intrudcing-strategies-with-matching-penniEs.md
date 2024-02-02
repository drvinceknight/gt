---
layout: post
title: "Introducing strategies with matching penniEs"
tags:
  - strategies
---

Today we mainly talked about what a strategy was: defining it as a way of
picking actions.

A recording of this class is available here: [https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=3a87cbb9-72fa-4a03-a335-b10500c67c26](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=17112445-87ad-493c-83d8-af9900c683e8)

We did this by pairing up and playing two different games:

1. The traditional [matching
   pennies](https://nashpy.readthedocs.io/en/stable/text-book/normal-form-games.html#matching-pennies)
   game defined by the two payoff matrices: \\(A=\begin{pmatrix}1 & -1\\\\-1 &
   1\end{pmatrix}\\) and \\(A=-B\\).
2. The modification of matching
   pennies which is the game defined by the two payoff matrices: \\(A=\begin{pmatrix}2 & -2\\\\-1 &
   1\end{pmatrix}\\) and \\(A=-B\\).

As well as briefly talking about strategies we mainly made sure everyone
understood the notion of picking from an action set, how this is not necessarily
random but also what we would mean by random.

I briefly (because I'm an idiot and thought I had 10 less minutes than
I did): showed [how to define a game using
nashpy](https://nashpy.readthedocs.io/en/stable/how-to/create-a-game.html). If
you would like to download the notebook I wrote in class it is [here]({{ site.baseurl }}/assets/2023-2024/nbs/2024-02-02-gt.ipynb).

At the end of class someone came up to me and said that for the second game,
they actually both chose their actions for the entire 5 plays before showing
them (as opposed to picking, showing and then picking the next). This is
arguably a "right way to do it" as the strategy
is completely independent of the actions of the opponent.
