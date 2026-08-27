---
layout: class-notes
title: "Routing Games"
tag: routing-games
---

## Activity (20 minutes)

**Goal.** Let students reach a Nash flow by selfish routing, compare it to the
optimal flow, and experience Braess's paradox: adding a road can make everyone
worse off.

**The network.** Drivers travel from Start ($S$) to End ($T$). Draw two routes
on the board:

- A top route: $S \to A$ along a small road whose travel time in minutes equals
  the number of cars on it, then $A \to T$ along a motorway fixed at 50 minutes.
- A bottom route: $S \to B$ along a motorway fixed at 50 minutes, then
  $B \to T$ along a small road whose time equals the number of cars on it.

**Phase 1 (no shortcut).**

1. Each student picks the top or bottom route and stands on that side. The
   number of students on a small road is its travel time.
2. Announce the two route times and let students re-choose to lower their own
   time, lobbing a few small bribentives to whichever route is currently faster.
   Repeat until nobody wants to switch.

With a class of 40 the split settles at 20 and 20, each route taking
$20 + 50 = 70$ minutes. This is the Nash flow, and here it is also the optimal
flow.

**Phase 2 (add a shortcut).**

3. Add a brand-new, instant road from $A$ to $B$ taking 0 minutes. There is now
   a tempting route $S \to A \to B \to T$ that uses both small roads and skips
   both motorways.
4. Let students re-choose, again tossing a few small bribentives to whichever
   route is currently faster. Everyone is drawn onto $S \to A$ and $B \to T$, so
   the class funnels onto the zig-zag: all 40 on each small road, taking
   $40 + 0 + 40 = 80$ minutes.
5. Point out that nobody can do better by switching back: the old routes now
   cost $40 + 50 = 90$ minutes. The new road is a Nash flow that is worse for
   everyone, 80 against 70.

## Discussion (20 minutes)

Discuss the **Routing Games** chapter.

Discussion Point: **After the definitions of flow and cost, ask students to
write down the flow and the costs in our network.**

Discussion Point: **After the definitions of Nash flow and optimal flow, ask
which was which in each phase, and why they differed once the shortcut was
added.**

Discussion Point: **After the potential function and marginal cost results, ask
students how each driver ignoring the congestion they impose on others explains
Braess's paradox.**

## From the activity to the exam answer

The activity above is written up as a marked exam question: **Question 1 (the in-class activity)** on the [Routing Games](/topics/routing-games.html) page, with a full worked solution. Closing the loop here is the step that helps students who find exams hard: work through that question together, or set it as the immediate follow-up, so they see the game they just played turned into a full-mark answer.
