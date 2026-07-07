---
layout: solution
title: "Repeated games"
tag: repeated-games
---

# Repeated games: worked solutions

Solutions to the example questions on the
[Repeated games](/topics/repeated-games.html) page. Each question is worth 25
marks.

## Question 1 [25 marks]

**(a) Interpretation.** [3]

\(\delta = 5/6\) is the probability that the game continues after each round (the
die not showing a 1). The expected number of rounds is
\(\dfrac{1}{1 - \delta} = \dfrac{1}{1/6} = 6\).

**(b) Discounted payoffs.** [6]

Hold the opponent's Grudger fixed and compare the focal player's two options. If
the player conforms, the opponent is never triggered, so both play High in every
round and the player earns 3 each round. If the player deviates to Low in the
first round, they earn 5 that round against the opponent's High, but this trips
the opponent's punishment, so both play Low for ever after, earning 1 each round.
Hence

\[
U_{\text{conform}} = \frac{3}{1 - \delta},
\qquad
U_{\text{deviate}} = 5 + \frac{\delta}{1 - \delta}.
\]

**(c) Cooperation at \(\delta = 5/6\).** [4]

\[
U_{\text{conform}} = \frac{3}{1/6} = 18,
\qquad
U_{\text{deviate}} = 5 + \frac{5/6}{1/6} = 5 + 5 = 10.
\]

Since \(18 > 10\), no player gains by deviating, so mutual cooperation is
sustained.

**(d) Threshold.** [5]

\[
\frac{3}{1 - \delta} \ge 5 + \frac{\delta}{1 - \delta}
\;\Longrightarrow\; 3 \ge 5 - 4\delta
\;\Longrightarrow\; \delta \ge \tfrac{1}{2}.
\]

Our die gives \(\delta = 5/6\), well above \(\tfrac{1}{2}\), so it made
cooperation easy to sustain: the future cast a long enough shadow.

**(e) A forgiving trigger.** [7]

Now a one-off Low is punished by only two rounds of mutual Low before both
return to High. A player who conforms still earns \(3\) every round, so
\(U_{\text{conform}} = \dfrac{3}{1 - \delta}\). A player who deviates to Low in
the first round earns \(5\) at once, then \(1\) in each of the two punishment
rounds, and \(3\) for ever after:

\[
U_{\text{deviate}} = 5 + \delta + \delta^{2} + \frac{3\delta^{3}}{1 - \delta}.
\]

Writing \(U_{\text{conform}} = 3 + 3\delta + 3\delta^{2} +
\dfrac{3\delta^{3}}{1 - \delta}\), the tails cancel and

\[
U_{\text{conform}} - U_{\text{deviate}}
= (3 - 5) + (3 - 1)\delta + (3 - 1)\delta^{2}
= 2\left(\delta^{2} + \delta - 1\right).
\]

Cooperation is sustained when this is non-negative, that is when
\(\delta^{2} + \delta - 1 \ge 0\), i.e. \(\delta \ge \dfrac{\sqrt{5} - 1}{2}
\approx 0.618\). At \(\delta = 5/6\),

\[
\delta^{2} + \delta - 1 = \frac{25}{36} + \frac{30}{36} - \frac{36}{36}
= \frac{19}{36} > 0,
\]

so our die still sustains cooperation. The threshold has risen from
\(\tfrac{1}{2}\) under Grudger to \(\tfrac{\sqrt{5} - 1}{2} \approx 0.618\):
shortening the punishment from a permanent grudge to two rounds weakens the
deterrent, so the players must be more patient to keep cooperating.

## Question 2 [25 marks]

**(a) Definitions.** (Bookwork.) [4]

- Given a two-player stage game \((A, B)\), an **infinitely repeated game with
  discounting** factor \(\delta\) plays that stage game infinitely often, giving
  utility \(U(s*r, s_c) = \sum*{i = 0}^{\infty} \delta^{i} u(s_r(i), s_c(i))\).
- A **strategy in a repeated game** is a mapping from every possible history of
  play to a probability distribution over the action set of the stage game.
- The **Grudger strategy** cooperates until the opponent defects, then defects
  for ever.
- The **average utility** is \(\bar{U}\_i(r, c) = (1 - \delta) U_i(r, c)\), the
  average payoff per stage when \(\delta\) is read as the probability of the
  game not ending.

**(b)(i) Discounted payoffs.** [3]

Hold the opponent's Grudger fixed. Conforming keeps both on mutual cooperation at
3 a round; defecting once earns 5 and then trips the opponent's punishment, after
which both defect at 1 a round. Hence

\[
U_{\text{conform}} = \frac{3}{1 - \delta},
\qquad
U_{\text{defect}} = 5 + \frac{\delta}{1 - \delta}.
\]

