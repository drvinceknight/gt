---
layout: class-notes
title: "Moran Processes"
tag: "moran-process"
---

**Activity** (approximately 60 minutes)

Use [moran process form]({{site.baseurl}}/assets/activities/moran_process/main.pdf) and have
students play in pairs.

**Also requires use of dice, allowing for multiples of 4 and 6.** For example:

- 1 d12 (12-sided dice), or  
- 1 d6 and 1 d4 (the example used in this page), or  
- 1 d6 and 1 d8.

**Virtual modification:** use breakout rooms of 4. For dice, show how to use the
Python `random` library.

Explain that we will aim to reproduce a Moran process with $n=3$.

![]({{site.baseurl}}/assets/activities/moran_process/moran_process.png)

We will do this with the Hawk–Dove game:

$$
A = \begin{pmatrix}
   0 & 3\\
   1 & 2
\end{pmatrix}
$$

Recall, this corresponds to sharing of 4 resources:

- two hawks both get nothing;
- a hawk meeting a dove gets 3 out of 4;
- a dove meeting a hawk gets 1 out of 4;
- a dove meeting a dove gets 2 out of 4.

Give students 5 minutes to write out the fitnesses of each type in each possible
situation.

Confirm:

|                  | $f(\text{hawk})$             | $f(\text{dove})$             |
|------------------|------------------------------|------------------------------|
| 1 hawk, 2 doves  | $0\times0 + 2\times3 = 6$    | $1\times1 + 1\times2 = 3$    |
| 2 hawks, 1 dove  | $1\times0 + 1\times3 = 3$    | $2\times1 + 0\times2 = 2$    |

Give students 5 minutes to write out the probabilities of selection of each type
in each possible situation.

Confirm:

|                 | Select | Selection: birth                      | Selection: death             |
|-----------------|---------|--------------------------------------|------------------------------|
| 1 hawk, 2 doves | hawk    | $\frac{6}{6 + 2\times3}$             | $\frac{1}{3}$                |
| 1 hawk, 2 doves | dove    | $\frac{2\times3}{6 + 2\times3}$      | $\frac{2}{3}$                |
| 2 hawks, 1 dove | hawk    | $\frac{2\times3}{2\times3 + 2}$      | $\frac{2}{3}$                |
| 2 hawks, 1 dove | dove    | $\frac{2}{2\times3 + 2}$             | $\frac{1}{3}$                |

**Let students simulate.**

Count from groups to obtain mean fixation rate of a hawk.

Show the following code that allows us to simulate the simulation undertaken by
the students (this is not the same code as in the notes):

```python
import collections
import matplotlib.pyplot as plt
import numpy as np
import tqdm

def roll_n_sided_dice(n=6):
    """Roll a dice with n sides."""
    return np.random.randint(1, n + 1)

class MoranProcess:
    """
    A class for a Moran process with a population of size n=3 using the
    standard hawk-dove game:

        A = [[0, 3],
             [1, 2]]

    Note that this is a simulation corresponding to an in-class activity
    where students roll dice.
    """
    def __init__(self, number_of_hawks=1, seed=None):
        if seed is not None:
            np.random.seed(seed)

        self.number_of_hawks = number_of_hawks
        self.number_of_doves = 3 - number_of_hawks

        self.dice_and_values_for_hawk_birth = {1: (6, {1, 2, 3}), 2: (4, {1, 2, 3})}
        self.dice_and_values_for_hawk_death = {1: (6, {1, 2}), 2: (6, {1, 2, 3, 4})}

        self.history = [(self.number_of_hawks, self.number_of_doves)]

    def step(self):
        """Select a hawk or a dove for birth and death, then update."""
        birth_dice, birth_values = self.dice_and_values_for_hawk_birth[self.number_of_hawks]
        death_dice, death_values = self.dice_and_values_for_hawk_death[self.number_of_hawks]

        select_hawk_for_birth = self.roll_dice_for_selection(dice=birth_dice, values=birth_values)
        select_hawk_for_death = self.roll_dice_for_selection(dice=death_dice, values=death_values)

        if select_hawk_for_birth:
            self.number_of_hawks += 1
        else:
            self.number_of_doves += 1

        if select_hawk_for_death:
            self.number_of_hawks -= 1
        else:
            self.number_of_doves -= 1

        self.history.append((self.number_of_hawks, self.number_of_doves))

    def roll_dice_for_selection(self, dice, values):
        """Return True if the roll is in the target set."""
        return roll_n_sided_dice(n=dice) in values

    def simulate(self):
        """Run the simulation until the number of hawks is 0 or 3."""
        while self.number_of_hawks in [1, 2]:
            self.step()
        return self.number_of_hawks

    def __len__(self):
        return len(self.history)
```

This carries out the simulations:

```python
repetitions = 10 ** 5
end_states = []
path_lengths = []

for seed in range(repetitions):
    mp = MoranProcess(seed=seed)
    end_states.append(mp.simulate())
    path_lengths.append(len(mp))

counts = collections.Counter(end_states)
counts[3] / repetitions
# ≈ 0.54666
```

Discuss obtaining theoretic probabilities of changing state:

$$
p_{10}=\frac{6}{12}\frac{1}{3}=\frac{1}{6}\qquad
p_{12}=\frac{6}{12}\frac{2}{3}=\frac{1}{3}\qquad
p_{21}=\frac{2}{8}\frac{2}{3}=\frac{1}{6}\qquad
p_{23}=\frac{6}{8}\frac{1}{3}=\frac{1}{4}
$$

**Now work through the notes, culminating in the proof of the theorem for the
absorption probabilities of a birth–death process.**

Discuss and use code from the chapter to show the fixation with the hawk–dove
game:

```python
a = np.array([[0, 3], [1, 2]])
```

Calculate theoretic value using the formula from the theorem:

$$
\begin{align*}
f_{1i} &= \frac{3(n-i)}{n - 1} = 3\frac{n-i}{n-1} \\
f_{2i} &= \frac{i + 2(n - i -1)}{n - 1} = \frac{2n - 2 - i}{n - 1}
\end{align*}
$$

This gives (for $n=3$):

|                  | $i=1$ | $i=2$ |
|------------------|-------|-------|
| $f_{1i}$         | 3     | 3/2   |
| $f_{2i}$         | 3/2   | 1     |
| $\gamma_i$       | 1/2   | 2/3   |

Thus:

$$
x_1 = \frac{1}{1 + 1/2 + 1/2\times2/3} = \frac{1}{11/6} \approx 0.545455
$$

**Discussion**

Work through the Moran Process chapter.

Discussion Point: After the definition of the moran process, ask how this differs from our example?

Discussion Point: After the definition of fixation probability, ask what the fixation probability of a hawk is based on our simulation?

Discussion Point: After the theoretic fixation in two types ask how this could be used for our example? Leave this as an exercise.
