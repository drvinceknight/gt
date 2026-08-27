---
layout: solution
title: "Social Choice"
tag: social-choice
---

# Social Choice: worked solutions

Solutions to the example questions on the
[Social Choice](/topics/social-choice.html) page.

## Question 1 [15 marks]

**(a) First choice votes.** [2]

First choice votes: \(A = 4\), \(B = 3\), \(C = 2\). The winner by first choice
votes is \(A\).

**(b) Borda.** [4]

Each alternative scores the number of alternatives a voter ranks it above, so
here a first place is worth 2 points, a second 1 and a third 0:

\[
A: 4(2) = 8, \qquad
B: 4(1) + 3(2) + 2(1) = 12, \qquad
C: 3(1) + 2(2) = 7.
\]

The Borda winner is \(B\).

**(c) Condorcet winner.** [4]

- \(A\) vs \(B\): \(A\) preferred by \(4\), \(B\) by \(3 + 2 = 5\); \(B\) beats
  \(A\).
- \(A\) vs \(C\): \(A\) preferred by \(4\), \(C\) by \(3 + 2 = 5\); \(C\) beats
  \(A\).
- \(B\) vs \(C\): \(B\) preferred by \(4 + 3 = 7\), \(C\) by \(2\); \(B\) beats
  \(C\).

\(B\) beats both \(A\) and \(C\), so \(B\) is the Condorcet winner.

**(d) Why the methods disagree, and a recommendation.** [5]

Counting first choice votes picks \(A\) because it looks only at top choices, and
\(A\) has the most. But a majority (\(5\) of \(9\)) rank \(A\) last, which the
first choice count ignores. Borda and Condorcet use the full rankings, the lower
preferences and the pairwise comparisons, and both select \(B\), who is preferred
to each rival by a majority. The methods disagree because counting first choice
votes discards everything except each voter's top choice. For the class vote,
\(B\) is the better outcome: it is the Condorcet winner, beating each alternative
head-to-head, so it commands majority support against any rival, whereas \(A\),
the winner on first choice votes, would lose a straight vote to either of the
others. A Condorcet (or Borda) method is therefore preferable here, as it reflects
the whole class's preferences rather than only first choices.

## Question 2 [18 marks]

**(a) Definitions.** (Bookwork.) [4]

