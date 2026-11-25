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

Every slide of the deck names the numbered section of the notes it is reading,
and the last slide gathers them into one table, marks what is examinable and
sets the reading for the next class. A "While you play" slide carries the rules:
leave it up while the room plays.

**The network.** Drivers travel from Start ($S$) to End ($T$). Draw two routes
on the board:

- A top route: $S \to A$ along a small road whose travel time in minutes equals
  the number of cars on it, then $A \to T$ along a motorway fixed at 50 minutes.
- A bottom route: $S \to B$ along a motorway fixed at 50 minutes, then
  $B \to T$ along a small road whose time equals the number of cars on it.

**Phase 1 (no shortcut).**

1. Each student picks the top or bottom route and puts a hand up when it is
   called. The number of hands for a route is the travel time on its small road.
2. Announce the two route times and ask again: anyone may switch to lower their
   own time, and a few small bribentives go to whichever route is currently
   faster. Repeat until nobody wants to switch.

With a class of 40 the split settles at 20 and 20, each route taking
$20 + 50 = 70$ minutes. This is the Nash flow, and here it is also the optimal
flow.

**Phase 2 (add a shortcut).**

3. Add a brand-new, instant road from $A$ to $B$ taking 0 minutes. There is now
   a tempting route $S \to A \to B \to T$ that uses both small roads and skips
   both motorways.
4. Call the three routes for hands again and let students re-choose, again
   tossing a few small bribentives to whichever route is currently faster.
   Everyone is drawn onto $S \to A$ and $B \to T$, so the class funnels onto the
   zig-zag: all 40 on each small road, taking
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

**Close on the last slide.** It names what the class was reading and sets the
reading for next time. Then run the quick quiz from the [Routing Games topic
page](/topics/routing-games.html): five questions on the screen, answered by a
show of hands. It takes five minutes and tells us both what landed.

## Answers for the deck

The counts in Phase 1 and Phase 2 come from the room. These are the rest.

**Phase 1.** The class settles at 20 and 20, so each route takes
\(20 + 50 = 70\) minutes. In the room, a driver who switches sides makes their
new road carry 21 cars, so their own time goes from \(70\) to \(71\). The slide
then makes the step to the model, where the traffic is non-atomic: each driver
is a negligible share of a flow of 40, one switch changes no road's time, and a
Nash flow is simply one where every used route takes the least time. Both routes
take 70, so this is a Nash flow. Here it is also the optimal flow. This
distinction is worth naming out loud, since the chapter's definitions, the
integral in the potential and the derivative in the marginal cost all rely on
it.

**Phase 2.** All 40 end up on \(S \to A \to B \to T\), taking
\(40 + 0 + 40 = 80\) minutes. Switching back to \(S \to A \to T\) would cost
\(40 + 50 = 90\), so nobody does.

**Why it got worse.** Add a sliver \(\delta\) of traffic to a road that already
carries \(x\). The sliver spends \(x\) minutes per driver, \(x\delta\) in all,
and slows each of the \(x\) already there by \(\delta\), another \(x\delta\). A
driver feels the first and ignores the second. The road's total time is
\(x \, c(x) = x^{2}\), so the sliver really adds
\(\frac{\mathrm{d}}{\mathrm{d}x}(x \, c(x))\,\delta = 2x\delta\): \(80\) minutes per
driver at \(x = 40\), against the \(40\) each one feels.

**Writing it down.** With \(C(f) = \sum_{e} f_e c_e(f_e)\), before the new road

\[
C(f) = 20 \times 20 + 20 \times 50 + 20 \times 50 + 20 \times 20 = 2800,
\]

which is \(70\) minutes each, and after it

\[
C(f) = 40 \times 40 + 40 \times 0 + 40 \times 40 = 3200,
\]

which is \(80\) minutes each.

**The two theorems.** The potential \(\Phi(f) = \sum_e \int_0^{f_e} c_e(x)\,
\mathrm{d}x\) is \(1600\) for the room's flow, all 40 on the new route, against
\(2400\) for twenty each way: the Nash flow minimises \(\Phi\), not the time.
The potential is an integral rather than a sum because the traffic is
non-atomic.
For the marginal costs, \(2x\) on a small road, \(50\) on a motorway and \(0\)
on the new road, the Nash flow sends 10 along the new road and 15 along each of
the other routes. Every route then costs \(100\) marginal minutes, and by the
second theorem this is the optimal flow.

**Price of anarchy.** The Nash flow costs \(C(\tilde f) = 3200\). The optimal
flow has 25 cars on each small road and 15 on each motorway, so
\(C(f^{*}) = 2 \times 25^{2} + 2 \times 15 \times 50 = 2750\), and the price of
anarchy is \(3200/2750 = 64/55 \approx 1.16\). Expect someone to say that a
planner would ignore the new road and send twenty each way: that costs
\(2800\), better than the room but not optimal, because a little use of the new
road helps. Question 1 on the topic page uses the normalised network instead,
one unit of traffic with motorways costing \(1\), where the planner ignores the
new road and the price of anarchy is \(4/3\).

## From the activity to the exam answer

The activity above is written up as a marked exam question: **Question 1 (the in-class activity)** on the [Routing Games](/topics/routing-games.html) page, with a full worked solution. Closing the loop here is the step that helps students who find exams hard: work through that question together, or set it as the immediate follow-up, so they see the game they just played turned into a full-mark answer.
