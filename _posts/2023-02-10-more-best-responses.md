---
layout: post
title:  "More best responses"
tags:
    - best-responses
---

Friday's class was hopefully helpful: we spent some time working on drawing
linear functions for best response calculations.

A recording of that class is available here: [cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=8d77c214-cc1e-4e66-928b-afa000c67cb1](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=8d77c214-cc1e-4e66-928b-afa000c67cb1).

We took at look at calculating the best response \\(\sigma\_c*\\) 
against 
the strategy \\(\sigma\_r=(x, 1-x)\\).

We saw that depending on the value of \\(x\\) we had 3 possible best responses:

- If \\(x=.8\\) then \\(\sigma\_c*=(1, 0)\\): we should always play the first:
  column.
- If \\(x=.1\\) then \\(\sigma\_c*=(0, 1)\\): we should always play the second
  column.
- If \\(x=1/3\\) then \\(\sigma\_c^*\\) can be any valid strategy: it does not
  matter what we do.

This leads to the concepts described in this section of the notes:
[nashpy.readthedocs.io/en/stable/text-book/best-responses.html#generic-best-responses-in-2-by-2-games](https://nashpy.readthedocs.io/en/stable/text-book/best-responses.html#generic-best-responses-in-2-by-2-games)

Which is that we could write down a generic form of \\(\sigma\_c^*\\):

\\[
\sigma\_c^*=
\begin{cases}
    (0, 1),&\text{ if } x > 1/3\\\\\\
    (1, 0),&\text{ if } x < 1/3\\\\\\
    \text{indifferent},&\text{ if } x = 1/3
\end{cases}
\\]

I left as an exercise to repeat the procedure for \\(\sigma\_r^*\\) which gives:


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

- [A general condition for a best response (in games that are bigger than 2 by
  2) which is the only way the above process works](https://nashpy.readthedocs.io/en/stable/text-book/best-responses.html#general-condition-for-a-best-response)
- [Using Nashpy to check the best response condition for pairs of strategies](https://nashpy.readthedocs.io/en/stable/how-to/check-best-responses.html#how-to-check-best-responses)

I did not use this in class but [here]({{ site.baseurl }}/assets/2022-2023/nbs/2023-02-10-gt.ipynb) is a Jupyter notebook with some of the
above in Python.
