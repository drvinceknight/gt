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

A Nash flow is a way the drivers split across the routes such that no individual
driver can reduce their own travel time by switching route; every route actually
used has minimal cost.

**(b) Nash flow before the shortcut.** [5]

Let \(x\) drivers take the top route and \(40 - x\) the bottom. The top route
costs \(x + 50\) and the bottom costs \(50 + (40 - x)\). At a Nash flow these are
equal:

\[
x + 50 = 50 + (40 - x) \;\Longrightarrow\; x = 20.
\]

So 20 drivers take each route, and every driver's travel time is
\(20 + 50 = 70\) minutes.

**(c) Nash flow after the shortcut.** [7]

Suppose all 40 drivers take \(S \to A \to B \to T\). Then 40 cars are on
\(S \to A\) and 40 on \(B \to T\), giving a travel time of \(40 + 0 + 40 = 80\)
minutes. A driver who deviates to the old top route \(S \to A \to T\) pays
\(40 + 50 = 90\) minutes, and one who deviates to \(S \to B \to T\) pays
\(50 + 40 = 90\) minutes. Both are worse than 80, so no driver can improve by
switching: the zig-zag flow is a Nash flow.

**(d) Braess's paradox.** [7]

Before the road, every driver took 70 minutes; after it, every driver takes 80.
Adding a road made everyone worse off. Each driver chooses the route that is best
for them, ignoring the extra congestion they add to the small roads \(S \to A\)
and \(B \to T\). The free shortcut tempts everyone onto both congested edges at
once, and the resulting Nash flow is more costly than the original. The selfish
(Nash) outcome need not be the social optimum, and extra capacity can make the
selfish outcome worse.

**(e) Price of Anarchy with the shortcut.** [3]

The Nash flow with the shortcut costs each driver \(80\) minutes, while the social
optimum (routing 20 drivers each way) costs \(70\). The Price of Anarchy is

\[
\frac{80}{70} = \frac{8}{7}.
\]

## Question 2 [25 marks]

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
\Phi(x) = \int_0^{1 - x} 1\,\mathrm{d}t + \int_0^{x} t\,\mathrm{d}t = (1 - x) + \frac{x^2}{2}.
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

The average cost is \(C\!\left(\tfrac{1}{4}\right) = 2\cdot\tfrac{1}{16} - \tfrac{1}{4} + 1 = \tfrac{7}{8}\).

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

**(a) Price of anarchy.** [4]

The price of anarchy is the ratio of the total travel cost at the worst Nash flow
to the total travel cost at the optimal flow:

\[
\text{PoA} = \frac{C(\text{Nash flow})}{C(\text{optimal flow})}.
\]

It measures how much worse selfish routing can be than a centrally optimal
routing.

**(b) The Nash flow.** [6]

At a Nash flow no user can lower their cost by switching link. If a fraction
\(x < 1\) used link 1, that link would cost \(x^p < 1\), below link 2's cost of
\(1\), so every user on link 2 would switch: this is not an equilibrium. With all
traffic on link 1 the cost there is \(1^p = 1\), equal to link 2's cost, so no
user can do better. Hence the Nash flow puts all traffic on link 1, with total
cost \(1 \cdot 1^p = 1\).

**(c) The optimal flow.** [9]

Routing a fraction \(x\) on link 1 gives total cost

\[
C(x) = x \cdot x^p + (1 - x) \cdot 1 = x^{p+1} + 1 - x.
\]

Minimising, \(C'(x) = (p + 1)x^p - 1 = 0\), so \(x^{*} = (p + 1)^{-1/p}\). Since
\(x^{*\,p+1} = x^{*}\cdot x^{*\,p} = x^{*}/(p + 1)\),

\[
C(x^{*}) = \frac{x^{*}}{p + 1} + 1 - x^{*} = 1 - x^{*}\left(1 - \frac{1}{p + 1}\right)
= 1 - x^{*}\,\frac{p}{p + 1}.
\]

The Nash cost is \(1\), so

\[
\text{PoA} = \frac{1}{C(x^{*})} = \frac{1}{1 - x^{*}\,\frac{p}{p + 1}},
\qquad x^{*} = (p + 1)^{-1/p}.
\]

**(d) The two regimes.** [6]

At \(p = 1\) we have \(x^{*} = \tfrac{1}{2}\) and
\(C(x^{*}) = 1 - \tfrac{1}{2}\cdot\tfrac{1}{2} = \tfrac{3}{4}\), so
\(\text{PoA} = \tfrac{4}{3}\), the familiar affine bound. As \(p \to \infty\),
\(\ln x^{*} = -\tfrac{1}{p}\ln(p + 1) \to 0\), so \(x^{*} \to 1\), and
\(\tfrac{p}{p+1} \to 1\); hence \(C(x^{*}) \to 1 - 1 = 0\) and
\(\text{PoA} \to \infty\).

With affine costs selfish routing is never worse than \(\tfrac{4}{3}\) times the
optimum. With steeply nonlinear costs the picture is very different: a congestion
cost that climbs sharply once a link fills up means selfish users pile onto link 1
until it just matches link 2, whereas the optimum holds almost all of them back.
The waste is then unbounded, and no constant bound on the price of anarchy can
hold across all cost functions.
