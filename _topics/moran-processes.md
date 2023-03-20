---
layout: topic
title:  "Moran Processes"
tag: "moran-process"
note_urls:
    - "https://nashpy.readthedocs.io/en/stable/text-book/moran-process.html"
video_urls:
    - "Modelling evolution in a discrete population: motivating the Moran process - [YouTube](https://youtu.be/oQKG4QtWatQ) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=171abded-8e0f-4c8d-bde9-afaa0104ee76)"
    - "The definition of the Moran process - [YouTube](https://youtu.be/hiuI7mkVmd8) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=16d87fbd-7b66-440e-96a3-afaa01050523)"
    - "Moran processes and games: fitness functions from games. - [YouTube](https://youtu.be/o-uaLs4LLkw) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=3047c830-8d08-45e4-a369-afaa01051bcf)"
    - "Selection probabilities for the Moran process on a game - [YouTube](https://youtu.be/2-zc5D-RHIM) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=95a35356-578d-4c86-a444-afaa01053346)"
    - "The Moran process with mutation - [YouTube](https://youtu.be/0UM3PTpyioo) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=e9ca08ff-be0d-4494-b786-afaa01055008)"
    - "The Moran process on 2 types: a mathematically tractable model. - [YouTube](https://youtu.be/BXrQIhpoaE4) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=d40fa7ed-1aae-4ccb-b6a4-afaa0105694d)"
    - "A formula for the fixation probability for Moran processes with 2 types.  - [YouTube](https://youtu.be/ivBLUqSkGBU) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=22f1e20c-1fa6-46df-91a6-afaa0105819f)"
    - "Using Python to simulate the Moran Process with Nashpy - [YouTube](https://youtu.be/H3Jv8WvBBvg) - [Private](https://cardiff.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=823ab610-84de-42f4-82fc-afaa0108b0fd)"
meeting_urls:
    - "https://github.com/drvinceknight/gt/blob/main/do/08-moran-process.rst"
---

## Typical Programming Exercises

For each of the following matrices \\(A\\) and initial populations \\(x_0\\), for the corresponding normal form game:

- create a variable `initial_population` which has value the corresponding `nashpy` initial population.
- create a variable `probabilities` which has value the fixation probabilities of the simulated [Moran process](https://nashpy.readthedocs.io/en/stable/how-to/obtain-fixation-probabilities.html) (using the given repetitions and random seed).

a. $$
    A = \begin{pmatrix}1 & 2 \\ 2 & 1\end{pmatrix}
    \qquad
    x_0 = \begin{pmatrix}10 & 0\end{pmatrix}
   $$

   `repetitions=500` and `seed=0`

b. $$
    A = \begin{pmatrix}1 & 2 \\ 2 & 1\end{pmatrix}
    \qquad
    x_0 = \begin{pmatrix}3 & 0\end{pmatrix}
   $$

   `repetitions=350` and `seed=4`

c. $$
    A = \begin{pmatrix}1 & 2 & 3 \\ 2 & 1 & 4 \\ 2 & 3 & 1\end{pmatrix}
    \qquad
    x_0 = \begin{pmatrix}3 & 1 & 2\end{pmatrix}
   $$

   `repetitions=1` and `seed=2`

d. $$
    A = \begin{pmatrix}1 & 2 & 3 \\ 2 & 1 & 4 \\ 2 & 3 & 1\end{pmatrix}
    \qquad
    x_0 = \begin{pmatrix}6 & 2 & 4\end{pmatrix}
   $$

   `repetitions=350` and `seed=0`

[Solutions]({{ site.baseurl }}/assets/solutions/moran-process.ipynb)
