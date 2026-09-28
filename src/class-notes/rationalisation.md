---
layout: class-notes
title: "Rationalisation"
tag: rationalisation
---

## Activity (20 minutes)

**Goal.** Let students feel the best response logic before we formalise it.

**The deck.** There is a write-on deck at
[/decks/rationalisation/main.pdf](/decks/rationalisation/main.pdf): the game
printed once, a table for what each pair committed to against each mix, and the
expected payoffs laid out with the working left blank.

Use [best responses](/assets/activities/best_responses/main.pdf) and have
students play against a mixed strategy. Before revealing how the opponent
plays, ask each pair to guess the opponent's mix and to commit to a response.
Then play against the actual mixed strategy:

    >>> import random
    >>> random.seed(0)  # Don't seed in class
    >>> ["r_2", "r_1"][random.random() < 0.8]  # 80 percent chance of r_2
    'r_2'

Compare the responses students committed to with the best response to the
revealed mix.

## Discussion (20 minutes)

Discuss the **Rationalisation** chapter.

Discussion Point: **After the definition of dominance, ask why dominance is not
relevant to the game we played.**

Discussion Point: **How does the best response condition apply to the matching
pennies game we played in class?**

## Answers for the deck

**The game.** Every cell of \(A\) and \(B\) adds to zero, so it is zero sum.

**The best responses.** Against \(\sigma_1 = (p, 1 - p)\) your two actions pay

\[
u_2(c_1, \sigma_1) = 1 - 3p, \qquad u_2(c_2, \sigma_1) = 3p - 1,
\]

so \(c_1\) is better exactly when \(p < 1/3\), and the two are equal at
\(p = 1/3\). The three mixes we play therefore give:

| The row player's mix | Best response | Your payoff |
|---|---|---|
| \((0.2,\ 0.8)\) | \(c_1\) | \(0.4\) |
| \((0.9,\ 0.1)\) | \(c_2\) | \(1.7\) |
| \((1/3,\ 2/3)\) | either | \(0\) |

The third one is chosen deliberately: it is the mix that makes you indifferent,
so nothing you do can beat it.

**Why dominance was no help.** Neither of your actions dominates the other,
since \(c_1\) is better for \(p < 1/3\) and \(c_2\) for \(p > 1/3\). Dominance
only rules out an action that is worse against *every* strategy of the opponent.
Both of yours are a best response to something, so we need the best response
condition instead.

**Closing the loop.** Your mix that makes the row player indifferent is
\((1/2, 1/2)\): it gives them \(0\) whichever row they pick. Together with their
\((1/3, 2/3)\) that is the Nash equilibrium of this game, and its value is
\(0\).

## From the activity to the exam answer

This activity feeds into the Nash equilibrium material. Use **Question 1 (the in-class activity)** on the [Nash Equilibrium](/topics/nash-equilibrium.html) page to show students how the ideas here become a full-mark exam answer.
