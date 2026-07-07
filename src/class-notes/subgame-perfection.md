---
layout: class-notes
title: "Subgame Perfection"
tag: subgame-perfection
---

This topic runs over **two classes**. The first class is the Traitors activity
and its debrief; the second class is the formal discussion of the chapter and
the worked exam question. The activity is the spine of both, so we set it out in
full.

## Activity: the Traitors (one class)

**Goal.** Show that a plan of action can look like an equilibrium at the start of
a game yet stop being optimal once a particular subgame is reached. This is the
gap between a Nash equilibrium of the whole game and one that is optimal in every
subgame, and it motivates subgame perfection.

We play the game three times: first with no guidance, then with a prescribed
voting rule, and finally with the rule in place but players free to break it for
fun. The contrast between the runs is the whole point, so leave time for all
three.

**Setup and numbers.** Deal a hidden role to every student: a small number are
Traitors, the rest are Faithful. Only the Traitors learn who the other Traitors
are. Seat the group in a fixed circle and keep that ordering for the whole game.
A clean default is **ten players with two Traitors**. The reason for this
particular count is worth knowing. Each round removes two players, one banished
by the day vote and one murdered at night, so the state \((n, m)\) (with \(n\)
players and \(m\) Traitors) loses two players a round. The Traitors win the moment
they reach parity, \(2m \ge n\); the Faithful win once every Traitor has been
banished. Starting from \((10, 2)\) the game runs

\[
(10, 2) \to (8, 2) \to (6, 2) \to (4, 2),
\]

reaching parity in **three rounds** if no Traitor is banished along the way, and
on average a little under four rounds once the random tie-break is taken into
account. That is short enough to play twice in a class. For a larger room, keep
two compliance rounds before the endgame by choosing \(n \approx 2m + 6\), so
three Traitors wants twelve players and four Traitors wants fourteen. This uses
more Traitors per head than the television show, which is deliberate: with the
show's ratio the interesting endgame is never reached inside a class.

Each round has two phases:

- *Night:* the Traitors silently agree on one Faithful to remove.
- *Day:* the group votes, and the most-voted player is banished, with ties broken
  at random and the banished player's role revealed.

**First game: no instruction.** Deal the roles, explain only the two phases and
the win conditions, and say nothing about how to vote. Let the group vote however
it likes. With free voting the Traitors collude covertly, and that collusion is
statistically indistinguishable from ordinary disagreement, so it usually goes
unpunished and the Traitors tend to win. Keep this run short, one or two rounds
is enough to make the point: the Faithful have no way to detect coordination.

**Second game: the Vote-Left rule.** Reset and deal fresh roles. Now prescribe a
rule: every player votes for the next surviving player to their left in the
circle. Two properties are worth drawing out by hand.

- *It is as fair as random voting.* Under full compliance every player receives
  exactly one vote, so the banishment is uniform, exactly the \(1/n\) chance a
  random vote would give.
- *It makes deviation visible.* Because each prescribed vote is a fixed function
  of public information, any departure from it is immediately and publicly
  identifiable. If a Traitor concentrates their vote, one player receives two
  votes and another receives none, and everyone can see who broke the rule.

Pair the rule with a punishment: a player seen to deviate is banished next.
While there are enough Faithful to carry out that punishment, complying with
Vote-Left is a best response for everyone, Faithful and Traitor alike, since a
detected deviation leads to certain banishment and a winning probability of zero.

**The endgame, and the deviation.** Play the second game on towards its end and
watch for the state \((6, 2)\), where \(n = 2m + 2\). From here a Traitor who
deviates is detected, but after the following night murder there are no longer
enough Faithful to outvote and banish them. The punishment threat has stopped
being credible, and the Traitors' best response flips: they should now collude
openly, banish a Faithful, and reach parity. This is the moment to pause. The
Traitors' colluding move is the optimal action *in that subgame*, and it is a
well-defined best response there whether or not any particular game actually
reaches it. That is exactly what subgame perfection asks of a strategy: it must
prescribe an optimal action at every subgame, including ones never reached in a
given play.

**Third game: when you are not sure.** Reset once more and keep the Vote-Left
rule, but now tell the group that anyone may break it now and then for fun, with
no warning. Reintroducing this noise undoes what Vote-Left bought us. A vote that
breaks the rule no longer points to a Traitor, since a Faithful might simply be
playing around, so the Faithful can no longer be sure who, if anyone, is
colluding. Let \(q\) be the Faithful's belief that a flagged suspect really is the Traitor.
Banishing a suspect becomes a gamble: with probability \(q\) it removes the
Traitor, and with probability \(1 - q\) it removes one of their own. When \(q\) is
low the threat to banish on suspicion is empty, because carrying it out is as
likely to cost the Faithful a friend as to catch a Traitor, and the Traitors
exploit exactly this. This is the game written up as the marked exam question
below, where the threshold on \(q\) is worked out in full.

**Debrief.** Three threads to pull together.

First, a rule that makes deviation visible is what turns the Faithful's threat
into a credible one. With free voting the Traitors' collusion is indistinguishable
from disagreement, so the threat to punish is empty; under Vote-Left a deviation
is unmistakable, so the threat bites and the Traitors comply.

Second, even Vote-Left has a limit. The punishment is credible early and not
credible late: with many Faithful left, "deviate and you will be banished" is a
real deterrent, but in the endgame the Faithful can no longer carry it out. Draw
the partial game tree for the last couple of rounds and circle the subgame at
\((6, 2)\) where the Traitors' best response changes.

Third, the rule's bite depends on being sure. Once players break Vote-Left for
fun, a flagged suspect is the Traitor only with some probability \(q\), and a
threat to banish on suspicion is non-credible when \(q\) is low. This is the same
picture as the marked exam question below: a plan can be a Nash equilibrium of the
whole game while relying on an action, banishing a suspect, that is not a best
response once its subgame is reached.

**A note for the curious.** The Vote-Left rule, the threshold \(n > 2m + 2\) for
its credibility, and the Traitors' optimal endgame deviation are worked out in
full in Knight, *The Vote-Left Equilibrium: A Deterministic Coordination Strategy
for the Faithful in The Traitors*, [arXiv:2605.10233](https://arxiv.org/abs/2605.10233).
The paper shows that Vote-Left is a Perfect Bayesian Equilibrium for every state
with \(n > 2m + 2\), and that it roughly triples the Faithful's winning
probability over random voting when the Traitors collude. None of this is
examinable; it is here for anyone who wants to see where the activity comes from.

## Discussion and worked question (one class)

The second class formalises the activity. Discuss the **Subgame Perfection**
chapter.

Work through the centipede game as the formal worked example of backwards
induction:

- Player 1 can take or pass (if take: (2, 0))
    - Player 2 can take or pass (if take: (1, 3))
        - Player 1 can take or pass (if take: (4, 2))
            - Player 2 can take or pass (if take: (3, 5))
                - Leaf: (4, 4)

Solve it by backwards induction, then contrast the subgame perfect equilibrium
with the strategy that passes at the first two nodes and takes at the last two.

Discussion point: **After the definition of backwards induction, ask what it
leads to for the centipede game.**

Discussion point: **After the subgame perfection definition, ask which
equilibrium is subgame perfect, and relate it to the Traitors punishment threat
that was credible early and failed in the endgame subgame.**

## From the activity to the exam answer

The third game above is written up as a marked exam question: **Question 1 (the in-class activity)** on the [Subgame Perfection](/topics/subgame-perfection.html) page, with a full worked solution. Closing the loop here is the step that helps students who find exams hard: work through that question together, or set it as the immediate follow-up, so they see the game they just played turned into a full-mark answer.