**(b)(ii) Smallest \(\delta\).** [3]

\[
\frac{3}{1 - \delta} \ge 5 + \frac{\delta}{1 - \delta}
\;\Longrightarrow\;
3 \ge 5 - 4\delta
\;\Longrightarrow\;
\delta \ge \tfrac{1}{2}.
\]

**(b)(iii) Subgame perfection.** [5]

Grudger is subgame perfect when no player can gain by deviating in _any_
subgame. There are two kinds of subgame. On the cooperative path, the condition
is exactly the no-deviation inequality of part (ii), so it holds for
\(\delta \ge \tfrac{1}{2}\). In the punishment phase, both players defect for
ever, which is the stage Nash equilibrium repeated; a one-off deviation to
cooperate earns \(0\) now and returns to mutual defection, so it cannot help.
Hence for \(\delta \ge \tfrac{1}{2}\) Grudger is a subgame perfect
equilibrium.

**(c) Folk Theorem.** (Bookwork.) [3]

Let \((u_1^{*}, u_2^{*})\) be a pair of Nash equilibrium payoffs of the stage
game. For every individually rational pair \((v_1, v_2)\) there exists
\(\bar{\delta}\) such that for all \(1 > \delta > \bar{\delta} > 0\) there is a
subgame perfect Nash equilibrium with payoffs \((v_1, v_2)\).

**(d) Individually rational payoff.** [3]

The **individually rational payoffs** are the average payoff pairs that exceed
the stage-game Nash equilibrium payoffs of both players. The stage game's unique
Nash equilibrium is mutual defection, paying \(1\) to each player, so a pair is
individually rational when each player's average payoff exceeds this stage Nash
value of \(1\).

**(e) Interpretation.** [4]

Mutual cooperation gives each player \(3 > 1\), so the pair \((3, 3)\) exceeds the
stage Nash payoff of \(1\) and is individually rational. By the Folk Theorem it
can therefore be sustained in a subgame perfect equilibrium when players are
patient enough, which matches the threshold \(\delta \ge \tfrac{1}{2}\) found
above.

## Question 3 [25 marks]

**(a) Definition.** (Bookwork.) [2]

A strategy profile is a **subgame perfect equilibrium** of a repeated game if,
after every history of play, the strategies restricted to the subgame that
follows form a Nash equilibrium of that subgame. Equivalently, no player can gain
by deviating in any subgame, not only on the equilibrium path.

**(b)(i) Backward induction.** [4]

We argue by backward induction. In the last round \(N\) the players face a single
play of the stage game, whose unique Nash equilibrium is mutual defection, so any
subgame perfect equilibrium defects in round \(N\). Working back, suppose every
round after \(k\) defects no matter what is played in round \(k\). Then the
continuation payoff is fixed, so a player at round \(k\) maximises only the
current stage payoff, where defection strictly dominates; hence both defect in
round \(k\) as well. By induction the unique subgame perfect equilibrium defects
in every round.

**(b)(ii) Why cooperation cannot be sustained.** [4]

By part (b)(i) the unique subgame perfect equilibrium plays mutual defection in
every round after every history, so its path contains no cooperation. A
cooperative agreement cannot be propped up by the threat of future punishment
because no such threat is credible: any punishment would have to be carried out
in a later subgame, yet every later subgame has mutual defection as its only
subgame perfect behaviour, fixed by the last-round argument. A player's
continuation payoff is therefore the same whether or not they cooperated, so it
can neither reward cooperation nor penalise defection. With the future fixed,
defection strictly dominates in the current stage, and cooperation unravels from
the final round back to the first.

**(c) Why backward induction does not apply to the infinite game.** [3]

Backward induction relies on a final subgame to anchor the recursion: it pins
down play in the last round, then in the round before, and so on. A finitely
repeated game has such a final round \(N\), which is why the argument of part (b)
succeeds. An infinitely repeated game has no final round, so the recursion has no
base case and cannot begin; there is no last stage from which to reason
backwards. This removes the unravelling argument, but does not by itself show
that cooperation can be sustained. It only leaves room for strategies such as
Grudger, whose threat of indefinite future punishment can deter a deviation when
players are patient enough.

**(d) Recomputed threshold with \(T = 4\).** [4]

Cooperation is sustained when conforming is at least as good as a one-shot
deviation against Grudger, that is \(U_{\text{conform}} \ge U_{\text{deviate}}\).
With temptation \(T = 4\),

\[
\frac{3}{1 - \delta} \ge 4 + \frac{\delta}{1 - \delta}
\;\Longrightarrow\;
3 \ge 4 - 3\delta
\;\Longrightarrow\;
\delta \ge \tfrac{1}{3}.
\]

**(e) Comment.** [3]

