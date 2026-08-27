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
worked solutions.

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

(a) Define a blocking pair and a stable matching, and write the preferences
above as maps \(f : S \to R^3\) and \(g : R \to S^3\), where \(S\) is the set
of mathematicians (the suitors) and \(R\) the set of physicists (the
reviewers). [5]

(b) Run the Gale-Shapley algorithm with the mathematicians proposing, showing
each step. [7]

(c) Write down the resulting matching. [3]

(d) Verify that the matching is stable by checking there is no blocking pair. [4]

(e) State whether the matching is optimal for the mathematicians or the
physicists. Explain what suitor-optimality means, and argue briefly why the
proposing side can never do better in any stable matching. [6]

### Question 2

Consider the matching game of size 3 with suitors \(S = \{A, B, C\}\) and
reviewers \(R = \{X, Y, Z\}\) whose preference maps are

\[
\begin{aligned}
f(A) &= (X, Y, Z) & \qquad g(X) &= (B, C, A) \\
f(B) &= (Y, Z, X) & \qquad g(Y) &= (C, A, B) \\
f(C) &= (Z, X, Y) & \qquad g(Z) &= (A, B, C)
\end{aligned}
\]

(a) Provide definitions for the following terms:

   - a matching game;
   - a blocking pair;
   - a stable matching;
   - the Gale-Shapley algorithm. [4]

(b) (i) Run the Gale-Shapley algorithm with the suitors proposing, showing each
   step, and state the resulting matching. [4]

   (ii) Run the Gale-Shapley algorithm with the reviewers proposing, showing
   each step, and state the resulting matching. [4]

(c) Show that \(\{A\text{-}Y, B\text{-}Z, C\text{-}X\}\) is also a stable
matching, so that this game has at least three stable matchings. [6]

(d) For each of the three stable matchings found, state where each suitor and
each reviewer ranks the partner they receive. Explain what this illustrates
about suitor-optimality and reviewer-pessimality of the matching returned by
the Gale-Shapley algorithm. [7]

### Question 3

The hospital-resident problem generalises the matching game: residents are
matched to hospitals, and each hospital \(h\) may take up to \(c_h\) residents.
The resident-proposing algorithm generalises the Gale-Shapley algorithm: pick
an unassigned resident, who proposes to the top hospital remaining on their
list; a hospital with a free place accepts, while a full hospital compares the
proposer with the residents it holds, keeping its \(c_h\) preferred residents
and rejecting the other, who removes that hospital from their list.

Four residents \(r_1, r_2, r_3, r_4\) apply to two hospitals \(H_1, H_2\),
each with capacity 2. Every resident prefers \(H_1\) to \(H_2\), and the
hospitals rank the residents as follows:

\[
\begin{aligned}
H_1 &: r_4 \succ r_3 \succ r_2 \succ r_1 \\
H_2 &: r_1 \succ r_2 \succ r_3 \succ r_4
\end{aligned}
\]

(a) The definitions for matching games do not apply directly here. By adapting
them, propose suitable definitions for the hospital-resident problem of: an
assignment, a blocking pair, and a stable assignment. [5]

(b) Run the resident-proposing algorithm, showing each step. [8]

(c) State the resulting assignment and verify that it is stable by checking
that no blocking pair exists. [6]

(d) Explain how the problem reduces to a matching game by replacing each
hospital with capacity \(c\) by \(c\) copies of itself, and state what the
theorems on the Gale-Shapley algorithm then tell us about the assignment
returned in part (b). [6]

### Question 4 (**hard**)

Call a reviewer \(r\) a **stable partner** of a suitor \(s\) if some stable
matching pairs \(s\) with \(r\); likewise \(s\) is then a stable partner of
\(r\).

(a) Using the notion of a stable partner, propose definitions of a
suitor-optimal stable matching and a reviewer-pessimal stable matching. [4]

(b) Consider the matching game of size 3 with suitors \(S = \{A, B, C\}\) and
reviewers \(R = \{X, Y, Z\}\), where every reviewer has the same preference
list \(B \succ A \succ C\), giving preference maps

\[
\begin{aligned}
f(A) &= (X, Y, Z) & \qquad g(X) &= (B, A, C) \\
f(B) &= (X, Y, Z) & \qquad g(Y) &= (B, A, C) \\
f(C) &= (Y, X, Z) & \qquad g(Z) &= (B, A, C)
\end{aligned}
\]

Run the Gale-Shapley algorithm with the suitors proposing and again with the
reviewers proposing, showing each step, and state both matchings. [7]

(c) Prove that if all reviewers share the same preference list then the
matching game has exactly one stable matching. [10]

(d) For the game of Question 2 the two runs of the algorithm return different
matchings, while in part (b) they coincide. Explain why the proposing side's
advantage vanishes when the reviewers all agree, referring to suitor-optimality
and reviewer-pessimality. [4]

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

### Marking exercise 1 (on Question 4(b), worth [7])

A student pastes the suitor-proposing half of Question 4(b) into a free AI
chatbot, which replies:

```text
Round 1. A and B both propose to X; C proposes to Y. X received A's
proposal first, so X keeps A and rejects B. Y accepts C.

Round 2. B proposes to Y. Y compares B with C: the list is B > A > C,
so Y rejects C and keeps B.

Round 3. C proposes to X. X already holds A and A > C, so C is
rejected. C proposes to Z, who accepts.

Result: {A-X, B-Y, C-Z}, which is the suitor-optimal stable
matching. ✅
```

### Marking exercise 2 (on Question 2(d), worth [7])

A student pastes Question 2(d) into a free AI chatbot, which replies:

```text
The Gale-Shapley algorithm favours the reviewers. The reviewers receive
all the proposals, so they can compare every offer and keep the best,
trading up whenever someone better comes along; the suitors, by
contrast, must work down their lists and take whatever they can get.
The algorithm is therefore reviewer-optimal: each reviewer obtains
their best stable partner, and each suitor obtains their worst.
```
