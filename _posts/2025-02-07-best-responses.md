---
layout: post
title: "Best responses against computer strategies"
tags:
  - best-responses
---

In class today we spoke more about strategies which are methods for picking
actions from action sets. Specifically we spoke about best responses: what is
the best strategy when faced with a given strategy.

A recording of that class is available [here](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=3bd27dc5-0f5a-487b-9ce0-b27801085e45).

I started class by discussing what the original expectations you had might have
been about Game Theory and if anyone had any queries. No one did which is good
news as I assume it means I've made the expectations of the class clear. If
that's not quite right and you still have any questions please get in touch!

I also reminded you that the deadline to form your groups was coming up, if you
need a hand to get in touch with your assigned group please let me know.

After this we played [matching pennies](https://vknight.org/gt/assets/activities/best_responses/main.pdf) against strategies played by a computer.
A large group of you seemed to grasp early that there was a "right" way to play
against the first two strategies.

We took at look at calculating the best response \\(\sigma_c\*\\)
against
the strategy \\(\sigma_r=(x, 1-x)\\).

We saw that depending on the value of \\(x\\) we had 3 possible best responses:

- If \\(x=.8\\) then \\(\sigma_c\*=(1, 0)\\): we should always play the first:
  column.
- If \\(x=.1\\) then \\(\sigma_c\*=(0, 1)\\): we should always play the second
  column.
- If \\(x=1/3\\) then \\(\sigma_c^\*\\) can be any valid strategy: it does not
  matter what we do.

All of this was lead by the idea that the expectation for a given \\(\sigma_c\\)
is a linear function. The function can either:

- Be increasing in \\(y\\): then it is optimised for \\(y=1\\).
- Be decreasing in \\(y\\): then it is optimised for \\(y=0\\).
- Be a flat line that does not depend on \\(y\\).

I pointed out that \\(\sigma^rB\\) is a
row vector that is essentially the **game from the column players point of view** for a given
value of \\(\sigma_r\\)\*.

This leads to the concepts described in this section of the notes:
[nashpy.readthedocs.io/en/stable/text-book/best-responses.html#generic-best-responses-in-2-by-2-games](https://nashpy.readthedocs.io/en/stable/text-book/best-responses.html#generic-best-responses-in-2-by-2-games)

Which is that we could write down a generic form of \\(\sigma_c^\*\\):

\\[
\sigma\_c^*=
\begin{cases}
(0, 1),&\text{ if } x > 1/3\\\\\\
(1, 0),&\text{ if } x < 1/3\\\\\\
\text{indifferent},&\text{ if } x = 1/3
\end{cases}
\\]

We spent some time then doing the same thing for \\(\sigma_r^\*\\):

\\[
\sigma\_r^* =
\begin{cases}
(1, 0),&\text{ if } y > 1/2\\\\\\
(0, 1),&\text{ if } y < 1/2\\\\\\
\text{indifferent},&\text{ if } y = 1/2
\end{cases}
\\]

(where \\(y\\) is the probability of being in the first column).

I then passed briefly over the remaining sections of the notes:

- [A general condition for a best response (in games that are bigger than 2 by 2) which is the only way the above process works](https://nashpy.readthedocs.io/en/stable/text-book/best-responses.html#general-condition-for-a-best-response)

One thing I did not do in class was:

- [Using Nashpy to check the best response condition for pairs of strategies](https://nashpy.readthedocs.io/en/stable/how-to/check-best-responses.html#how-to-check-best-responses)