- A **social welfare function** maps every preference profile (a list of the
  voters' individual strict preference orderings) to a collective strict linear
  ordering of the alternatives.
- **Condorcet's method** selects the **Condorcet winner**, the alternative that a
  strict majority of voters prefers to every other alternative, when one exists.
- **Borda's method** awards each alternative \(k\) points from a voter who ranks
  it above exactly \(k\) other alternatives; the alternative with the highest
  total score across all voters is the **Borda winner**.
- **Simple majority rule** ranks alternative \(x\) above \(y\) if and only if a
  strict majority of voters prefer \(x\) to \(y\).

**(b)(i) First choice votes.** [2]

First choice votes: \(A = 3\), \(B = 2\), \(C = 2\); the winner by first choice
votes is \(A\).

**(b)(ii) Borda.** [3]

\[
A: 3(2) = 6, \quad B: 3(1) + 2(2) + 2(1) = 9, \quad C: 2(1) + 2(2) = 6.
\]

The Borda winner is \(B\).

**(b)(iii) Condorcet.** [3]

\(A\) vs \(B\): \(B\) wins \(4\)-\(3\). \(B\) vs \(C\): \(B\) wins \(5\)-\(2\). So
\(B\) beats both and is the Condorcet winner.

**(b)(iv) Comment.** [2]

Counting first choice votes elects \(A\) on top choices alone, but \(A\) loses to
both \(B\) and \(C\) head-to-head. Borda and Condorcet both elect \(B\), which is
preferred by a majority against each rival. The methods disagree because counting
first choice votes ignores lower preferences.

**(c) Condorcet winner.** [4]

A **Condorcet winner** beats every other candidate in pairwise majority votes. It
may fail to exist because pairwise majorities can be cyclic, in which case no
candidate beats all others. For this profile, however, a Condorcet winner does
exist, namely \(B\): so for these seven voters majority rule is well behaved, the
pairwise relation is transitive (\(B \succ A\), \(B \succ C\), and \(C \succ A\)),
and there is a single alternative that a majority prefers to every other. The
existence of a Condorcet winner tells us there is no majority cycle here.

## Question 3 [19 marks]

**(a) Definitions.** (Bookwork.) [4]

- A **Condorcet winner** is an alternative that a strict majority of voters
  prefers to every other alternative.
- A **Borda winner** is the alternative with the highest total Borda score,
  where each voter awards an alternative \(k\) points for ranking it above
  exactly \(k\) other alternatives.

**(b)(i) Pairwise majorities.** [3]

- \(A\) vs \(B\): \(A\) preferred by \(2 + 1 = 3\) voters, \(B\) by \(2\); \(A\)
  beats \(B\).
- \(B\) vs \(C\): \(B\) preferred by \(2 + 2 = 4\) voters, \(C\) by \(1\); \(B\)
  beats \(C\).
- \(C\) vs \(A\): \(C\) preferred by \(2 + 1 = 3\) voters, \(A\) by \(2\); \(C\)
  beats \(A\).

**(b)(ii) No Condorcet winner.** [2]

The majorities cycle \(A \succ B \succ C \succ A\), so no candidate beats all the
others; there is no Condorcet winner.

**(b)(iii) Condorcet cycle.** [4]

Every individual ranking is transitive, yet the collective majority relation is
cyclic. This is a Condorcet cycle: aggregating transitive individual
preferences by pairwise majority can produce an intransitive collective
preference, so majority rule need not yield a consistent ranking.

**(c) Borda's method.** [6]

Each alternative scores the number of alternatives a voter ranks it above (2
points for a first place, 1 for a second, 0 for a third):

\[
A: 2(2) + 2(0) + 1(1) = 5, \qquad
B: 2(1) + 2(2) + 1(0) = 6, \qquad
C: 2(0) + 2(1) + 1(2) = 4.
\]

The Borda ranking is \(B \succ A \succ C\): a complete, transitive ranking,
even though pairwise majority cycles on the very same profile. The reason is
the information each method uses: pairwise majority looks only at *isolated
head-to-head contests*, in each of which the losers' margins are discarded, so
the separate verdicts can disagree and form a cycle. Borda instead uses
*positional* information, each alternative's rank in every voter's full list,
and sums a single number per alternative; ordering alternatives by their scores
can never produce a cycle. The price of escaping the cycle is the pairwise
viewpoint itself: here the Borda winner \(B\) loses its head-to-head contest
with \(A\) by \(3\) votes to \(2\). Borda avoids intransitivity precisely by
giving up pairwise (independence) information in favour of positional scores.

## Question 4 [25 marks]

**(a) Manipulability and strategy-proofness.** [4]

A voter **manipulates** a voting rule when, by submitting a ballot that does not
reflect their true preferences, they obtain a collective outcome they strictly
prefer to the one their sincere ballot would produce, with the other voters'
ballots held fixed. A rule is **manipulable** if some preference profile admits
such a voter, and **strategy-proof** if no voter can ever gain by voting
insincerely, so that sincere voting is always a best response.

**(b) Sincere Borda scores.** [6]

With 2, 1 and 0 points for first, second and third,

\[
\begin{aligned}
A &: 5(2) + 4(0) + 3(1) = 13, \\
B &: 5(1) + 4(2) + 3(0) = 13, \\
C &: 5(0) + 4(1) + 3(2) = 10.
\end{aligned}
\]

So \(A\) and \(B\) tie on 13 points, ahead of \(C\) on 10: the sincere outcome is
a tie between \(A\) and \(B\).

**(c) A profitable manipulation.** [9]

Take one of the five voters whose sincere preference is \(A \succ B \succ C\).
They rank \(A\) first, so they would rather \(A\) win outright than share first
place with \(B\). Suppose this voter instead submits \(A \succ C \succ B\),
keeping \(A\) top but demoting \(B\) below \(C\). Only their ballot changes: \(B\)
loses the point it received from this voter and \(C\) gains one, while \(A\) is
unaffected. The profile becomes

   - 4 voters: \(A \succ B \succ C\);
   - 1 voter: \(A \succ C \succ B\);
   - 4 voters: \(B \succ C \succ A\);
   - 3 voters: \(C \succ A \succ B\),

with scores

\[
\begin{aligned}
A &: 4(2) + 1(2) + 4(0) + 3(1) = 13, \\
B &: 4(1) + 1(0) + 4(2) + 3(0) = 12, \\
C &: 4(0) + 1(1) + 4(1) + 3(2) = 11.
\end{aligned}
\]

Now \(A\) wins outright with 13 points. The manipulating voter, who ranks \(A\)
first, strictly prefers this to the sincere \(A\)-\(B\) tie, so the misreport is
profitable and Borda's method is manipulable on this profile.

**(d) Independence of irrelevant alternatives and Gibbard-Satterthwaite.** [6]

The voter changed only where \(C\) sits relative to \(B\); they still rank \(A\)
above \(B\). Independence of irrelevant alternatives requires the collective
ranking of \(A\) and \(B\) to depend only on how the voters rank \(A\) against
\(B\), so moving the irrelevant alternative \(C\) should leave that verdict
untouched. Under Borda it does not: promoting \(C\) drains a point from \(B\) and
breaks the tie in \(A\)'s favour. This failure of independence of irrelevant
alternatives is exactly what makes the manipulation possible. The
Gibbard-Satterthwaite theorem shows the phenomenon is unavoidable: every
non-dictatorial voting rule over three or more alternatives is manipulable, so no
reasonable rule, Borda included, can be strategy-proof.

## Marking exercises

**Marking exercise 1 (Question 1(b)).**

The winner is right but the scores are not Borda scores as defined in this
course: an alternative scores the number of alternatives a voter ranks it
above, so 2, 1 and 0 points here, giving \(A: 8\), \(B: 12\), \(C: 7\) as in
the solution above. The \((3, 2, 1)\) scheme adds one point per voter to
every alternative, which is why the ranking survives; an answer using it has
not answered the question asked.

The closing claim is the serious error: it is *not* true that any decreasing
point scheme gives the same ranking. Only schemes obtained from \((2, 1, 0)\)
by a positive affine transformation do. With points \((10, 1, 0)\), for
example, this same profile gives \(A: 40 + 3 = 43\), \(B: 4 + 30 + 2 = 36\),
\(C: 3 + 20 = 23\), and the winner switches to \(A\). A fair mark is [2] of
[4].

**Marking exercise 2 (Question 4(b) and (c)).**

Part (b) is correct: the sincere outcome is the \(A\)-\(B\) tie on 13, as in
the solution above, so [6] of [6].

In part (c) the chosen ballot and the conclusion are right, but the scores
are wrong: moving \(C\) above \(B\) does not only take a point from \(B\), it
*gives* one to \(C\), whose score becomes \(11\), not \(10\). The slip is
detectable without recomputing anything: each of the 12 voters hands out
\(2 + 1 + 0 = 3\) points, so the scores must total \(36\), and
\(13 + 12 + 10 = 35\). A fair mark is [7] of [9].

The final sentence gets the Gibbard-Satterthwaite theorem backwards, twice.
The theorem states that every non-dictatorial rule over three or more
alternatives *is* manipulable, so the example *confirms* it, violating
nothing; and it is a theorem about all voting rules, not a definition of
fairness. That sentence belongs to part (d), where it would cost marks.
