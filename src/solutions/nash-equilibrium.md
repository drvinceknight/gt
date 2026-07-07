---
layout: solution
title: "Nash Equilibrium"
tag: nash-equilibrium
---

# Nash Equilibrium: worked solutions

Solutions to the example questions on the
[Nash Equilibrium](/topics/nash-equilibrium.html) page. Each question is worth 25
marks.

## Question 1 [25 marks]

**(a) Symmetric zero-sum game.** [3]

The column player's matrix is
\(M_c = -M = \begin{pmatrix} 0 & 1 & -1 \\ -1 & 0 & 1 \\ 1 & -1 & 0 \end{pmatrix}\).
It is zero sum because \(M + M_c = 0\): one player's gain is exactly the other's
loss. It is symmetric because \(M = -M^{\top}\), so interchanging the two players
maps the game to itself while negating the payoffs.

**(b) Utilities for the three strategy pairs.** [3]

The row player's utility is \(u_r = \sigma_r M \sigma_c^{\top}\) and, as the game
is zero sum, the column player's is \(u_c = -u_r\). For
\(\sigma_c = (\tfrac{1}{2}, \tfrac{1}{2}, 0)\) we have
\(M \sigma_c^{\top} = (-\tfrac{1}{2}, \tfrac{1}{2}, 0)\).

1. \(\sigma_r = (\tfrac{1}{3}, 0, \tfrac{2}{3})\):
   \(u_r = \tfrac{1}{3}(-\tfrac{1}{2}) + 0 + \tfrac{2}{3}(0) = -\tfrac{1}{6}\), so
   \((u_r, u_c) = (-\tfrac{1}{6}, \tfrac{1}{6})\).
2. \(\sigma_r = (\tfrac{1}{3}, \tfrac{1}{3}, \tfrac{1}{3})\):
   \(u_r = \tfrac{1}{3}(-\tfrac{1}{2} + \tfrac{1}{2} + 0) = 0\), so
   \((u_r, u_c) = (0, 0)\).
3. \(\sigma_r = \sigma_c = (\tfrac{1}{3}, \tfrac{1}{3}, \tfrac{1}{3})\): here
   \(M \sigma_c^{\top} = (0, 0, 0)\), so \(u_r = 0\) and \((u_r, u_c) = (0, 0)\).

**(c) The uniform strategy is a Nash equilibrium.** [9]

The best response condition states that \(\sigma_r\) is a best response to
\(\sigma_c\) if and only if every action in its support yields the maximal
expected payoff, that is \(\sigma_r(i) > 0 \Rightarrow (M\sigma_c^{\top})_i =
\max_k (M\sigma_c^{\top})_k\). Take both players uniform,
\(\sigma = \left(\tfrac{1}{3}, \tfrac{1}{3}, \tfrac{1}{3}\right)\). Against
\(\sigma_c = \sigma\), the row player's expected payoffs are

\[
\text{Rock}: \tfrac{0 - 1 + 1}{3} = 0, \quad
\text{Paper}: \tfrac{1 + 0 - 1}{3} = 0, \quad
\text{Scissors}: \tfrac{-1 + 1 + 0}{3} = 0.
\]

All three actions give the maximal payoff \(0\), so every action in the support
of \(\sigma_r\) is a best response: by the best response condition \(\sigma_r\) is
a best response. By the symmetry of the game the same holds for the column
player, so \((\sigma, \sigma)\) is a Nash equilibrium, with value \(0\).

**(d) Uniqueness.** [6]

In Rock-Paper-Scissors every action is beaten by another, so no Nash equilibrium
can place all weight on a proper subset of the actions: whatever the support of
the opponent's strategy, a player can deviate to the action that beats the
opponent's most likely choice. Hence in any equilibrium each player mixes over
all three actions, and by the best response condition is indifferent between
them. Writing \(\sigma_c = (a, b, c)\) with \(a + b + c = 1\), the row player's
payoffs are

\[
\text{Rock}: c - b, \quad \text{Paper}: a - c, \quad \text{Scissors}: b - a.
\]

