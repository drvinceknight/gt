12 Contemporary research
========================

Corresponding chapters
----------------------

- `Contemporary research <http://vknight.org/gt/chapters/13/>`_

Objectives
----------

- Discuss different papers that will be looked at.
- Answer queries about assessment of these papers.


Explain that in future sessions we will discuss the papers, students will be
expected to have read them. This will allow me to answer any questions they
might have.

Studying the emergence of invasiveness in tumours using game theory
-------------------------------------------------------------------

https://link.springer.com/article/10.1140/epjb/e2008-00249-y

- A paper that looks at the GT of cancer: it reads like a proof of concept
  sitting in literature that already exists on the subject.
- Main result is confirming intuitive understanding of proliferation/motility.
  Increased nutrients implies less motility.
- Use two different approaches: describe an analytic evo game. Note that there
  is a typo in the game:

  .. math::
     \begin{pmatrix}
        b/2 & b - c\\
        b   & b - c/2
     \end{pmatrix}


  Also note that this is showing the utility of the column player so that's
  slightly different from the framework in the course.

  The solution comes from::

      >>> import sympy as sym
      >>> p, b, c = sym.symbols("p, b, c")
      >>> sym.solveset(p * (b - c / 2) + (1 - p) * (b - c) - p * (b) - (1 - p) * (b / 2), p)
      {(b - 2*c)/(b - c)}

  They also describe how a mixed stable solution will also exist: What does that
  correspond to in notes?

  And the theorem about evolutionary stability: what does that correspond to?

- They implement a Cellular automaton model (why?): does this compare to the evo
  game or to a Moran process?
- Improvements could include:
      - more complex dynamics;
      - using more phenotypes (strategies);
      - finite population analytical model;

Here is a blog post on the EGT blog about this paper:
https://egtheory.wordpress.com/2013/07/05/motility/

Iterated Prisoner's Dilemma contains strategies that dominate any evolutionary opponent
---------------------------------------------------------------------------------------

http://www.pnas.org/content/109/26/10409.abstract

- A paper that looks at memory one strategies in the IPD.
- The paper makes use of a clever mathematical theorem (Cramer's theorem) to
  show that there is a
  linear relationship between the utility of two memory 1 players (eqn 6).
  This is because the linear relationship:

  .. math::

     \alpha S_{X} + \beta S_{Y} + \gamma

  is shown to be the ratio two determinants (essentially one determinant with a
  scaling factor). The columns of the corresponding matrix however are
  independent across both players (one has only :math:`p` variables and another,
  only :math:`q` variables). Thus, choosing a particular set of values for the
  :math:`p` can set the linear relationship above to be 0.
- This
  shows that it's possible for one player to set the score of the other. **It is
  however not possible for a player to set it's own score.**.
- The paper then goes on to show that **it is** possible to set a value where
  the strategy's payoff is a factor of :math:`\chi` more than the opponent.
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
  process they mention. There is one graphic of the evolutionary process and
  note that's claimed to be for :math:`\chi=5`, we can read off the graph that
  the final utilty of the opponent is 1.6, so :math:`S_y-P=1.6-1=.6` and
  :math:`.6\times 5=3` whereas we see that the utility of the other player is
  indeed :math:`3 + 1`.
- What occurs if two ZD strategies attempt to play each other?


Measuring the price of anarchy in critical care unit interactions
-----------------------------------------------------------------

https://link.springer.com/article/10.1057/s41274-016-0100-8

- A piece of work that applies Nash equilibria to the interaction of two health
  providers. It assumes that a hospital's strategy is a threshold at which
  patients are deviated to other hospitals.
- This is one of a few papers on health care logistics that uses Game Theory.
- To calculate the utilities a Markov model (just like the model of Reactive
  strategies) is used. For every strategy pair that Markov model is used to get
  the utilities.
- The main theorem in the paper is one that allows for an easily calculation of
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

Evolution Reinforces Cooperation with the Emergence of Self-Recognition Mechanisms: an empirical study of the Moran process for the iterated Prisoner's dilemma
---------------------------------------------------------------------------------------------------------------------------------------------------------------

- This is a paper that studies the Prisoner's dilemma in a Moran process.
- It uses all the strategies from the Axelrod library but also includes 3
  strategies that were trained using a genetic algorithm specifically for the
  Paper. These are trained using a genetic algorithm.
- These make use of Finite State Machines: a structure that maps states and
  actions to another state and action.
- The paper starts by showing why the numerical simulation is necessary with how
  the theoretic values do not match up with the simulated ones for stochastic
  strategies.
- Then it goes on to examine two main scenarios: resistance and invasion.
- One observation is that the results for N=2 (just 2 strategies, 1 of each
  type) differ quite a lot from N>3. This implies that a lot of theoretic
  research isn't quite right.
- The other observation is that the trained strategies do well:
  - Strategies with handshakes (self recognition mechanisms) do well in
    resistance.
  - Strategies trained for scores against opponents do well at invasion.
- Some discussion is given to the placing of a particular type of strategy that
  is of interest in the literature (the Press and Dyson paper) but does not do
  well here.

Here is are two blog posts on this subject:

- http://vknight.org/unpeudemath/math/2017/07/28/sophisticated-ipd-strategies-beat-simple-ones.html
- http://marcharper.codes/2017-07-31/axelrod.html
