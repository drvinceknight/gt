---
layout: topic
title: "Repeated games"
tag: repeated-games
note_urls:
  - "https://vknight.org/gtb/chapters/repeated-games/"
---

## Example questions

The following are exam-type questions in the style of the examination paper.
**Each question is worth 25 marks.** Attempt them in full before reading the
worked solutions.

### Question 1 (based on the in-class activity)

In class we played "Will it end?": pairs played the contractor stage game

\[
A = \begin{pmatrix} 3 & 0 \\ 5 & 1 \end{pmatrix}
\]

(first action High, second action Low), and after each round rolled a die,
continuing unless a 1 was rolled, so the game continued with probability
\(\delta = 5/6\).

(a) Interpret \(\delta = 5/6\) and state the expected number of rounds. [3]

(b) Both players use the Grudger strategy (play High until the opponent
plays Low, then Low for ever). Holding the opponent's Grudger fixed, write down
the discounted payoff to a player who conforms and plays High in every round,
and to one who deviates to Low in the first round. [6]

(c) Determine whether mutual cooperation is sustained at \(\delta = 5/6\). [4]

(d) Find the smallest \(\delta\) for which cooperation is sustained, and hence
say whether our die made cooperation easy or hard to sustain. [5]

(e) Suppose the players replace Grudger with a forgiving trigger: a single Low
is punished by mutual Low for two rounds, after which both return to High.
Holding the opponent to this strategy, determine whether cooperation is
sustained with our die (\(\delta = 5/6\)). Find the smallest \(\delta\) for which
it is sustained, and compare with the Grudger threshold of part (d). [7]

### Question 2

(a) Provide definitions for the following terms:

- an infinitely repeated game with discounting;
- a strategy in a repeated game;
- the Grudger strategy;
- the average utility. [4]

(b) Two players repeatedly play the Prisoner's Dilemma with row-player stage
payoffs

\[
\begin{pmatrix}
3 & 0 \\
5 & 1
\end{pmatrix},
\]

cooperate first, defect second, infinitely repeated and discounted by
\(\delta \in (0, 1)\). Both use the Grudger strategy.

(i) Holding the opponent's Grudger fixed, write down the discounted payoff to
a player who conforms and cooperates in every round, and to one who defects in
the first round. [3]

(ii) Hence find the smallest \(\delta\) for which cooperation is sustained.
[3]

(iii) Show that Grudger is a subgame perfect equilibrium for \(\delta\)
above this threshold, by checking that no player can gain by deviating either
on the cooperative path or in the punishment phase. [5]

(c) State the Folk Theorem. [3]

(d) Define the individually rational payoff and state its value for this
Prisoner's Dilemma. [3]

(e) Explain what the Folk Theorem implies for cooperation in this game. [4]

### Question 3

(a) Define a subgame perfect equilibrium of a repeated game. [2]

(b) The Prisoner's Dilemma above is now repeated a finite and commonly known
number of times \(N\).

(i) Use backward induction to determine the subgame perfect equilibrium. [4]

(ii) Explain why cooperation cannot be sustained in any subgame perfect
equilibrium. [4]

(c) Explain why the backward-induction argument from part (b) does not apply
to an infinitely repeated Prisoner's Dilemma. [3]

(d) Return to the infinitely repeated game with Grudger, but with temptation
payoff \(T = 4\) in place of \(5\). Recompute the smallest \(\delta\) for which
cooperation is sustained. [4]

(e) Comment on how the threshold for \(\delta\) changes with the temptation
payoff. [3]

(f) With stage payoffs \(R = 3\), \(P = 1\), \(S = 0\) and general temptation
\(T\), show that the threshold is \(\delta^{*} = \dfrac{T - 3}{T - 1}\), and
state what happens to it as \(T\) grows. [5]

### Question 4 (**hard**)

Two players repeatedly play the Prisoner's Dilemma with stage payoffs \(R = 3\)
for mutual cooperation, \(T = 5\) for a unilateral defection, \(P = 1\) for mutual
defection and \(S = 0\) for being defected against, discounted by
\(\delta \in (0, 1)\). They use a forgiving trigger of length \(T\): both
cooperate until someone defects in a cooperative round, then both defect for
exactly \(T\) rounds, after which they return to cooperation and ignore the
deviation.

(a) Holding the opponent to this strategy, write down the discounted payoff to a
player who conforms and cooperates in every round, and to one who defects once in
the first round and is then punished. [4]

(b) Show that cooperation is sustained if and only if
\(2\delta - \delta^{\,T+1} \ge 1\). [8]

(c) Show that the resulting threshold \(\delta^{*}(T)\) is decreasing in \(T\), and
that as \(T \to \infty\) it tends to \(\tfrac{1}{2}\), the grim-trigger
threshold. [6]

(d) Prove that, for \(\delta\) above the threshold, the forgiving trigger is a
subgame perfect equilibrium, by checking with the one-shot deviation principle
that no player can gain from a single deviation on the cooperative path or during
the punishment phase. [7]

## Optional further reading

You do not need any of this to follow the topic, but the following chapters of
the textbook may help if you would like more background:

- [Direct Reciprocity](https://vknight.org/gtb/chapters/direct-reciprocity/),
  which applies repeated play to the iterated Prisoner's Dilemma and reactive
  strategies.
- [Subgame Perfection](https://vknight.org/gtb/chapters/subgame-perfection/),
  which refines the equilibria that survive in a repeated interaction.
