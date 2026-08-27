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

Two delivery companies send vans from their own warehouses to a shared depot
\(t\). Company 1 must route \(r_1 = 1/2\) units of traffic from \(s_1\), and
company 2 must route \(r_2 = 1/2\) units from \(s_2\). Each company has a
dedicated road to the depot, and each can instead send vans through a junction
\(a\) onto a shared ring road. The network is \(G = (V, E)\) with
\(V = \{s_1, s_2, a, t\}\) and

\[
E = \{(s_1, t), (s_1, a), (s_2, t), (s_2, a), (a, t)\},
\]

with cost functions

\[
c_{s_1, t}(x) = x, \qquad
c_{s_2, t}(x) = \frac{1}{2}, \qquad
c_{s_1, a}(x) = c_{s_2, a}(x) = 0, \qquad
c_{a, t}(x) = x,
\]

where on the ring road \(x\) is the total flow from both companies.

(a) Write down the sets of paths \(\mathcal{P}_1\) and \(\mathcal{P}_2\).
Writing \(\alpha\) for the flow on \((s_1, t)\) and \(\beta\) for the flow on
\((s_2, t)\), give the flow vector \(f\), state the conditions for \(f\) to be
feasible, and show that the total cost is

\[
C(\alpha, \beta) = \alpha^2 + \frac{\beta}{2} + (1 - \alpha - \beta)^2.
\]

[7]

(b) Find the Nash flow \(\tilde f\) and its total cost, verifying that the
Nash condition holds for both commodities. [7]

(c) Find the optimal flow \(f^{*}\) and its total cost. [7]

(d) Compute the price of anarchy. Explain how the optimal flow treats company 2
differently from the Nash flow, and relate the value you obtain to the price of
anarchy of Pigou's example with affine costs. [4]

## Marking exercises (optional)

These exercises are entirely optional: they are extra practice, not extra
content. The best way to use an AI assistant is to be its examiner, not its
student: checking work is exactly the skill the examination rewards, and the
skill you will need to use these tools well. Each exercise gives a transcript
in the style of a widely used free AI chatbot answering one of the example
questions above. Every transcript contains at least one error. Mark it as an
examiner would: find each error, explain what goes wrong, and award a mark
out of the marks of the original question. A marker's report for each
transcript is on the solutions page.

### Marking exercise 1 (on Question 3(b)(i) and (ii), worth [4] and [5])

A student pastes Question 3(b) into a free AI chatbot, which replies:

```text
Nash flow: drivers switch routes until the costs are equal: 2x = 1
gives x = 1/2, and each route then costs 1. ✅

Optimal flow: the social planner also wants the two routes to cost the
same, since otherwise some drivers are on a more expensive route and
the allocation could be improved. So the optimal flow is also x = 1/2,
with average cost 1. This network has no inefficiency, and its Price of
Anarchy is 1.
```

### Marking exercise 2 (on Question 2(c), worth [8])

A student pastes Question 2(c) into a free AI chatbot, which replies:

```text
The potential function of a routing game is the total cost of the flow:

    Φ(x) = (1 - x)·1 + x·x = 1 - x + x²

Minimising: Φ'(x) = -1 + 2x = 0 gives x = 1/2. This is the Nash flow,
confirming the theorem that the Nash flow minimises the potential
function. ✅
```

## Optional further reading

You do not need any of this to follow the topic, but the following may help if
you would like more background:

- [Nash Equilibrium](https://vknight.org/gtb/chapters/nash-equilibrium/), since a
  Nash flow is the Nash equilibrium of the routing game.
- [Karush-Kuhn-Tucker Conditions](https://vknight.org/gtb/appendices/interior-point-optimisation/),
  which cover the constrained optimisation of flows.
