---
layout: topic
title: "Matching Games"
tag: matching-games
note_urls:
  - "https://vknight.org/gtb/chapters/matching-games/"
---

## Example questions

The following are exam-type questions in the style of the examination paper.
**Each question is worth 25 marks.** Attempt them in full before reading the
worked solutions. Throughout, three applicants \(A, B, C\) are matched to three
roles \(X, Y, Z\) with preferences

\[
\begin{aligned}
A &: X \succ Y \succ Z & \qquad X &: B \succ A \succ C \\
B &: Y \succ X \succ Z & \qquad Y &: A \succ B \succ C \\
C &: X \succ Y \succ Z & \qquad Z &: A \succ B \succ C
\end{aligned}
\]

### Question 1 (based on the in-class activity)

In the matching activity, three mathematicians propose to three physicists. The
mathematicians Gauss (G), Noether (N) and Turing (T) and physicists Einstein
(E), Curie (C) and Newton (W) have preferences

\[
\begin{aligned}
G &: C \succ E \succ W & E &: N \succ G \succ T \\
N &: C \succ W \succ E & C &: G \succ N \succ T \\
T &: E \succ C \succ W & W &: T \succ G \succ N
\end{aligned}
\]

(a) Define a blocking pair and a stable matching. [3]

(b) Run the Gale-Shapley algorithm with the mathematicians proposing, showing
each round. [7]

(c) Write down the resulting matching. [3]

(d) Verify that the matching is stable by checking there is no blocking pair. [6]

(e) State whether the matching is optimal for the mathematicians or the
physicists. Explain what proposer-optimality means, and argue briefly why the
proposing side can never do better in any stable matching. [6]

### Question 2

(a) Provide definitions for the following terms:

   - a matching game;
   - a blocking pair;
   - a stable matching;
   - the Gale-Shapley algorithm. [4]

(b) (i) Apply the applicant-proposing Gale-Shapley algorithm, showing each round
   of proposals and rejections. [6]

   (ii) State the resulting matching. [2]

   (iii) State which side of the market this matching is optimal for, naming the
   relevant result. [3]

(c) Apply the role-proposing Gale-Shapley algorithm to the same instance, showing
your working, and state the resulting matching. [8]

(d) State whether the two matchings differ, and comment on what this shows about
who benefits from being the proposing side. [2]

### Question 3

(a) State the theorem that the Gale-Shapley algorithm returns a stable matching,
and the result on applicant-optimality and reviewer sub-optimality. [5]

(b) Consider the proposed matching \(\{A\text{-}Z, B\text{-}Y, C\text{-}X\}\).

   (i) Determine whether it is stable. [4]

   (ii) Identify a blocking pair and justify your answer. [4]

(c) Consider the matching \(\{A\text{-}X, B\text{-}Y, C\text{-}Z\}\).

   (i) Verify that it is stable by checking that no blocking pair exists. [7]

   (ii) Explain why the applicant-proposing algorithm returns this particular
   stable matching, and what it means for it to be applicant-optimal. [5]

### Question 4 (**hard**)

This question concerns why the applicant-proposing Gale-Shapley algorithm produces
the matching it does. Call a role \(r\) an achievable partner for applicant
\(a\) if some stable matching pairs \(a\) with \(r\).

(a) Define an achievable partner and an applicant-optimal stable matching. [4]

(b) Prove, by induction on the rounds of the applicant-proposing Gale-Shapley
algorithm, that no applicant is ever rejected by an achievable partner. You may
assume that a rejection occurs only when a role holds a proposal it strictly
prefers. [11]

(c) Deduce that the applicant-proposing algorithm returns the applicant-optimal
stable matching. [5]

(d) State the corresponding result for the roles, and use the three-applicant
instance at the head of this page to illustrate that the applicant-proposing and
role-proposing algorithms can return different matchings. [5]
