---
layout: solution
title: "Auctions"
tag: auctions
---

# Auctions: worked solutions

Solutions to the example questions on the
[Auctions](/topics/auctions.html) page.

## Question 1 [19 marks]

**(a) Second-price auction.** [3]

In a second-price (Vickrey) auction each bidder submits one sealed bid; the
highest bidder wins and pays the second-highest bid, not their own.

**(b) Truthful outcome.** [3]

With truthful bids \(10, 7, 4\), bidder 1 wins (highest bid) and pays the
second-highest bid \(7\), for a payoff of \(10 - 7 = 3\).

**(c) Truthful bidding is weakly dominant.** [7]

Fix the others' bids and let \(m\) be the highest of them. Bidding the true value
\(10\): when \(10 > m\) bidder 1 wins and pays \(m\) for payoff \(10 - m \ge 0\);
when \(10 < m\) they lose, for payoff \(0\). Compare other bids:

- Bidding above \(10\) only changes the outcome when \(m\) lies between \(10\) and
  the higher bid, in which case they win but pay \(m > 10\), a negative payoff;
  otherwise nothing changes. Never better.
- Bidding below \(10\) only changes the outcome when \(m\) lies between the lower
  bid and \(10\), in which case they now lose (\(0\)) instead of winning for
  \(10 - m > 0\); otherwise nothing changes. Never better.

So bidding \(10\) is at least as good as any other bid, whatever the others do: it
is weakly dominant.

**(d) Why this matters.** [4]

Because truthful bidding is weakly dominant, a bidder need not know or guess the
others' values or bids to bid optimally, so bidding is simple. Since the
highest-value bidder wins, the outcome is also efficient.

**(e) First-price.** [2]

No. In a first-price auction the winner pays their own bid, so bidding the true
value \(10\) and winning gives payoff \(10 - 10 = 0\). A bidder does strictly
better by shading their bid below their value, and the best amount to shade
depends on the other bidders' behaviour, so truthful bidding is neither dominant
nor optimal.

## Question 2 [21 marks]

**(a) Definitions.** (Bookwork.) [3]

- An **auction game** with \(N\) bidders consists of private valuations \(v_i\)
  drawn from random variables \(V_i\), bids \(b_i\) from bidding strategies
  \(b_i : V_i \to B_i\), an allocation rule \(q\) and a payment rule \(p\); the
  utility of bidder \(i\) is \(u_i = v_i q_i - p_i\).
- A **Bayesian Nash equilibrium** is a strategy profile in a game of incomplete
  information such that, given their own type, each player's strategy maximises
  their expected utility, assuming the other players' strategies are fixed and
  beliefs about types are correct.
- A **weakly dominant strategy** is at least as good as any other strategy
  against every opponent profile, and strictly better against at least one.

**(b)(i) Truthful bidding is weakly dominant.** [7]

Fix the others' bids and let \(m\) be the highest. Bidding \(b\) wins when
\(b > m\), paying \(m\), for payoff \(v - m\), else \(0\).

- If \(v > m\): bidding \(v\) wins for \(v - m \ge 0\); any \(b > m\) gives the
  same, any \(b \le m\) gives \(0 \le v - m\).
- If \(v < m\): bidding \(v\) gives \(0\); any \(b > m\) gives \(v - m < 0\), any
  \(b \le m\) gives \(0\).
- If \(v = m\): every bid gives \(0\).

So bidding \(v\) is always at least as good, hence weakly dominant.

**(b)(ii) Equilibrium.** [2]

Every bidder bidding their own value, \(b(v) = v\), is a Bayesian Nash
equilibrium.

**(c)(i) Expected revenue.** [3]

The winner pays the second-highest value \(\min(v_1, v_2)\), so using the
expectation given in the question,

\[
R = \mathbb{E}[\min(v_1, v_2)] = \tfrac{1}{3}.
\]

**(c)(ii) Winner's expected payoff.** [3]

The winner has value \(\max(v_1, v_2)\) and pays \(\min(v_1, v_2)\), so by
linearity of expectation and the facts given in the question the expected payoff
is

