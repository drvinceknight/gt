---
layout: solution
title: "Subgame Perfection"
tag: subgame-perfection
---

# Subgame Perfection: worked solutions

Solutions to the example questions on the
[Subgame Perfection](/topics/subgame-perfection.html) page. Each question is worth
25 marks.

## Question 1 [25 marks]

**(a) Extensive form.** [3]

```
            Traitor
           /        \
       comply       deviate
        (1, 2)        |
                  Faithful
                  /        \
              banish      carry on
             (-1, -1)      (3, 0)
```

**(b) Subgame perfect equilibrium.** [5]

By backward induction, at the Faithful's node banish gives \(-1\) and carry on
gives \(0\), so the Faithful carry on: on an even chance, banishing the suspect is
as likely to remove a Faithful as the Traitor, and is not worth the risk. The
Traitor then compares deviate \(\to (3, 0)\), worth \(3\), with comply \(\to 1\),
and deviates. The subgame perfect equilibrium is (deviate, carry on) with payoffs
\((3, 0)\).

**(c) A Nash equilibrium.** [7]

Consider (comply, banish). Given that the Faithful will banish, the Traitor's
payoff is deviate \(\to -1\) versus comply \(\to 1\), so comply is a best response.
Given that the Traitor complies, the Faithful node is off the path of play, so any
action, including banish, is a best response. Hence (comply, banish) is a Nash
equilibrium with payoffs \((1, 2)\).

**(d) Not subgame perfect.** [6]

It is not subgame perfect because in the subgame after deviate, banish gives the
Faithful \(-1\) while carry on gives \(0\): banish is not optimal there, so it is a
non-credible threat. The Traitor complies only because of that threat. This is the
third game in the activity: once players break Vote-Left for fun, the Faithful
cannot be sure a flagged suspect is the colluding Traitor, so a threat to banish on
suspicion does not survive contact with the decision, since acting on a hunch is as
likely to remove a friend as the Traitor.

**(e) How the uncertainty changes things.** [4]

Write \(q\) for the Faithful's belief that the suspect is the Traitor. Banishing
yields \((-5, 3)\)
if the suspect is the Traitor and \((3, -5)\) if it is a Faithful, so its expected
payoffs are \((3 - 8q,\ 8q - 5)\). Two thresholds follow.

- The threat deters the Traitor, that is comply is a best response to banish, iff
  \(1 \ge 3 - 8q\), i.e. \(q \ge \tfrac{1}{4}\).
- The threat is credible, that is banish is the Faithful's best response in the
  subgame, iff \(8q - 5 \ge 0\), i.e. \(q \ge \tfrac{5}{8}\).

Hence for \(q < \tfrac{1}{4}\) the Traitor deviates even under the threat, and the
only equilibrium is (deviate, carry on). For \(\tfrac{1}{4} \le q < \tfrac{5}{8}\)
the threat deters but is not credible, so (comply, banish) is a Nash equilibrium
that is not subgame perfect, while the subgame perfect prediction remains (deviate,
carry on). For \(q \ge \tfrac{5}{8}\) banishing is credible and (comply, banish) is
subgame perfect. The threat sustains compliance as a non-subgame-perfect Nash
equilibrium exactly on \(\tfrac{1}{4} \le q < \tfrac{5}{8}\), and Vote-Left's value
is that it drives \(q\) towards one, where the threat finally bites.

## Question 2 [25 marks]

**(a) Definitions.** (Bookwork.) [5]

- An \(N\)-player **extensive form game** with complete information consists of a
  finite set of players \(\mathcal{N}\) with \(|\mathcal{N}| = N\); a tree
  \(G = (V, E, x^0)\) with vertex set \(V\), edge set \(E\), and root
  \(x^0 \in V\); a partition \((V_i)_{i \in \mathcal{N}}\) of the non-terminal
  vertices that assigns each decision node to a player; a set \(O\) of outcomes;
  and a function \(u\) mapping each terminal node (leaf) of \(G\) to an element of
  \(O\).
- A node \(x\) **initiates a subgame** if and only if \(x\) and all successors of
  \(x\) lie in information sets containing only successors of \(x\).
