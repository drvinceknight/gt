---
layout: class-notes
title: "Rationalisation"
tag: rationalisation
---

## Activity (20 minutes)

**Goal.** Let students feel the best response logic before we formalise it.

**The deck.** There is a write-on deck at
[/decks/rationalisation/main.pdf](/decks/rationalisation/main.pdf). It carries
the game, a table for the six rounds played in pairs, and the three-mix table
that used to be a separate sheet, so nothing else needs printing.

Every slide of the deck names the numbered section of the notes it is reading,
and the last slide gathers them into one table, marks what is examinable and
sets the reading for the next class. The rules of the activity sit on the slide
that is up while the room plays, so a pair working alone is not going from
memory.

**First, in pairs.** Pair the students up and have them decide who is the row
player. They play matching pennies for six rounds, choosing at the same time,
and fill in every column: both actions, both payoffs and both running totals.
The payoffs are mirror images, so the table is easy to fill, and the pairs then
meet the asymmetric game we actually want against the dice.

**Then against the dice.** The row player is now a die with a known mix.
Before each roll a student commits to \(c_1\) or \(c_2\); then roll, read off
\(r_1\) or \(r_2\), and score. Six rounds for each of three mixes:

| Mix | \(r_1\) on a roll of |
|---|---|
| \(\sigma_1 = (1/4,\ 3/4)\) | 1 to 3 |
| \(\sigma_1 = (3/4,\ 1/4)\) | 1 to 9 |
| \(\sigma_1 = (1/3,\ 2/3)\) | 1 to 4 |

One D12 per pair covers all three, which is why the mixes are quarters and
thirds rather than the tenths we used to use. Twelfths divide exactly by both,
so each probability is exact rather than approximated. The three are chosen so
that one sits below the indifference point, one above it and one exactly on it,
which is the whole point of the exercise. Note that no single standard die can
produce \(0.2\) and \(0.9\) alongside \(1/3\): that would need a multiple of 30
faces.

Because the students roll their own dice, the mixes are printed on the deck
rather than hidden. The commitment still matters: they must write down their
\(c_1\) or \(c_2\) before each roll, so the running total is a fair test of the
reply they chose rather than of hindsight.

## Discussion (20 minutes)

Discuss the **Rationalisation** chapter.

Discussion Point: **After the definition of dominance, ask why dominance is not
relevant to the game we played.**

Discussion Point: **How does the best response condition apply to the matching
pennies game we played in class?**

**Close on the last slide.** It names what the class was reading and sets the
reading for next time. Then run the quick quiz from the [Nash Equilibrium topic
page](/topics/nash-equilibrium.html): five questions on the screen, answered by
a show of hands. It takes five minutes and tells us both what landed.

## Answers for the deck

Headings match the deck's page numbers, so this can sit open on a second screen
while the deck is projected.

**Page 2, the game.** Zero sum: every cell adds to \(0\). The action sets are
\(A_r = \{r_1, r_2\}\) and \(A_c = \{c_1, c_2\}\). If the row player picks
\(r_1\) and the column player \(c_2\), the column player scores \(+2\) and the
row player \(-2\).

**Page 3, matching pennies.** Zero sum again. Neither action is dominated, and
there is no equilibrium in pure actions, so anyone who always shows the same
thing loses to an opponent who notices. The equilibrium is both players mixing
\((1/2,\ 1/2)\), with value \(0\).

**Page 4, the dice.** One D12 per pair. The last entry in each \(\sum u_2\)
column is the six-round total to circle.

| Mix | \(r_1\) on | Best reply | Per round | Over six rounds |
|---|---|---|---|---|
| \((1/4,\ 3/4)\) | 1 to 3 | \(c_1\) | \(1/4\) | \(3/2\) |
| \((3/4,\ 1/4)\) | 1 to 9 | \(c_2\) | \(5/4\) | \(15/2\) |
| \((1/3,\ 2/3)\) | 1 to 4 | either | \(0\) | \(0\) |

**Page 5, working it out.** Against \(\sigma_1 = (p,\ 1 - p)\),

\[
u_2(c_1, \sigma_1) = 1 - 3p, \qquad u_2(c_2, \sigma_1) = 3p - 1.
\]

Plotted against \(p\), the two lines cross at \(p = 1/3\). Writing the column
player's mix as \(\sigma_2 = (x,\ 1 - x)\), the best response is \(x^* = 1\) when
\(p < 1/3\), \(x^* = 0\) when \(p > 1/3\), and any \(x\) at \(p = 1/3\). Neither
action is dominated, because which one is better depends on the mix: dominance
only rules out an action that is worse against *every* strategy of the opponent,
so the best response condition is what we need. The column player's own
indifferent mix is \((1/2,\ 1/2)\), which with the row player's \((1/3,\ 2/3)\)
is the Nash equilibrium; the value of the game is \(0\).

**What to watch for in the pairs rounds.** Nothing to compute here, so watch
instead for pairs who settle into one action and get punished for it, and for
pairs who start alternating. Name both in the debrief: the first shows why a
pure strategy is exploitable, the second is the room inventing mixed strategies
before we have defined them.

## From the activity to the exam answer

This activity feeds into the Nash equilibrium material. Use **Question 1 (the in-class activity)** on the [Nash Equilibrium](/topics/nash-equilibrium.html) page to show students how the ideas here become a full-mark exam answer.
