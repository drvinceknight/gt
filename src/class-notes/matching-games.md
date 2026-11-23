---
layout: class-notes
title: "Matching Games"
tags:
  - matching-games
---

## Activity (20 minutes)

**Goal.** Motivate the need for a stable matching, then find one with the
Gale-Shapley algorithm, run once together and once by the students.

**The deck.** There is a write-on deck at
[/decks/matching-games/main.pdf](/decks/matching-games/main.pdf): the people,
their rankings, a page for one pair's matching, a single diagram with each
person's ranking under them for the mathematicians proposing (write each round
on it and erase the rejections), the algorithm written out, and a
self-contained page for the students to run it with the physicists proposing.

Every slide of the deck names the numbered section of the notes it is reading,
and the last slide gathers them into one table, marks what is examinable and
sets the reading for the next class. The rules of the activity sit on the slide
that is up while the room plays, so a pair working alone is not going from
memory.

Slides 2 and 3 introduce the four mathematicians and the four physicists in
words: what each person is like, what they look for in a collaborator and what
puts them off. Slides 4 to 19 then take one person at a time: their card on the
left and the four people on the other side on the right, then the same page
again with that person's ranking revealed. Ask the room to guess the order
before moving on; the class does not work out the rankings, which takes too
long, but each one should feel earned. The same descriptions are on
[this preference sheet](/assets/activities/matching-scientists/main.pdf) for
anyone who wants a copy on paper.

Slide 20 gathers the rankings, and the room's task is to use them. In pairs, the
students match every mathematician with a physicist, aiming for a matching that
nobody would walk away from. Slide 21 takes one pair's matching and asks for a
blocking pair. Then work through the algorithm with the mathematicians
proposing on slide 22, a single diagram with every ranking under its person
that is written on and erased round by round, and check the result on slide
23. Slide 24 writes the algorithm down, and slide 25 is for the students: it
carries the algorithm and the same diagram, so they can run it with the
physicists proposing without turning back. Slide 26 lists every person's
ranking beside their partner in each matching and how far down the ranking
that partner is, which makes it plain who gains from proposing.

The rankings are:

**Mathematicians**

- Gauss: Curie > Newton > Einstein > Feynman
- Noether: Feynman > Einstein > Curie > Newton
- Turing: Einstein > Feynman > Newton > Curie
- Euler: Feynman > Einstein > Curie > Newton

**Physicists**

- Einstein: Noether > Turing > Gauss > Euler
- Curie: Noether > Turing > Gauss > Euler
- Newton: Gauss > Turing > Euler > Noether
- Feynman: Euler > Noether > Turing > Gauss

These rankings have two stable matchings, which is what
lets the last part of the deck show that the proposing side does better.

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

gauss.set_prefs([curie, newton, einstein, feynman])
noether.set_prefs([feynman, einstein, curie, newton])
turing.set_prefs([einstein, feynman, newton, curie])
euler.set_prefs([feynman, einstein, curie, newton])

einstein.set_prefs([noether, turing, gauss, euler])
curie.set_prefs([noether, turing, gauss, euler])
newton.set_prefs([gauss, turing, euler, noether])
feynman.set_prefs([euler, noether, turing, gauss])

game = matching.games.StableMarriage(mathematicians, physicists)
game.solve()

```

## Discussion (20 minutes)

Show students the notes, when you get to the algorithm work through the
algorithm with the students.

**Close on the last slide.** It names what the class was reading and sets the
reading for next time. Then run the quick quiz from the [Matching Games topic
page](/topics/matching-games.html): five questions on the screen, answered by a
show of hands. It takes five minutes and tells us both what landed.

## Answers for the deck

Slide 5 writes the rankings as the maps \(f : S \to R^4\) and
\(g : R \to S^4\), with the mathematicians as suitors and the physicists as
reviewers, which is the form Question 1(a) asks for.

**A blocking pair.** Any pairing the class writes down will do, but if they need
prompting: pair Gauss with Curie, Noether with Newton, Turing with Einstein and
Euler with Feynman. Then Noether and Einstein block it, since Noether has her
worst physicist and prefers Einstein, and Einstein has his second choice and
prefers Noether.

**Deferred acceptance, with the mathematicians proposing.** It takes four
rounds, all drawn on the one diagram:

1. Gauss proposes to Curie, Noether and Euler both to Feynman, Turing to
   Einstein. Feynman holds Euler and rejects Noether.
2. Noether proposes to Einstein. Einstein prefers Noether, so holds her and
   rejects Turing.
3. Turing proposes to Feynman. Feynman still prefers Euler, so rejects Turing.
4. Turing proposes to Newton, who holds him.

**The matching.** Gauss with Curie, Noether with Einstein, Turing with Newton,
Euler with Feynman. It is stable: there is no blocking pair. Gauss and Euler
have their first choice. Noether would rather have Feynman, but Feynman prefers
Euler. Turing would rather have Einstein or Feynman, but each prefers who they
hold.

**The physicists propose.** Two rounds. Einstein and Curie both propose to
Noether, Newton to Gauss and Feynman to Euler; Noether holds Einstein and
rejects Curie. Curie then proposes to Turing, who holds her. The matching is
Gauss with Newton, Noether with Einstein, Turing with Curie and Euler with
Feynman, which is also stable.

**Who does better.** The proposers. Gauss gets Curie, his first choice, when
the mathematicians propose, and Newton, his second, when the physicists do.
Turing gets his third choice rather than his fourth. Newton and Curie gain in
the opposite direction. Deferred acceptance returns the suitor-optimal stable
matching, so every suitor gets the best partner they could have in *any*
stable matching, and every reviewer the worst.

## From the activity to the exam answer

The activity above is written up as a marked exam question: **Question 1 (the in-class activity)** on the [Matching Games](/topics/matching-games.html) page, with a full worked solution. Closing the loop here is the step that helps students who find exams hard: work through that question together, or set it as the immediate follow-up, so they see the game they just played turned into a full-mark answer.
