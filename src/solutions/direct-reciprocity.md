---
layout: solution
title: "Direct Reciprocity"
tag: direct-reciprocity
---

# Direct Reciprocity: worked solutions

Solutions to the example questions on the
[Direct Reciprocity](/topics/direct-reciprocity.html) page. Each question is worth
25 marks.

## Question 1 [25 marks]

**(a) Named strategies.** [3]

\((1, 1)\) is Always Cooperate (AllC), \((0, 0)\) is Always Defect (AllD),
\((1, 0)\) is Tit For Tat (TFT) and \(\left(\tfrac{1}{2}, \tfrac{1}{2}\right)\)
is Random.

**(b) Transition matrix.** [7]

The state records the previous round's actions as (player 1, player 2). Each
player reacts to the opponent's last action, and it is convenient to write the
reactive probabilities as fractions: \(p = \tfrac{4}{5}\), \(q = \tfrac{1}{5}\)
for player 1 and \(p' = \tfrac{3}{5}\), \(q' = \tfrac{1}{10}\) for player 2. The
two players choose independently, so each transition probability is a product of
one factor from each. Working through the four starting states,

\[
\begin{aligned}
CC &\to \bigl(pp',\, p(1-p'),\, (1-p)p',\, (1-p)(1-p')\bigr)
   = \left(\tfrac{12}{25}, \tfrac{8}{25}, \tfrac{3}{25}, \tfrac{2}{25}\right), \\
CD &\to \bigl(qp',\, q(1-p'),\, (1-q)p',\, (1-q)(1-p')\bigr)
   = \left(\tfrac{3}{25}, \tfrac{2}{25}, \tfrac{12}{25}, \tfrac{8}{25}\right), \\
DC &\to \bigl(pq',\, p(1-q'),\, (1-p)q',\, (1-p)(1-q')\bigr)
   = \left(\tfrac{2}{25}, \tfrac{18}{25}, \tfrac{1}{50}, \tfrac{9}{50}\right), \\
DD &\to \bigl(qq',\, q(1-q'),\, (1-q)q',\, (1-q)(1-q')\bigr)
   = \left(\tfrac{1}{50}, \tfrac{9}{50}, \tfrac{2}{25}, \tfrac{18}{25}\right).
\end{aligned}
\]

