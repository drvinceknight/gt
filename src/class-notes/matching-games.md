---
layout: class-notes
title: "Matching Games"
tags:
  - matching-games
---

## Activity (20 minutes)

**Goal.** Elicit preferences and motivate the need for a stable matching.

Use [this preference sheet](/assets/activities/matching-scientists/main.pdf) and
ask students to work in groups to identify preferences for each mathematician and
physicist.

Arrive at this:

**Mathematicians**

- Gauss: Curie > Newton > Feynman > Einstein
- Noether: Curie > Feynman > Einstein > Newton
- Turing: Feynman > Curie > Einstein > Newton
- Euler: Newton > Curie > Einstein > Feynman

**Physicists**

- Einstein: Noether > Gauss > Turing > Euler
- Curie: Noether > Euler > Turing > Gauss
- Newton: Gauss > Euler > Noether > Turing
- Feynman: Turing > Noether > Gauss > Euler

The following will obtain a stable matching:

```python

import matching
import matching.games

mathematicians = [
    matching.Player("Gauss"),
    matching.Player("Noether"),
    matching.Player("Turing"),
    matching.Player("Euler"),
]

physicists = [
    matching.Player("Einstein"),
    matching.Player("Curie"),
    matching.Player("Newton"),
    matching.Player("Feynman"),
]

gauss, noether, turing, euler = mathematicians
einstein, curie, newton, feynman = physicists

gauss.set_prefs([curie, newton, feynman, einstein])
noether.set_prefs([curie, feynman, einstein, newton])
turing.set_prefs([feynman, curie, einstein, newton])
euler.set_prefs([newton, curie, einstein, feynman])

einstein.set_prefs([noether, gauss, turing, euler])
curie.set_prefs([noether, euler, turing, gauss])
newton.set_prefs([gauss, euler, noether, turing])
feynman.set_prefs([turing, noether, gauss, euler])

game = matching.games.StableMarriage(mathematicians, physicists)
game.solve()

```

## Discussion (20 minutes)

Show students the notes, when you get to the algorithm work through the
algorithm with the students.

## From the activity to the exam answer

The activity above is written up as a marked exam question: **Question 1 (the in-class activity)** on the [Matching Games](/topics/matching-games.html) page, with a full worked solution. Closing the loop here is the step that helps students who find exams hard: work through that question together, or set it as the immediate follow-up, so they see the game they just played turned into a full-mark answer.
