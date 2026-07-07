---
layout: solution
title: "Cooperative Games"
tag: cooperative-games
---

# Cooperative Games: worked solutions

Solutions to the example questions on the
[Cooperative Games](/topics/cooperative-games.html) page. Each question is worth
25 marks.

## Question 1 [25 marks]

**(a) Definitions.** (Bookwork.) [5]

A **characteristic function game** \(G = (N, v)\) is a set of players \(N\) with a
function \(v : 2^N \to \mathbb{R}\) giving each coalition a worth. The **Shapley
value** of player \(i\) is \(\phi_i = \frac{1}{N!}\sum_{\pi} \Delta_\pi(i)\), the
average over all orderings \(\pi\) of the marginal contribution
\(\Delta_\pi(i) = v(S_\pi(i) \cup \{i\}) - v(S_\pi(i))\), where \(S_\pi(i)\) is the
set of players preceding \(i\) in \(\pi\).

**(b) Marginal contribution vectors.** [8]

\[
\begin{aligned}
(1, 2, 3) &: (2, 3, 5) & (1, 3, 2) &: (2, 4, 4) \\
(2, 1, 3) &: (4, 1, 5) & (2, 3, 1) &: (6, 1, 3) \\
(3, 1, 2) &: (4, 4, 2) & (3, 2, 1) &: (6, 2, 2)
\end{aligned}
\]

**(c) Shapley value.** [6]

\[
\phi_1 = \frac{2 + 2 + 4 + 6 + 4 + 6}{6} = \frac{24}{6} = 4,
\quad
\phi_2 = \frac{3 + 4 + 1 + 1 + 4 + 2}{6} = \frac{15}{6} = \frac{5}{2},
\quad
\phi_3 = \frac{5 + 4 + 5 + 3 + 2 + 2}{6} = \frac{21}{6} = \frac{7}{2}.
\]

So \(\phi = \left(4, \tfrac{5}{2}, \tfrac{7}{2}\right)\).

**(d) Efficiency and interpretation.** [6]

\(4 + \tfrac{5}{2} + \tfrac{7}{2} = 4 + 6 = 10 = v(N)\), so the allocation is
efficient. The three parts are worth only \(2 + 1 + 2 = 5\) on their own, half of
\(v(N) = 10\), so half of the aid's value comes from the parts reinforcing one
another. The Shapley value shares this synergy by averaging each part's marginal
contribution over all six orders. The maths forms the strongest pairs
(\(v(\{1, 3\}) = 6\) with the story and \(v(\{1, 2\}) = 5\) with the picture), so
the Theorist receives the most, \(4\), double the \(2\) the maths scores alone.
The picture is weakest both alone (\(1\)) and in its pairs, so the Artist
receives the least, \(\tfrac{5}{2}\), and the Storyteller receives
\(\tfrac{7}{2}\). The Shapley value is therefore a fair division of the ten: it
rewards each student by the average value their part adds, not by what it is
worth in isolation.

## Question 2 [25 marks]

**(a) Definitions.** (Bookwork.) [5]

- A **characteristic function game** \(G = (N, v)\) is given by a set of players
  \(N\) and a **characteristic function** \(v : 2^N \to \mathbb{R}\) mapping every
  coalition (subset of \(N\)) to a payoff.
- A **payoff vector** \(\lambda \in \mathbb{R}_{\ge 0}^N\) allocates the value of
  the grand coalition among the players, with \(\sum_{i} \lambda_i = v(N)\).
- Given a permutation \(\pi\) of the players, the **marginal contribution** of
  player \(i\) is \(\Delta_\pi^G(i) = v(S_\pi(i) \cup \{i\}) - v(S_\pi(i))\),
  where \(S_\pi(i)\) is the set of players preceding \(i\) in \(\pi\).
- The **Shapley value** of player \(i\) is
  \(\phi_i(G) = \frac{1}{N!} \sum_{\pi} \Delta_\pi^G(i)\), the average marginal
  contribution over all \(N!\) orderings of the players.

**(b)(i) Marginal contribution vectors.** [5]

\[
\begin{aligned}
(1, 2, 3) &: (0, 90, 30) & (1, 3, 2) &: (0, 40, 80) \\
(2, 1, 3) &: (90, 0, 30) & (2, 3, 1) &: (50, 0, 70) \\
(3, 1, 2) &: (80, 40, 0) & (3, 2, 1) &: (50, 70, 0)
\end{aligned}
\]

**(b)(ii) Shapley value.** [6]

\[
\phi_1 = \frac{270}{6} = 45, \qquad \phi_2 = \frac{240}{6} = 40, \qquad \phi_3 = \frac{210}{6} = 35.
\]

So \(\phi = (45, 40, 35)\).

**(b)(iii) Efficiency.** [3]

\(45 + 40 + 35 = 120 = v(\{1, 2, 3\})\), so the Shapley value is efficient.

**(c) Interpretation.** [6]

The Shapley value is the fair allocation of the grand coalition's worth obtained
by averaging each player's marginal contribution over every order in which the
coalition could form. It rewards a player according to how much they add, on
average, to the coalitions they join. It is regarded as fair because of the
properties it uniquely satisfies: **efficiency** (the whole worth \(v(N)\) is
shared out), **symmetry** (players who contribute equally to every coalition get
equal shares), the **null player** property (a player who never adds value gets
nothing) and **additivity** (the value of two combined games is the sum of the
separate values). Together these axioms pin the Shapley value down as the unique
fair allocation.

## Question 3 [25 marks]

**(a) Properties.** (Bookwork.) [6]

