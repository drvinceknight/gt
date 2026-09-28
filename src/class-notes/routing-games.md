---
layout: class-notes
title: "Routing Games"
tag: routing-games
---

## Activity (20 minutes)

**Goal.** Let students reach a Nash flow by selfish routing, compare it to the
optimal flow, and experience Braess's paradox: adding a road can make everyone
worse off.

**The deck.** There is a write-on deck at
[/decks/routing-games/main.pdf](/decks/routing-games/main.pdf): one page per
step, with the network already drawn and every number the class produces left
blank. Project it and annotate it live on a tablet, so no class time goes on
drawing the network and the finished pages can be shared afterwards.

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

## Answers for the deck

The counts in Phase 1 and Phase 2 come from the room. These are the rest.

**Phase 1.** The class settles at 20 and 20, so each route takes
\(20 + 50 = 70\) minutes. A driver who switches sides makes their new road carry
21 cars, so their own time goes from \(70\) to \(71\): nobody moves, and this is
a Nash flow. Here it is also the optimal flow.

**Phase 2.** All 40 end up on \(S \to A \to B \to T\), taking
\(40 + 0 + 40 = 80\) minutes. Switching back to \(S \to A \to T\) would cost
\(40 + 50 = 90\), so nobody does.

**Why it got worse.** Joining a road that already carries \(x\) cars, my own
time is \(x + 1\) minutes, and I add one minute to each of the \(x\) drivers
already there, so \(x\) minutes to everyone else. I pay the first and ignore the
second. The road's total time is \(x \, c(x) = x^{2}\), and one more car really
adds \(\frac{\mathrm{d}}{\mathrm{d}x}(x \, c(x)) = 2x\), not \(1\).

**Writing it down.** With \(C(f) = \sum_{e} f_e c_e(f_e)\), before the new road

\[
C(f) = 20 \times 20 + 20 \times 50 + 20 \times 50 + 20 \times 20 = 2800,
\]

which is \(70\) minutes each, and after it

\[
C(f) = 40 \times 40 + 40 \times 0 + 40 \times 40 = 3200,
\]

which is \(80\) minutes each.

**Price of anarchy.** Left alone we take \(80\) minutes each. A planner who
ignored the new road and sent 20 each way would give us \(70\), so the price of
anarchy is \(80/70 = 8/7 \approx 1.14\). This is the value asked for in
Question 1(e).

## From the activity to the exam answer

The activity above is written up as a marked exam question: **Question 1 (the in-class activity)** on the [Routing Games](/topics/routing-games.html) page, with a full worked solution. Closing the loop here is the step that helps students who find exams hard: work through that question together, or set it as the immediate follow-up, so they see the game they just played turned into a full-mark answer.
