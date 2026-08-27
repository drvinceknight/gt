---
layout: topic
title: "Auctions"
tag: auctions
note_urls:
  - "https://vknight.org/gtb/chapters/auction-games/"
---

## Example questions

The following are exam-type questions in the style of the examination paper,
with marks at the rates used in the papers. **A question totalling fewer than
25 marks would, in the examination, be combined with further parts, often one
of the examinable proofs, to make a full 25-mark question.** Attempt them in
full before reading the worked solutions. Some parts use expected values of
ordered uniform samples; each question states the facts you may use, and their
derivations are in the
[order statistics appendix](https://vknight.org/gtb/appendices/order-statistics/)
of the textbook.

### Question 1 (based on the in-class activity)

In class we ran a sealed-bid second-price auction. Suppose three bidders have
private values \(v_1 = 10\), \(v_2 = 7\) and \(v_3 = 4\); the highest bidder wins
and pays the second-highest bid.

(a) Explain the rules of a second-price (Vickrey) auction. [3]

(b) If all bidders bid truthfully, determine the winner, the price paid and the
winner's payoff. [3]

(c) Show, for bidder 1, that bidding the true value \(v_1 = 10\) is a weakly
dominant strategy, by considering bids above and below 10 and showing neither
can do better whatever the others bid. [7]

(d) Explain why truthful bidding being a weakly dominant strategy is a desirable
property of the second-price auction. [4]

(e) If the auction were instead first-price (the winner pays their own bid),
would bidding your true value still be weakly dominant? Briefly explain. [2]

### Question 2

(a) Provide definitions for the following terms:

   - an auction game;
   - a Bayesian Nash equilibrium;
   - a weakly dominant strategy. [3]

(b) Consider a sealed-bid second-price (Vickrey) auction for a single item, where
the highest bidder wins and pays the second-highest bid.

   (i) Show that bidding one's value \(b = v\) is a weakly dominant strategy. [7]

   (ii) Hence state the Bayesian Nash equilibrium. [2]

(c) Two bidders have values drawn independently from the uniform distribution on
\([0, 1]\) and bid truthfully. You may use that for two such values,
\(\mathbb{E}[\min(v_1, v_2)] = \tfrac{1}{3}\) and
\(\mathbb{E}[\max(v_1, v_2)] = \tfrac{2}{3}\).

   (i) Compute the seller's expected revenue. [3]

   (ii) Compute the expected payoff to the winning bidder. [3]

   (iii) State, without further calculation, what the revenue equivalence theorem
   says the seller's expected revenue would be in a first-price auction for these
   bidders. [3]

### Question 3

(a) State the symmetric Bayesian Nash equilibrium bidding function for \(N\)
bidders with values uniform on \([0, 1]\) in a first-price auction. [3]

(b) Take two such bidders, each bidding \(b(v) = v/2\). You may use that for two
independent values \(v_1, v_2\) uniform on \([0, 1]\),
\(\mathbb{P}(v_1 \leq z) = z\) for \(z \in [0, 1]\),
\(\mathbb{E}[\min(v_1, v_2)] = \tfrac{1}{3}\) and
\(\mathbb{E}[\max(v_1, v_2)] = \tfrac{2}{3}\).

   (i) Compute the seller's expected revenue. [3]

   (ii) Compute the expected payoff of a bidder who knows their own value is
   \(v\), taking the expectation over the other bidder's value. [4]

   (iii) Compute the seller's expected revenue in the corresponding second-price
   auction and state the revenue equivalence result. [3]

(c) Explain the intuition behind revenue equivalence. [5]

(d) State the two conditions on the auctions that the revenue equivalence theorem
requires, and confirm that they hold here. [3]

### Question 4 (**hard**)

A single item is sold by sealed-bid first-price auction to \(N\) bidders. The
values \(v_1, \dots, v_N\) are independent, each uniform on \([0, 1]\). The
highest bidder wins and pays their own bid. We look for a symmetric equilibrium in
which every bidder uses the same strictly increasing, differentiable bidding
function \(b\) with \(b(0) = 0\). Throughout you may use that a value uniform on
\([0, 1]\) satisfies \(\mathbb{P}(v_i \leq z) = z\) for \(z \in [0, 1]\), and that
the expected value of the \(k\)-th smallest of \(N\) independent such values is
\(\dfrac{k}{N + 1}\).

(a) Suppose every bidder other than bidder 1 uses \(b\). If bidder 1 has value
\(v\) and submits the bid \(b(z)\), that is bids as though their value were
\(z\), show that the probability they win is \(z^{N-1}\), and hence that their
expected payoff is \(U(z) = z^{N-1}\bigl(v - b(z)\bigr)\). [6]

(b) In equilibrium the optimal choice is \(z = v\) for every \(v\). Use this to
derive the differential equation
\(\dfrac{d}{dv}\bigl[v^{N-1} b(v)\bigr] = (N-1) v^{N-1}\), and solve it with
\(b(0) = 0\) to obtain \(b(v) = \dfrac{N-1}{N}\, v\). [10]

(c) Show that the seller's expected revenue is \(\dfrac{N-1}{N+1}\). [5]

(d) State the revenue equivalence theorem, and verify it for these bidders by
computing the seller's expected revenue in the corresponding second-price
auction. [4]

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

### Marking exercise 1 (on Question 1(c), worth [7])

A student pastes Question 1(c) into a free AI chatbot, which replies:

```text
Claim: bidding the true value v1 = 10 is a strictly dominant strategy.

Suppose bidder 1 bids 12 instead. If the highest rival bid is 11,
bidder 1 wins and pays 11, making a loss of 1. So bidding higher is
worse.

Suppose bidder 1 bids 8 instead. If the highest rival bid is 9, bidder
1 loses and gets 0, whereas bidding 10 would have won for a profit of
1. So bidding lower is worse.

Since bidding higher is worse and bidding lower is worse, bidding
exactly 10 is strictly dominant. ∎
```

### Marking exercise 2 (on Question 3(b)(i) and (iii), worth [3] and [3])

A student pastes Question 3(b) into a free AI chatbot, which replies:

```text
First-price revenue: the winner is the bidder with the higher value and
pays their own bid, so the seller's expected revenue is
E[max(v1, v2)] = 2/3.

Second-price revenue: the winner pays the second-highest value, so the
expected revenue is E[min(v1, v2)] = 1/3.

Conclusion: the first-price auction raises twice the revenue of the
second-price auction, which is why sellers generally prefer first-price
auctions. 💰
```

## Optional further reading

You do not need any of this to follow the topic, but the following may help if
you would like more background:

- [Order Statistics](https://vknight.org/gtb/appendices/order-statistics/),
  which derives the expected values of ordered uniform samples that the
  questions above state as given facts.
