---
layout: solution
title: "Matching Games"
tag: matching-games
---

# Matching Games: worked solutions

Solutions to the example questions on the
[Matching Games](/topics/matching-games.html) page. Each question is worth 25
marks.

## Question 1 [25 marks]

**(a) Definitions and notation.** [5]

A pair \((m, p)\) that is not matched together is a **blocking pair** if \(m\)
prefers \(p\) to their current partner and \(p\) prefers \(m\) to theirs. A
**stable matching** is a matching with no blocking pair. With
\(S = \{G, N, T\}\) and \(R = \{E, C, W\}\), the preferences are the maps

\[
\begin{aligned}
f(G) &= (C, E, W) & g(E) &= (N, G, T) \\
f(N) &= (C, W, E) & g(C) &= (G, N, T) \\
f(T) &= (E, C, W) & g(W) &= (T, G, N).
\end{aligned}
\]

**(b) Gale-Shapley (mathematicians proposing).** [7]

We assign every mathematician and physicist to be unmatched, then repeatedly
pick an unmatched suitor.

- Pick \(G\): the top of \(f(G)\) is \(C\), who is unmatched, so \(M(G) = C\).
- Pick \(N\): the top of \(f(N)\) is \(C\), who is matched; since
  \(g(C) = (G, N, T)\), \(C\) prefers their current partner \(G\), so \(N\)
  remains unmatched and we remove \(C\) from \(N\)'s list: \(f(N) = (W, E)\).
- Pick \(T\): the top of \(f(T)\) is \(E\), who is unmatched, so \(M(T) = E\).
- Pick \(N\): the top of \(f(N)\) is now \(W\), who is unmatched, so
  \(M(N) = W\).

All suitors are matched, so the algorithm terminates.

**(c) Matching.** [3]

\(\{G\text{-}C,\; N\text{-}W,\; T\text{-}E\}\).

**(d) Stability.** [4]

\(G\) has \(C\) (first choice) and \(T\) has \(E\) (first choice), so neither is in
a blocking pair. \(N\) has \(W\) and would prefer \(C\), but \(C\) prefers its
partner \(G\) to \(N\), so \((N, C)\) does not block. There is no blocking pair, so
the matching is stable.

**(e) Optimality.** [6]

The mathematicians propose, so the matching is **suitor-optimal** for the
mathematicians: suitor-optimality means each suitor is matched to the best
stable partner they could have in *any* stable matching. The proposing side can
never do better than this: in Gale-Shapley a suitor is only rejected by a
reviewer who holds a proposal they prefer, and considering the first time a
reviewer rejects a stable partner leads to a contradiction with stability, so
no suitor is ever rejected by a stable partner. Since suitors work down their
preference lists, each ends with the best stable partner available to them, and
this matching is the best stable one for the suitors.

## Question 2 [25 marks]

**(a) Definitions.** (Bookwork.) [4]

- A **matching game** of size \(N\) consists of two disjoint sets, suitors
  \(S\) and reviewers \(R\) each of size \(N\), with preference maps
  \(f : S \to R^N\) and \(g : R \to S^N\). A **matching** \(M\) is a bijection
  between \(S\) and \(R\).
- A pair \((s, r)\) is a **blocking pair** of a matching \(M\) if
  \(M(s) \neq r\) but \(s\) prefers \(r\) to \(M(s)\) and \(r\) prefers \(s\) to
  \(M^{-1}(r)\).
- A **stable matching** is a matching with no blocking pair.
- The **Gale-Shapley algorithm** is:

    1. Assign every \(s \in S\) and \(r \in R\) to be unmatched.
    2. Pick some unmatched \(s \in S\) and let \(r\) be the top of \(s\)'s
       preference list:
        - if \(r\) is unmatched, set \(M(s) = r\);
        - if \(r\) is matched and prefers \(s\) to \(M^{-1}(r)\), set
          \(M(s) = r\) and unmatch the previous partner;
        - otherwise \(s\) remains unmatched and \(r\) is removed from \(s\)'s
          preference list.
    3. Repeat step 2 until every \(s \in S\) is matched.

  It returns a stable matching.

**(b)(i) Suitors proposing.** [4]

- Pick \(A\): the top of \(f(A)\) is \(X\), who is unmatched, so \(M(A) = X\).
- Pick \(B\): the top of \(f(B)\) is \(Y\), who is unmatched, so \(M(B) = Y\).
- Pick \(C\): the top of \(f(C)\) is \(Z\), who is unmatched, so \(M(C) = Z\).