Lowering the temptation from \(5\) to \(4\) lowers the threshold from
\(\tfrac{1}{2}\) to \(\tfrac{1}{3}\). A smaller temptation makes a one-shot
defection less attractive relative to staying on the cooperative path, so
cooperation survives for a wider range of discount factors. The dependence is
monotone: the threshold rises with the temptation payoff \(T\), as part (f) makes
precise.

**(f) General threshold.** [5]

With \(R = 3\), \(P = 1\), \(S = 0\) and general temptation \(T\), the
no-deviation condition against Grudger is

\[
\frac{3}{1 - \delta} \ge T + \frac{\delta}{1 - \delta}.
\]

Multiplying through by \(1 - \delta > 0\) preserves the inequality and gives
\(3 \ge T(1 - \delta) + \delta = T - \delta(T - 1)\), hence
\(\delta(T - 1) \ge T - 3\). Since \(T > 1\) we have \(T - 1 > 0\), so dividing by
\(T - 1\) keeps the direction:

\[
\delta \ge \frac{T - 3}{T - 1} = \delta^{*}.
\]

Writing \(\delta^{*} = 1 - \dfrac{2}{T - 1}\) makes the behaviour transparent: as
\(T\) grows, \(\dfrac{2}{T - 1}\) shrinks, so \(\delta^{*}\) increases towards
\(1\). The greater the temptation, the more patient the players must be to
sustain cooperation. For \(T \le 3\) we have \(\delta^{*} \le 0\) and cooperation
is sustained for every \(\delta \in (0, 1)\).

## Question 4 [25 marks]

**(a) Conform and deviate payoffs.** [4]

Conforming yields mutual cooperation for ever:

\[
V_{\text{C}} = \frac{R}{1 - \delta} = \frac{3}{1 - \delta}.
\]

Defecting once earns the temptation payoff now, then \(T\) rounds of mutual
defection, then a return to cooperation:

\[
V_{\text{D}} = T + P\sum_{k=1}^{T}\delta^k + R\,\frac{\delta^{\,T+1}}{1 - \delta}
= 5 + \frac{\delta\bigl(1 - \delta^{T}\bigr)}{1 - \delta} + \frac{3\,\delta^{\,T+1}}{1 - \delta}.
\]

**(b) The sustaining condition.** [8]

Cooperation is sustained when \(V_{\text{C}} \ge V_{\text{D}}\). Multiplying
through by \(1 - \delta\),

\[
3 \ge 5(1 - \delta) + \delta\bigl(1 - \delta^{T}\bigr) + 3\,\delta^{\,T+1}.
\]

Expanding the right-hand side,

\[
3 \ge 5 - 5\delta + \delta - \delta^{\,T+1} + 3\,\delta^{\,T+1}
= 5 - 4\delta + 2\,\delta^{\,T+1}.
\]

Rearranging gives \(4\delta \ge 2 + 2\,\delta^{\,T+1}\), that is

\[
2\delta - \delta^{\,T+1} \ge 1.
\]

**(c) Dependence on the punishment length.** [6]

Let \(\varphi_T(\delta) = 2\delta - \delta^{\,T+1}\); the threshold
\(\delta^{*}(T)\) solves \(\varphi_T(\delta) = 1\). For fixed \(\delta \in (0, 1)\)
the term \(\delta^{\,T+1}\) decreases as \(T\) increases, so \(\varphi_T(\delta)\)
increases with \(T\). A larger \(T\) therefore satisfies the inequality at a
smaller \(\delta\), so \(\delta^{*}(T)\) is decreasing in \(T\). As
\(T \to \infty\), \(\delta^{\,T+1} \to 0\) and the condition becomes
\(2\delta \ge 1\), giving \(\delta^{*} \to \tfrac{1}{2}\). This is exactly the
grim-trigger threshold, in which the punishment lasts for ever.

**(d) Subgame perfection.** [7]

By the one-shot deviation principle it suffices to rule out a profitable single
deviation in each type of subgame, assuming conformity thereafter.

On the cooperative path, a one-shot defection gives the payoff \(V_{\text{D}}\) of
part (a) against the continuation \(V_{\text{C}}\); the calculation of part (b)
shows \(V_{\text{C}} \ge V_{\text{D}}\) exactly when \(2\delta - \delta^{\,T+1}
\ge 1\), so no such deviation pays above the threshold.

During the punishment phase both players are due to defect. A one-shot deviation
to cooperate earns \(S = 0\) this round instead of \(P = 1\), and leaves the
remaining count and all future play unchanged, since the strategy ignores
behaviour within the punishment phase. The deviation loses \(1 - 0 = 1\) now and
gains nothing later, so it is never profitable.

No profitable one-shot deviation exists in any subgame, so the forgiving trigger
is subgame perfect for \(\delta \ge \delta^{*}(T)\).
