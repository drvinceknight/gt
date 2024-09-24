import matplotlib.pyplot as plt
import nashpy as nash
import numpy as np


plt.rcParams.update({'font.size': 14, 'font.weight': 'bold'})

# Payoff matrix obtained by using the Axelrod library and the documentation
# written here: https://axelrod.readthedocs.io/en/stable/tutorials/running_axelrods_first_tournament/index.html#creating-the-tournament
A = np.array([
    [3.   , 2.975, 3.   , 3.   , 3.   , 2.975, 3.   , 3.   , 2.625, 2.985, 1.409, 1.14  , 1.469 , 2.217, 2.238 ],
    [3.   , 2.98 , 3.02 , 3.004, 3.   , 2.98 , 3.   , 3.   , 2.975, 1.165, 1.297, 1.076 , 1.325 , 2.824, 2.836 ],
    [3.   , 2.97 , 3.   , 3.   , 3.   , 2.97 , 3.   , 3.   , 2.757, 0.075, 2.22 , 2.658 , 2.718 , 1.57 , 1.52  ],
    [3.   , 2.974, 3.   , 3.   , 3.   , 2.974, 3.   , 3.   , 3.056, 0.472, 2.088, 2.383 , 2.428 , 1.995, 2.129 ],
    [3.   , 2.975, 3.   , 3.   , 3.   , 2.975, 3.   , 3.   , 3.316, 1.285, 1.343, 1.331 , 1.413 , 2.802, 2.648 ],
    [3.   , 2.98 , 3.02 , 3.004, 3.   , 2.98 , 3.   , 3.   , 2.63 , 2.525, 1.375, 1.191 , 1.685 , 2.873, 2.928 ],
    [3.   , 2.975, 3.   , 3.   , 3.   , 2.975, 3.   , 3.   , 2.043, 1.055, 1.173, 1.111 , 1.315 , 3.033, 2.967 ],
    [3.   , 2.975, 3.   , 3.   , 3.   , 2.975, 3.   , 3.   , 2.047, 1.045, 1.271, 1.121 , 1.215 , 3.003, 2.915 ],
    [2.625, 2.775, 3.162, 2.676, 1.846, 2.605, 1.383, 1.382, 1.5  , 3.143, 1.463, 1.371 , 2.064 , 2.74 , 2.892 ],
    [2.985, 1.015, 4.9  , 3.302, 1.36 , 1.1  , 1.005, 1.17 , 2.748, 1.   , 2.22 , 2.646 , 1.19  , 2.67 , 2.582 ],
    [1.434, 1.307, 3.52 , 2.828, 1.458, 1.4  , 1.173, 1.271, 1.723, 3.495, 1.293, 1.136 , 1.315 , 2.414, 2.443 ],
    [1.165, 1.076, 3.228, 2.753, 1.371, 1.216, 1.111, 1.131, 1.451, 3.211, 1.151, 1.1675, 1.27  , 2.293, 2.327 ],
    [1.494, 1.285, 3.188, 2.763, 1.648, 1.71 , 1.21 , 1.145, 2.369, 1.04 , 1.29 , 1.2   , 1.3995, 2.317, 2.374 ],
    [2.227, 0.909, 3.92 , 2.81 , 1.127, 0.803, 0.553, 0.648, 1.18 , 1.225, 1.824, 2.053 , 1.987 , 2.265, 2.279 ],
    [2.258, 0.891, 3.925, 2.704, 1.168, 0.658, 0.537, 0.68 , 0.997, 1.237, 1.833, 2.102 , 1.979 , 2.304, 2.2745]])

ipd = nash.Game(A, A.T)

timepoints = np.linspace(0, 25, 500)
xs = ipd.replicator_dynamics(timepoints=timepoints)

fig, axarr = plt.subplots(nrows=2, ncols=1, figsize=(10, 9))

ax = axarr[0]
for i, x in enumerate(zip(*xs)):
    if x[-1] > 10 ** -2:
        ax.plot(x, label=f"{i}")
    else:
        ax.plot(x)
ax.set_ylim(0, 1)
ax.set_title("Evolution of strategies in Axelrod's 1st tournament")
ax.set_xlabel("Time")
ax.set_ylabel("Population proportion")
ax.legend()

ax = axarr[1]
ax.plot(np.sum([x * (A @ x) for x in xs], axis=1))
ax.set_ylim(0, 5)
ax.set_xlabel("Time")
ax.set_title("Average per turn utility")

fig.tight_layout()
fig.savefig("main.pdf", transparent=True)
