---
layout: topic
title:  "Replicator Dynamics"
tag: "replicator-dynamics"
note_urls:
    - "https://nashpy.readthedocs.io/en/stable/text-book/replicator-dynamics.html"
video_urls:
    - "Evolution of aggression and sharing: the replicator dynamics with the Hawk Dove Game - [YouTube](https://youtu.be/tDTVRvfaaQo) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=c8121ebf-b1d1-440d-8fda-afaa00cd10b2)"
    - "A mathematical model of evolution: the replicator dynamics equations. - [YouTube](https://youtu.be/Ixdu3m44Zqk) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=89340661-bd52-4aa8-96d8-afaa0104b6f2)"
    - "Stability of the replicator dynamics equation. - [YouTube](https://youtu.be/I5C5nKr-Hrk) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=83452cf2-b388-4895-adef-afaa0104b8af)"
    - "Evolutionary stability of the Replicator Dynamics Equations - [YouTube](https://youtu.be/5j1NQ5uvqMY) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=614357a3-9542-4f9c-bcd1-afaa0104ba1e)"
    - "Allowing for mutation in evolution: the replicator mutation dynamics equations. - [YouTube](https://youtu.be/gA4h9CEqCCA) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=026b0fd0-f756-4fd4-953c-afaa0104c3e9)"
    - "Using Python to solve the Replicator Dynamics Equation with Nashpy - [YouTube](https://youtu.be/u3mdoVStT8A) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=c93d4263-24f9-4435-9685-afaa0104d6dc)"
meeting_urls:
    - "https://github.com/drvinceknight/gt/blob/main/do/07-evolutionary-game-theory.rst"
---

## Typical Programming Exercises

1. Create a variable `populations` which has value a list containing all population vectors for the replicator dynamics (with `timepoints=numpy.linspace(0, 1, 500)`) for the Normal Form Game defined by:
   $$A = \begin{pmatrix}1 & - 1\\ -1 & 1\end{pmatrix} \qquad B = \begin{pmatrix}-1 & 1\\ 1 & -1\end{pmatrix}$$
2. Output a list containing all population vectors for the replicator dynamics (with `timepoints=numpy.linspace(0, 1, 500)`) for the Normal Form Game defined by:
   $$A = \begin{pmatrix}3 & 2\\ 3 & 1\end{pmatrix} \qquad B = \begin{pmatrix}4 & 9\\ 5 & 3\end{pmatrix}$$
3. Create a variable `last_population` which has value the final population vectors for the replicator dynamics (with `timepoints=numpy.linspace(0, 1, 500)`) for the Normal Form Game defined by:
   $$A = \begin{pmatrix}1 & - 1\\ -1 & 1\end{pmatrix}$$
4. Output the final population vectors for the replicator dynamics (with `timepoints=numpy.linspace(0, 1, 500)`) for the Normal Form Game defined by:
   $$A = \begin{pmatrix}-3 & - 1 & 4\\ 2 & -1 &  1\\ 0 & 3 & -2\end{pmatrix}$$

[Solutions]({{ site.baseurl }}/assets/solutions/replicator-dynamics.ipynb)
