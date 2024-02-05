---
layout: post
title: "Best responses against computer strategies"
tags:
  - best-responses
---

In class today we spoke more about strategies which are methods for picking
actions from action sets. Specifically we spoke about best responses: what is
the best strategy when faced with a given strategy.

A recording of that class is available here: [https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=45a3c766-d0bc-4b49-8f7f-b10800c652b0](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=45a3c766-d0bc-4b49-8f7f-b10800c652b0).

We started class by discussing what the original expectations you had might have
been about Game Theory:

- Someone mentioned being surprised by how much mathematics was involved.
- Someone mentioned the Golden Balls game show. I'm not entirely sure if this
  a reflection on an expectation for more **Parlour/Recreational Games** (like
  [Nim](https://en.wikipedia.org/wiki/Nim) or just specific to Golden Balls. If
  it's the latter well I have good news, Golden Balls is actually a version of
  the prisoners dilemma and in fact we'll be spending a lot of time on this when
  looking at the mathematics of cooperation.

After this we played [matching pennies](https://vknight.org/gt/assets/activities/best_responses/main.pdf) against strategies played by a computer.
As usual you all had some great suggestions and good ideas. Thank you for your
engagement and the discussions we're having in class.

We took at look at calculating the best response \\(\sigma_c\*\\) (although in
class I used \\(\sigma_2\\) interchangeably)
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

An interesting concept one of you raised was that \\(\sigma^rB\\) which is a
row vector is essentially the **game from the column players point of view**. I
hadn't heard anyone put that like that and it's completely correct \*for a given
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

I left as an exercise to repeat the procedure for \\(\sigma_r^\*\\) which gives:

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
- [Using Nashpy to check the best response condition for pairs of strategies](https://nashpy.readthedocs.io/en/stable/how-to/check-best-responses.html#how-to-check-best-responses)

I started writing a notebook to demonstrate some things but realised that I was
rushing things so I'm going to do that at the start of the next class.