Every suitor proposes to a different reviewer, so no proposal is ever refused.
The matching is \(M_S = \{A\text{-}X, B\text{-}Y, C\text{-}Z\}\): every suitor
has their first choice.

**(b)(ii) Reviewers proposing.** [4]

- Pick \(X\): the top of \(g(X)\) is \(B\), who is unmatched, so \(X\) is
  matched to \(B\).
- Pick \(Y\): the top of \(g(Y)\) is \(C\), who is unmatched, so \(Y\) is
  matched to \(C\).
- Pick \(Z\): the top of \(g(Z)\) is \(A\), who is unmatched, so \(Z\) is
  matched to \(A\).

Again no proposal is refused. The matching is
\(M_R = \{A\text{-}Z, B\text{-}X, C\text{-}Y\}\): every reviewer has their
first choice.

**(c) A third stable matching.** [6]

Write \(M = \{A\text{-}Y, B\text{-}Z, C\text{-}X\}\) and check every pair not
matched by \(M\):

- \((A, X)\): \(A\) prefers \(X\) to \(Y\), but \(g(X) = (B, C, A)\) ranks
  \(A\) last, so \(X\) prefers its partner \(C\). Not blocking.
- \((A, Z)\): \(A\) prefers their partner \(Y\) to \(Z\). Not blocking.
- \((B, Y)\): \(B\) prefers \(Y\) to \(Z\), but \(g(Y) = (C, A, B)\) ranks
  \(B\) last, so \(Y\) prefers its partner \(A\). Not blocking.
- \((B, X)\): \(B\) prefers their partner \(Z\) to \(X\). Not blocking.
- \((C, Z)\): \(C\) prefers \(Z\) to \(X\), but \(g(Z) = (A, B, C)\) ranks
  \(C\) last, so \(Z\) prefers its partner \(B\). Not blocking.
- \((C, Y)\): \(C\) prefers their partner \(X\) to \(Y\). Not blocking.

There is no blocking pair, so \(M\) is stable and the game has at least the
three stable matchings \(M_S\), \(M\) and \(M_R\).

**(d) What the three matchings illustrate.** [7]

In \(M_S\) every suitor has their **first** choice and every reviewer their
**third**: \(X\) receives \(A\), \(Y\) receives \(B\) and \(Z\) receives
\(C\), each bottom of the reviewer's list. In \(M\) every suitor and every
reviewer has their **second** choice. In \(M_R\) every suitor has their
**third** choice and every reviewer their **first**.

This illustrates the two theorems. The run with the suitors proposing returns
the **suitor-optimal** stable matching: no suitor does better in any stable
matching (here each already has their first choice), and by
**reviewer-pessimality** this same matching is the worst stable matching for
every reviewer (here each has their last choice). Exchanging the roles of the
two sides gives the mirror image \(M_R\). The stable matching \(M\) sits
strictly between the two extremes for everyone, and no run of the algorithm
ever returns it: whichever side proposes secures the outcome that is best for
that side across all stable matchings.

## Question 3 [25 marks]

**(a) Proposed definitions.** [5]

We adapt the matching game definitions to allow a hospital to hold several
residents. Any proposal capturing the same ideas earns the marks.

- An **assignment** allocates each resident to at most one hospital so that no
  hospital \(h\) receives more than \(c_h\) residents.
- A pair \((r, h)\) not assigned together is a **blocking pair** if \(r\)
  prefers \(h\) to their current hospital (or \(r\) is unassigned), and \(h\)
  either has a free place or prefers \(r\) to at least one of the residents
  assigned to it.
- A **stable assignment** is an assignment with no blocking pair.

**(b) The resident-proposing algorithm.** [8]

All residents have the list \((H_1, H_2)\), and \(H_1\) ranks
\(r_4 \succ r_3 \succ r_2 \succ r_1\). We repeatedly pick an unassigned
resident.

- Pick \(r_1\): proposes to \(H_1\), which has a free place, so \(H_1\) holds
  \(\{r_1\}\).
- Pick \(r_2\): proposes to \(H_1\), which has a free place, so \(H_1\) holds
  \(\{r_1, r_2\}\) and is now full.
- Pick \(r_3\): proposes to \(H_1\), which is full. Of \(\{r_1, r_2, r_3\}\)
  the two that \(H_1\) prefers are \(r_3\) and \(r_2\), so \(r_1\) is rejected:
  \(H_1\) holds \(\{r_2, r_3\}\) and \(r_1\) removes \(H_1\) from their list.
- Pick \(r_1\): proposes to \(H_2\), which has a free place, so \(H_2\) holds
  \(\{r_1\}\).
