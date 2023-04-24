---
layout: post
title:  "A paper on applying Game Theory to cancer"
tags:
    - replicator-dynamics
---

In class today I discussed this paper: [Studying the emergence of invasiveness
in tumours using game
theory](https://link.springer.com/article/10.1140/epjb/e2008-00249-y).

A recording of the class is available here:
[cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=ef53ee0b-d5f2-4890-bdb5-afe600b5f614](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=ef53ee0b-d5f2-4890-bdb5-afe600b5f614).

Here is a brief summary/exploration of some of the paper:

- This is a paper that looks at the GT of cancer: it reads like a proof of concept
  sitting in literature that already exists on the subject.
- The main result is confirming intuitive understanding of proliferation/motility.
  Increased nutrients implies less motility.
- It uses two different approaches: describe an analytic evolutionary model. Note that there
  is a typo in the game:

  $$\begin{pmatrix}
        b/2 & b - c\\
        b   & b - c/2
     \end{pmatrix}
  $$

  Also note that this is showing the utility of the column player so that's
  slightly different from the framework in the course.

  The solution comes from:

  ```python
  >>> import sympy as sym
  >>> p, b, c = sym.symbols("p, b, c")
  >>> sym.solveset(p * (b - c / 2) + (1 - p) * (b - c) - p * (b) - (1 - p) * (b / 2), p)
  {(b - 2*c)/(b - c)}
  ```

  They also describe how a mixed stable solution will also exist which
  corresponds to the stability of the replicator dynamics equation. 

- They implement a Cellular automaton model which is somewhat related to the
  Moran Process
- Improvements could include:
      - more complex dynamics;
      - using more phenotypes (strategies);
      - finite population analytical model;

Here is a blog post on the EGT blog about this paper:
[https://egtheory.wordpress.com/2013/07/05/motility/](egtheory.wordpress.com/2013/07/05/motility/)
