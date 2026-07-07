---
layout: topic
title: "Nash Equilibrium"
tag: nash-equilibrium
note_urls:
  - "https://vknight.org/gtb/chapters/nash-equilibrium/"
---

## Example questions

The following are exam-type questions in the style of the examination paper, and
are intended to be a little harder than the examination itself.
**Each question is worth 25 marks.** Attempt them in full before reading the
worked solutions.

### Question 1 (based on the in-class activity)

In class we ran a Rock-Paper-Scissors tournament. The row player's payoff matrix,
with actions ordered (Rock, Paper, Scissors), using \(+1\) for a win, \(-1\) for
a loss and \(0\) for a draw, is

\[
M = \begin{pmatrix} 0 & -1 & 1 \\ 1 & 0 & -1 \\ -1 & 1 & 0 \end{pmatrix}.
\]

(a) Explain why this is a symmetric zero-sum game, write down the column player's
payoff matrix. [3]

(b) Obtain the utilities to both players for the following pairs of strategies:

1. \(\sigma_r = (\tfrac{1}{3}, 0, \tfrac{2}{3})\qquad \sigma_c = (\tfrac{1}{2}, \tfrac{1}{2}, 0) \)
2. \(\sigma_r = (\tfrac{1}{3}, \tfrac{1}{3}, \tfrac{1}{3})\qquad \sigma_c = (\tfrac{1}{2}, \tfrac{1}{2}, 0) \)
3. \(\sigma_r = (\tfrac{1}{3}, \tfrac{1}{3}, \tfrac{1}{3})\qquad \sigma_c = (\tfrac{1}{3}, \tfrac{1}{3}, \tfrac{1}{3}) \)

[3]

(c) Using the best response condition, prove that both players playing each
action with probability \(\tfrac{1}{3}\) is a Nash equilibrium. [9]

(d) Prove that this is the _unique_ Nash equilibrium: show that in any Nash
equilibrium each player is indifferent between all three actions, and deduce the
mixing probabilities. [6]

(e) For Rock-Paper-Scissors-Lizard-Spock, in which each of five actions beats two
others and loses to two, state the Nash equilibrium and justify it by the same
indifference argument. [4]

### Question 2

(a) Provide definitions for the following terms:

- a normal form game;
- a strictly dominated strategy;
- a best response strategy;
- a Nash equilibrium;
- the support of a strategy. [5]

(b) Consider the normal form game defined by

\[
M_r =
\begin{pmatrix}
4 & 1 \\
0 & 3
\end{pmatrix}
\qquad
M_c =
\begin{pmatrix}
3 & 0 \\
1 & 4
\end{pmatrix},
\]

where \(M_r\) gives the payoffs of the row player and \(M_c\) those of the column
player.

(i) Obtain all pure Nash equilibria. [4]

(ii) By sketching the row player's expected utilities against
\(\sigma_2 = (y, 1 - y)\) and the column player's against
\(\sigma_1 = (x, 1 - x)\), find the value of \(y\) at which the row player is
indifferent and the value of \(x\) at which the column player is
indifferent. [4]

(iii) State the best response condition, and use it (or the support
enumeration algorithm) to obtain the mixed Nash equilibrium. [5]

(iv) Compute each player's expected payoff at the mixed Nash equilibrium, and
determine whether each player would prefer it to the pure Nash equilibria. [7]

### Question 3

(a) Define a strictly dominated strategy and a weakly dominated strategy, and
give an example of a game with an action that is weakly but not strictly
dominated. [5]

(b) Consider the Prisoner's Dilemma defined by

\[
M_r =
\begin{pmatrix}
3 & 0 \\
5 & 1
\end{pmatrix}
\qquad
M_c =
\begin{pmatrix}
3 & 5 \\
0 & 1
\end{pmatrix}.
\]

(i) Using iterated elimination of strictly dominated strategies, obtain the
Nash equilibrium, justifying each elimination. [4]

(ii) Explain why the equilibrium is worse for both players than the outcome in
which each plays their first action, and why that better outcome cannot be
sustained in a one-shot game. [4]

(c) Consider the coordination game defined by

\[
M_r =
\begin{pmatrix}
2 & 0 \\
0 & 1
\end{pmatrix}
\qquad
M_c =
\begin{pmatrix}
1 & 0 \\
0 & 2
\end{pmatrix}.
\]

(i) Obtain all pure Nash equilibria. [3]

(ii) Using the best response condition, obtain the mixed Nash equilibrium. [6]

(iii) Compute each player's expected payoff at the mixed Nash equilibrium, and
show that it is worse for both players than either pure equilibrium. [3]

### Question 4 (**hard**)

A two-player symmetric game has row-player payoff matrix \(A\); the column player
has payoff matrix \(A^T\). The game is symmetric and zero-sum when \(A\) is
antisymmetric, \(A^T = -A\).

(a) Show that for an antisymmetric \(A\), every strategy \(\sigma\) satisfies
\(\sigma A \sigma^T = 0\). Interpret this: a player using any strategy against an
identical opponent has expected payoff zero. [5]

(b) Using the best response condition, show that \((\sigma^*, \sigma^*)\) is a
symmetric Nash equilibrium if and only if \((A \sigma^{*T})_i \le 0\) for every
action \(i\), with equality on the support of \(\sigma^*\). Deduce that the value
of the game is zero. [6]

(c) Consider the weighted Rock-Paper-Scissors game with

\[
A = \begin{pmatrix} 0 & -1 & \beta \\ 1 & 0 & -\beta \\ -\beta & \beta & 0 \end{pmatrix},
\qquad \beta > 0.
\]

By solving \(A \sigma^{*T} = 0\), find the full-support symmetric Nash
equilibrium, and confirm it reduces to \(\bigl(\tfrac{1}{3}, \tfrac{1}{3},
\tfrac{1}{3}\bigr)\) when \(\beta = 1\). [8]

(d) Describe how the equilibrium changes as \(\beta\) varies between \(0\) and
\(\infty\), and interpret what the weight \(\beta\) does to the players' use of
each action. [6]

## Optional further reading

You do not need any of this to follow the topic, but the following chapters of
the textbook may help if you would like more background:

- [Best response polytopes](https://vknight.org/gtb/chapters/best-response-polytopes/),
  which gives a geometric view of equilibria and introduces the Lemke-Howson
  algorithm for finding them.
- [Zero-Sum Games](https://vknight.org/gtb/chapters/zero-sum-games/), which
  treats the special case of strictly opposed interests through minimax and
  linear programming.
