---
layout: topic
title: "Replicator Dynamics"
tag: "replicator-dynamics"
note_urls:
  - "https://vknight.org/gtb/chapters/replicator-dynamics/"
---

## Example questions

The following are exam-type questions in the style of the examination paper.
**Each question is worth 25 marks.** Attempt them in full before reading the
worked solutions.

### Question 1 (based on the in-class activity)

In class we played the snowdrift game: two drivers meet at a snowdrift and each
chooses to Dig or Stay. With actions ordered (Dig, Stay), the row player's
payoff matrix is

\[
A = \begin{pmatrix} 3 & 2 \\ 4 & 0 \end{pmatrix}.
\]

Let \(x\) be the proportion of the population that plays Dig.

(a) Write down the fitness \(f_D\) of Dig and \(f_S\) of Stay as functions of
\(x\). [3]

(b) Write down the replicator equation for \(x\) and simplify it to a product of
factors. [7]

(c) Find all stable populations of the dynamics. [3]

(d) By examining the sign of \(\dot{x}\), determine which stable population the
dynamics approach from any interior start, and relate this to where the class
settled. [6]

(e) Determine whether the interior stable population is an evolutionarily stable
strategy, justifying your answer both from the stability of the population and
from the requirement that a small invading group of the other strategy must earn
a lower fitness than the residents. [6]

### Question 2

(a) Write down the replicator dynamics equation for a two-type population with
fitness functions \(f_1\) and \(f_2\). [3]

(b) Road users drive on the left \((L)\) or the right \((R)\). With \(x\) the
proportion driving on the left, the fitness functions are \(f_L(x) = 1 + x\) and
\(f_R(x) = 1 + (1 - x)\).

   (i) Give an interpretation of the fitness functions. [2]

   (ii) Derive the replicator dynamics equation. [6]

   (iii) Obtain all stable populations. [4]

   (iv) By examining the sign of \(\dot{x}\) near each stable population,
   determine which are approached by the dynamics, and state which are
   evolutionarily stable strategies. [8]

   (v) This game has two stable populations, everyone driving left and everyone
   driving right. Explain what determines which side everyone ends up driving on,
   and why the symmetric mixed population is never observed in practice. [2]

### Question 3

Rock-Paper-Scissors is played in a large population. With actions ordered
(Rock, Paper, Scissors), the focal-player payoff matrix is

\[
A = \begin{pmatrix} 0 & -1 & 1 \\ 1 & 0 & -1 \\ -1 & 1 & 0 \end{pmatrix},
\]

where a win scores \(1\), a loss \(-1\) and a tie \(0\). Let
\(x = (x_R, x_P, x_S)\) be the proportions playing each action, with
\(x_R + x_P + x_S = 1\).

(a) Write down the fitness \(f_R\), \(f_P\) and \(f_S\) of each strategy as
functions of the population, and show that the average fitness \(\phi\) is
zero. [5]

(b) Write down the replicator dynamics equations for \(\dot{x}_R\),
\(\dot{x}_P\) and \(\dot{x}_S\). [4]

(c) Show that the only interior stable population, with all three strategies
present, is \(x_R = x_P = x_S = \tfrac{1}{3}\). [5]

(d) Let \(H(x) = x_R x_P x_S\). Show that \(\tfrac{d}{dt} \ln H = 0\) along any
interior trajectory, so that \(H\) is constant. Hence describe the trajectories
and explain why the interior population is stable but not asymptotically
stable. [7]

(e) Explain why the interior population is not an evolutionarily stable
strategy, and interpret the dynamics in terms of the cyclic structure of the
game. [4]

### Question 4 (**hard**)

Consider a symmetric game with payoff matrix \(A\) and an interior evolutionarily
stable strategy \(x^{*}\), so every component of \(x^{*}\) is positive and
\(x^{*} A x > x A x\) for every population \(x \neq x^{*}\) in a neighbourhood of
\(x^{*}\). Define

\[
V(x) = \sum_i x^{*}_i \ln\!\frac{x^{*}_i}{x_i}.
\]

(a) Show that \(V(x) \ge 0\) for every interior \(x\), with equality only at
\(x = x^{*}\). You may use the concavity of \(\ln\). [5]

(b) Show that along any interior trajectory of the replicator dynamics

\[
\frac{d}{dt} V(x) = -\bigl(x^{*} A x - x A x\bigr).
\]

[9]

(c) Use the evolutionarily stable strategy condition to deduce that
\(\tfrac{d}{dt} V < 0\) for \(x \neq x^{*}\) near \(x^{*}\), so that \(V\) is a
Lyapunov function and \(x^{*}\) is asymptotically stable. [6]

(d) Contrast this with the Rock-Paper-Scissors game of Question 3, where the
interior population is not an evolutionarily stable strategy. Explain why there the
analogue of \(V\) is replaced by a conserved quantity \(H\) and the trajectories
are closed orbits rather than converging to the centre. [5]

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

### Marking exercise 1 (on Question 2(b)(ii) and (iii), worth [6] and [4])

A student pastes Question 2(b) into a free AI chatbot, which replies:

```text
The replicator equation compares a strategy's fitness with its rival's:

    dx/dt = x (f_L - f_R) = x ((1 + x) - (2 - x)) = x (2x - 1)

Setting dx/dt = 0 gives the stable populations: x = 0 (nobody drives on
the left) and x = 1/2 (half on each side). ✅
```

### Marking exercise 2 (on Question 1(e), worth [6])

A student pastes Question 1(e) into a free AI chatbot, which replies:

```text
The interior fixed point solves f_D = f_S: here x + 2 = 4x, so
x* = 2/3. The dynamics converge to x* from every interior starting
point, and every stable fixed point of the replicator dynamics is an
evolutionarily stable strategy, so x* = 2/3 is an ESS. ∎
```

## Optional further reading

You do not need any of this to follow the topic, but the following chapters of
the textbook may help if you would like more background:

- [Evolutionary Biology](https://vknight.org/gtb/chapters/evolutionary-biology/),
  which gives the biological background to evolutionary game theory.
- [Numerical Integration](https://vknight.org/gtb/appendices/numerical-integration/),
  which covers the numerical methods behind solving the replicator dynamics
  equation.
- [Evolutionary Dynamics on Graphs](https://vknight.org/gtb/chapters/graph-dynamics/),
  which extends the dynamics to structured, non-well-mixed populations.
- [Learning and Evolutionary Dynamics](https://vknight.org/gtb/chapters/further-learning-dynamics/),
  which places the dynamics within a broader family of update rules.