\[
\mathbb{E}[\max(v_1, v_2) - \min(v_1, v_2)]
= \tfrac{2}{3} - \tfrac{1}{3} = \tfrac{1}{3}.
\]

**(c)(iii) Revenue equivalence.** [3]

By the revenue equivalence theorem, the first-price auction for the same two
uniform bidders raises the *same* expected revenue, \(\tfrac{1}{3}\), even though
the winner pays their own (shaded) bid rather than the second value.

## Question 3 [21 marks]

**(a) Equilibrium bid.** (Bookwork.) [3]

\[
b(v) = \frac{N - 1}{N}\, v, \qquad \text{which for } N = 2 \text{ gives } b(v) = v/2.
\]

**(b)(i) Expected revenue.** [3]

Both bidders bid half their value, so the bidder with the higher value places
the higher bid and wins. In a first-price auction the winner pays their own
bid, which is half their value: the payment is \(\max(v_1, v_2)/2\). Using the
expectation given in the question,

\[
R = \tfrac{1}{2}\,\mathbb{E}[\max(v_1, v_2)]
= \tfrac{1}{2}\times\tfrac{2}{3} = \tfrac{1}{3}.
\]

**(b)(ii) Expected payoff of a bidder with value \(v\).** [4]

A bidder with value \(v\) wins when the other's value is below \(v\), which by
the given uniform probability \(\mathbb{P}(v_1 \leq z) = z\) has probability
\(v\), and then pays \(v/2\):

\[
(v - \tfrac{v}{2})\cdot v = \frac{v^2}{2}.
\]

**(b)(iii) Second-price revenue.** [3]

The second-price auction raises \(\mathbb{E}[\min(v_1, v_2)] = \tfrac{1}{3}\), the
same as the first-price auction. This is the revenue equivalence theorem: the two
formats raise equal expected revenue.

**(c) Intuition.** [5]

In both formats a bidder with value \(v\) wins exactly when the other value is
below \(v\), so their probability of winning is \(v\). Compare their expected
payoffs. In the first-price auction, part (b)(ii) gives \(v^2/2\). In the
second-price auction they bid truthfully, win with probability \(v\), and pay
the other's value. Conditional on being below \(v\), the other's value is
uniform on \([0, v]\), so the payment averages the midpoint \(v/2\): again

\[
v\left(v - \tfrac{v}{2}\right) = \frac{v^2}{2}.
\]

This is no coincidence. A bidder's payoff comes entirely from knowing their own
value, and what that knowledge is worth depends only on how often each value
wins, which the two formats share. Once the expected payoff is pinned down, so
is the expected payment: the bidder receives value \(v\) with probability
\(v\), worth \(v^2\), so in either format they pay \(v^2 - \tfrac{v^2}{2} =
\tfrac{v^2}{2}\) on average. The seller's revenue is the total of these
expected payments, hence equal. In other words, the bid shading in the
first-price auction exactly offsets, on average, the discount of paying the
second price.

**(d) Conditions.** [3]

Revenue equivalence requires that the two auctions (i) always allocate the item to
the bidder with the highest value, and (ii) give a bidder with the lowest possible
value (here \(v = 0\)) zero expected surplus. Both hold here: each format awards
the item to the highest bidder, and a bidder with value \(0\) never profits in
either, so the theorem applies and the revenues coincide.

## Question 4 [25 marks]

**(a) Winning probability and expected payoff.** [6]

Because \(b\) is strictly increasing, bidder 1's bid \(b(z)\) beats another
bidder's bid \(b(v_j)\) precisely when \(z > v_j\). The \(N - 1\) other values are
independent and uniform on \([0, 1]\), so

\[
\mathbb{P}(\text{win}) = \mathbb{P}(v_j < z \text{ for all } j \neq 1) = z^{N-1},
\]

ties having probability zero. Winning yields a surplus \(v - b(z)\) and the bidder
pays only on winning, while losing yields zero, so

\[
U(z) = z^{N-1}\bigl(v - b(z)\bigr).
\]

**(b) The equilibrium bid.** [10]

Differentiating,

\[
U'(z) = (N-1) z^{N-2}\bigl(v - b(z)\bigr) - z^{N-1} b'(z).
\]

