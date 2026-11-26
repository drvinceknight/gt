---
layout: class-notes
title: "Auctions"
tag: "auctions"
---

## Activity (20 minutes)

**Goal.** Compare a first-price and a second-price sealed auction with private
values, see bidders shade in one and bid their value in the other, and find that
the seller makes about the same from both.

**The deck.** There is a write-on deck at
[/decks/auctions/main.pdf](/decks/auctions/main.pdf): the rules and payoff
left blank, to fill in before anyone plays; a single "While you play" slide
with the rules of both rounds, two grids of bid against value and the average
price boxes; the two cases of the weak dominance argument on number lines; the
shaded first-price bid; and the seller's revenue in each format.

Every slide of the deck names the numbered section of the notes it is reading,
and the last slide gathers them into one table, marks what is examinable and
sets the reading for the next class. Leave the "While you play" slide up while
the room plays.

**Requires one D12 per student, or per group passed round.** The class already
ran the dollar auction, where everyone's value is the same; here each value is
private, which is the setting of the chapter and of Question 1.

Put the room in threes. Each student rolls a D12 without showing anyone: that
is their value for the item. Each writes a bid on paper and the three reveal at
once.

1. Round 1, first price. The highest bid wins and pays its own bid; the winner
   scores their value minus their bid, the others score 0.
2. Round 2, second price. Everyone rolls a fresh value. The highest bid wins and
   pays the second highest bid.

Every winner gets bribentives based on their score, value minus price, so the
prize is the auction's own payoff and depends on how well they bid rather than
on the die. Do not reward the highest value: that is luck, and it would give
nobody a reason to bid carefully.
Then collect a handful of groups' values and bids for each round and mark them
on the two grids: second-price bids should sit near the line bid = value and
first-price bids below it. Ask each group for the price paid in each round and
write the two averages in.

## Discussion (20 minutes)

Work through the Auctions chapter.

Discussion Point: **After the definition of an auction, ask what the rules are
for the sealed auction we just played.**

Discussion Point: **After two theorems ask why I chose the auction I did?**

**Close on the last slide.** It names what the class was reading and points to
the Order Statistics appendix as extra reading, for anyone who wants to see
where the averages of 9 and 6 come from. Then run the quick quiz from the [Auctions topic
page](/topics/auctions.html): five questions on the screen, answered by a show
of hands. It takes five minutes and tells us both what landed.

## Answers for the deck

The values, bids and average prices come from the room. These are the rest.

**The rules.** Everyone submits one sealed bid without seeing anyone else's, and
the highest bidder wins. In a first-price auction the winner pays their own bid;
in a second-price auction they pay the second highest bid. With value \(v\), the
second-price payoff is \(v\) minus the second highest bid for the winner and
\(0\) for everyone else.

**Should you bid your value?** Write \(v\) for your value and \(b\) for the
highest bid among everybody else. You win when your bid beats \(b\), and you
then pay \(b\) whatever you bid, so your bid only changes *whether* you win, not
what you pay.

- Bidding above \(v\) only wins you the extra auctions where \(b\) lies between
  \(v\) and your bid. In those you pay \(b > v\) and make a loss.
- Bidding below \(v\) only loses you auctions where \(b\) lies between your bid
  and \(v\), which you would have won at a profit. When you still win you pay
  the same \(b\) as before.

Neither can do better, so bidding your true value is weakly dominant.

**First price.** Bidding your value and winning scores \(0\), so you shade
below it. With \(N\) bidders and values uniform, the equilibrium bid is
\(b = \frac{N - 1}{N}v\): the book states it for values on \([0, 1]\), and it
scales to any interval starting at \(0\). With \(N = 3\), \(b = \frac{2}{3}v\),
the line drawn on the first-price grid. In a second-price auction you need to
know nothing about the others; in a first-price auction how far to shade
depends on how many others there are.

**What the seller made.** With three values uniform on \([0, 12]\), the highest
averages \(9\) and the second highest \(6\): the \(k\)-th smallest of \(N\)
uniform values averages \(\frac{k}{N + 1}\) of the way along, which is the
theorem on expected order statistics in the book's
[Order Statistics appendix](https://vknight.org/gtb/appendices/order-statistics/). The second-price seller gets the
second highest value, \(6\) on average; the first-price seller gets
\(\frac{2}{3}\) of the highest, also \(6\). That is revenue equivalence. A D12 is
discrete, so the room's exact targets are slightly different: \(6.5\) for the
second-price round and about \(6.3\) for the first-price round if everyone bids
\(\frac{2}{3}v\). Either way the two averages should be close, and a gap of a
pound or so between them is noise from a few dozen groups.

## From the activity to the exam answer

The activity above is written up as a marked exam question: **Question 1 (the in-class activity)** on the [Auctions](/topics/auctions.html) page, with a full worked solution. Closing the loop here is the step that helps students who find exams hard: work through that question together, or set it as the immediate follow-up, so they see the game they just played turned into a full-mark answer.
