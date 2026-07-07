---
layout: solution
title: "Moran Process"
tag: "moran-process"
---

# Moran Process: worked solutions

Solutions to the example questions on the
[Moran Process](/topics/moran-process.html) page. Each question is worth 25
marks.

## Question 1 [25 marks]

**(a) The two random choices.** [3]

At each step one individual is selected to reproduce, with probability
proportional to its fitness, and one individual is selected uniformly at random to
die. A copy of the reproducing individual replaces the one that dies.

**(b) Fitnesses.** [6]

With \(v_H = 2\) Hawks and \(v_D = 2\) Doves,

\[
f_H = (2 - 1)A_{HH} + 2 A_{HD} = 1 \cdot 0 + 2 \cdot 3 = 6,
\qquad
f_D = (2 - 1)A_{DD} + 2 A_{DH} = 1 \cdot 2 + 2 \cdot 1 = 4.
\]

**(c) Probability the number of Hawks increases.** [7]

The number of Hawks rises by one when a Hawk reproduces and a Dove dies:

\[
\frac{2 f_H}{2 f_H + 2 f_D} \cdot \frac{v_D}{N}
= \frac{12}{12 + 8} \cdot \frac{2}{4}
= \frac{3}{5} \cdot \frac{1}{2} = \frac{3}{10}.
\]

**(d) Fixation and absorbing states.** [5]

The fixation probability of a type is the probability that the population
eventually becomes composed entirely of that type. The process has two absorbing
states, all Hawks and all Doves: once only one type remains there is no other type
to copy, so the state can no longer change.

**(e) Direction of drift.** [4]

The number of Hawks falls by one when a Dove reproduces and a Hawk dies:

\[
\frac{2 f_D}{2 f_H + 2 f_D} \cdot \frac{v_H}{N}
= \frac{8}{20} \cdot \frac{2}{4} = \frac{2}{5} \cdot \frac{1}{2} = \frac{1}{5}.
\]

Hence \(\gamma = \dfrac{P(\text{decrease})}{P(\text{increase})} =
\dfrac{1/5}{3/10} = \dfrac{2}{3} < 1\). Since \(\gamma < 1\) the process is more
likely to gain a Hawk than to lose one from this state, so it tends to drift
towards more Hawks.

## Question 2 [25 marks]

**(a) Definitions.** (Bookwork.) [4]

- The **Moran process** assumes a constant population of \(N\) individuals of
  \(m\) types with a fitness function. At each step one individual is selected to
  reproduce with probability proportional to its fitness, one individual is
  selected uniformly at random to be removed, and a copy of the reproducing
  individual replaces it. This repeats until a single type remains.
- The **fixation probability** of a type is the probability that the population
  eventually becomes composed entirely of individuals of that type.
- **Neutral drift** is the case where the mutant has the same fitness as the
  residents (\(r = 1\), equivalently selection intensity \(w = 0\)); a single
  mutant then fixes with probability \(1/N\).
- The **relative fitness** \(r\) of a mutant is its fitness divided by the
  resident fitness.

The formula quoted in the question follows from the general fixation result.
Because the mutant has constant relative fitness, with \(f_M = r\) and
\(f_R = 1\) every ratio is the same:

\[
\gamma_k = \frac{f_R}{f_M} = \frac{1}{r} = r^{-1} \qquad \text{for all } k.
\]

The products in the general formula are therefore powers of \(r^{-1}\), so for a
single mutant (\(i = 1\)),

\[
\rho = \frac{1}{1 + \sum_{k=1}^{N-1} (r^{-1})^k} = \frac{1}{\sum_{k=0}^{N-1} r^{-k}}.
\]

Summing the geometric series, valid for \(r \neq 1\), gives

\[
\rho = \frac{1 - r^{-1}}{1 - r^{-N}}.
\]

**(b)(i) Neutral drift.** [3]

When \(r = 1\) all individuals are equally likely ancestors, so
\(\rho = 1/N\).

**(b)(ii) \(N = 4\), \(r = 2\).** [3]

