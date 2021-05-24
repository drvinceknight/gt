import matplotlib.pyplot as plt

x1s = [0, 1]
first_line = [1 / 3 - 3 * x for x in x1s]
second_line = [1 / 13 - 6 / 13 * x for x in x1s]
plt.figure()
plt.plot(first_line, label="$1/3-3x_1$ (label: 2)")
plt.plot(second_line, label="$1/13-6/13x_1$ (label: 3)")
plt.legend()
plt.savefig("AA-row-player-strategy-polytope.png")
