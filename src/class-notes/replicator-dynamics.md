---
layout: class-notes
title: "Replicator Dynamics"
tag: "replicator-dynamics"
---

## Activity (20 minutes)

**Goal.** Build the replicator equation from a physical process and watch a
population converge to a stable rest point, so that frequency-dependent
selection is felt before the equation is written down.

**The room is a population.** Each student is one individual playing the
**snowdrift game**: two drivers meet at a snowdrift blocking the road and each
chooses to **Dig** or **Stay**. Clearing the drift is worth 4 to each driver;
digging costs 2, shared if both dig. With actions ordered (Dig, Stay) the row
player's payoffs are

$$
A = \begin{pmatrix} 3 & 2 \\ 4 & 0 \end{pmatrix}
$$

so two diggers get 3 each, a lone digger gets 2 while the stayer free-rides for
4, and two stayers get 0.

Run it as follows:

1. Every student picks Dig or Stay and stands on the corresponding side of the
   room. Record the fraction $x$ on the Dig side.
2. With the current split, compute each side's fitness:
   $f_D = 3x + 2(1 - x)$ and $f_S = 4x$. Read off which side is doing better.
3. **Evolutionary step.** Lob a few small bribentives to the higher-fitness
   side, then move a small fixed number of students (say two or three) from the
   lower-fitness side to the higher-fitness side. Record the new $x$.
4. Repeat for several rounds, plotting $x$ against the round on the board.

Rewarding the fitter side each round makes the pull towards it tangible and
gives students a reason to switch. Whatever the starting split, the population
settles near $x = 2/3$, where $f_D = f_S$.

**Debrief.** Draw out the equation from what they saw:

- A strategy that is doing well but is **rare** grows only slowly, because few
  individuals play it to begin with; a strategy that is doing well and is
  **common** grows fast. The number that switch is proportional to how many
  already play it ($x$) times how far above average its fitness is
  ($f - \phi$). That is exactly $\dot{x} = x(f - \phi)$.
- Each round, with a small step, is one step of **Euler's method** on the
  replicator equation; shrinking the step traces the continuous trajectory.
  This is the link to the numerical integration reading.
- Contrast briefly with Rock-Paper-Scissors, where the same dynamics never
  settle but cycle: a useful caution that a rest point is not always reached.

## Discussion (20 minutes)

Work through the Replicator Dynamics chapter.

Discussion Point: **After the definition of the replicator dynamics equation,
ask how this differs from our example?**

Discussion Point: **After the definition of an ESS, ask whether the rest point
$x = 2/3$ from our snowdrift game is an ESS, and contrast it with the
Rock-Paper-Scissors equilibrium, which is not.**

Discussion Point: **After the characterisation of the ESS theorem ask how we
could use this to find the ESS for the replicator dynamics equation?**

## From the activity to the exam answer

The activity above is written up as a marked exam question: **Question 1 (the in-class activity)** on the [Replicator Dynamics](/topics/replicator-dynamics.html) page, with a full worked solution. Closing the loop here is the step that helps students who find exams hard: work through that question together, or set it as the immediate follow-up, so they see the game they just played turned into a full-mark answer.
