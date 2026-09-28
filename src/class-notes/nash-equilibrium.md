---
layout: class-notes
title: "Nash equilibrium"
tag: nash-equilibrium
---

## Activity (20 minutes)

**Goal.** Build towards the Nash equilibrium of a symmetric zero-sum game
through repeated play.

**The deck.** There is a write-on deck at
[/decks/nash-equilibrium/main.pdf](/decks/nash-equilibrium/main.pdf): the
rules of Rock Paper Scissors Lizard Spock as two diagrams, a tally of what the
room played, an empty Rock-Paper-Scissors payoff grid to fill in and mark best
responses on, and the indifference equations laid out with the working left
blank.

Play a "divisional" class round robin tournament of Rock Paper Scissors Lizard
Spock. Ask students to play in groups of four, then ask the winners to stand up
and keep playing until a single class champion remains.

The champion plays me for a bribentive.

## Discussion (20 minutes)

Discuss the **Nash equilibrium** chapter.

Discussion Point: **After the definition of support enumeration algorithm, ask how many steps to obtain the Nash equilibrium for our game?**

## Answers for the deck

**The rules.** Each action wins \(2\), loses \(2\) and draws \(1\). The game is
symmetric and zero sum, and the two payoffs in any cell add to \(0\).

**The payoff matrix.** Ordering the actions (Rock, Paper, Scissors), the row
player's matrix is

\[
M = \begin{pmatrix} 0 & -1 & 1 \\ 1 & 0 & -1 \\ -1 & 1 & 0 \end{pmatrix},
\]

and the column player's is \(M^{T} = -M\). No cell has both players' best
responses circled: against Rock I want Paper, against Paper I want Scissors,
against Scissors I want Rock. So any equilibrium has to be *mixed*.

**The best response condition.** \(\sigma\) is a best response to \(\tau\) if
and only if every action in the support of \(\sigma\) maximises the expected
payoff against \(\tau\). In words, every action I actually use has to be a best
response, so all of them give me the same expected payoff.

**The indifference equations.** With \(\sigma_c = (x, y, 1 - x - y)\),

\[
u_r(\text{Rock}, \sigma_c) = 1 - x - 2y, \qquad
u_r(\text{Paper}, \sigma_c) = 2x + y - 1, \qquad
u_r(\text{Scissors}, \sigma_c) = y - x.
\]

Setting the first equal to the third gives \(y = 1/3\), and the second equal to
the third gives \(x = 1/3\), so \(\sigma_c = (1/3, 1/3, 1/3)\) and all three
expected payoffs are \(0\).

**How much work.** Three actions have \(2^3 - 1 = 7\) non-empty supports each,
so \(7 \times 7 = 49\) pairs; five actions have \(31\) each and \(961\) pairs.
This is the answer to the discussion point above. It is worth adding that for a
non-degenerate game only pairs of *equal size* need checking, which is
\(\sum_k \binom{3}{k}^2 = 19\) pairs for three actions and \(251\) for five.
Either number makes the point that enumeration does not scale.

## From the activity to the exam answer

The activity above is written up as a marked exam question: **Question 1 (the in-class activity)** on the [Nash Equilibrium](/topics/nash-equilibrium.html) page, with a full worked solution. Closing the loop here is the step that helps students who find exams hard: work through that question together, or set it as the immediate follow-up, so they see the game they just played turned into a full-mark answer.