In state \(CD\), for instance, player 2 defected last round so player 1 uses
\(q = \tfrac{1}{5}\), while player 1 cooperated so player 2 uses
\(p' = \tfrac{3}{5}\); the row is
\(\left(\tfrac{3}{25}, \tfrac{2}{25}, \tfrac{12}{25}, \tfrac{8}{25}\right)\).
Collecting the rows, with both indices ordered \((CC, CD, DC, DD)\),

\[
M =
\begin{pmatrix}
\frac{12}{25} & \frac{8}{25} & \frac{3}{25} & \frac{2}{25} \\[6pt]
\frac{3}{25} & \frac{2}{25} & \frac{12}{25} & \frac{8}{25} \\[6pt]
\frac{2}{25} & \frac{18}{25} & \frac{1}{50} & \frac{9}{50} \\[6pt]
\frac{1}{50} & \frac{9}{50} & \frac{2}{25} & \frac{18}{25}
\end{pmatrix}.
\]

**(c) Confirming the stationary distribution.** [7]

The stationary distribution \(\pi\) gives the long-run fraction of rounds the
play spends in each of the states \((CC, CD, DC, DD)\); it is the probability
vector satisfying \(\pi M = \pi\). The proposed
\(\pi = \tfrac{1}{245}\left(26, 65, 44, 110\right)\) has non-negative entries
summing to \(26 + 65 + 44 + 110 = 245\) over \(245\), that is to 1.

To check \(\pi M = \pi\), multiply \(\pi\) by each column of \(M\) in turn. The
four columns are
\(\left(\tfrac{12}{25}, \tfrac{3}{25}, \tfrac{2}{25}, \tfrac{1}{50}\right)\),
\(\left(\tfrac{8}{25}, \tfrac{2}{25}, \tfrac{18}{25}, \tfrac{9}{50}\right)\),
\(\left(\tfrac{3}{25}, \tfrac{12}{25}, \tfrac{1}{50}, \tfrac{2}{25}\right)\) and
\(\left(\tfrac{2}{25}, \tfrac{8}{25}, \tfrac{9}{50}, \tfrac{18}{25}\right)\), so

\[
\begin{aligned}
(\pi M)_{CC} &= \tfrac{1}{245}\bigl(26 \cdot \tfrac{12}{25}
  + 65 \cdot \tfrac{3}{25} + 44 \cdot \tfrac{2}{25}
  + 110 \cdot \tfrac{1}{50}\bigr) = \tfrac{1}{245} \cdot 26 = \tfrac{26}{245}, \\
(\pi M)_{CD} &= \tfrac{1}{245}\bigl(26 \cdot \tfrac{8}{25}
  + 65 \cdot \tfrac{2}{25} + 44 \cdot \tfrac{18}{25}
  + 110 \cdot \tfrac{9}{50}\bigr) = \tfrac{1}{245} \cdot 65 = \tfrac{65}{245}, \\
(\pi M)_{DC} &= \tfrac{1}{245}\bigl(26 \cdot \tfrac{3}{25}
  + 65 \cdot \tfrac{12}{25} + 44 \cdot \tfrac{1}{50}
  + 110 \cdot \tfrac{2}{25}\bigr) = \tfrac{1}{245} \cdot 44 = \tfrac{44}{245}, \\
(\pi M)_{DD} &= \tfrac{1}{245}\bigl(26 \cdot \tfrac{2}{25}
  + 65 \cdot \tfrac{8}{25} + 44 \cdot \tfrac{9}{50}
  + 110 \cdot \tfrac{18}{25}\bigr) = \tfrac{1}{245} \cdot 110 = \tfrac{110}{245}.
\end{aligned}
\]

Each bracket collapses to an integer, returning \(\pi\) exactly, so \(\pi M =
\pi\) and \(\pi\) is stationary. Each player's long-run average payoff is the
expectation of their stage payoff under \(\pi\). Player 1 earns
\((R, S, T, P) = (3, 0, 5, 1)\) across \((CC, CD, DC, DD)\) and player 2 earns
\((3, 5, 0, 1)\), so

\[
\bar{u}_1 = \frac{3(26) + 0(65) + 5(44) + 1(110)}{245}
= \frac{78 + 220 + 110}{245} = \frac{408}{245} \approx 1.665,
\]

\[
\bar{u}_2 = \frac{3(26) + 5(65) + 0(44) + 1(110)}{245}
= \frac{78 + 325 + 110}{245} = \frac{513}{245} \approx 2.094.
\]

**(d) Care with Tit For Tat.** [8]

Tit For Tat is \((p, q) = (1, 0)\), with both entries on the boundary
\(\{0, 1\}\). The resulting Markov chain may be periodic or reducible rather than
ergodic, so a unique stationary distribution need not exist. The long-run
behaviour must then be read directly from the transition structure and the
starting state rather than from a stationary distribution.

## Question 2 [25 marks]

**(a) Reactive strategies.** (Bookwork.) [5]

A **reactive strategy** \((p, q)\) cooperates with probability \(p\) after the
opponent cooperated and \(q\) after the opponent defected. The named strategies
are \(\text{AllC} = (1, 1)\), \(\text{AllD} = (0, 0)\),
\(\text{TFT} = (1, 0)\), \(\text{Random} = (\tfrac{1}{2}, \tfrac{1}{2})\).

**(b)(i) Intermediate quantities.** [4]

Writing the strategies as fractions,
\((p, q) = \left(\tfrac{4}{5}, \tfrac{2}{5}\right)\) and
\((p', q') = \left(\tfrac{3}{5}, \tfrac{1}{10}\right)\), so

\[
r_1 = p - q = \tfrac{2}{5}, \quad r_2 = p' - q' = \tfrac{1}{2}, \quad
1 - r_1 r_2 = \tfrac{4}{5}.
\]

\[
s_1 = \frac{\tfrac{1}{10}\cdot\tfrac{2}{5} + \tfrac{2}{5}}{\tfrac{4}{5}}
= \frac{11/25}{4/5} = \frac{11}{20},
\qquad
s_2 = \frac{\tfrac{2}{5}\cdot\tfrac{1}{2} + \tfrac{1}{10}}{\tfrac{4}{5}}
= \frac{3/10}{4/5} = \frac{3}{8}.
\]

**(b)(ii) Stationary distribution.** [4]

Substitute \(s_1 = \tfrac{11}{20}\) and \(s_2 = \tfrac{3}{8}\), with
\(1 - s_1 = \tfrac{9}{20}\) and \(1 - s_2 = \tfrac{5}{8}\), into
\(\pi = \bigl(s_1 s_2, s_1(1 - s_2), (1 - s_1)s_2, (1 - s_1)(1 - s_2)\bigr)\):

\[
\pi = \left(\tfrac{11}{20}\cdot\tfrac{3}{8},\ \tfrac{11}{20}\cdot\tfrac{5}{8},\
\tfrac{9}{20}\cdot\tfrac{3}{8},\ \tfrac{9}{20}\cdot\tfrac{5}{8}\right)
= \left(\tfrac{33}{160}, \tfrac{55}{160}, \tfrac{27}{160}, \tfrac{45}{160}\right).
\]

**(b)(iii) Long-run average payoffs.** [5]

Each player's long-run average payoff weights their stage payoff by \(\pi\).
Player 1 earns \((R, S, T, P) = (3, 0, 5, 1)\) across \((CC, CD, DC, DD)\) and
player 2 earns \((3, 5, 0, 1)\), so

\[
\bar{u}_1 = \frac{3(33) + 0(55) + 5(27) + 1(45)}{160}
= \frac{279}{160} \approx 1.744,
\]

\[
\bar{u}_2 = \frac{3(33) + 5(55) + 0(27) + 1(45)}{160}
= \frac{419}{160} \approx 2.619.
\]

**(b)(iv) Who does better.** [2]

Player 2 does better,
\(\bar{u}_2 = \tfrac{419}{160} \approx 2.619 > \bar{u}_1 = \tfrac{279}{160}
\approx 1.744\). Player 2's strategy \(\left(\tfrac{3}{5}, \tfrac{1}{10}\right)\)
cooperates less and forgives less than player 1's
\(\left(\tfrac{4}{5}, \tfrac{2}{5}\right)\), so it exploits player 1's greater
willingness to cooperate,
spending more time in the \(CD\) state (player 1 cooperating while player 2
defects).

**(c) Why pure strategies need care.** [3]

The closed form requires \(0 < p, q, p', q' < 1\) so that the chain is ergodic
with a unique stationary distribution. Tit For Tat has \(p = 1, q = 0\) on the
boundary, so the chain may be periodic or reducible; the stationary behaviour
must then be found directly from the transition structure.

**(d) Ergodic Markov chain.** (Bookwork.) [2]

A Markov chain is **ergodic** if it is irreducible and aperiodic, so that it has a
unique stationary distribution to which it converges from any initial state.

## Question 3 [25 marks]

**(a) Transition matrix.** (Bookwork.) [5]

With rows and columns ordered \((CC, CD, DC, DD)\),

\[
M =
\begin{pmatrix}
pp' & p(1-p') & (1-p)p' & (1-p)(1-p') \\
qp' & q(1-p') & (1-q)p' & (1-q)(1-p') \\
pq' & p(1-q') & (1-p)q' & (1-p)(1-q') \\
qq' & q(1-q') & (1-q)q' & (1-q)(1-q')
\end{pmatrix}.
\]