Setting them equal, \(c - b = a - c\) gives \(2c = a + b\), and \(a - c = b - a\)
gives \(2a = b + c\); with \(a + b + c = 1\) these force
\(a = b = c = \tfrac{1}{3}\). By symmetry \(\sigma_r\) is also uniform, so the
equilibrium is unique.

**(e) Rock-Paper-Scissors-Lizard-Spock.** [4]

By the same symmetry each action beats two others and loses to two, so against
the uniform strategy each action earns \(\tfrac{2(+1) + 2(-1)}{5} = 0\): all five
are best responses. As in part (d), no equilibrium can leave any action unused, so
the unique Nash equilibrium is each player playing each of the five actions with
probability \(\tfrac{1}{5}\), with value \(0\).

## Question 2 [25 marks]

**(a) Definitions.** (Bookwork.) [5]

- An \(N\)-player **normal form game** consists of a finite set of \(N\) players,
  an action set \(\mathcal{A}_i\) for each player, and a payoff function
  \(u_i : \mathcal{A}_1 \times \dots \times \mathcal{A}_N \to \mathbb{R}\) for
  each player.
- An action \(a_i \in \mathcal{A}_i\) is **strictly dominated** if there is a
  strategy \(\sigma_i \in \Delta(\mathcal{A}_i)\) with
  \(u_i(\sigma_i, s_{-i}) > u_i(a_i, s_{-i})\) for all \(s_{-i} \in S_{-i}\).
- A strategy \(s^{*}\) for player \(i\) is a **best response** to \(s_{-i}\) if
  \(u_i(s^{*}, s_{-i}) \ge u_i(s, s_{-i})\) for all \(s \in \Delta(\mathcal{A}_i)\).
- A strategy profile is a **Nash equilibrium** if each player's strategy is a best
  response to the others'.
- The **support** of a strategy is the set of actions it plays with positive
  probability.

**(b)(i) Pure Nash equilibria.** [4]

Underlining best responses (each column for the row player in \(M_r\), each row
for the column player in \(M_c\)):

\[
M_r =
\begin{pmatrix}
\underline{4} & 1 \\
0 & \underline{3}
\end{pmatrix}
\qquad
M_c =
\begin{pmatrix}
\underline{3} & 0 \\
1 & \underline{4}
\end{pmatrix}.
\]

Both payoffs are underlined in the top-left and bottom-right cells, giving the
pure Nash equilibria \(\{((1, 0), (1, 0)), ((0, 1), (0, 1))\}\).

**(b)(ii) Sketches and indifference.** [4]

Against \(\sigma_2 = (y, 1 - y)\):
\(u_1(r_1) = 4y + (1 - y) = 1 + 3y\) (from \((0,1)\) to \((1,4)\)) and
\(u_1(r_2) = 3(1 - y) = 3 - 3y\) (from \((0,3)\) to \((1,0)\)); they cross where
\(1 + 3y = 3 - 3y\), i.e. \(y = \tfrac{1}{3}\). Against \(\sigma_1 = (x, 1 - x)\):
\(u_2(c_1) = 3x + (1 - x) = 1 + 2x\) and \(u_2(c_2) = 4(1 - x) = 4 - 4x\); they
cross where \(1 + 2x = 4 - 4x\), i.e. \(x = \tfrac{1}{2}\).

**(b)(iii) Mixed Nash equilibrium.** [5]

By the best response condition, writing the row player's matrix as \(A = M_r\), a
strategy \(\sigma_r^{*}\) is a best response to \(\sigma_c\) if and only if

\[
\sigma_{r^{*}}(i) > 0 \quad \Rightarrow \quad
(A \sigma_c^{\top})_i = \max_{k \in \mathcal{A}_1}(A \sigma_c^{\top})_k
\quad \text{for all } i \in \mathcal{A}_1,
\]

