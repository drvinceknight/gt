---
layout: topic
title: "Subgame Perfection"
tag: subgame-perfection
note_urls:
  - "https://vknight.org/gtb/chapters/subgame-perfection/"
---

## Example questions

The following are exam-type questions in the style of the examination paper,
with marks at the rates used in the papers. **A question totalling fewer than
25 marks would, in the examination, be combined with further parts, often one
of the examinable proofs, to make a full 25-mark question.** Attempt them in
full before reading the worked solutions.

### Question 1 (based on the in-class activity)

In the Traitors debrief we saw that the Faithful's threat to banish a deviator
works only when they can be sure who deviated. Once players sometimes break
Vote-Left for fun, a flagged suspect might be the colluding Traitor or merely a
Faithful having fun, and the threat can lose its bite. We model this with a
two-stage game. Let \(q\) be the Faithful's belief, the probability they
assign, that the suspect they are poised to banish is the Traitor rather than
someone breaking Vote-Left for fun. The Traitor chooses to **comply** with
Vote-Left or **deviate** (keep colluding); the Faithful then choose to **banish**
the suspect or **carry on**. Complying gives payoffs (Traitor, Faithful) of
\((1, 2)\), and carrying on after a deviation gives \((3, 0)\). Banishing the
suspect is a gamble: it yields \((-5, 3)\) if the suspect really is the Traitor,
which happens with probability \(q\), and \((3, -5)\) if the suspect is an innocent
Faithful, with probability \(1 - q\). Taking \(q = \tfrac{1}{2}\), the expected
payoff to banishing is therefore \(\tfrac{1}{2}(-5, 3) + \tfrac{1}{2}(3, -5) =
(-1, -1)\).

(a) Represent the game in extensive form (draw the tree). [3]

(b) Use backward induction to find the subgame perfect equilibrium and its
payoffs. [5]

(c) Show that (comply, banish) is a Nash equilibrium of the game. [5]

(d) Explain why (comply, banish) is not subgame perfect, and how this mirrors the
Traitors threat to banish a suspect that does not survive contact with the actual
decision once the Faithful are unsure who deviated. [6]

(e) More generally, let the suspect be the Traitor with probability \(q\), so that
banishing gives expected payoffs \((3 - 8q,\ 8q - 5)\). Determine the range of
\(q\) for which the threat deters the Traitor, the range for which it is credible,
and hence the range for which (comply, banish) is a Nash equilibrium that is not
subgame perfect. [4]

### Question 2

(a) Provide definitions for the following terms:

   - an extensive form game;
   - a subgame;
   - backward induction;
   - a subgame perfect equilibrium. [5]

(b) An entrant must decide whether to **enter** a market or **stay out**. If the
entrant enters, the incumbent must decide whether to **fight** or
**accommodate**. The payoffs (entrant, incumbent) are: stay out \((0, 2)\);
enter then fight \((-1, -1)\); enter then accommodate \((1, 1)\).

   (i) Draw the game in extensive form. [2]

   (ii) Use backward induction to find the subgame perfect equilibrium and the
   resulting payoffs. [3]

   (iii) Find a Nash equilibrium of the game that is not subgame perfect, and
   explain why it is not. [5]

   (iv) Write the game in normal form and confirm the pure Nash equilibria. [3]

(c) Explain the difference between a Nash equilibrium and a subgame perfect
equilibrium. [3]

(d) State the theorem on the existence of a subgame perfect equilibrium in finite
games of perfect information. [4]

### Question 3

(a) Define sequential rationality. [2]

(b) Player 1 chooses \(L\) or \(R\). After \(L\), player 2 chooses \(\ell\)
(payoffs \((3, 1)\)) or \(r\) (payoffs \((0, 0)\)). After \(R\), player 2
chooses \(\ell\) (payoffs \((2, 2)\)) or \(r\) (payoffs \((1, 3)\)).

   (i) Use backward induction to find the subgame perfect equilibrium and its
   payoffs. [3]

   (ii) Write the game in normal form. [4]

   (iii) Obtain all pure Nash equilibria. [4]

   (iv) State which Nash equilibrium is subgame perfect, and for each of the
   others identify the non-credible threat that makes it fail. [4]

(c) Consider the centipede game: player 1 may take, giving \((2, 0)\), or pass;
then player 2 may take, giving \((1, 3)\), or pass; then player 1 may take,
giving \((4, 2)\), or pass, giving the leaf \((3, 5)\).

   (i) Solve the game by backward induction. [5]

   (ii) State the subgame perfect outcome and payoffs, and comment on why the
   prediction is striking given that both players could do better. [3]

### Question 4 (**hard**)

Two firms compete by choosing quantities, one after the other. Inverse demand is
\(P(Q) = a - Q\), where \(Q = q_1 + q_2\) is total output and \(a > 0\); marginal
costs are zero, so firm \(i\) earns profit \(q_i P(Q)\). Firm 1 (the leader)
chooses \(q_1\) first; firm 2 (the follower) observes \(q_1\) and then chooses
\(q_2\).

(a) Explain what a subgame perfect equilibrium is for a game with continuous
action sets. [3]

(b) By backward induction, find the follower's best response \(q_2(q_1)\). [6]

(c) Hence find the leader's subgame perfect quantity, the follower's quantity, and
the resulting profits. [8]

(d) Compare with the simultaneous-move (Cournot) equilibrium, in which
\(q_1 = q_2 = a/3\), and explain the first-mover advantage in terms of
commitment: why the leader gains by moving first even though the follower observes
the choice. [8]

## Marking exercises (optional)

These exercises are entirely optional: they are extra practice, not extra
content. The best way to use an AI assistant is to be its examiner, not its
student: checking work is exactly the skill the examination rewards, and the
skill you will need to use these tools well. Each exercise gives a transcript
in the style of a widely used free AI chatbot answering one of the example
questions above. Every transcript contains at least one error. Mark it as an
examiner would: find each error, explain what goes wrong, and award a mark
out of the marks of the original question. A marker's report for each
transcript is on the solutions page.

### Marking exercise 1 (on Question 2(b)(ii) and (iii), worth [3] and [5])

A student pastes Question 2(b) into a free AI chatbot, which replies:

```text
Backward induction: if the entrant enters, the incumbent compares
fighting (-1) with accommodating (1) and accommodates. Anticipating
this, the entrant compares staying out (0) with entering (1) and
enters. The subgame perfect equilibrium is (enter, accommodate), with
payoffs (1, 1). ✅

A Nash equilibrium that is not subgame perfect: consider (stay out,
accommodate): the entrant stays out, and the incumbent would
accommodate if entered. This is a Nash equilibrium, but it is not
subgame perfect, because the entrant's choice to stay out is not
optimal in every subgame.
```

### Marking exercise 2 (on Question 4(b) and (c), worth [6] and [8])

A student pastes Question 4 into a free AI chatbot, which replies:

```text
Each firm maximises q_i (a - q1 - q2). The first-order conditions are

    a - 2 q1 - q2 = 0,    a - q1 - 2 q2 = 0

Solving simultaneously gives q1 = q2 = a/3, with profits a²/9 each.
Firm 1 moves first, so it simply commits to a/3, and firm 2 follows
with a/3. Moving first makes no difference: both firms play the same
equilibrium either way. ♟️
```

## Optional further reading

You do not need this to follow the topic, but the
[Repeated Games](https://vknight.org/gtb/chapters/repeated-games/) chapter of the
textbook may help if you would like more background on subgame perfect
equilibria over a long horizon.