\[
\rho = \frac{1 - \tfrac{1}{2}}{1 - \tfrac{1}{16}} = \frac{\tfrac{1}{2}}{\tfrac{15}{16}} = \frac{8}{15} \approx 0.533.
\]

**(b)(iii) \(N = 4\), \(r = \tfrac{1}{2}\).** [3]

\[
\rho = \frac{1 - 2}{1 - 16} = \frac{-1}{-15} = \frac{1}{15} \approx 0.067.
\]

**(b)(iv) Comparison.** [5]

The neutral value is \(1/4 = 0.25\). An advantageous mutant (\(r = 2\)) fixes more
often (\(\tfrac{8}{15} \approx 0.53\)), while a disadvantageous one
(\(r = \tfrac{1}{2}\)) fixes far less often (\(\tfrac{1}{15} \approx 0.07\)); so
selection raises or lowers fixation relative to drift. Even so, the strongly
advantageous mutant fixes only about half the time: starting as a single
individual it is very likely to be lost by chance in the first few steps, before
its fitness advantage can act. Selection improves a rare mutant's odds but is far
from guaranteeing that it takes over.

**(c) Limit.** [4]

For \(r > 1\), \(r^{-N} \to 0\) as \(N \to \infty\), so

\[
\rho = \frac{1 - r^{-1}}{1 - r^{-N}} \to \frac{1 - r^{-1}}{1} = 1 - r^{-1}.
\]

**(d) Interpretation.** [3]

Even in an arbitrarily large population an advantageous mutant fixes with
probability only \(1 - 1/r\), bounded away from \(1\): a beneficial mutation is
likely to be lost while still rare. For \(r = 2\) this limit is \(\tfrac{1}{2}\).

## Question 3 [25 marks]

**(a) Fixation formula.** (Bookwork.) [4]

\[
\rho_i = \frac{1 + \sum_{k=1}^{i-1} \prod_{j=1}^{k} \gamma_j}{1 + \sum_{k=1}^{N-1} \prod_{j=1}^{k} \gamma_j},
\qquad \gamma_i = \frac{p_{i, i-1}}{p_{i, i+1}}.
\]

**(b)(i) Fitnesses.** [5]

\[
f_H(1) = 0 + 2(3) = 6, \quad f_D(1) = 1 + 2 = 3,
\qquad
f_H(2) = 0 + 3 = 3, \quad f_D(2) = 2 + 0 = 2.
\]

**(b)(ii) Ratios.** [4]

\[
\gamma_1 = \frac{f_D(1)}{f_H(1)} = \frac{3}{6} = \frac{1}{2},
\qquad
\gamma_2 = \frac{f_D(2)}{f_H(2)} = \frac{2}{3}.
\]

**(b)(iii) Fixation from one Hawk.** [4]

\[
\rho_1 = \frac{1}{1 + \gamma_1 + \gamma_1 \gamma_2}
= \frac{1}{1 + \tfrac{1}{2} + \tfrac{1}{3}} = \frac{1}{\tfrac{11}{6}} = \frac{6}{11} \approx 0.545.
\]

**(b)(iv) Fixation from two Hawks.** [4]

\[
\rho_2 = \frac{1 + \gamma_1}{1 + \gamma_1 + \gamma_1 \gamma_2}
= \frac{1 + \tfrac{1}{2}}{\tfrac{11}{6}} = \frac{\tfrac{3}{2}}{\tfrac{11}{6}} = \frac{9}{11} \approx 0.818.
\]

**(c) Interpretation.** [4]

A single Hawk fixes with probability \(\tfrac{6}{11}\), and starting from two
Hawks fixation is more likely still at \(\tfrac{9}{11}\): the more Hawks initially
present, the more likely they take over. Applying the criterion, a single Hawk
has \(\rho_1 = \tfrac{6}{11} \approx 0.545 > \tfrac{1}{3} = 1/N\), so a single
Hawk fixes more often than a neutral mutant would: Hawks are favoured by
selection.