- Pick \(r_4\): proposes to \(H_1\), which is full. Of \(\{r_2, r_3, r_4\}\)
  the two that \(H_1\) prefers are \(r_4\) and \(r_3\), so \(r_2\) is rejected:
  \(H_1\) holds \(\{r_3, r_4\}\) and \(r_2\) removes \(H_1\) from their list.
- Pick \(r_2\): proposes to \(H_2\), which has a free place, so \(H_2\) holds
  \(\{r_1, r_2\}\) and is full.

All residents are assigned, so the algorithm terminates.

**(c) The assignment and its stability.** [6]

The assignment is

\[
H_1 \colon \{r_3, r_4\}, \qquad H_2 \colon \{r_1, r_2\}.
\]

Residents \(r_3\) and \(r_4\) hold their first choice, so neither is in a
blocking pair. Residents \(r_1\) and \(r_2\) each prefer \(H_1\) to their
assigned \(H_2\), but \(H_1\) is full and prefers both of its residents
\(r_4\) and \(r_3\) to each of \(r_2\) and \(r_1\) (its list is
\(r_4 \succ r_3 \succ r_2 \succ r_1\)), so neither \((r_1, H_1)\) nor
\((r_2, H_1)\) blocks. There is no blocking pair, so the assignment is stable.

**(d) Reduction to a matching game.** [6]

Replace \(H_1\) by two seats \(H_1^{(1)}, H_1^{(2)}\) and \(H_2\) by two seats
\(H_2^{(1)}, H_2^{(2)}\). Each seat inherits its hospital's preference list
over the residents, and each resident replaces every hospital in their list by
that hospital's seats in a fixed order. This gives a matching game of size 4
with the residents as suitors and the seats as reviewers, and a full hospital
keeping its \(c_h\) preferred residents is exactly its seats each holding
their preferred proposal, so runs of the resident-proposing algorithm
correspond to runs of the Gale-Shapley algorithm on this game.

The theorems on the Gale-Shapley algorithm then tell us that the algorithm
terminates with a stable assignment, that every execution (whatever order the
residents are picked in) returns the **same** assignment, and that this
assignment is suitor-optimal for the residents: each resident receives the
best hospital they are assigned in any stable assignment, while by
reviewer-pessimality the hospitals do as badly as they do in any stable
assignment.

## Question 4 [25 marks]

**(a) Proposed definitions.** [4]

Any proposal capturing the following ideas earns the marks. A stable matching
is **suitor-optimal** if every suitor is matched to their
most preferred stable partner; that is, no suitor could be matched to a
partner they prefer in any stable matching. A stable matching is
**reviewer-pessimal** if every reviewer is matched to their least preferred
stable partner; that is, no stable matching gives any reviewer a partner they
like less.

**(b) The two algorithms on the common-list instance.** [7]

Suitors proposing:

- Pick \(A\): the top of \(f(A)\) is \(X\), who is unmatched, so \(M(A) = X\).
- Pick \(B\): the top of \(f(B)\) is \(X\), who is matched; \(X\) prefers
  \(B\) to its current partner \(A\) (since \(g(X) = (B, A, C)\)), so \(A\) is
  unmatched and \(M(B) = X\); \(X\) is removed from \(A\)'s list.
- Pick \(A\): the top of \(A\)'s list is now \(Y\), who is unmatched, so
  \(M(A) = Y\).
- Pick \(C\): the top of \(f(C)\) is \(Y\), who is matched; \(Y\) prefers
  its current partner \(A\) to \(C\), so \(Y\) is removed from \(C\)'s list.
- Pick \(C\): the top of \(C\)'s list is now \(X\), who is matched; \(X\)
  prefers its current partner \(B\) to \(C\), so \(X\) is removed from \(C\)'s
  list.
- Pick \(C\): the top of \(C\)'s list is now \(Z\), who is unmatched, so
  \(M(C) = Z\).

Reviewers proposing:

- Pick \(X\): the top of \(g(X)\) is \(B\), who is unmatched, so \(X\) is
  matched to \(B\).
- Pick \(Y\): the top of \(g(Y)\) is \(B\), who is matched; \(B\) prefers
  their current partner \(X\) to \(Y\), so \(B\) is removed from \(Y\)'s list.
- Pick \(Y\): the top of \(Y\)'s list is now \(A\), who is unmatched, so
  \(Y\) is matched to \(A\).
- Pick \(Z\): the top of \(g(Z)\) is \(B\), who is matched; \(B\) prefers
  \(X\) to \(Z\), so \(B\) is removed from \(Z\)'s list.
