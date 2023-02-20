---
layout: post
title:  "Introducing strategies with matching pennies"
tags:
    - strategies
---

Today we mainly talked about what a strategy was: defining it as a way of
picking actions.

A recording of this class is available here: [https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=17112445-87ad-493c-83d8-af9900c683e8](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=17112445-87ad-493c-83d8-af9900c683e8)

We did this by pairing up and playing two different games:

1. The traditional [matching
   pennies](https://nashpy.readthedocs.io/en/stable/text-book/normal-form-games.html#matching-pennies)
   game defined by the two payoff matrices: \\(A=\begin{pmatrix}1 & -1\\\\-1 &
   1\end{pmatrix}\\) and \\(A=-B\\).
2. The modification of matching
   pennies which is the game defined by the two payoff matrices: \\(A=\begin{pmatrix}2 & -2\\\\-1 &
   1\end{pmatrix}\\) and \\(A=-B\\).

For the second game there was some interesting discussion about which player
might have an advantage: the row player or the column player? We wil revisit
this.

There was one or two mentions of strategies where a player chose a particular
atcion \\(2/3\\)rds of the time. If you are curious about what this might be,
you can read ahead to [the course chapter on best responses](https://nashpy.readthedocs.io/en/stable/text-book/best-responses.html).

I briefly (because I'm an idiot and thought I had 10 less minutes than
I did): showed [how to define a game using
nashpy](https://nashpy.readthedocs.io/en/stable/how-to/create-a-game.html). If
you would like to download the notebook I wrote in class it is [here]({{ site.baseurl }}/assets/2022-2023/nbs/2023-02-03-gt.ipynb).

Finally, I have added an [FAQ](https://vknight.org/gt/#faqs) about installing
Python.
