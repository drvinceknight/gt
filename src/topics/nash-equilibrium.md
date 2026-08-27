---
layout: topic
title: "Nash Equilibrium"
tag: nash-equilibrium
note_urls:
  - "https://vknight.org/gtb/chapters/nash-equilibrium/"
---

## Example questions

The following are exam-type questions in the style of the examination paper,
and are intended to be a little harder than the examination itself, with marks
at the rates used in the papers. **A question totalling fewer than 25 marks
would, in the examination, be combined with further parts, often one of the
examinable proofs, to make a full 25-mark question.** Attempt them in full
before reading the worked solutions.

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

1. \(\sigma_r = (\tfrac{1}{3}, 0, \tfrac{2}{3})\qquad
   \sigma_c = (\tfrac{1}{2}, \tfrac{1}{2}, 0) \)
2. \(\sigma_r = (\tfrac{1}{3}, \tfrac{1}{3}, \tfrac{1}{3})\qquad
   \sigma_c = (\tfrac{1}{2}, \tfrac{1}{2}, 0) \)
3. \(\sigma_r = (\tfrac{1}{3}, \tfrac{1}{3}, \tfrac{1}{3})\qquad
   \sigma_c = (\tfrac{1}{3}, \tfrac{1}{3}, \tfrac{1}{3}) \)

[3]

(c) Using the best response condition, prove that both players playing each
action with probability \(\tfrac{1}{3}\) is a Nash equilibrium. [5]

(d) Prove that this is the _unique_ Nash equilibrium: show that in any Nash
equilibrium each player is indifferent between all three actions, and deduce the
mixing probabilities. [5]

(e) For Rock-Paper-Scissors-Lizard-Spock, in which each of five actions beats two
others and loses to two, state the Nash equilibrium and justify it by the same
indifference argument. [3]

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
indifferent. [6]

(iii) State the best response condition, and use it (or the support
enumeration algorithm) to obtain the mixed Nash equilibrium. [5]

(iv) Compute each player's expected payoff at the mixed Nash equilibrium, and
determine whether each player would prefer it to the pure Nash equilibria. [4]

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
sustained in a one-shot game. [3]

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

(ii) Using the best response condition, obtain the mixed Nash equilibrium. [5]

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
A = \begin{pmatrix}
0 & -1 & \beta \\ 1 & 0 & -\beta \\ -\beta & \beta & 0
\end{pmatrix},
\qquad \beta > 0.
\]

By solving \(A \sigma^{*T} = 0\), find the full-support symmetric Nash
equilibrium, and confirm it reduces to \(\bigl(\tfrac{1}{3}, \tfrac{1}{3},
\tfrac{1}{3}\bigr)\) when \(\beta = 1\). [8]

(d) Describe how the equilibrium changes as \(\beta\) varies between \(0\) and
\(\infty\), and interpret what the weight \(\beta\) does to the players' use of
each action. [6]

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

### Marking exercise 1 (on Question 2(b)(iii), worth [5])

A student pastes Question 2(b)(iii) into a free AI chatbot, which replies:

```text
Step 1: Set up the indifference conditions.

In a mixed Nash equilibrium, each player must be indifferent between
their two strategies; otherwise they would simply play the better one!

Step 2: Find the row player's mix.

Let the row player play their first action with probability x. Using
the row player's matrix M_r, indifference between their two actions
gives

    4x + 1(1 - x) = 0x + 3(1 - x)

so 3x + 1 = 3 - 3x, which solves to give x = 1/3. ✅

Step 3: Find the column player's mix.

Let the column player play their first action with probability y.
Using the column player's matrix, indifference between their two
actions gives

    3y + 1(1 - y) = 0y + 4(1 - y)

so 2y + 1 = 4 - 4y, which solves to give y = 1/2. ✅

Conclusion.

The unique Nash equilibrium of this game is:

    σ1 = (1/3, 2/3),    σ2 = (1/2, 1/2)

Let me know if you would like me to walk through any of the steps in
more detail!
```

### Marking exercise 2 (on Question 3(b)(i) and (ii), worth [4] and [3])

A student pastes Question 3(b) into a free AI chatbot, which replies:

```text
Finding the dominated strategies.

Compare the two rows of the row player's matrix M_r. The second row
gives 5 > 3 against the first column and 1 > 0 against the second, so
the first action is weakly dominated by the second and can be
eliminated. By the symmetry of the game the column player's first
action is also weakly dominated, and it can be eliminated too.

The equilibrium.

The only cell that survives is both players choosing their second
action, with payoffs (1, 1). This is the Nash equilibrium obtained by
iterated elimination.

Why can the players not do better?

Although (3, 3) looks better for both players, the equilibrium (1, 1)
is Pareto efficient, because neither player can improve their payoff by
changing their own strategy. Cooperation cannot be sustained in a
one-shot game because each player has an incentive to deviate. This is
the famous Prisoner's Dilemma!
```

## Optional further reading

You do not need any of this to follow the topic, but the following chapters of
the textbook may help if you would like more background:

- [Best response polytopes](https://vknight.org/gtb/chapters/best-response-polytopes/),
  which gives a geometric view of equilibria and introduces the Lemke-Howson
  algorithm for finding them.
- [Zero-Sum Games](https://vknight.org/gtb/chapters/zero-sum-games/), which
  treats the special case of strictly opposed interests through minimax and
  linear programming.
