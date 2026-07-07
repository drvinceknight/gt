---
layout: class-notes
title: "Repeated Games"
tag: repeated-games
---

## Activity (20 minutes)

**Goal.** Make the shadow of the future tangible: introduce repeated play and
the discount factor as the probability that the game continues, before we
formalise any of it.

Run "Will it end?". Students pair off. In each round both players secretly
choose to bid **High** or **Low** for a contract, using the stage game

$$
A =
\begin{pmatrix}
3 & 0 \\
5 & 1
\end{pmatrix}
$$

where the first action is High (cooperate) and the second is Low (undercut).
After every round the pair rolls a die: on a 1 the repeated game ends, otherwise
it continues to another round. So the game continues with probability
$\delta = 5/6$. Players keep a running total.

Run it a couple of times. Some pairs stop after one round, others run long. Then
hand out a bribentive to the podium, the three individual students with the
highest average score per round, and ask:

- Did you play differently knowing the game might continue?
- Would you bid High in a round you knew for certain was the last?
- Now end the game on a 1 **or** a 2 (so $\delta = 4/6$) and replay. Does a
  shorter expected future change how willing you are to cooperate?

**Debrief.** Connect their experience to the chapter: $\delta$ is the
probability the game does not end, the expected number of rounds is
$1/(1 - \delta)$, and cooperation is easier to sustain when $\delta$ is large.
Contrast this with a game of a fixed, commonly known length, where backward
induction unravels cooperation from the last round.

## Discussion (20 minutes)

Discuss the **Repeated Games** chapter.

Discussion Point: **After the definition of a strategy in a repeated game, ask
what a strategy looked like in our dice game, given the history of play.**

Discussion Point: **After the definition of an infinitely repeated game with
discounting, ask how our die roll corresponds to $\delta$.**

Discussion Point: **After the Folk Theorem, ask what it means for cooperation
in the contractor game and more generally.**

Discussion Point: **After the finite-horizon discussion, ask why backward
induction kills cooperation when the number of rounds is known in advance.**

## From the activity to the exam answer

The activity above is written up as a marked exam question: **Question 1 (the in-class activity)** on the [Repeated games](/topics/repeated-games.html) page, with a full worked solution. Closing the loop here is the step that helps students who find exams hard: work through that question together, or set it as the immediate follow-up, so they see the game they just played turned into a full-mark answer.