- **Backward induction** is the process of analysing a game from back to front:
  at each information set we remove the strategies that are dominated.
- A **subgame perfect equilibrium** is a Nash equilibrium in which the strategy
  profile specifies a Nash equilibrium for every subgame of the game, including
  subgames that might not be reached during play.

**(b)(i) Extensive form.** [2]

```
            entrant
           /        \
      stay out      enter
       (0, 2)         |
                  incumbent
                  /        \
               fight    accommodate
              (-1,-1)      (1, 1)
```

**(b)(ii) Subgame perfect equilibrium.** [3]

The incumbent accommodates (\(1 > -1\)). Anticipating this, the entrant enters
(\(1 > 0\)). The subgame perfect equilibrium is (enter, accommodate) with
payoffs \((1, 1)\).

**(b)(iii) A Nash equilibrium that is not subgame perfect.** [5]

(stay out, fight) is a Nash equilibrium: given the threat to fight, the entrant
prefers staying out (\(0 > -1\)); given the entrant stays out, the incumbent's
node is unreached so fight is a best response. It is not subgame perfect because
fight is not optimal in the subgame after entry (\(-1 < 1\)); it is a
non-credible threat.

**(b)(iv) Normal form.** [3]

With the entrant as the row player and the incumbent as the column player:

| | fight | accommodate |
|---|---|---|
| stay out | \((0, 2)\) | \((0, 2)\) |
| enter | \((-1, -1)\) | \((1, 1)\) |

Checking best responses, the pure Nash equilibria are (stay out, fight) and
(enter, accommodate), confirming part (iii): the former is the non-subgame-perfect
one.

**(c) Nash versus subgame perfect.** [3]

A Nash equilibrium only requires each strategy to be optimal given the others
along the path of play, so it can rely on non-credible threats off the path. A
subgame perfect equilibrium additionally requires optimality in every subgame,
ruling such threats out.

**(d) Existence theorem.** (Bookwork.) [4]

Every finite game with perfect information has a Nash equilibrium in pure
strategies, and backward induction identifies one. In games with perfect
information the equilibrium obtained through backward induction is moreover
subgame perfect.

## Question 3 [25 marks]

**(a) Sequential rationality.** (Bookwork.) [2]

**Sequential rationality** requires that an optimal strategy for a player
maximises that player's expected payoff, conditional on every information set at
which that player has a decision, whether or not it is reached in equilibrium.

**(b)(i) Backward induction.** [3]

After \(L\), player 2 chooses \(\ell\) (\(1 > 0\)); after \(R\), player 2
chooses \(r\) (\(3 > 2\)). Player 1 then compares \(L \to (3, 1)\) with
\(R \to (1, 3)\) and chooses \(L\). The subgame perfect equilibrium is \(L\),
with player 2 playing \(\ell\) after \(L\) and \(r\) after \(R\); payoffs
\((3, 1)\).

**(b)(ii) Normal form.** [4]

Player 2 strategies are (action after \(L\), action after \(R\)):

| | \((\ell, \ell)\) | \((\ell, r)\) | \((r, \ell)\) | \((r, r)\) |
|---|---|---|---|---|
| \(L\) | \((3, 1)\) | \((3, 1)\) | \((0, 0)\) | \((0, 0)\) |
| \(R\) | \((2, 2)\) | \((1, 3)\) | \((2, 2)\) | \((1, 3)\) |

**(b)(iii) Pure Nash equilibria.** [4]

Checking best responses gives \((L, (\ell, \ell))\), \((L, (\ell, r))\) and
\((R, (r, r))\).

**(b)(iv) Subgame perfection.** [4]

Only \((L, (\ell, r))\) is subgame perfect: it is the only equilibrium in which
player 2 acts optimally in both subgames, playing \(\ell\) after \(L\) and \(r\)
after \(R\). Each of the other two specifies a suboptimal action in an unreached
subgame, but they fail subgame perfection for different reasons.

In \((R, (r, r))\), player 2 plays \(r\) after \(L\), worth \(0\) rather than the
optimal \(\ell\) worth \(1\). This is a non-credible threat that does real work:
it leaves player 1 with \(0\) from \(L\) against \(1\) from \(R\), so it deters
player 1 from \(L\) and sustains the choice of \(R\). Were player 2 to play the
credible \(\ell\), player 1 would get \(3\) from \(L\) and switch.

