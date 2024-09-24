import matplotlib.pyplot as plt
import nashpy as nash
import numpy as np

A = np.array([[3, 1], [0, 2]])
B = np.array([[2, 1], [0, 3]])
game = nash.Game(A)
ys = [0, 1]
sigma_rs = [(1, 0), (0, 1)]
u_rs = [[game[sigma_r, (y, 1 - y)][0] for y in ys] for sigma_r in sigma_rs]
u_cs = [[game[sigma_r, (y, 1 - y)][1] for y in ys] for sigma_r in sigma_rs]

fig, (ax1, ax2) = plt.subplots(ncols=2)

ax1.plot(ys, u_rs[0], label="$(A\sigma_c^T)_1$")
ax1.plot(ys, u_rs[1], label="$(A\sigma_c^T)_2$")
ax2.xlabel("$\sigma_c=(y, 1-y)$")
plt.title("Utility to row player")
plt.legend()
plt.savefig("main.pdf")