**(b)(i) Tit For Tat against Always Defect.** [4]

Substitute \((p, q) = (1, 0)\) and \((p', q') = (0, 0)\) into the matrix of part
(a). Player 2 never cooperates, so its two factors are \(p' = q' = 0\), and
player 1 simply copies player 2's last action. For example the \(CC\) row is
\(\bigl(pp', p(1-p'), (1-p)p', (1-p)(1-p')\bigr) = (0, 1, 0, 0)\). Hence

\[
M =
\begin{pmatrix}
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}.
\]

**(b)(ii) Long-run outcome.** [4]

From \(CC\): \(CC \to CD \to DD\), and \(DD\) is absorbing. Tit For Tat is
exploited once (the move to \(CD\)) and play then settles at mutual defection.
The long-run outcome is \(DD\) with payoff \(1\) to each player.

**(c)(i) Tit For Tat against Always Cooperate.** [4]

Substitute \((p, q) = (1, 0)\) and \((p', q') = (1, 1)\) into the matrix of part
(a). Player 2 always cooperates, so its two factors are \(p' = q' = 1\), and
player 1 again copies player 2's last action. For example the \(CC\) row is
\(\bigl(pp', p(1-p'), (1-p)p', (1-p)(1-p')\bigr) = (1, 0, 0, 0)\). Hence

