---
layout: topic
title: "Routing Games"
tag: routing-games
note_urls:
  - "https://vknight.org/gtb/chapters/routing-games/"
---

## Example questions

The following are exam-type questions in the style of the examination paper.
**Each question is worth 25 marks.** Attempt them in full before reading the
worked solutions.

### Question 1 (based on the in-class activity)

In class we ran Braess's paradox. Forty drivers travel from \(S\) to \(T\).
Initially there are two routes: the top route is a small road \(S \to A\) whose
travel time in minutes equals the number of cars on it, followed by a motorway
\(A \to T\) fixed at 50 minutes; the bottom route is a motorway \(S \to B\) fixed
at 50 minutes followed by a small road \(B \to T\) whose time equals the number
of cars on it.

(a) Explain what a Nash flow is in this setting. [3]

(b) Find the Nash flow and the resulting travel time for each driver. [5]

(c) A new road \(A \to B\) taking 0 minutes is added. Show that all 40 drivers
using the route \(S \to A \to B \to T\) is now a Nash flow, and find the travel
time. [7]

(d) Compare the two travel times and explain, in terms of each driver ignoring
the congestion they impose on others, why adding a road made everyone worse off.
[7]

(e) With the shortcut in place, a social planner could still route 20 drivers
each way (ignoring the shortcut) for an average of 70 minutes. Compute the price
of anarchy of the network with the shortcut. [3]

### Question 2

(a) Provide definitions for the following terms:

   - a routing game;
   - a feasible flow;
   - a Nash flow;
   - an optimal flow. [4]

(b) A unit of traffic travels from \(s\) to \(t\) on two parallel routes, with
costs \(c_1(x) = 1\) and \(c_2(x) = x\) where \(x\) is the flow on route 2.

   (i) Find the Nash flow and its average cost. [3]

   (ii) Find the optimal flow and its average cost. [4]

   (iii) Compute the Price of Anarchy. [3]

(c) Define the potential function of a routing game, write down \(\Phi(x)\) for
this network, and show that minimising \(\Phi(x)\) recovers the Nash flow. [8]

(d) State the theorem relating the potential function to the Nash flow, and
explain why it makes Nash flows straightforward to compute. [3]

### Question 3

(a) Define the marginal cost of a route, and state the theorem relating the
optimal flow to the Nash flow for the marginal cost functions. [4]

(b) A unit of traffic travels from \(s\) to \(t\) on two parallel routes, with
costs \(c_1(x) = 2x\) and \(c_2(x) = 1\), where \(x\) is the flow on route 1.

   (i) Find the Nash flow and its average cost. [4]

   (ii) Find the optimal flow and its average cost. [5]

   (iii) Write the marginal cost functions and verify that the optimal flow is
   the Nash flow for the marginal costs. [5]

   (iv) Compute the Price of Anarchy. [3]

(c) Explain what the Price of Anarchy measures, and state what it would equal if
both routes had constant, flow-independent costs. [4]

### Question 4 (**hard**)

A unit of traffic travels from \(s\) to \(t\) on two parallel links. Link 1 has
cost \(c_1(x) = x^p\) with \(p \ge 1\), where \(x\) is the flow on link 1, and
link 2 has constant cost \(c_2(x) = 1\).

(a) Define the price of anarchy of a routing game. [4]

(b) Show that the Nash flow sends all traffic on link 1, and that its total travel
cost is \(1\). [6]

(c) Find the optimal flow by minimising the total travel cost
\(C(x) = x \cdot x^p + (1 - x)\), and hence show that the price of anarchy is

\[
\text{PoA} = \frac{1}{1 - x^{*}\,\frac{p}{p + 1}},
\qquad x^{*} = (p + 1)^{-1/p}.
\]

[9]

(d) Evaluate the price of anarchy at \(p = 1\), show that it tends to infinity as
\(p \to \infty\), and interpret what this says about selfish routing when costs
are steeply nonlinear, contrasting it with the affine case. [6]

## Optional further reading

You do not need any of this to follow the topic, but the following may help if
you would like more background:

- [Nash Equilibrium](https://vknight.org/gtb/chapters/nash-equilibrium/), since a
  Nash flow is the Nash equilibrium of the routing game.
- [Karush-Kuhn-Tucker Conditions](https://vknight.org/gtb/appendices/interior-point-optimisation/),
  which cover the constrained optimisation of flows.
