---
layout: class-notes
title: "Rationalisation"
tag: rationalisation
---

## Activity (20 minutes)

**Goal.** Let students feel the best response logic before we formalise it.

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

## From the activity to the exam answer

This activity feeds into the Nash equilibrium material. Use **Question 1 (the in-class activity)** on the [Nash Equilibrium](/topics/nash-equilibrium.html) page to show students how the ideas here become a full-mark exam answer.
