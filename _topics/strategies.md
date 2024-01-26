---
layout: topic
title: "Strategies"
tag: strategies
note_urls:
  - "https://nashpy.readthedocs.io/en/stable/text-book/strategies.html"
video_urls:
  - "Choosing actions in Game Theory: Strategies for Rock Paper Scissors - [YouTube](https://youtu.be/VCWuBl0JUUU) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=5256f688-2698-4778-8a75-af93010f95ce)"
  - "Definition of a strategy in Game Theory - [YouTube](https://youtu.be/DXd2xs1U8kc) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=6bd678d4-2156-4229-a1a8-af93010fa4dc)"
  - "Definition of the support of a strategy: what actions will be played - [YouTube](https://youtu.be/3eeep5LyfX0) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=88e2d8b4-fb98-4f86-80c2-af93010fa7eb)"
  - "Calculating expected utilities when strategies interact in Game Theory - [YouTube](https://youtu.be/I1RLLsB1lSM) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=3bad1ce0-6925-41cf-84d3-af93010fae03)"
  - "A linear algebraic approach to computing expected utilities in Game Theory - [YouTube](https://youtu.be/mY5bGOrQ0ZQ) - [Private] - [A linear algebraic approach to computing expected utilities in Game Theory](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=96d46249-a48b-4b33-a05c-af93010fb86e)"
  - "Using python to calculate expected utilities in Game Theory with Nashpy - [YouTube](https://youtu.be/b5CitajtmVk) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=75320011-fde9-4147-93d3-af93010fbcb9)"
---

## Typical Programming Exercises

1. Create a variable `utilities` which has value the expected utilities for both players for the following Normal Form Game when the row player is playing \\(\sigma_r=(.4, .6)\\) and the column player is playing \\(\sigma_c=(0, 1)\\):
   $$A = \begin{pmatrix}1 & - 1\\ -1 & 1\end{pmatrix} \qquad B = \begin{pmatrix}-1 & 1\\ 1 & -1\end{pmatrix}$$
2. Output the expected utility for both players for the following Normal Form Game when the row player is playing \\(\sigma_r=(1 / 3, 2 / 3)\\) and the column player is playing \\(\sigma_c=(1 / 2, 1 / 2)\\):
   $$A = \begin{pmatrix}3 & 2\\ 3 & 1\end{pmatrix} \qquad B = \begin{pmatrix}4 & 9\\ 5 & 3\end{pmatrix}$$
3. Create a variable `utilities` which has value the expected utilities for both
   players for the following zero sum Normal Form Game
   defined by:
   $$A = \begin{pmatrix}1 & - 1\\ -1 & 1\end{pmatrix}$$
   when the row player is playing \\(\sigma_r=(0, 1)\\) and the column player is
   playing \\(\sigma_c=(1/4, 3/4)\\).
4. Output the expected utilities for both players for the following zero sum Normal Form Game
   defined by:
   $$A = \begin{pmatrix}-3 & - 1 & 4\\ 2 & -1 &  1\\ 0 & 3 & -2\end{pmatrix}$$
   when the row player is playing \\(\sigma_r=(0, 1, 0)\\) and the column player is
   playing \\(\sigma_c=(1/4, 1/4, 1/2)\\).

[Solutions]({{ site.baseurl }}/assets/solutions/strategies.ipynb)
