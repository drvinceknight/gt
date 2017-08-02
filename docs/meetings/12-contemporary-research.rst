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
