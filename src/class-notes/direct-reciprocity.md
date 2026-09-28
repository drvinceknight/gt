---
layout: class-notes
title: "Direct Reciprocity"
tag: direct-reciprocity
---

## Activity (two classes: the IPD tournament runs long)

**Goal.** Surface the strategies students use when reciprocity is possible and
let a class-wide iterated Prisoner's Dilemma tournament motivate reactive
strategies. This activity is happy to run across two classes: the first to play
the tournament, the second to analyse the results.

**The deck.** There is a write-on deck at
[/decks/direct-reciprocity/main.pdf](/decks/direct-reciprocity/main.pdf),
covering both classes: a round-robin scoreboard, a row per team for its
strategy as a pair \((p, q)\), and an empty \(4 \times 4\) transition matrix.

**First class.** Watch the Golden Balls video. Then split the class into four
teams and run an iterated Prisoner's Dilemma tournament, each team submitting a
strategy that is played against every other team:

$$
A =
\begin{pmatrix}
3 & 0 \\
5 & 1
\end{pmatrix}
\qquad
B =
\begin{pmatrix}
3 & 5 \\
0 & 1
\end{pmatrix}
$$

Keep a running scoreboard and hand out a bribentive to the winning team.

**Second class.** Reveal the strategies each team played and rank them. Discuss
which did well and why, drawing out reciprocity, retaliation and forgiveness.
Ask each team to write their strategy as a reactive strategy $(p, q)$, where $p$
is the probability of cooperating after the opponent cooperated and $q$ after
they defected.

## Discussion (20 minutes)

Discuss the **Direct Reciprocity** chapter.

Discussion Point: **After the definition of a reactive strategy, ask students
to express the strategy their team played as a pair $(p, q)$.**

Discussion Point: **After the Markov chain of two reactive strategies, ask how
the long-run outcome of two teams' strategies could be computed.**

Discussion Point: **After discussing Tit For Tat, ask: the Folk Theorem tells
us cooperation can be sustained; what does this chapter add to that?**

## Answers for the deck

**The named strategies.** \((1, 1)\) is Always Cooperate, \((0, 0)\) is Always
Defect, \((1, 0)\) is Tit For Tat, and
\(\left(\tfrac{1}{2}, \tfrac{1}{2}\right)\) is Random.

**The Markov chain.** With \((p, q) = (4/5, 1/5)\) against
\((p', q') = (3/5, 1/10)\) and states ordered \((CC, CD, DC, DD)\), where the
first letter is mine, my next move depends on their last and theirs on my last:

\[
P = \begin{pmatrix}
12/25 & 8/25 & 3/25 & 2/25 \\
3/25 & 2/25 & 12/25 & 8/25 \\
2/25 & 18/25 & 1/50 & 9/50 \\
1/50 & 9/50 & 2/25 & 18/25
\end{pmatrix}
\]

Every row adds to one, which is the check to make as the class fills it in.

**The long run.** \(\pi = \tfrac{1}{245}(26, 65, 44, 110)\) satisfies
\(\pi P = \pi\). My long-run average payoff is
\(\pi \cdot (3, 0, 5, 1) = 408/245 \approx 1.67\) and theirs is
\(\pi \cdot (3, 5, 0, 1) = 513/245 \approx 2.09\). Mutual cooperation for ever
would have paid \(3\) each, so both teams lose by roughly a point a round to
their own retaliation.

**Why Tit For Tat needs care.** It is deterministic, so the chain it induces is
not ergodic: it can lock into a cycle and the stationary distribution is no
longer unique or independent of where you start. The usual fix is to perturb it
slightly, which is what a strategy like Generous Tit For Tat does.

## From the activity to the exam answer

The activity above is written up as a marked exam question: **Question 1 (the in-class activity)** on the [Direct Reciprocity](/topics/direct-reciprocity.html) page, with a full worked solution. Closing the loop here is the step that helps students who find exams hard: work through that question together, or set it as the immediate follow-up, so they see the game they just played turned into a full-mark answer.
