---
layout: class-notes
title: "Matching Games"
tags:
  - matching-games
---

## Activity (20 minutes)

Use [this preference sheet]({{site.baseurl}}/assets/activities/matching-scientists/main.pdf) and ask students to work in groups to 
identify preferences for each mathematician and physicist.

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