In \((L, (\ell, \ell))\), player 2 plays \(\ell\) after \(R\), worth \(2\) rather
than the optimal \(r\) worth \(3\). Here the suboptimal action sustains nothing:
player 1 prefers \(L\) regardless of what is specified after \(R\), exactly as in
the subgame perfect equilibrium. The profile survives only because the \(R\)
subgame is off the path, so player 2 is indifferent to what is specified there.

**(c)(i) Centipede by backward induction.** [5]

- At the final decision, player 1 compares take \((4, 2)\) with pass \((3, 5)\)
  and takes (\(4 > 3\)).
- At the middle decision, player 2 compares take \((1, 3)\) with passing into
  \((4, 2)\), worth \(2\), and takes (\(3 > 2\)).
- At the first decision, player 1 compares take \((2, 0)\) with passing into
  \((1, 3)\), worth \(1\), and takes (\(2 > 1\)).

**(c)(ii) Subgame perfect outcome.** [3]

Player 1 takes at the first decision, so the subgame perfect outcome is to stop
immediately with payoffs \((2, 0)\). The prediction is striking because both
players would do better at the final leaf \((3, 5)\): backward induction unravels
all cooperation from the end, even though passing throughout would leave both
better off. This tension between the subgame perfect prediction and mutual
benefit is exactly what makes the centipede game famous.

## Question 4 [25 marks]

**(a) Subgame perfection with continuous actions.** [3]

A subgame perfect equilibrium is a strategy for each firm that induces a Nash
equilibrium in every subgame. Here the relevant subgames are the leader's choice
at the root and the follower's choice after each possible \(q_1\). Subgame
perfection requires the follower to choose optimally after every \(q_1\), not only
on the equilibrium path, and the leader to choose optimally anticipating that
response.

**(b) The follower's best response.** [6]

After observing \(q_1\), the follower solves

\[
\max_{q_2}\ q_2\bigl(a - q_1 - q_2\bigr).
\]

The first-order condition is \(a - q_1 - 2 q_2 = 0\), giving

\[
q_2(q_1) = \frac{a - q_1}{2}.
\]

**(c) The leader's choice.** [8]

The leader anticipates \(q_2(q_1)\) and solves

\[
\max_{q_1}\ q_1\bigl(a - q_1 - q_2(q_1)\bigr)
= q_1\left(a - q_1 - \frac{a - q_1}{2}\right)
= \frac{q_1(a - q_1)}{2}.
\]

The first-order condition \(a - 2 q_1 = 0\) gives \(q_1 = \dfrac{a}{2}\), and hence

\[
q_2 = \frac{a - a/2}{2} = \frac{a}{4},
\qquad Q = \frac{3a}{4},
\qquad P = a - \frac{3a}{4} = \frac{a}{4}.
\]

The profits are

\[
\pi_1 = q_1 P = \frac{a}{2}\cdot\frac{a}{4} = \frac{a^2}{8},
\qquad
\pi_2 = q_2 P = \frac{a}{4}\cdot\frac{a}{4} = \frac{a^2}{16}.
\]

**(d) First-mover advantage.** [8]

At the Cournot equilibrium each firm produces \(a/3\) and earns
\(\dfrac{a}{3}\bigl(a - \tfrac{2a}{3}\bigr) = \dfrac{a^2}{9}\). The leader does
strictly better as first mover, \(\dfrac{a^2}{8} > \dfrac{a^2}{9}\), while the
follower does worse, \(\dfrac{a^2}{16} < \dfrac{a^2}{9}\).

The advantage comes from commitment. By moving first the leader fixes \(q_1 = a/2\)
irreversibly, and the follower's best response is to cut back to \(q_2 = a/4\).
The leader cannot gain this way in the simultaneous game, where a plan to produce
\(a/2\) is not credible: given the rival also at \(a/2\), each would want to
deviate. Observability is precisely what gives the commitment its bite; the
follower, seeing the large quantity, rationally accommodates it, and the leader
captures the larger share.