that is, every action played with positive probability must earn the maximal
expected payoff. For an equilibrium in which both supports have size two, every
action lies in the support, so each player must be indifferent between their two
actions and hence make the other indifferent. From part (ii) the column player is
indifferent at \(x = \tfrac{1}{2}\) and the row player at \(y = \tfrac{1}{3}\), so
the mixed Nash equilibrium is
\(\left(\left(\tfrac{1}{2}, \tfrac{1}{2}\right), \left(\tfrac{1}{3}, \tfrac{2}{3}\right)\right)\).

**(b)(iv) Payoffs and comparison.** [7]

At the mixed equilibrium each player is indifferent, so the row player earns
\(u_1(r_1) = 1 + 3 \cdot \tfrac{1}{3} = 2\) and the column player earns
\(u_2(c_1) = 1 + 2 \cdot \tfrac{1}{2} = 2\); the payoff profile is \((2, 2)\). The
pure equilibria give \((4, 3)\) at \(((1,0),(1,0))\) and \((3, 4)\) at
\(((0,1),(0,1))\). Each player earns at least \(3\) in either pure equilibrium,
which exceeds the mixed payoff of \(2\), so both players would prefer either pure
equilibrium to the mixed one: the mixed equilibrium is the worst of the three for
both players.

## Question 3 [25 marks]

**(a) Definitions.** (Bookwork.) [5]

- An action \(a_i \in \mathcal{A}_i\) is **strictly dominated** if there is a
  strategy \(\sigma_i \in \Delta(\mathcal{A}_i)\) with
  \(u_i(\sigma_i, s_{-i}) > u_i(a_i, s_{-i})\) for all \(s_{-i}\).
- It is **weakly dominated** if there is such a \(\sigma_i\) with
  \(u_i(\sigma_i, s_{-i}) \ge u_i(a_i, s_{-i})\) for all \(s_{-i}\) and strict
  inequality for at least one \(s_{-i}\).
- Example: with row-player payoffs
  \(\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}\), row 2 is weakly dominated by
  row 1 (\(1 \ge 1\) and \(1 > 0\)) but not strictly, since against the first
  column both rows give \(1\).

**(b)(i) Iterated elimination.** [4]

For the row player, row 2 strictly dominates row 1 (\(5 > 3\) and \(1 > 0\)), so
row 1 is eliminated. With only row 2 remaining, the column player's payoffs are
\(0\) for column 1 and \(1\) for column 2, so column 2 strictly dominates column
1 and column 1 is eliminated. The single surviving profile is
\(((0, 1), (0, 1))\), the Nash equilibrium, with payoffs \((1, 1)\).

**(b)(ii) Interpretation.** [4]

The outcome in which each plays their first action gives \((3, 3)\), which both
players prefer to the equilibrium \((1, 1)\) since \(3 > 1\). It cannot be
sustained in a one-shot game: from \((3, 3)\) either player can deviate to their
second action and earn \(5 > 3\), so it is not a Nash equilibrium. Strict
dominance drives both players to their second action and hence to the inferior
outcome \((1, 1)\).

**(c)(i) Pure Nash equilibria.** [3]

\[
M_r =
\begin{pmatrix}
\underline{2} & 0 \\
0 & \underline{1}
\end{pmatrix}
\qquad
M_c =
\begin{pmatrix}
\underline{1} & 0 \\
0 & \underline{2}
\end{pmatrix}.
\]

The pure Nash equilibria are \(\{((1, 0), (1, 0)), ((0, 1), (0, 1))\}\), with
payoffs \((2, 1)\) and \((1, 2)\).

**(c)(ii) Mixed Nash equilibrium.** [6]

By the best response condition each player makes the other indifferent. The row
player makes the column player indifferent: \(u_2(c_1) = x\) and
\(u_2(c_2) = 2(1 - x)\), equal at \(x = 2 - 2x\), so \(x = \tfrac{2}{3}\). The
column player makes the row player indifferent: \(u_1(r_1) = 2y\) and
\(u_1(r_2) = 1 - y\), equal at \(2y = 1 - y\), so \(y = \tfrac{1}{3}\). The mixed
Nash equilibrium is
\(\left(\left(\tfrac{2}{3}, \tfrac{1}{3}\right), \left(\tfrac{1}{3}, \tfrac{2}{3}\right)\right)\).

