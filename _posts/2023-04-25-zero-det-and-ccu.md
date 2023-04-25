---
layout: post
title:  "Zero Determinant strategies and CCU interactions"
tags:
    - prisoners-dilemma
    - best-responses
    - contemporary-research
---

In class today I discussed this paper two papers:

- [Iterated Prisoner's Dilemma contains strategies that dominate any evolutionary opponent](http://www.pnas.org/content/109/26/10409.abstract)
- [Measuring the price of anarchy in critical care unit interactions](https://link.springer.com/article/10.1057/s41274-016-0100-8)

A recording of the class is available here:
[cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=42e029aa-0366-4733-a6a9-afea0094ebae](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=42e029aa-0366-4733-a6a9-afea0094ebae).

The two papers are pretty different, the first looks at specific strategies for
the Prisoners Dilemma (and when this paper was published it made a lot of noise)
and the second is an application of Game Theory to health care interactions.

Here is a brief summary of the Press and Dyson paper:

- This is a paper that looks at memory one strategies in the IPD.
- The paper makes use of a clever mathematical theorem (Cramer's theorem) to
  show that there is a
  linear relationship between the utility of two memory 1 players (eqn 6).
- This
  shows that it's possible for one player to set the score of the other. **It is
  however not possible for a player to set it's own score.**.
- The paper then goes on to show that **it is** possible to set a value where
  the strategy's payoff is a factor of \\(\chi\\) more than the opponent.
  This
  **linkage** (it is now a win-win situation) of the strategies implies that
  both strategies maximise their payoffs when the opponent cooperates.
- The paper also describes playing against an "evolutionary" player which has a
  "theory of mind", ie which adapts. They make a claim (the title of the
  article) that numerical evidence indicates the such a player would evolve
  towards cooperation.
- The paper has two appendices which provide further proofs, one of the theorems
  for example is that short memory strategies are sufficient. This seems limited
  as it only considers a match and not a sufficient evolutionary setting (such
  as a
  Moran process or a tournament). The other proves that the evolutionary process
  will
  stabilise (ultimately all results are being calculated at steady state).
- A deeper literature review placing this paper in it's proper context would be
  beneficial.
- Perhaps some more numerical examples would have been helpful to highlight the
  process they mention. 

Here is a brief summary of the Critical Care Unit interaction paper:

- A piece of work that applies Nash equilibria to the interaction of two health
  providers. It assumes that a hospital's strategy is a threshold at which
  patients are deviated to other hospitals.
- This is one of a few papers on health care logistics that uses Game Theory.
- To calculate the utilities a Markov model is used. For every strategy pair that Markov model is used to get
  the utilities.
- The main theorem in the paper is one that allows for an easy calculation of
  the Nash equilibria by showing that the best response functions are mutually
  increasing which implies that there will be a single intersection of the best
  response functions.
- The above theorem is proven for some conditions which correspond to two
  scenarios.
- The paper then uses this to compute the PoA: price of anarchy looking at a
  comparison between the optimal coordinated behaviour and the Nash equilibria.
  Similarly to a Prisoners dilemma.
- This is used to find a target that aligns selfish behaviour with coordinated
  behaviour.
- Things that could be improved: more players, non stationarity and different
  models of behaviour.
