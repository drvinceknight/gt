---
layout: class-notes
title: "Absorbing Markov Chains"
tag: absorbing-markov-chains
---

## Activity (20 minutes)

Ask students to identify states of a student on an undergraduate degree

1. Year 1: 1
2. Year 2: 2
3. Year 3: 3
4. Year 4: 4
5. Year in industry: I
6. Year abroad: A
7. Exit (reasons could be dropping out or getting a job): E
8. Graduate: G

Lead students to identify a transition matrix, for example:

$$
P =
\begin{pmatrix}
0.15 & 0.6 & 0 & 0 & 0 & 0 & 0.25 & 0 \\
0 & 0.15 & 0.3 & 0 & 0.2 & 0.1 & 0.25 & 0 \\
0 & 0 & 0.1 & 0.15 & 0 & 0 & 0.05 & 0.7 \\
0 & 0 & 0 & 0.1 & 0 & 0 & 0 & 0.9 \\
0 & 0 & 0.9 & 0 & 0 & 0 & 0.1 & 0 \\
0 & 0 & 0.9 & 0 & 0 & 0.05 & 0.05 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 1
\end{pmatrix}
$$

Now discuss where the identify sub matrix is and what that corresponds to.

Give general form of an absorbing Markov chain:

$$
P = \begin{pmatrix}
Q & R\\
0 & 1\\
\end{pmatrix}
$$

Then discuss fundamental matrix:

$$
N = (1 - Q) ^ {-1}
$$

Where the entries of $N_{ij}$ gives average number of times in step $j$ giving
starting in step $i$ before absorption.

Then discuss absorption probability matrix:

$$
B = NR
$$

$B_{ij}$ is the probability of eventually being absorbed in to absorbing state
$j$ when being in state $i$.

Use the following code to make the calculations here:

```python
import numpy as np

P = np.array(
    (
        (.15, .6, 0, 0, 0, 0, .25, 0),
        (0, .15, .3, 0, .2, .1, .25, 0),
        (0, 0, 0.1, 0.15, 0, 0, .05, 0.7),
        (0, 0, 0, .1, 0, 0, 0, .9),
        (0, 0, .9, 0, 0, 0, .1, 0),
        (0, 0, .9, 0, 0, 0.05, .05, 0),
        (0, 0, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 0, 0, 1),
    )
)
assert all(P.sum(axis=1) == 1)
```

```python
Q = P[:-2,:-2]
```

```python
R = P[:-2,-2:]
```

```python
I = P[-2:,-2:]
```

```python
N = np.linalg.inv(np.eye(len(Q)) - Q)
```

```python
B = N @ R
```

## Discussion (20 minutes)

Discuss the **Absorbing Markov chain** appendix: specifically highlighting the
Guassian elimination algorithm for computing the matrix inverse.
