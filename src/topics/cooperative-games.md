---
layout: topic
title: "Cooperative Games"
tag: cooperative-games
note_urls:
  - "https://vknight.org/gtb/chapters/cooperative-games/"
---

## Example questions

The following are exam-type questions in the style of the examination paper.
**Each question is worth 25 marks.** Attempt them in full before reading the
worked solutions.

### Question 1 (based on the in-class activity)

In the revision-aid activity, three students make a one-page aid for a game
theory topic: the Theorist does the maths, the definitions and a worked example
(player 1); the Artist draws the picture, a diagram (player 2); and the
Storyteller writes the story, the plain-English intuition (player 3). The class
scored the winning aid out of ten
for each combination of the parts on show, giving a
characteristic function game on \(N = \{1, 2, 3\}\) with \(v(\emptyset) = 0\),
\(v(\{1\}) = 2\), \(v(\{2\}) = 1\), \(v(\{3\}) = 2\), \(v(\{1, 2\}) = 5\),
\(v(\{1, 3\}) = 6\), \(v(\{2, 3\}) = 4\) and \(v(\{1, 2, 3\}) = 10\).

(a) Define a characteristic function game and the Shapley value. [5]

(b) Compute the marginal contribution of each player in each of the six
orderings of the players. [8]

(c) Hence compute the Shapley value. [6]

(d) Verify that the Shapley value is efficient, and interpret the result: the
three parts are worth only \(2 + 1 + 2 = 5\) on their own, so half of the aid's
value comes from the parts reinforcing one another. Explain how the Shapley value
shares this synergy. [6]

### Question 2

(a) Provide definitions for the following terms:

   - a characteristic function game \(G = (N, v)\);
   - a payoff vector;
   - the marginal contribution of a player to a coalition;
   - the Shapley value. [5]

(b) Consider the game on \(N = \{1, 2, 3\}\) with \(v(\emptyset) = 0\),
\(v(\{1\}) = v(\{2\}) = v(\{3\}) = 0\), \(v(\{1, 2\}) = 90\),
\(v(\{1, 3\}) = 80\), \(v(\{2, 3\}) = 70\), \(v(\{1, 2, 3\}) = 120\).

   (i) Compute the marginal contribution vector for each of the six orderings of
   the players. [5]

   (ii) Hence compute the Shapley value. [6]

   (iii) Verify that the Shapley value is efficient. [3]

(c) Explain what the Shapley value represents, and state which of its defining
properties (efficiency, null player, symmetry, additivity) justify calling it a
fair division. [6]

### Question 3

(a) State the efficiency, null player, symmetry and additivity properties of the
Shapley value. [6]

(b) Consider the game on \(N = \{1, 2, 3\}\) with \(v(S) = 1\) if \(|S| \ge 2\)
and \(v(S) = 0\) otherwise.

   (i) Using symmetry and efficiency, write down the Shapley value. [4]

   (ii) State, with reason, whether any player is a null player. [2]

(c) Consider the game on \(N = \{1, 2, 3\}\) with \(v(S) = 4\) if
\(\{1, 2\} \subseteq S\) and \(v(S) = 0\) otherwise.

   (i) Identify the null player. [3]

   (ii) Compute the Shapley value using the six orderings. [5]

   (iii) Verify efficiency, confirm that players 1 and 2 are symmetric and receive
   equal payoffs, and interpret the result. [5]

### Question 4 (**hard**)

This question uses the additivity of the Shapley value to compute it without
summing over all orderings.

(a) State the additivity property of the Shapley value, and explain what the sum
\(v + w\) of two characteristic function games on the same player set means. [4]

(b) For a non-empty coalition \(T \subseteq N\), the unanimity game \(u_T\) is
defined by \(u_T(S) = 1\) if \(T \subseteq S\) and \(u_T(S) = 0\) otherwise. Using
the symmetry, null player and efficiency properties, show that the Shapley value
of \(u_T\) gives \(1/|T|\) to each member of \(T\) and \(0\) to every other
player. [6]

(c) Consider the game on \(N = \{1, 2, 3\}\) given by
\(v = 2\, u_{\{1,2\}} + 3\, u_{\{1,2,3\}}\). Write down \(v(S)\) for every
coalition \(S\), and use additivity with part (b) to compute the Shapley value.
Verify that it is efficient. [9]

(d) Explain how the decomposition into unanimity games shows where each player's
share comes from, and why additivity is a useful shortcut compared with summing
marginal contributions over all \(n!\) orderings. [6]

## Optional further reading

You do not need this to follow the topic, but the chapter on
[The Core](https://vknight.org/gtb/chapters/the-core/) may help if you would like
more background on stable allocations alongside the Shapley value.
