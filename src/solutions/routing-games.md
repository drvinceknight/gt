---
layout: solution
title: "Routing Games"
tag: routing-games
---

# Routing Games: worked solutions

Solutions to the example questions on the
[Routing Games](/topics/routing-games.html) page. Each question is worth 25
marks.

## Question 1 [25 marks]

**(a) Nash flow.** [3]

The traffic is non-atomic: one unit of flow split across the routes, with each
driver a negligible share of it. A Nash flow is a feasible split in which every
route actually used has minimal cost: if \(f_{P_1} > 0\) then
\(c_{P_1}(f) \leq c_{P_2}(f)\) for every other route \(P_2\), with both costs
evaluated at the same flow \(f\). Since one driver's switch does not change
\(f\), no driver can then reduce their own cost by switching route.

**(b) Nash flow before the new road.** [5]

Let \(x\) be the flow on the top route and \(1 - x\) the flow on the bottom. The
top route costs \(x + 1\) and the bottom costs \(1 + (1 - x)\). Both routes are
used, so at a Nash flow the two costs are equal:

\[
x + 1 = 2 - x \;\Longrightarrow\; x = \frac{1}{2}.
\]

Half of the traffic takes each route, and each route costs
\(\frac{1}{2} + 1 = \frac{3}{2}\).

**(c) Nash flow after the new road.** [7]

Suppose all of the traffic takes \(S \to A \to B \to T\). Both small roads then
carry a flow of \(1\), so this route costs \(1 + 0 + 1 = 2\). At the same flow,
the top route \(S \to A \to T\) costs \(1 + 1 = 2\) and the bottom route
\(S \to B \to T\) costs \(1 + 1 = 2\). The only route in use has cost \(2\), and
no other route is cheaper, so the Nash condition holds: sending everything
along \(S \to A \to B \to T\) is a Nash flow, and every driver's cost is \(2\).

**(d) Braess's paradox.** [5]

Before the new road every driver's cost was \(\frac{3}{2}\); after it, every
driver's cost is \(2\). Adding a road made everyone worse off. Each driver
chooses the route that is best for them, ignoring the extra congestion they add
to the small roads \(S \to A\) and \(B \to T\). The free road draws everyone onto
both congested edges at once, and the resulting Nash flow is more costly than
the original. The selfish (Nash) outcome need not be the social optimum, and
extra capacity can make the selfish outcome worse.

**(e) Price of Anarchy with the new road.** [5]

The marginal cost of an edge with cost \(c(x)\) is
\(\frac{\mathrm{d}}{\mathrm{d}x}\big(x\,c(x)\big)\): \(2x\) on each small road,
\(1\) on each motorway and \(0\) on the new road. With half of the traffic on
each of the top and bottom routes and none on \(S \to A \to B \to T\), each small
road carries \(\frac{1}{2}\) and has marginal cost \(1\). The marginal cost of
each route is then

\[
\underbrace{1 + 1}_{S \to A \to T} = \underbrace{1 + 1}_{S \to B \to T}
= \underbrace{1 + 0 + 1}_{S \to A \to B \to T} = 2.
\]

Every used route has minimal marginal cost, so this flow is a Nash flow for the
marginal costs, and so, by the theorem that an optimal flow is a Nash flow for
marginal costs, it is the optimal flow. Its total cost is

\[
C(f^{*}) = \frac{1}{2} \cdot \frac{1}{2} + \frac{1}{2} \cdot 1
+ \frac{1}{2} \cdot 1 + \frac{1}{2} \cdot \frac{1}{2} = \frac{3}{2},
\]

against \(C(\tilde f) = 1 \cdot 1 + 1 \cdot 0 + 1 \cdot 1 = 2\) for the Nash flow.
The Price of Anarchy is

\[
\frac{C(\tilde f)}{C(f^{*})} = \frac{2}{3/2} = \frac{4}{3}.
\]

The planner makes no use of the new road at all, and the price of anarchy is
the same \(\frac{4}{3}\) as Pigou's example in Question 2: with affine costs this
is the worst that selfish routing can do.

## Question 2 [25 marks]

