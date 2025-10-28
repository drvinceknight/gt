---
layout: post
title: "Using absorbing Markov chains to model the timeline of an undergraduate program"
tags:
  - absorbing-markov-chains
---

In class we talked explored one of my favourite mathematical tools: Absorbing
Markov Chains to model the lifeline of a student going through an undergraduate
degree. This isn't a particular tool that is only used in Game Theory but is in
fact used in a number of different areas. It is however the fundamental building
block for the next evolutionary game theoretic model we will be looking at.

You can see a recording of this [here](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=0aa08f51-5a20-47a2-9919-b37e0094de13).

We started by discussing the various states a student can be in going through
their degree:

1. Year 1: 1
2. Year 2: 2
3. Year 3: 3
4. Year 4: 4
5. Year in industry: I
6. Year abroad: A
7. Exit (reasons could be dropping out or getting a job): E
8. Graduate: G

We drew these states and then wrote down all the ways a student can go from one
state to the next:

![]({{site.baseurl}}/assets/2025-2026/boards/2025-10-27/main.jpg)

These arrows only show possible connections but do not represent how probable
any given route is. We use a transition matrix for this: \\(P\_{ij}\\) gives the
probability of going from state \\(i\\) to state \\(j\\). In our case we came up with
a transition matrix \\(P\\).

On the photo of the board you can see the general form of an absorbing Markov
chain which must have at least one \\(1\\) in the diagonal which indicates that the
corresponding state will never be exited once reached.

$$
P = \begin{pmatrix}
    Q & R\\
    0 & \mathbb{1}\\
\end{pmatrix}
$$

From that I used some basic Python to compute the following values:

- The fundamental matrix:

$$N = (\mathbb{1} - Q)^{-1}$$

- The absorption probability matrix:

$$B=NR$$

The main computationally challenging part of this calculation is inverting a
matrix.
You can find the notebook I used to do all this [here]({{site.baseurl}}/assets/2025/2026/nbs/degree-pathways.ipynb)
and also an algorithm for doing this by hand [here](https://vknight.org/gtb/main-16/#sec-gauss-jordan).

We obtained:

$$
B=\begin{pmatrix}
0.54922601 & 0.45077399 \\
0.36140351 & 0.63859649 \\
0.05555556 & 0.94444444 \\
0.00000000 & 1.00000000 \\
0.15000000 & 0.85000000 \\
0.10526316 & 0.89473684
\end{pmatrix}
$$

The first row of that matrix tells us that 54% of first years end up exiting
without graduating. Whereas the fourth row which corresponds to year 4 students
says that 100% of those students end up graduating.
