---
layout: topic
title: "Auctions"
tag: auctions
note_urls:
  - "https://vknight.org/gtb/chapters/auction-games/"
---

## Example questions

The following are exam-type questions in the style of the examination paper.
**Each question is worth 25 marks.** Attempt them in full before reading the
worked solutions.

### Question 1 (based on the in-class activity)

In class we ran a sealed-bid second-price auction. Suppose three bidders have
private values \(v_1 = 10\), \(v_2 = 7\) and \(v_3 = 4\); the highest bidder wins
and pays the second-highest bid.

(a) Explain the rules of a second-price (Vickrey) auction. [3]

(b) If all bidders bid truthfully, determine the winner, the price paid and the
winner's payoff. [4]

(c) Show, for bidder 1, that bidding the true value \(v_1 = 10\) is a weakly
dominant strategy, by considering bids above and below 10 and showing neither
can do better whatever the others bid. [9]

(d) Explain why truthful bidding being a weakly dominant strategy is a desirable
property of the second-price auction. [7]

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
\([0, 1]\) and bid truthfully.

   (i) Compute the seller's expected revenue. [5]

   (ii) Compute the expected payoff to the winning bidder. [5]

   (iii) State, without further calculation, what the revenue equivalence theorem
   says the seller's expected revenue would be in a first-price auction for these
   bidders. [3]

### Question 3

(a) State the symmetric Bayesian Nash equilibrium bidding function for \(N\)
bidders with values uniform on \([0, 1]\) in a first-price auction. [3]

(b) Take two such bidders, each bidding \(b(v) = v/2\).

   (i) Compute the seller's expected revenue. [5]

   (ii) Compute the interim expected payoff of a bidder with value \(v\). [5]

   (iii) Compute the seller's expected revenue in the corresponding second-price
   auction and state the revenue equivalence result. [4]

(c) Explain the intuition behind revenue equivalence. [5]

(d) State the two conditions on the auctions that the revenue equivalence theorem
requires, and confirm that they hold here. [3]

### Question 4 (**hard**)

A single item is sold by sealed-bid first-price auction to \(N\) bidders. The
values \(v_1, \dots, v_N\) are independent, each uniform on \([0, 1]\). The
highest bidder wins and pays their own bid. We look for a symmetric equilibrium in
which every bidder uses the same strictly increasing, differentiable bidding
function \(b\) with \(b(0) = 0\).

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
