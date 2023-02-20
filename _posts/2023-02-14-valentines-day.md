---
layout: post
title:  "Valentines day"
tags:
    - normal-form-games
    - best-responses
    - support-enumeration
    - assessment
---

In today's class we spoke about a deadline for the individual coursework but
spent most of our time taking the initial steps that a research project would
take to model gift giving for Valentines day.

A recording of that class is available here: [https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=4f547fb9-f578-4091-b3f8-afa400a59c20](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=4f547fb9-f578-4091-b3f8-afa400a59c20).

**We agreed to an individual coursework deadline of Friday the 24th of March at
11am.**

After that discussion we started having an initial discussion about the
possibility of modelling Valentines day as a possible research project.

The approach we decided to take was from the point of view of a couple wondering
whether or not to buy each other gifts.

We agreed on an action set for both players of \\(\{\beta, \overline\beta\}\\)
where \\(\beta\\) corresponds to giving a gift and \\(\overline\beta\\)
corresponds to not giving a gift.

Some starting games we played around with were:

\\[
    A = 
    \begin{pmatrix}
        3 & 2 \\\\\\
        -3 & 0\\\
    \end{pmatrix}
    \qquad
    B = A ^ T
\\]

This corresponds to the case where both individuals have the same preferences
(which is why \\(A = B ^ T\\)) **and they both like to get gifts**.

Using [`nashpy`'s support enumeration implementation](https://nashpy.readthedocs.io/en/stable/text-book/support-enumeration.html) we find that there is a single [Nash equilibrium](https://nashpy.readthedocs.io/en/stable/text-book/best-responses.html#definition-of-nash-equilibrium) where both players give each other gifts:

\\[\sigma\_r = (1, 0)\qquad \sigma\_c = (1, 0)\\]

This is relatively intuitive: if both players like getting gifts (as reflected by
the utilities we chose)then it makes sense that giving gifts is what they should
do.

In the scenario where both players agree to not buy gifts for each other we used
the following utilities:

\\[
    A = 
    \begin{pmatrix}
        3 & 2 \\\\\\
        -3 & 0\\\
    \end{pmatrix}
    \qquad
    B = A ^ T
\\]

There are 3 Nash equilibria in this case:

\\[\sigma\_r = (1, 0)\qquad \sigma\_c = (1, 0)\\]
\\[\sigma\_r = (0, 1)\qquad \sigma\_c = (0, 1)\\]
\\[\sigma\_r = (1 / 2, 1 / 2)\qquad \sigma\_c = (1 / 2, 1 / 2)\\]

While there are 3 different "stable" situations here they do not necessarily
give the same expected utility. We can calculate that by taking the average
utility of both players:

\\[
    \frac{\sigma\_r A \sigma\_c ^ T + \sigma\_r B \sigma\_c ^ T}{2}
\\]

which in this case gives:

- Both players giving gifts gives an average utility of \\(3\\)
- Both players not giving gifts gives an average utility of \\(5\\)
- Both players randomly alternating between actions gives an average utility of \\(2\\)

The final case we considered was when both players had different utilities: the
row player cares more about Valentines day:

\\[
    A = 
    \begin{pmatrix}
        5 & 0 \\\\\\
        3 & 1\\\
    \end{pmatrix}
    \qquad
    B =
    \begin{pmatrix}
        3 & -2 \\\\\\
        3 & 1\\\
    \end{pmatrix}
\\]

There is a single equilibria in this case:

\\[\sigma\_r = (1, 0)\qquad \sigma\_c = (1, 0)\\]

with both players choosing to give gifts.

Note that if we modify the matrix \\(B\\) slightly things might change. Let us
assume some parameter \\(\alpha\\) that we add to the second row of \\(B\\): ie
this is an extra utility that we give to the column player fore not giving a
gift.

\\[
    B =
    \begin{pmatrix}
        3 & -2 + \alpha \\\\\
        3 & 1 + \alpha\\\
    \end{pmatrix}
\\]

We can then see how this affects the best and worst average utility of the
players as a function of \\(\alpha\\) in [this plot]({{ site.baseurl
}}/assets/2022-2023/nbs/2023-02-14-valentines_day.png).

We can see there is a region of space where we have different equilibria (the
minimum and the maximum is not the same)
followed by a point at which there is a single equilibria again (but this is
probably the equilibria where both players do not give gifts).

If we were to continue all this we would probably ask the following questions:

1. How would game theory help us "solve" this problem (if we consider it to be a
   problem). I suspect the answer would be to look at the effect of genuine (or
   as Thomas said in class: "efficient") communication. How does that modify our
   game matrices?
2. Adding a third action: having a hidden gift that the players only unleash to "save
   face"
3. Repeating this: if the couple remembers what happened last year and acts
   accordingly this corresponds to a [repeated
   game](https://vknight.org/gt/topics/repeated-games.html) and it becomes a
   similar problem to a blog post I wrote a few years back about the [dilemma of giving gifts](https://vknight.org/unpeudemath/code/2015/12/15/The-Prisoners-Dilemma-of-Christmas-Gifts.html)

The notebook I used in class (with some modifications to do a bit of what I wrote about) is  [here]({{ site.baseurl }}/assets/2022-2023/nbs/2023-02-14-gt.ipynb).
above in Python.