Optimality at \(z = v\) requires \(U'(v) = 0\):

\[
(N-1) v^{N-2}\bigl(v - b(v)\bigr) - v^{N-1} b'(v) = 0.
\]

Expanding and rearranging,

\[
(N-1) v^{N-1}
= (N-1) v^{N-2} b(v) + v^{N-1} b'(v)
= \frac{d}{dv}\bigl[v^{N-1} b(v)\bigr].
\]

Integrating from \(0\) to \(v\) and using \(b(0) = 0\),

\[
v^{N-1} b(v) = (N-1) \int_0^v t^{N-1}\, dt = (N-1)\frac{v^N}{N},
\qquad \text{so} \qquad
b(v) = \frac{N-1}{N}\, v.
\]

A bidder shades their bid below their value, and the shading shrinks as \(N\)
grows: more competition pushes bids towards the value.

**(c) Expected revenue.** [5]

The seller receives the winning bid, \(b\) evaluated at the largest value:

\[
\mathbb{E}[\text{revenue}]
= \mathbb{E}\!\left[b\Bigl(\max_i v_i\Bigr)\right]
= \frac{N-1}{N}\, \mathbb{E}\!\left[\max_i v_i\right].
\]

The maximum of \(N\) independent uniform values is the \(N\)-th smallest, so the
fact given in the question yields \(\mathbb{E}[\max_i v_i] = \dfrac{N}{N+1}\) and
the expected revenue is
\(\dfrac{N-1}{N} \cdot \dfrac{N}{N+1} = \dfrac{N-1}{N+1}\).

**(d) Revenue equivalence.** [4]

The revenue equivalence theorem states that, when values are independent and
identically distributed, any two auctions that always award the item to the
highest-value bidder and give a bidder with the lowest possible value zero
expected surplus raise the same expected revenue for the seller. In the
second-price auction the winner pays the second-highest value, that is the
\((N-1)\)-th smallest of the \(N\) uniform values, so by the fact given in the
question the expected revenue is \(\dfrac{N-1}{N+1}\), the same as in part (c).

## Marking exercises

**Marking exercise 1 (Question 1(c)).**

Two errors, one of kind and one of coverage.

- The dominance is *weak*, not strict. If the highest rival bid is \(5\),
  then bids of \(8\), \(10\) and \(12\) all win and all pay \(5\): identical
  payoffs, so bidding \(10\) is not strictly better than every alternative.
  In a second-price auction the bid only decides *whether* you win, not what
  you pay, so most changes of bid change nothing at all. That is precisely
  why the correct claim is weak dominance.
- The argument checks one alternative bid against one convenient rival bid
  each. Dominance is a statement about *every* alternative bid against
  *every* configuration of rival bids: the argument must split into cases by
  where the highest rival bid \(m\) falls relative to the two bids, as in
  the solution above, and show the truthful bid is never worse in any case.

A fair mark is [3] of [7]: the two scenarios chosen do illustrate the two
ways a deviation can hurt, but the claim proved is the wrong one and the
case analysis is incomplete.

**Marking exercise 2 (Question 3(b)(i) and (iii)).**

The first-price revenue forgets the equilibrium: the question sets both
bidders' strategies to \(b(v) = v/2\), so the winner pays half the higher
value and the revenue is
\(\tfrac{1}{2}\mathbb{E}[\max(v_1, v_2)] = \tfrac{1}{3}\), as in the
solution above. Bidders who pay their own bids shade them; taking the
revenue to be \(\mathbb{E}[\max]\) prices a first-price auction as if
bidders were truthful.

The second-price value \(\tfrac{1}{3}\) is right, but the conclusion is then
exactly backwards: the two formats raise the *same* expected revenue, which
is the revenue equivalence theorem, whose conditions part (d) verifies for
this setting. The claim that sellers should prefer first-price auctions
because they raise twice as much is wrong on both counts. A fair mark is
[1] of [3] for (b)(i), which correctly identifies who wins, and [1] of [3]
for (b)(iii), where the number is right but the stated relationship between
the formats is the opposite of the theorem the part asks for.
