---
layout: post
title: "Routing Games: Pigou's example"
tags:
  - matching-games
  - auctions
---

In class on Friday we looked at [matching-games](https://vknight.org/gtb/main-11/) and today we looked at
[auctions](https://vknight.org/gtb/main-12/).

You can see a recording of this:

- [here for matching games](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=778eb9d3-e2c0-4212-abd2-b3890108341e).
- [here for auctions](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=34e3c6db-636a-4d71-87dc-b38c00a55902).

### Matching Games

For Matching games I started by asking you to come up with individual rankings
for physicists to work with mathematicians and versa:

![]({{site.baseurl}}/assets/2025-2026/boards/2025-11-07/main.jpg)

Using this we described potential matchings. In our particular case this always
lead to a bad matching for Turing but this was nonetheless the only matching
that was stable.

We then spoke about the Gale-Shapley algorithm which is a powerful yet simple
tool for finding stable matchings.

### Auctions

Today we started with another auction for a £5 note.

I started by asking you all to write down what you thought was the value of that
£5 to you. Some of you assigned quite a high value (more than £5) and some quite
a low value (less than £5).

![]({{site.baseurl}}/assets/2025-2026/boards/2025-11-07/main.jpg)

After that I said that the auction would be that the highest bidder would win
the £5 and pay the second highest bid.

This lead to a discussion about what the optimal bidding pattern was based on
value. Tim, who "won" the £5 (and owes me £7) had a strategy based on the
assumption that everyone would bid *near* £5 so his winning bid of £50 would
work.

There are two theorems with the associated chapter, the first of which actually
shows in expectation the optimal bid is to in fact bid your value.
