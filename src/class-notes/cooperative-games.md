---
layout: class-notes
title: "Cooperative Games"
tag: "cooperative-games"
---

## Activity (30 minutes)

**Goal.** Motivate fair division and the question the Shapley value answers: a
team produces one thing together, the parts reinforce each other, and we have to
split the proceeds fairly when the parts did not contribute equally.

**The deck.** There is a write-on deck at
[/decks/cooperative-games/main.pdf](/decks/cooperative-games/main.pdf): the
seven coalition scores as boxes to fill in as the class calls them out, then the
six orderings as a table of marginal contributions.

Run "The revision aid". The whole room plays at once in teams of three (about
twenty teams in a class of sixty). In roughly twelve minutes each team makes a
one-page revision aid for a game theory topic, on a single poster with three
clearly separated parts, one per student:

- the Theorist writes the maths: the key definitions and a worked example;
- the Artist draws the picture: a payoff matrix, a game tree or a plot;
- the Storyteller tells the story: the plain-English intuition or a memorable scenario.

Set the same topic for a fair contest, or give each team a different topic so the
gallery ends up covering the syllabus.

Put every poster on the wall. The class is the market: each student walks the
gallery and places one vote on the aid they would most want to revise from, but
not their own. The aid with the most votes wins, and its team takes the
bribentive. Photograph the winners and share them: they are real revision
material for the class.

Now the part that makes it a cooperative game. Take the winning aid and split its
prize fairly among the three students by the Shapley value, with the
characteristic function supplied live by the class. Cover the poster and reveal
the parts in combination, asking the class to score what is on show out of ten:

- each part on its own (the maths; the picture; the story);
- each pair of parts;
- the whole aid, anchored at ten so the rest are judged against it.

These seven numbers are the worth of each coalition of the three students, and
they are not additive: a picture on its own is a cryptic diagram, but beside the
maths and a plain-English story it makes the topic click. Write them on the
board, compute the Shapley value, and hand out the bribentive in those shares.

**Debrief.** The three parts are worth only a few points on their own, yet the
whole aid scores ten, so most of the value comes from the parts reinforcing one
another. The Shapley value is what shares that synergy fairly: it pays each
student the average value their part adds over every order in which the aid could
come together, so the part that combines best with the others is rewarded most,
above what it is worth alone. This is exactly Question 1, now with numbers the
class produced.

## Discussion (20 minutes)

Work through the Cooperative Games chapter.

Discussion Point: **After the definition of a characteristic function game, point
out that the seven scores the class gave are exactly the characteristic
function.**

Discussion Point: **After the definition of marginal contribution, ask how much
the maths is worth on its own and how much it adds once the picture and story are
already there; the same part contributes more in company.**

Discussion Point: **After the definition of the Shapley value, ask for the steps,
then work through the six orderings for the winning aid.**

## Answers for the deck

The seven scores come from the class. These are the answers for the example on
the exam page, where \(v(\{1\}) = 2\), \(v(\{2\}) = 1\), \(v(\{3\}) = 2\),
\(v(\{1,2\}) = 5\), \(v(\{1,3\}) = 6\), \(v(\{2,3\}) = 4\) and
\(v(\{1,2,3\}) = 10\), with 1 the maths, 2 the picture and 3 the story.

| Order | Maths adds | Picture adds | Story adds |
|---|---|---|---|
| maths, picture, story | 2 | 3 | 5 |
| maths, story, picture | 2 | 4 | 4 |
| picture, maths, story | 4 | 1 | 5 |
| picture, story, maths | 6 | 1 | 3 |
| story, maths, picture | 4 | 4 | 2 |
| story, picture, maths | 6 | 2 | 2 |
| **Average** | **4** | **5/2** | **7/2** |

**The Shapley value** is therefore \((4, \; 5/2, \; 7/2)\). It adds to 10, the
worth of the whole aid, which is efficiency.

**The synergy.** The three parts are worth \(2 + 1 + 2 = 5\) on their own, so
half of the aid's value comes from the parts reinforcing one another. Each
student is paid more than their part alone: the maths gains 2, and the picture
and the story gain \(3/2\) each. The maths gains most because it combines best
with the other two, not because it scores highest by itself.

## From the activity to the exam answer

The activity above is written up as a marked exam question: **Question 1 (the in-class activity)** on the [Cooperative Games](/topics/cooperative-games.html) page, with a full worked solution. Closing the loop here is the step that helps students who find exams hard: work through that question together, or set it as the immediate follow-up, so they see the game they just played turned into a full-mark answer.
