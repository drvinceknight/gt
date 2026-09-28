---
layout: class-notes
title: "Matching Games"
tags:
  - matching-games
---

## Activity (20 minutes)

**Goal.** Elicit preferences and motivate the need for a stable matching.

**The deck.** There is a write-on deck at
[/decks/matching-games/main.pdf](/decks/matching-games/main.pdf): the
preference lists waiting to be filled in, then four copies of the bipartite
diagram so each round of proposals can be drawn on top of the last.

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

## Answers for the deck

**A blocking pair.** Any pairing the class writes down will do, but if they need
prompting: pair Gauss with Curie, Noether with Newton, Turing with Einstein and
Euler with Feynman. Then Noether and Curie block it, since Noether has her worst
physicist and prefers Curie, and Curie has her worst mathematician and prefers
Noether.

**Deferred acceptance, with the mathematicians proposing.** It takes four
rounds, which is why there are four diagrams:

1. Gauss and Noether both propose to Curie, Turing to Feynman, Euler to Newton.
   Curie holds Noether and rejects Gauss.
2. Gauss proposes to Newton. Newton prefers Gauss, so holds Gauss and rejects
   Euler.
3. Euler proposes to Curie. Curie still prefers Noether, so rejects Euler.
4. Euler proposes to Einstein, who holds him.

**The matching.** Gauss with Newton, Noether with Curie, Turing with Feynman,
Euler with Einstein. It is stable: there is no blocking pair. Gauss would rather
have Curie, but Curie has Noether and prefers her; Euler would rather have
Newton or Curie, but both prefer who they already have.

**Who does better.** The proposers. Deferred acceptance returns the
suitor-optimal stable matching, so every mathematician gets the best physicist
they could have in *any* stable matching, and every physicist the worst.

## From the activity to the exam answer

The activity above is written up as a marked exam question: **Question 1 (the in-class activity)** on the [Matching Games](/topics/matching-games.html) page, with a full worked solution. Closing the loop here is the step that helps students who find exams hard: work through that question together, or set it as the immediate follow-up, so they see the game they just played turned into a full-mark answer.
