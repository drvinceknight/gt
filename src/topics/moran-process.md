---
layout: topic
title: "Moran Process"
tag: "moran-process"
note_urls:
  - "https://vknight.org/gtb/chapters/moran-process/"
---

## Example questions

The following are exam-type questions in the style of the examination paper.
**Each question is worth 25 marks.** Attempt them in full before reading the
worked solutions.

### Question 1 (based on the in-class activity)

In class we simulated a Moran process for the Hawk-Dove game with payoff matrix

\[
A = \begin{pmatrix} 0 & 3 \\ 1 & 2 \end{pmatrix}
\]

(rows and columns ordered Hawk, Dove), where the fitness of a type in a state
with \(v_H\) Hawks and \(v_D\) Doves is
\(f_i = (v_i - 1)A_{ii} + \sum_{j \neq i} v_j A_{ij}\).

(a) Describe the two random choices made at each step of a Moran process. [3]

(b) In a population of size \(N = 4\) with two Hawks and two Doves, compute the
fitness of a Hawk and of a Dove. [6]

(c) Compute the probability that, at the next step, the number of Hawks increases
by one. [7]

(d) Define the fixation probability, and explain why this process has exactly two
absorbing states. [5]

(e) Compute the probability that the number of Hawks decreases by one, and hence
the ratio \(\gamma = P(\text{decrease})/P(\text{increase})\). What does the value
of \(\gamma\) tell you about the direction in which the process tends to drift
from this state? [4]

### Question 2

(a) Provide definitions for the following terms:

   - the Moran process;
   - the fixation probability of a mutant;
   - neutral drift;
   - the relative fitness of a mutant. [4]

(b) A single mutant of constant relative fitness \(r\), whose fitness does not
depend on the composition of the population, is placed among \(N - 1\) residents
of fitness \(1\). Its fixation probability is
\(\rho = \dfrac{1 - r^{-1}}{1 - r^{-N}}\).

   (i) State the value under neutral drift and explain it. [3]

   (ii) Compute \(\rho\) when \(N = 4\) and \(r = 2\). [3]

   (iii) Compute \(\rho\) when \(N = 4\) and \(r = \tfrac{1}{2}\). [3]

   (iv) Comment on the comparison of the three values, and explain why even a
   strongly advantageous mutant is far from certain to take over when it starts
   as a single individual. [5]

(c) Show that as \(N \to \infty\) with \(r > 1\), \(\rho \to 1 - r^{-1}\). [4]

(d) Interpret this limit. [3]

### Question 3

(a) State the formula for the fixation probability \(\rho_i\) of a birth-death
process, in terms of the ratios \(\gamma_i = p_{i, i-1}/p_{i, i+1}\). [4]

(b) A Moran process of size \(N = 3\) uses the Hawk-Dove game
\(A = \begin{pmatrix} 0 & 3 \\ 1 & 2 \end{pmatrix}\) (first type Hawk). In state
\(i\), \(f_H(i) = (i - 1)A_{11} + (N - i)A_{12}\),
\(f_D(i) = i A_{21} + (N - i - 1)A_{22}\) and \(\gamma_i = f_D(i)/f_H(i)\).

   (i) Compute \(f_H\) and \(f_D\) for \(i = 1\) and \(i = 2\). [5]

   (ii) Compute \(\gamma_1\) and \(\gamma_2\). [4]

   (iii) Compute the fixation probability \(\rho_1\) of a single Hawk. [4]

   (iv) Compute the fixation probability \(\rho_2\) starting from two Hawks. [4]

(c) Interpret the two fixation probabilities, and using the criterion
\(\rho_1 > 1/N\) determine whether Hawks are favoured by selection. [4]

### Question 4 (**hard**)

Consider a constant-fitness Moran process: a population of \(N\) individuals
contains a number of a mutant type, of fitness \(f_M = r\) with \(r > 0\), among
residents of fitness \(f_R = 1\). Let \(\rho_i\) be the fixation probability of
the mutant type starting from \(i\) mutants.

(a) In state \(i\), write down the transition probabilities \(P_{i \to i+1}\) and
\(P_{i \to i-1}\), and hence show that \(\gamma_i = P_{i \to i-1}/P_{i \to i+1} =
r^{-1}\) for every \(i\), so the ratio does not depend on the state. [4]

(b) Using the general fixation formula, show that the fixation probability of a
single mutant is \(\rho_1 = \dfrac{1 - r^{-1}}{1 - r^{-N}}\) for \(r \neq 1\), and
\(\rho_1 = 1/N\) for \(r = 1\). [6]

(c) A mutant is favoured by selection if \(\rho_1 > 1/N\). Writing
\(\gamma = r^{-1}\), prove that \(\rho_1 > 1/N\) if and only if \(r > 1\). You may
find it helpful to consider \(g(\gamma) = 1 - \gamma^N - N(1 - \gamma)\). [10]

(d) Deduce \(\lim_{N \to \infty} \rho_1\) for \(r > 1\), and explain what it shows
about the fate of a single advantageous mutant in a large population, contrasting
the role of selection with that of drift. [5]

## Optional further reading

You do not need any of this to follow the topic, but the following chapters of
the textbook may help if you would like more background:

- [Evolutionary Biology](https://vknight.org/gtb/chapters/evolutionary-biology/),
  which gives the biological background to evolutionary game theory.
- [Absorbing Markov Chains](https://vknight.org/gtb/appendices/absorbing-markov-chains/), which underpins
  the calculation of fixation probabilities.
- [Evolutionary Dynamics on Graphs](https://vknight.org/gtb/chapters/graph-dynamics/),
  which extends the process to structured, non-well-mixed populations.
- [Learning and Evolutionary Dynamics](https://vknight.org/gtb/chapters/further-learning-dynamics/),
  which places the process within a broader family of update rules.
