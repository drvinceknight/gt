---
layout: post
title: "Routing Games: Pigou's example"
tags:
  - routing-games
---

In class today we looked at the [Routing Games](https://vknight.org/gtb/main-10/). 
We did this by considering Pigou's Example.

You can see a recording of this [here](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=f0229828-d3d4-4566-b468-b38500a54ea6).

Pigou's example is a simple model of congestion there are 2 choices available to
traffic, the first is not affected by traffic, the other is heavily affected by
traffic (the more people using it, the worse it is).

This simple situation is modelling as a routing game which requires the network
diagram and congestion functions you can see here:

![]({{site.baseurl}}/assets/2025-2026/boards/2025-11-03/main.jpg)

The calculations we carried out included:

- Identifying the most *efficient* flow: half the population take each edge.
- Identifying the Nash flow: the entire population using the shortcut (making it
as slow as the other way)
- Finding the Nash flow by optimising the Potential function.
- Finding the optimal flow by finding the Nash flow for a slightly modified
game.

The final thing I spoke about was Braess' Paradox which is an important idea, it
is theoretically interesting but empirically has real negative implications:
adding capacity to networks may lead to a worse performance.
