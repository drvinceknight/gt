---
layout: topic
title: "Direct Reciprocity"
tag: direct-reciprocity
note_urls:
  - "https://vknight.org/gtb/chapters/direct-reciprocity/"
---

## Example questions

The following are exam-type questions in the style of the examination paper.
**Each question is worth 25 marks.** Attempt them in full before reading the
worked solutions.

### Question 1 (based on the in-class activity)

In class we ran an iterated Prisoner's Dilemma tournament and then wrote each
team's strategy as a reactive strategy \((p, q)\), where \(p\) is the probability
of cooperating after the opponent cooperated and \(q\) after they defected. Two
teams played \((p, q) = (4/5, 1/5)\) and \((p', q') = (3/5, 1/10)\) in an
infinitely repeated game.

(a) Name the reactive strategies \((1, 1)\), \((0, 0)\), \((1, 0)\) and
\(\left(\tfrac{1}{2}, \tfrac{1}{2}\right)\). [3]

(b) With the state space ordered \((CC, CD, DC, DD)\), write down the full
\(4 \times 4\) Markov chain transition matrix for the two strategies above. [7]

(c) Confirm that

\[
\pi = \tfrac{1}{245}\left(26, \; 65, \; 44, \; 110\right)
\]

is the stationary distribution of this Markov chain, and use it to obtain each
player's long-run average payoff (with \(R = 3\), \(P = 1\), \(T = 5\),
\(S = 0\)). [7]

(d) Explain why a strategy such as Tit For Tat, \((1, 0)\), needs care when this
Markov-chain method is applied. [8]

### Question 2

(a) Define a reactive strategy for the Prisoner's Dilemma, and give the
\((p, q)\) representation of Always Cooperate, Always Defect, Tit For Tat and
Random. [5]

(b) Two players use the reactive strategies \((p, q) = (4/5, 2/5)\) and
\((p', q') = (3/5, 1/10)\). With \(r_1 = p - q\), \(r_2 = p' - q'\),

\[
\begin{gathered}
s_1 = \frac{q' r_1 + q}{1 - r_1 r_2}, \qquad
s_2 = \frac{q r_2 + q'}{1 - r_1 r_2}, \\
\pi = \bigl(s_1 s_2, s_1(1 - s_2), (1 - s_1)s_2, (1 - s_1)(1 - s_2)\bigr).
\end{gathered}
\]

(i) Compute \(r_1, r_2, s_1, s_2\). [4]

(ii) Compute the stationary distribution \(\pi\). [4]

(iii) Using \(R = 3\), \(P = 1\), \(T = 5\), \(S = 0\), compute the long-run
average payoff to each player. [5]

(iv) State which player does better in the long run, and explain why in terms
of the two reactive strategies. [2]

(c) Explain why a pure strategy such as Tit For Tat \((1, 0)\) must be treated
separately when computing a stationary distribution. [3]

(d) Define an ergodic Markov chain. [2]

### Question 3

(a) For two reactive strategies \((p, q)\) and \((p', q')\), write down the
transition matrix of the Markov chain on the states \((CC, CD, DC, DD)\). [5]

(b) Player 1 uses Tit For Tat and player 2 uses Always Defect, both cooperating
in the first round.

(i) Write the transition matrix for this pair. [4]

(ii) Starting from \(CC\), find the sequence of states, the long-run outcome
and the long-run payoff to each player. [4]

(c) Player 1 uses Tit For Tat and player 2 uses Always Cooperate.

(i) Write the transition matrix for this pair. [4]

(ii) Starting from \(CC\), find the long-run outcome and the long-run payoff
to each player. [4]

(d) Comment on how Tit For Tat fares against a cooperator compared with a
defector, and what this suggests about why Tit For Tat performed well in
Axelrod's tournaments. [4]

### Question 4 (**hard**)

Two players use reactive strategies \((p, q)\) and \((p', q')\) in the infinitely
repeated Prisoner's Dilemma, with stage payoffs \(R = 3\), \(P = 1\), \(T = 5\),
\(S = 0\). Write \(r_1 = p - q\) and \(r_2 = p' - q'\), and assume the opponent's
strategy is not pure, so that the long-run cooperation probabilities are
well defined.

(a) Let \(c_t\) and \(c'_t\) be the two players' probabilities of cooperating in
round \(t\). Explain why \(c_{t+1} = q + (p - q)\, c'_t\). [4]

(b) Assuming \(c_t \to s_1\) and \(c'_t \to s_2\), derive
\(s_1 = \dfrac{q + r_1 q'}{1 - r_1 r_2}\). [6]

(c) Show that if player 1 uses Tit For Tat, \((p, q) = (1, 0)\), then
\(s_1 = s_2\) whatever reactive strategy player 2 uses. [6]

(d) Deduce that the two players earn equal long-run payoffs when player 1 uses Tit
For Tat, and explain how this property accounts for Tit For Tat's success in
Axelrod's tournaments. [9]

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

### Marking exercise 1 (on Question 2(b)(i), worth [4])

A student pastes Question 2(b)(i) into a free AI chatbot, which replies:

```text
First the intermediate quantities: r1 = p - q = 4/5 - 2/5 = 2/5 and
r2 = p' - q' = 3/5 - 1/10 = 1/2, so 1 - r1 r2 = 1 - 1/5 = 4/5.

Now the long-run cooperation rate of player 1:

    s1 = (q' r1 + p) / (1 - r1 r2)
       = ((1/10)(2/5) + 4/5) / (4/5)
       = (21/25) / (4/5)
       = 21/20 = 1.05

so player 1 cooperates about 105% of the time in the long run, that is,
essentially always. 🤝
```

### Marking exercise 2 (on Question 3(d), worth [4])

A student pastes Question 3(d) into a free AI chatbot, which replies:

```text
Tit For Tat performed so well in Axelrod's tournaments because it is a
ruthless exploiter: by copying the opponent's previous move it stays
one step ahead, beating each opponent it meets and racking up the
highest score in the round robin.
```

## Optional further reading

You do not need any of this to follow the topic, but the following may help if
you would like more background:

- [Repeated Games](https://vknight.org/gtb/chapters/repeated-games/), which sets
  out the infinitely repeated games that direct reciprocity builds on.
- [Ergodic Markov Chains and Stationary Distributions](https://vknight.org/gtb/appendices/ergodic-markov-chains/),
  which underpin the stationary-distribution calculations used here.
