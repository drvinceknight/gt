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
