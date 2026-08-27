---
layout: topic
title: "Social Choice"
tag: social-choice
note_urls:
  - "https://vknight.org/gtb/chapters/social-choice/"
---

## Example questions

The following are exam-type questions in the style of the examination paper,
with marks at the rates used in the papers. **A question totalling fewer than
25 marks would, in the examination, be combined with further parts, often one
of the examinable proofs, to make a full 25-mark question.** Attempt them in
full before reading the worked solutions.

### Question 1 (based on the in-class activity)

In class we voted on which topic to revise, and compared methods. Nine students
rank three topics \(A, B, C\): four rank \(A \succ B \succ C\), three rank
\(B \succ C \succ A\), and two rank \(C \succ B \succ A\).

(a) Rank the topics by number of first choice votes and determine the
winner. [2]

(b) Compute the Borda scores and the Borda winner. [4]

(c) Determine whether there is a Condorcet winner. [4]

(d) The methods disagree; explain why ranking by first choice votes picks a
different winner, with reference to which preferences each method uses, and state
which method you would recommend for the class vote, justifying your choice. [5]

### Question 2

(a) Provide definitions for the following terms:

   - a social welfare function;
   - Condorcet's method;
   - Borda's method;
   - simple majority rule. [4]

(b) Seven voters rank three candidates \(A, B, C\):

   - 3 voters: \(A \succ B \succ C\);
   - 2 voters: \(B \succ C \succ A\);
   - 2 voters: \(C \succ B \succ A\).

   (i) Determine the winner by number of first choice votes. [2]

   (ii) Determine the Borda winner. [3]

   (iii) Determine the Condorcet winner, if one exists. [3]

   (iv) Comment on the disagreement between the methods. [2]

(c) Explain what a Condorcet winner is and why one may fail to exist. State what
the existence of a Condorcet winner for this profile tells you about majority
rule here. [4]

### Question 3

(a) Define a Condorcet winner and a Borda winner. [4]

(b) Five voters rank three candidates \(A, B, C\):

   - 2 voters: \(A \succ B \succ C\);
   - 2 voters: \(B \succ C \succ A\);
   - 1 voter: \(C \succ A \succ B\).

   (i) Compute all three pairwise majority comparisons. [3]

   (ii) Show that there is no Condorcet winner. [2]

   (iii) Explain the Condorcet cycle: why the collective majority preference
   can be intransitive even when every individual ranking is transitive. [4]

(c) Apply Borda's method to the same profile and give the resulting ranking.
Explain why Borda's method can never produce a cycle, even though pairwise
majority does here, referring to positional versus pairwise information. [6]

### Question 4 (**hard**)

An election over three alternatives \(A\), \(B\) and \(C\) uses Borda's method.
Twelve voters have preferences

   - 5 voters: \(A \succ B \succ C\);
   - 4 voters: \(B \succ C \succ A\);
   - 3 voters: \(C \succ A \succ B\).

(a) Define what it means for a voting rule to be manipulable, and what it means
for a rule to be strategy-proof. [4]

(b) Compute the Borda score of each alternative and determine the sincere
outcome. [6]

(c) Consider one of the five voters whose sincere preference is
\(A \succ B \succ C\). Show that by submitting an insincere ballot this voter can
change the outcome to one they strictly prefer, stating the ballot they submit
and the resulting scores. [9]

(d) The manipulating voter altered only the position of \(C\), the alternative
they care least about, yet the collective ranking of \(A\) and \(B\) changed.
Explain how this violates independence of irrelevant alternatives, and relate the
example to the Gibbard-Satterthwaite theorem. [6]

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

### Marking exercise 1 (on Question 1(b), worth [4])

A student pastes Question 1(b) into a free AI chatbot, which replies:

```text
Borda's method gives 3 points for a first place, 2 for a second and 1
for a third.

  A: 4(3) + 3(1) + 2(1) = 17
  B: 4(2) + 3(3) + 2(2) = 21
  C: 4(1) + 3(2) + 2(3) = 16

The Borda winner is B. 🏆 Note that the choice of points does not
matter: any decreasing point scheme gives the same Borda ranking.
```

### Marking exercise 2 (on Question 4(b) and (c), worth [6] and [9])

A student pastes Question 4(b) and (c) into a free AI chatbot, which replies:

```text
Sincere scores: A: 5(2) + 3(1) = 13, B: 4(2) + 5(1) = 13,
C: 3(2) + 4(1) = 10. So A and B tie on 13 points. ✅

The manipulation: one of the A > B > C voters submits A > C > B
instead. Only B's score changes: it drops by one point. The new scores
are A: 13, B: 12, C: 10, so A now wins outright, which the manipulator
strictly prefers to the tie.

This possibility violates the Gibbard-Satterthwaite theorem, which
states that a fair voting rule cannot be manipulated.
```
