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

**(a) Definitions.** [3]

A pair \((m, p)\) that is not matched together is a **blocking pair** if \(m\)
prefers \(p\) to their current partner and \(p\) prefers \(m\) to theirs. A
**stable matching** is a matching with no blocking pair.

**(b) Gale-Shapley (mathematicians proposing).** [7]

- Round 1: \(G \to C\), \(N \to C\), \(T \to E\). \(C\) holds \(G\) (since
  \(G \succ N\)) and rejects \(N\); \(E\) holds \(T\).
- Round 2: \(N \to W\) (next on \(N\)'s list). \(W\) holds \(N\).

No free proposers remain.

**(c) Matching.** [3]

\(\{G\text{-}C,\; N\text{-}W,\; T\text{-}E\}\).

**(d) Stability.** [6]

\(G\) has \(C\) (first choice) and \(T\) has \(E\) (first choice), so neither is in
a blocking pair. \(N\) has \(W\) and would prefer \(C\), but \(C\) prefers its
partner \(G\) to \(N\), so \((N, C)\) does not block. There is no blocking pair, so
the matching is stable.

**(e) Optimality.** [6]

The mathematicians propose, so the matching is **mathematician-optimal**:
proposer-optimality means each proposer is matched to the best partner they could
have in *any* stable matching. The proposing side can never do better than this: in
Gale-Shapley a proposer is only rejected by a reviewer who has a partner they
prefer, and one can show by induction that no reviewer ever rejects a proposer
who could be matched to them in some stable matching. So no proposer is ever
denied a partner that a stable matching could have given them, and this matching
is the best stable one for the proposers.

## Question 2 [25 marks]

**(a) Definitions.** (Bookwork.) [4]

- A **matching game** of size \(N\) consists of two disjoint sets, proposers
  \(S\) and reviewers \(R\) each of size \(N\), with preference maps
  \(f : S \to R^N\) and \(g : R \to S^N\). A **matching** \(M\) is a bijection
  between \(S\) and \(R\).
- A pair \((s, r)\) is a **blocking pair** of a matching \(M\) if
  \(M(s) \neq r\) but \(s\) prefers \(r\) to \(M(s)\) and \(r\) prefers \(s\) to
  \(M^{-1}(r)\).
- A **stable matching** is a matching with no blocking pair.
- The **Gale-Shapley algorithm** repeatedly takes an unmatched proposer and has
  them propose to the next reviewer on their preference list; the reviewer keeps
  whichever proposer they prefer and rejects the other, removing them from that
  proposer's list, until everyone is matched. It returns a stable matching.

**(b)(i) Applicant-proposing.** [6]

- Round 1: \(A \to X\), \(B \to Y\), \(C \to X\). \(X\) keeps \(A\) (since
  \(B \succ A \succ C\)) and rejects \(C\); \(Y\) holds \(B\).
- Round 2: \(C \to Y\). \(Y\) keeps \(B\) (since \(A \succ B \succ C\)) and
  rejects \(C\).
- Round 3: \(C \to Z\), accepted.

**(b)(ii) Matching.** [2]

\(\{A\text{-}X, B\text{-}Y, C\text{-}Z\}\).

**(b)(iii) Optimality.** [3]

This matching is **applicant-optimal**: each applicant gets the best role it can
have in any stable matching.

**(c) Role-proposing.** [8]

- Round 1: \(X \to B\), \(Y \to A\), \(Z \to A\). \(A\) keeps \(Y\) (since
  \(X \succ Y \succ Z\)) and rejects \(Z\); \(B\) holds \(X\).
- Round 2: \(Z \to B\). \(B\) keeps \(X\) (since \(Y \succ X \succ Z\)) and
  rejects \(Z\).
- Round 3: \(Z \to C\), accepted.

The resulting matching is \(\{A\text{-}Y, B\text{-}X, C\text{-}Z\}\), which
differs from the applicant-proposing outcome: it is role-optimal.

**(d) Who benefits from proposing.** [2]

The two matchings differ (\(A\) gets \(X\) when applicants propose but \(Y\) when
roles propose, and likewise for \(B\)). This shows that whichever side proposes
does better: proposing secures the proposer-optimal stable matching, so being the
proposing side is an advantage.

## Question 3 [25 marks]

**(a) Theorems.** (Bookwork.) [5]

The Gale-Shapley algorithm always terminates and returns a stable matching, so a
stable matching exists. All executions yield the same matching, and in it every
proposer has the best partner they could have in any stable matching
(proposer-optimality).

**(b)(i) Stability of \(\{A\text{-}Z, B\text{-}Y, C\text{-}X\}\).** [4]

Applicant \(A\) holds its least preferred role \(Z\), so we look for a preferred
role that also prefers \(A\); the matching is not stable.

**(b)(ii) Blocking pair.** [4]

\((A, X)\): \(A\) prefers \(X\) to \(Z\), and \(X\) prefers \(A\) to its assigned
\(C\) (since \(B \succ A \succ C\)). Both prefer each other, so \((A, X)\) blocks
the matching.

**(c)(i) Stability of \(\{A\text{-}X, B\text{-}Y, C\text{-}Z\}\).** [7]

- \(A\) has \(X\), its first choice, so \(A\) is in no blocking pair.
- \(B\) has \(Y\), its first choice, so \(B\) is in no blocking pair.
- \(C\) has \(Z\) and would prefer \(X\) or \(Y\); but \(X\) prefers its partner
  \(A\) to \(C\) (\(B \succ A \succ C\)), and \(Y\) prefers its partner \(B\) to
  \(C\) (\(A \succ B \succ C\)), so neither will switch.

No blocking pair exists, so the matching is stable.

**(c)(ii) Why it is returned.** [5]

Applicants \(A\) and \(B\) both receive their first choice, which no stable
matching can improve on. The applicant-proposing algorithm returns the
**applicant-optimal** stable matching: each applicant is matched to the best role
it could have in *any* stable matching. Since \(A\) and \(B\) already hold their
top roles and \(C\) takes the only role left, this matching gives every applicant
the best it could possibly get, so it is exactly the one the algorithm
produces.

## Question 4 [25 marks]

**(a) Definitions.** [4]

A role \(r\) is an achievable partner for an applicant \(a\) if there is at least
one stable matching in which \(a\) is matched to \(r\). A stable matching is
applicant-optimal if every applicant is matched to their most preferred achievable
partner; that is, no applicant could be matched to a role they prefer in any
stable matching.

**(b) No applicant is rejected by an achievable partner.** [11]

We argue by induction on the rounds of the algorithm. The inductive claim is that
up to the current round no applicant has been rejected by an achievable partner.
This holds vacuously before the first rejection.

Suppose, for contradiction, that the claim first fails when role \(r\) rejects
applicant \(a\), and that \(r\) is achievable for \(a\): some stable matching \(M\)
pairs \(a\) with \(r\). The rejection means \(r\) holds a proposal from an
applicant \(a'\) whom it strictly prefers to \(a\). Because this is the first time
an achievable partner does any rejecting, \(a'\) has not yet been rejected by any
achievable partner, so \(r\) is at least as good for \(a'\) as every achievable
partner of \(a'\); in particular \(a'\) weakly prefers \(r\) to its partner in
\(M\).

Now consider \(M\). In \(M\), applicant \(a\) is matched to \(r\), and \(a'\) is
matched to some role it likes no better than \(r\). So \(a'\) prefers \(r\) to its
\(M\)-partner, and \(r\) prefers \(a'\) to \(a\), its \(M\)-partner. The pair
\((a', r)\) therefore blocks \(M\), contradicting the stability of \(M\). Hence no
achievable partner ever rejects, and the claim holds throughout.

**(c) Applicant-optimality.** [5]

During the algorithm each applicant proposes down their preference list, and by
part (b) they are never rejected by an achievable partner. So when the algorithm
ends, each applicant is matched to the most preferred role that did not reject
them, which is their most preferred achievable partner. Every applicant
simultaneously attains their best achievable partner, so the matching returned is
applicant-optimal.

**(d) The other side, and an illustration.** [5]

The symmetric argument with the roles proposing shows the role-proposing algorithm
returns the role-optimal stable matching; and the applicant-optimal matching is
simultaneously role-pessimal, giving each role its worst achievable partner. The
two one-sided algorithms therefore need not agree. For the instance on the
matching games page, with applicants \(A, B, C\) and roles \(X, Y, Z\), the
applicant-proposing algorithm pairs \(A\)-\(X\), \(B\)-\(Y\), \(C\)-\(Z\), whereas
the role-proposing algorithm pairs the better-placed applicants with the roles
that most want them: \(B\)-\(X\) and \(A\)-\(Y\), with \(C\)-\(Z\). The proposing
side does at least as well in its own run, which is why the two matchings can
differ.