- **Efficiency:** \(\sum_i \phi_i = v(N)\), the value of the grand coalition.
- **Null player:** if \(v(C \cup \{i\}) = v(C)\) for all coalitions \(C\), then
  \(\phi_i = 0\).
- **Symmetry:** if \(v(C \cup \{i\}) = v(C \cup \{j\})\) for all coalitions \(C\)
  containing neither \(i\) nor \(j\), then \(\phi_i = \phi_j\).
- **Additivity:** for two games \((N, v_1)\) and \((N, v_2)\), the Shapley value
  of their sum is the sum of the Shapley values.

**(b)(i) Shapley value.** [4]

All players are interchangeable, so by symmetry and efficiency
(\(\sum \phi_i = v(N) = 1\)),

\[
\phi = \left(\tfrac{1}{3}, \tfrac{1}{3}, \tfrac{1}{3}\right).
\]

**(b)(ii) Null players.** [2]

None: each player \(i\) has \(v(\{i, j\}) - v(\{j\}) = 1 \neq 0\), so adding any
player can change a coalition's worth.

**(c)(i) Null player.** [3]

Player 3 is a null player: \(v(S \cup \{3\}) = v(S)\) for every coalition \(S\),
since the worth depends only on whether \(\{1, 2\} \subseteq S\).

**(c)(ii) Shapley value.** [5]

The marginal contribution vectors are

\[
\begin{aligned}
(1, 2, 3) &: (0, 4, 0) & (1, 3, 2) &: (0, 4, 0) \\
(2, 1, 3) &: (4, 0, 0) & (2, 3, 1) &: (4, 0, 0) \\
(3, 1, 2) &: (0, 4, 0) & (3, 2, 1) &: (4, 0, 0)
\end{aligned}
\]

giving \(\phi_1 = \tfrac{12}{6} = 2\), \(\phi_2 = \tfrac{12}{6} = 2\),
\(\phi_3 = 0\). So \(\phi = (2, 2, 0)\).

**(c)(iii) Efficiency, symmetry and interpretation.** [5]

\(2 + 2 + 0 = 4 = v(N)\), so the allocation is efficient. Players 1 and 2 are
symmetric: for any coalition \(C\) containing neither, \(\{1, 2\} \not\subseteq C\)
and \(\{1, 2\} \not\subseteq C \cup \{1\}\) and likewise for \(2\), so
\(v(C \cup \{1\}) = v(C \cup \{2\}) = 0\); by symmetry they receive equal payoffs,
and indeed \(\phi_1 = \phi_2 = 2\). The null player 3 receives nothing, exactly as
the null player property requires. So the two essential players split the worth
equally and the player who contributes nothing gets nothing: the Shapley value
allocates fairly.

## Question 4 [25 marks]

**(a) Additivity.** [4]

The Shapley value \(\phi\) is additive: for any two games \(v\) and \(w\) on the
same player set, \(\phi(v + w) = \phi(v) + \phi(w)\). The game \(v + w\) is the
characteristic function game whose worth for each coalition \(S\) is
\((v + w)(S) = v(S) + w(S)\). Additivity says that if a game splits into a sum of
simpler games, its Shapley value is the sum of the Shapley values of the parts.

**(b) The unanimity game.** [6]

In \(u_T\) a coalition is worth \(1\) exactly when it contains every member of
\(T\). Any player \(i \notin T\) is a null player: adding them to a coalition never
changes whether \(T\) is contained, so their marginal contribution is always
\(0\), and the null player property gives them \(0\). The members of \(T\) are
symmetric: interchanging any two of them leaves the game unchanged, so the
symmetry property gives them equal shares. By efficiency the shares sum to
\(u_T(N) = 1\), so each of the \(|T|\) members of \(T\) receives \(1/|T|\):

\[
\phi_i(u_T) = \begin{cases} 1/|T| & i \in T, \\ 0 & i \notin T. \end{cases}
\]

**(c) Applying additivity.** [9]

Writing out \(v = 2\, u_{\{1,2\}} + 3\, u_{\{1,2,3\}}\),

\[
\begin{aligned}
v(\emptyset) &= 0, & v(\{1\}) = v(\{2\}) = v(\{3\}) &= 0, \\
v(\{1,2\}) &= 2, & v(\{1,3\}) = v(\{2,3\}) &= 0, \\
v(\{1,2,3\}) &= 2 + 3 = 5.
\end{aligned}
\]

By part (b), \(\phi(u_{\{1,2\}}) = \bigl(\tfrac{1}{2}, \tfrac{1}{2}, 0\bigr)\) and
\(\phi(u_{\{1,2,3\}}) = \bigl(\tfrac{1}{3}, \tfrac{1}{3}, \tfrac{1}{3}\bigr)\).
Additivity gives

\[
\phi(v) = 2\left(\tfrac{1}{2}, \tfrac{1}{2}, 0\right)
+ 3\left(\tfrac{1}{3}, \tfrac{1}{3}, \tfrac{1}{3}\right)
= (1, 1, 0) + (1, 1, 1) = (2, 2, 1).
\]

The shares sum to \(5 = v(\{1,2,3\})\), so the Shapley value is efficient.

**(d) Interpretation.** [6]

The decomposition reads off each player's share as a sum of contributions, one
from each unanimity game in the decomposition. Players 1 and 2 each draw
\(1\) from the \(2\, u_{\{1,2\}}\) part, the value that only their pair can unlock,
and a further \(1\) from the grand-coalition part \(3\, u_{\{1,2,3\}}\); player 3
draws only from the grand-coalition part. Additivity turns a sum over all six
orderings into the addition of two known answers. More generally every game can be
written as a combination of unanimity games, so the Shapley value of any game
follows from the simple formula in part (b) together with additivity, avoiding the
\(n!\) orderings entirely.