**(c)(iii) Payoffs and inefficiency.** [3]

At the mixed equilibrium the row player earns \(u_1(r_1) = 2y = \tfrac{2}{3}\) and
the column player earns \(u_2(c_1) = x = \tfrac{2}{3}\). Each pure equilibrium
gives the players \(2\) and \(1\) (in some order), and even the smaller of these,
\(1\), exceeds \(\tfrac{2}{3}\). So the mixed equilibrium is worse for both
players than either pure equilibrium: a failure to coordinate.

## Question 4 [25 marks]

**(a) Antisymmetry forces a zero diagonal value.** [5]

The quantity \(s = \sigma A \sigma^T\) is a scalar, so it equals its own
transpose. Using \(A^T = -A\),

\[
s = \sigma A \sigma^T = \bigl(\sigma A \sigma^T\bigr)^T = \sigma A^T \sigma^T
= -\sigma A \sigma^T = -s.
\]

Hence \(s = -s\), so \(s = 0\). A player who uses any strategy \(\sigma\) against
an opponent using the same \(\sigma\) therefore earns an expected payoff of zero.

**(b) Equilibrium condition and value.** [6]

By the best response condition, \(\sigma^*\) is a best response to \(\sigma^*\) if
and only if every action in the support of \(\sigma^*\) is itself a best response,
and no action does strictly better. The payoff to playing pure action \(i\)
against \(\sigma^*\) is \((A \sigma^{*T})_i\), while \(\sigma^*\) itself earns
\(\sigma^* A \sigma^{*T} = 0\) by part (a). So \((\sigma^*, \sigma^*)\) is a Nash
equilibrium if and only if

\[
(A \sigma^{*T})_i \le 0 \text{ for all } i,
\qquad (A \sigma^{*T})_i = 0 \text{ for } i \text{ in the support of } \sigma^*.
\]

Playing \(\sigma^*\) guarantees the row player an expected payoff of \(0\) against
any opponent strategy, and by symmetry the column player can likewise guarantee
\(0\); since the game is zero-sum the two guarantees are consistent only if the
value is exactly \(0\).

**(c) The weighted equilibrium.** [8]

A full-support equilibrium has \(A \sigma^{*T} = 0\). Writing
\(\sigma^* = (x, y, z)\),

\[
\begin{aligned}
-y + \beta z &= 0 \quad\Rightarrow\quad y = \beta z, \\
x - \beta z &= 0 \quad\Rightarrow\quad x = \beta z, \\
-\beta x + \beta y &= 0 \quad\Rightarrow\quad x = y,
\end{aligned}
\]

which are consistent with \(x = y = \beta z\). The normalisation
\(x + y + z = 1\) gives \(z(2\beta + 1) = 1\), so

\[
\sigma^* = \left(\frac{\beta}{2\beta + 1},\ \frac{\beta}{2\beta + 1},\ \frac{1}{2\beta + 1}\right).
\]

When \(\beta = 1\) this is \(\bigl(\tfrac{1}{3}, \tfrac{1}{3}, \tfrac{1}{3}\bigr)\),
recovering standard Rock-Paper-Scissors.

**(d) Interpretation.** [6]

As \(\beta\) increases the equilibrium weight on Rock and Paper rises towards
\(\tfrac{1}{2}\) each while Scissors falls towards \(0\); as \(\beta \to 0\) almost
all the weight goes onto Scissors. The parameter \(\beta\) scales the stakes of
the contests that Scissors is involved in: a larger \(\beta\) makes the swings
around Scissors more severe, and in equilibrium the players protect themselves by
playing Scissors less often and the other two actions more. The equilibrium
always keeps every action a best response, so no action is ever abandoned for any
finite \(\beta > 0\), but the mixing tilts smoothly with the weight.
