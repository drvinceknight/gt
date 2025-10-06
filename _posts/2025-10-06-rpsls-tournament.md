---
layout: post
title: "A rock paper scissors lizard spock tournament"
tags:
  - about
  - nash-equilibrium
---

In class today we gave a quick summary of what we have seen so far, ran a Rock
Paper Scissor Lizard Spock tournament (**Tom** took my candy **again**) and talked
over the support enumeration algorithm which is the important part of the Nash
equilibrium chapter.

A recording of the class is available [here](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=543e2f80-0614-4528-be4b-b36900b5dcf2).

### Summary of the first week

I asked you all to talk amongst yourselves and remind each other what we saw
last week. We came up with:

- Definitions of Normal Form and Extensive Form Games (we have mainly used
  Normal Form Games so far);
- Calculation of expected utilities;
- Some specific types of strategies:
  - Dominated strategies: ones that should never be played
  - Best response strategies: given what everyone else is doing (an incomplete
    strategy profile) what is the best thing to do.

### A rock paper scissors lizard tournament

After this we moved on to class rock paper scissors lizard spock tournament.

The first time I heard of this game (a variation of rock paper scissors) was in
an episode of the Big Bang Theory. You can find a clip of it here:
[YouTube](https://youtu.be/x5Q6-wMx-K8) and a summary of the rules are available
[here](https://github.com/drvinceknight/gt/blob/main/do/static/rpsls/main.pdf).

Before we started I asked us to modify the rules so that you could only choose
from 2 actions:

- Paper
- Lizard

This was not interesting: everyone just picked Lizard. Adding Rock (or indeed
any of the other actions) adds a best response.

After everyone played their tournaments (a knock out with a final)
following that there was a "last player standing" session which lead to the
grand final. **Tom** was victorious here and we had a
conversation about what made someone be good at Rock Paper Scissors Lizard
Spock.

Quite quickly we got to the idea of being unpredictable as opposed to knowing
something about your opponent (**Peter** mentioned that apparently we are all more
likely to play Rock first).

### The Support Enumeration Algorithm

I talked over the [Support Enumeration algorithm in the Nash equilibrium chapter](https://vknight.org/gtb/main-4/#def-support-enumeration-algorithm).
This is an algorithm that uses the [Best Response Condition from the previous
chapter](https://vknight.org/gtb/main-2/#thrm-best-response-condition) to
systematically check all places a Nash equilibrium **could be**.

The first step of the algorithm is to consider all potential pairs of
[supports](https://vknight.org/gtb/main-2/#sec-rock-paper-scissors-lizard-spock)
of a strategy: this corresponds to considering all possible allow actions.

In the case of Rock Paper Scissors where there are 3 actions overall this gives:
\\(3 + 3 + 1=7\\) actions (3 support with just one action, 3 supports with one omitted
action and 1 support with all actions). The algorithm requires us to consider
all pairs of potential supports which is technically \\(7 ^ 2 = 49\\) although
practically, as we will see, we will do much less.