## Question 4 [25 marks]

**(a) The ratio is state-independent.** [4]

In state \(i\) the number of mutants rises by one when a mutant is copied and a
resident is removed, and falls by one when a resident is copied and a mutant is
removed:

\[
P_{i \to i+1} = \frac{i f_M}{i f_M + (N - i) f_R} \cdot \frac{N - i}{N},
\qquad
P_{i \to i-1} = \frac{(N - i) f_R}{i f_M + (N - i) f_R} \cdot \frac{i}{N}.
\]

Taking the ratio, the shared denominator and the factor \(i(N - i)/N\) cancel:

\[
\gamma_i = \frac{P_{i \to i-1}}{P_{i \to i+1}}
= \frac{(N - i) f_R \cdot i}{i f_M \cdot (N - i)}
= \frac{f_R}{f_M} = \frac{1}{r} = r^{-1},
\]

which is independent of \(i\).

**(b) Fixation of a single mutant.** [6]

With \(\gamma_k = \gamma = r^{-1}\) for all \(k\), the products in the general
formula are powers of \(\gamma\), so

\[
\rho_1 = \frac{1}{1 + \sum_{k=1}^{N-1} \gamma^k} = \frac{1}{\sum_{k=0}^{N-1} \gamma^k}.
\]

For \(\gamma \neq 1\) the geometric sum gives
\(\sum_{k=0}^{N-1}\gamma^k = \dfrac{1 - \gamma^N}{1 - \gamma}\), hence

\[
\rho_1 = \frac{1 - \gamma}{1 - \gamma^N} = \frac{1 - r^{-1}}{1 - r^{-N}}.
\]

For \(\gamma = 1\), that is \(r = 1\), the sum is \(N\) and \(\rho_1 = 1/N\).

**(c) The selection criterion.** [10]

Write \(\gamma = r^{-1}\), so \(r > 1\) is equivalent to \(\gamma < 1\). A short
calculation gives

\[
\rho_1 - \frac{1}{N}
= \frac{1 - \gamma}{1 - \gamma^N} - \frac{1}{N}
= \frac{N(1 - \gamma) - (1 - \gamma^N)}{N(1 - \gamma^N)}
= \frac{-g(\gamma)}{N(1 - \gamma^N)},
\]

where \(g(\gamma) = 1 - \gamma^N - N(1 - \gamma)\). We have \(g(1) = 0\) and

\[
g'(\gamma) = -N\gamma^{N-1} + N = N\bigl(1 - \gamma^{N-1}\bigr),
\]

which is positive for \(\gamma < 1\) and negative for \(\gamma > 1\). So \(g\) has
a strict maximum at \(\gamma = 1\), where \(g(1) = 0\); hence \(g(\gamma) < 0\) for
every \(\gamma > 0\) with \(\gamma \neq 1\). Therefore \(-g(\gamma) > 0\), and the
sign of \(\rho_1 - 1/N\) is the sign of \(1 - \gamma^N\):

- if \(\gamma < 1\) then \(1 - \gamma^N > 0\), so \(\rho_1 > 1/N\);
- if \(\gamma > 1\) then \(1 - \gamma^N < 0\), so \(\rho_1 < 1/N\).

Thus \(\rho_1 > 1/N\) if and only if \(\gamma < 1\), that is if and only if
\(r > 1\).

**(d) The large-population limit.** [5]

For \(r > 1\) we have \(r^{-N} \to 0\) as \(N \to \infty\), so

\[
\rho_1 \to \frac{1 - r^{-1}}{1} = 1 - \frac{1}{r}.
\]

Even in an arbitrarily large population an advantageous mutant fixes with
probability only \(1 - 1/r\), bounded away from \(1\). From part (c) selection
fixes the direction, a mutant being favoured exactly when \(r > 1\), for every
\(N\); but it does not guarantee fixation. While the mutant is rare, drift can
remove it before its fitness advantage takes effect, and it is lost with
probability at least \(1/r\).