\[
M =
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 \\
1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0
\end{pmatrix}.
\]

**(c)(ii) Long-run outcome.** [4]

From \(CC\) the state stays at \(CC\) forever, so the long-run outcome is mutual
cooperation with payoff \(R = 3\) to each player.

**(d) Comment.** [4]

Against a cooperator Tit For Tat cooperates and both earn the mutual cooperation
payoff \(3\); against a defector it quickly switches to defection, conceding only
a single round of exploitation before settling at \(1\). Tit For Tat reciprocates
the opponent's behaviour, doing well against cooperators while avoiding sustained
exploitation by defectors. This is exactly why it performed so well in Axelrod's
tournaments: it is *nice* (never the first to defect), *retaliatory* (punishes
defection at once) and *forgiving* (returns to cooperation as soon as the
opponent does), so it scores highly against cooperative strategies without being
exploited by aggressive ones.

## Question 4 [25 marks]

**(a) The reactive recurrence.** [4]

A reactive player cooperates with probability \(p\) after the opponent cooperated
and \(q\) after the opponent defected. In round \(t\) the opponent cooperated with
probability \(c'_t\), so player 1's probability of cooperating in the next round
is

\[
c_{t+1} = p\, c'_t + q\,(1 - c'_t) = q + (p - q)\, c'_t.
\]

**(b) Long-run cooperation probabilities.** [6]

By symmetry player 2 satisfies \(c'_{t+1} = q' + r_2\, c_t\). At the fixed point
\(s_1 = q + r_1 s_2\) and \(s_2 = q' + r_2 s_1\). Substituting the second into the
first,

\[
s_1 = q + r_1\bigl(q' + r_2 s_1\bigr) = q + r_1 q' + r_1 r_2 s_1,
\]

so \(s_1(1 - r_1 r_2) = q + r_1 q'\) and

\[
s_1 = \frac{q + r_1 q'}{1 - r_1 r_2}.
\]

**(c) Tit For Tat matches the opponent.** [6]

Tit For Tat is \((p, q) = (1, 0)\), so \(r_1 = p - q = 1\) and \(q = 0\). Then
\(1 - r_1 r_2 = 1 - r_2\), and

\[
s_1 = \frac{0 + 1\cdot q'}{1 - r_2} = \frac{q'}{1 - r_2},
\qquad
s_2 = \frac{q' + r_2\cdot 0}{1 - r_2} = \frac{q'}{1 - r_2}.
\]

Hence \(s_1 = s_2\): Tit For Tat ends up cooperating at exactly the same long-run
rate as its opponent, whatever reactive strategy the opponent uses.

**(d) Equal payoffs and tournament success.** [9]

Write \(s = s_1 = s_2\). The long-run distribution over
\((CC, CD, DC, DD)\) is
\(\pi = \bigl(s^2,\ s(1 - s),\ (1 - s)s,\ (1 - s)^2\bigr)\), so the two off-diagonal
states \(CD\) and \(DC\) are equally likely. The players' long-run payoffs are

\[
u_1 = 3\pi_{CC} + 0\,\pi_{CD} + 5\,\pi_{DC} + 1\,\pi_{DD},
\qquad
u_2 = 3\pi_{CC} + 5\,\pi_{CD} + 0\,\pi_{DC} + 1\,\pi_{DD},
\]

and their difference is

\[
u_1 - u_2 = 5\bigl(\pi_{DC} - \pi_{CD}\bigr) = 5\bigl(s(1 - s) - s(1 - s)\bigr) = 0.
\]

So Tit For Tat always earns exactly what its opponent earns: it never loses a
head-to-head encounter. This is the property behind its success in Axelrod's
tournaments. Tit For Tat never beats any single opponent, yet it is never
exploited either, and because the strategies that defect lose heavily against one
another, Tit For Tat's habit of drawing every match left it with the highest total
score.