- Pick \(Z\): the top of \(Z\)'s list is now \(A\), who is matched; \(A\)
  prefers their current partner \(Y\) to \(Z\), so \(A\) is removed from
  \(Z\)'s list.
- Pick \(Z\): the top of \(Z\)'s list is now \(C\), who is unmatched, so
  \(Z\) is matched to \(C\).

Both algorithms return the same matching,
\(\{A\text{-}Y,\; B\text{-}X,\; C\text{-}Z\}\).

**(c) Uniqueness with a common preference list.** [10]

Let all reviewers share the preference list
\(s_{\sigma(1)} \succ s_{\sigma(2)} \succ \cdots \succ s_{\sigma(N)}\) over the
suitors. We prove by induction on \(N\) that there is exactly one stable
matching. The base case \(N = 1\) is immediate.

Consider the top-ranked suitor \(s_{\sigma(1)}\), whom every reviewer prefers
to every other suitor, and let \(r^{\star}\) be \(s_{\sigma(1)}\)'s own most
preferred reviewer. Every stable matching \(M\) pairs \(s_{\sigma(1)}\) with
\(r^{\star}\): if not, then \(s_{\sigma(1)}\) prefers \(r^{\star}\) to
\(M(s_{\sigma(1)})\), and \(r^{\star}\), like every reviewer, ranks
\(s_{\sigma(1)}\) first, so prefers \(s_{\sigma(1)}\) to its own partner; the
pair \((s_{\sigma(1)}, r^{\star})\) blocks \(M\), a contradiction.

Now remove \(s_{\sigma(1)}\) and \(r^{\star}\). What remains is an instance
with \(N - 1\) suitors in which the reviewers still share a common list (the
restriction of the original one). A matching of the full instance is stable if
and only if it pairs \(s_{\sigma(1)}\) with \(r^{\star}\) and restricts to a
stable matching of the smaller instance: no pair involving \(s_{\sigma(1)}\) or
\(r^{\star}\) can block, since each holds their most preferred partner, and any
other blocking pair blocks the smaller instance too, and conversely. By the
induction hypothesis the smaller instance has a unique stable matching, so the
full instance does as well.

**(d) Why the proposer's advantage vanishes.** [4]

The run with the suitors proposing returns the suitor-optimal stable matching,
which is simultaneously reviewer-pessimal, and symmetrically for the run with
the reviewers proposing. The two outcomes differ exactly when there is more
than one stable matching, as in Question 2, where each side's run selects its
own extreme. When all reviewers agree, part (c) shows the set of stable
matchings is a singleton, so best and worst stable partners coincide for
everyone: there is only one stable matching for either run to return, and no
advantage to proposing.

## Marking exercises

**Marking exercise 1 (Question 4(b)).**

Round 1 breaks the algorithm: a reviewer holding a proposal always trades up
when a preferred suitor proposes, and when several proposals arrive in the
same round the reviewer keeps the best of them. Order of arrival is
irrelevant. \(X\)'s list is \(B \succ A \succ C\), so \(X\) keeps \(B\) and
rejects \(A\); "first come, first served" is not the Gale-Shapley algorithm.
The correct run, as in the solution above, ends in
\(\{A\text{-}Y,\ B\text{-}X,\ C\text{-}Z\}\).

The reported matching also fails the check the question itself suggests:
\((B, X)\) is a blocking pair, since \(B\) ranks \(X\) first, above the
assigned \(Y\), and \(X\) ranks \(B\) above the assigned \(A\). So the
transcript's "stable matching" is not stable, and the error was catchable by
running the definition over the final answer, with no need to re-run the
algorithm. A fair mark is [2] of [7]: rounds 2 and 3 apply the algorithm
correctly to a state that should never have arisen.

**Marking exercise 2 (Question 2(d)).**

This is exactly backwards, and it is the direction the examinable theorems
settle: the Gale-Shapley matching is *suitor-optimal* and
*reviewer-pessimal*. Every suitor obtains their best stable partner and
every reviewer their worst.

The "compare every offer" intuition is seductive but wrong. A reviewer only
ever chooses among the suitors who happen to propose to them, and each
suitor starts at the top of their own list and stops at the best reviewer
who will hold them; a reviewer's held partner only improves as far as the
proposals arriving allow, which is to their worst stable partner. Question
2's data shows it directly: the suitor-proposing run gives every suitor
their first choice, and the reviewer-proposing run gives every reviewer
theirs; whichever side proposes does better. A fair mark is [1] of [7], for
correctly observing that the two sides are treated asymmetrically.