[YouTube video](https://www.youtube.com/watch?v=QZlxrhmdtBk)

**(a) Definitions.** (Bookwork.) [4]

- A **routing game** \((G, r, c)\) is defined on a graph \(G = (V, E)\) with
  source-sink pairs, each carrying a commodity \(r_i\) of traffic; every edge
  \(e\) has a non-negative, continuous and non-decreasing cost function
  \(c_e\).
- A flow \(f\), a vector indexed by the paths, is a **feasible flow** if for
  each commodity \(i\) the flow on its paths sums to the demand,
  \(\sum_{P \in \mathcal{P}_i} f_P = r_i\), with \(f_P \ge 0\).
- A **Nash flow** is a feasible flow \(\tilde{f}\) such that for every commodity
  \(i\) and any two of its paths \(P_1, P_2\) with \(f_{P_1} > 0\) we have
  \(c_{P_1}(f) \le c_{P_2}(f)\); every used path has minimal cost.
- An **optimal flow** is a feasible flow minimising the total cost
  \(C(f) = \sum_{e \in E} c_e(f_e) f_e\).

**(b)(i) Nash flow.** [3]

Route 1 always costs \(1\) and route 2 costs \(x \le 1\), so all traffic uses
route 2: \(x = 1\) with average cost \(1\).

**(b)(ii) Optimal flow.** [4]

\(C(x) = x^2 + (1 - x)\), minimised at \(C'(x) = 2x - 1 = 0\), so
\(x = \tfrac{1}{2}\) with average cost \(\tfrac{3}{4}\).

**(b)(iii) Price of Anarchy.** [3]

\[
\frac{1}{3/4} = \frac{4}{3}.
\]

**(c) Potential function.** [8]

The **potential function** is \(\Phi = \sum_e \int_0^{f_e} c_e(t)\,\mathrm{d}t\).
For this network, with flow \(x\) on route 2 and \(1 - x\) on route 1,

\[
\Phi(x) = \int_0^{1 - x} 1\,\mathrm{d}t + \int_0^{x} t\,\mathrm{d}t
= (1 - x) + \frac{x^2}{2}.
\]

Then \(\Phi'(x) = -1 + x = 0\) gives \(x = 1\), and \(\Phi''(x) = 1 > 0\), so the
minimiser is \(x = 1\). This is the Nash flow of part (b)(i): minimising the
potential function recovers the Nash flow, in contrast to minimising the total
cost which gives the optimal flow \(x = \tfrac{1}{2}\).

**(d) Theorem.** (Bookwork.) [3]

A feasible flow \(\tilde{f}\) is a Nash flow of \((G, r, c)\) if and only if it
minimises the potential function \(\Phi\). This makes Nash flows easy to compute:
rather than reasoning about every driver's incentive to switch, we just minimise
a single function \(\Phi\) by calculus, exactly as above.

## Question 3 [25 marks]

[YouTube video](https://www.youtube.com/watch?v=VcGNRhe9yNE)

**(a) Marginal cost and theorem.** (Bookwork.) [4]

The **marginal cost** of a route with cost \(c_e\) carrying flow \(f_e\) is
\(\dfrac{\mathrm{d}}{\mathrm{d} f_e}\bigl(f_e\, c_e(f_e)\bigr)\). The theorem
states that the optimal flow of a routing game is the Nash flow of the game with
each cost function replaced by its marginal cost.

**(b)(i) Nash flow.** [4]

With flow \(x\) on route 1, costs are \(2x\) and \(1\). Equilibrium equalises
them: \(2x = 1\), so \(x = \tfrac{1}{2}\). Each route then costs \(1\), giving
average cost \(1\).

**(b)(ii) Optimal flow.** [5]

\[
C(x) = x(2x) + (1 - x)(1) = 2x^2 - x + 1,
\qquad C'(x) = 4x - 1 = 0 \Rightarrow x = \tfrac{1}{4}.
\]

The average cost is
\(C\!\left(\tfrac{1}{4}\right) = 2\cdot\tfrac{1}{16} - \tfrac{1}{4} + 1
= \tfrac{7}{8}\).

**(b)(iii) Marginal costs.** [5]

The marginal costs are \(\tfrac{\mathrm{d}}{\mathrm{d}x}(x \cdot 2x) = 4x\) on
route 1 and \(\tfrac{\mathrm{d}}{\mathrm{d}x}(x \cdot 1) = 1\) on route 2.
Equalising them, \(4x = 1\) gives \(x = \tfrac{1}{4}\), which is exactly the
optimal flow, confirming the theorem.

**(b)(iv) Price of Anarchy.** [3]

\[
\frac{1}{7/8} = \frac{8}{7}.
\]

**(c) Interpreting the Price of Anarchy.** [4]

The Price of Anarchy is the ratio of the cost of the selfish (Nash) flow to the
cost of the optimal flow: it measures how much worse self-interested routing is
than a coordinated social optimum. If both routes had constant, flow-independent
costs, then no driver's choice would affect anyone else, the Nash flow would
coincide with the optimal flow, and the Price of Anarchy would equal \(1\). It is
congestion, costs that rise with flow, that creates the gap.

## Question 4 [25 marks]

**(a) Paths, flow vector and cost.** [7]

Each commodity can use its dedicated road or reach the depot through the
junction:

\[
\mathcal{P}_1 = \{(s_1, t),\, (s_1, a, t)\},
\qquad
\mathcal{P}_2 = \{(s_2, t),\, (s_2, a, t)\}.
\]

With \(\alpha\) on \((s_1, t)\), feasibility for commodity 1 forces
\(1/2 - \alpha\) on \((s_1, a, t)\), and similarly for commodity 2, so

\[
f = \bigl(f_{(s_1, t)},\, f_{(s_1, a, t)},\, f_{(s_2, t)},\, f_{(s_2, a, t)}\bigr)
= \left(\alpha,\, \tfrac{1}{2} - \alpha,\, \beta,\, \tfrac{1}{2} - \beta\right),
\]

which is feasible when \(0 \le \alpha \le \tfrac{1}{2}\) and
\(0 \le \beta \le \tfrac{1}{2}\). The ring road carries the traffic of both
companies,
\(f_{(a, t)} = (\tfrac{1}{2} - \alpha) + (\tfrac{1}{2} - \beta) = 1 - \alpha - \beta\).
Summing \(c_e(f_e)\, f_e\) over the edges (the connectors cost nothing):

\[
C(\alpha, \beta) = \alpha \cdot \alpha + \frac{1}{2}\,\beta
+ (1 - \alpha - \beta)(1 - \alpha - \beta)
= \alpha^2 + \frac{\beta}{2} + (1 - \alpha - \beta)^2.
\]

**(b) The Nash flow.** [7]

Write \(s = 1 - \alpha - \beta\) for the flow on the ring road, and suppose both
commodities use both of their paths, so each commodity's two paths cost the
same:

\[
\alpha = s \quad\text{(commodity 1)},
\qquad
\frac{1}{2} = s \quad\text{(commodity 2)}.
\]

These give \(\alpha = \tfrac{1}{2}\) and hence \(\beta = 0\): the solution sits
on the boundary, with commodity 1 sending nothing through the junction and
commodity 2 sending nothing on its dedicated road. We therefore verify the Nash
condition at \(\tilde f = (\tfrac{1}{2}, 0, 0, \tfrac{1}{2})\) directly.
Commodity 1 uses only \((s_1, t)\), at cost \(\tfrac{1}{2}\); its alternative
\((s_1, a, t)\) costs \(0 + s = \tfrac{1}{2}\). Commodity 2 uses only
\((s_2, a, t)\), at cost \(\tfrac{1}{2}\); its alternative \((s_2, t)\) costs
\(\tfrac{1}{2}\). Every used path has minimal cost, so \(\tilde f\) is a Nash
flow.

This is in fact the only Nash flow. If \(s > \tfrac{1}{2}\) then commodity 2's
ring path costs more than its dedicated road, so \(\beta = \tfrac{1}{2}\) and
\(s = \tfrac{1}{2} - \alpha \le \tfrac{1}{2}\), a contradiction; if
\(s < \tfrac{1}{2}\) then its dedicated road is the dearer, so \(\beta = 0\) and
\(s = 1 - \alpha \ge \tfrac{1}{2}\), again a contradiction. Hence
\(s = \tfrac{1}{2}\), and if commodity 1 used the ring path the Nash condition
would force \(\tfrac{1}{2} \le \alpha\), so \(\alpha = \tfrac{1}{2}\) and
\(\beta = 0\). The total cost is

\[
C(\tilde f) = \left(\frac{1}{2}\right)^2 + \frac{1}{2}\cdot 0
+ \left(\frac{1}{2}\right)^2 = \frac{1}{2}.
\]

**(c) The optimal flow.** [7]

The cost \(C(\alpha, \beta)\) is strictly convex, so the stationary point is the
minimiser provided it is feasible. Stationarity gives

\[
\begin{aligned}
\frac{\partial C}{\partial \alpha} &= 2\alpha - 2(1 - \alpha - \beta) = 0, \\
\frac{\partial C}{\partial \beta} &= \frac{1}{2} - 2(1 - \alpha - \beta) = 0.
\end{aligned}
\]

The second equation gives ring-road flow \(1 - \alpha - \beta = \tfrac{1}{4}\),
and then the first gives \(\alpha = \tfrac{1}{4}\), hence
\(\beta = \tfrac{1}{2}\). Both lie in \([0, \tfrac{1}{2}]\), so

\[
f^{*} = \left(\frac{1}{4}, \frac{1}{4}, \frac{1}{2}, 0\right),
\qquad
C(f^{*}) = \frac{1}{16} + \frac{1}{4} + \frac{1}{16} = \frac{3}{8}.
\]

As a check, the marginal costs are \(2x\), \(\tfrac{1}{2}\) and \(2x\), and
equalising them for each commodity gives \(2\alpha = 2(1 - \alpha - \beta)\) and
\(\tfrac{1}{2} = 2(1 - \alpha - \beta)\): exactly the stationarity conditions,
confirming that the optimal flow is the Nash flow for the marginal costs.

**(d) The price of anarchy.** [4]

\[
\text{PoA} = \frac{C(\tilde f)}{C(f^{*})} = \frac{1/2}{3/8} = \frac{4}{3}.
\]

At the Nash flow company 2 has no incentive to use its dedicated road, since
both of its options cost \(\tfrac{1}{2}\), so its vans fill half the ring road.
The planner instead routes company 2 entirely on its dedicated road, which costs
it nothing extra because that cost is flow-independent, and frees the ring road
so that company 1 can split its traffic at a cost of \(\tfrac{1}{4}\) per path
rather than \(\tfrac{1}{2}\). All of the saving comes from company 1, while
company 2 is no worse off. The value \(\tfrac{4}{3}\) is exactly the price of
anarchy of Pigou's example: all the cost functions here are affine, and this
two-commodity network attains the same worst-case bound.

## Marking exercises

**Marking exercise 1 (Question 3(b)(i) and (ii)).**

The Nash flow is correct: [4] of [4].

The optimal flow is not found by equalising costs: equal costs on all used
routes is precisely the *Nash* condition, so the transcript has simply
computed the Nash flow twice. The optimal flow minimises the average cost
\(C(x) = 2x^2 + (1 - x)\), giving \(C'(x) = 4x - 1 = 0\), \(x =
\tfrac{1}{4}\) and average cost \(\tfrac{7}{8} < 1\), as in the solution
above. The justification offered, that unequal costs mean "the allocation
could be improved", is exactly wrong: an optimum deliberately leaves the
\(\tfrac{1}{4}\) of drivers on the congestible route facing a *lower* cost
than the rest, trading a few drivers' time for less congestion overall,
which is what equalising *marginal* costs in part (iii) captures. The
downstream claim that the Price of Anarchy is \(1\) falls with it: the
correct value is \(\tfrac{8}{7}\). A fair mark is [0] of [5] for (ii).

**Marking exercise 2 (Question 2(c)).**

The potential function is not the total cost. Each edge contributes the
*integral* of its cost function up to its flow,

\[
\Phi(x) = \int_0^{1 - x} 1 \, \mathrm{d}t + \int_0^{x} t \, \mathrm{d}t
= (1 - x) + \frac{x^2}{2},
\]

whose minimum over \([0, 1]\) is at \(x = 1\): the Nash flow sends all the
traffic down route 2, where both routes then cost \(1\), as in the solution
above. What the transcript minimised, \(\sum_e x_e c_e(x_e)\), is the total
cost, and its minimiser \(x = \tfrac{1}{2}\) is the *optimal* flow, not the
Nash flow. The answer even fails its own check: at \(x = \tfrac{1}{2}\)
route 2 costs \(\tfrac{1}{2}\) and route 1 costs \(1\), so every driver on
route 1 would switch, which is not a Nash flow by definition. The
distinction between \(\sum_e x_e c_e(x_e)\) and
\(\sum_e \int_0^{x_e} c_e(t)\,\mathrm{d}t\) is exactly the distinction
between the optimal and the Nash flow, which is why the two theorems in this
topic are worth keeping apart. A fair mark is [2] of [8], for the shape of
the definition and the calculus.
