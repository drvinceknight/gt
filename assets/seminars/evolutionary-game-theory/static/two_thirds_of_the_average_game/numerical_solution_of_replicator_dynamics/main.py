import numpy as np
import scipy.integrate

import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams.update({'font.size': 14, 'font.weight': 'bold'})

def get_uniform_population(N=101):
    return np.ones(N) / (N)

def get_distance_from_two_thirds(x):
    N = len(x)
    indices = np.arange(0, N)

    return (indices - 2/3 * np.sum(indices * x)) ** 2
    
def get_fitness(x=None):            

    return 1 / (1 + get_distance_from_two_thirds(x=x))

def get_derivative(x, t, N=101):
    
    fitness = get_fitness(x=x)
    phi = np.sum(x * fitness)

    return x * (fitness - phi)

ts = np.linspace(0, 1_000, 500)
x = get_uniform_population(N=101)
xs = scipy.integrate.odeint(func=get_derivative, y0=x, t=ts)

zoom = 20
number_of_labelled_strategies = 5
zoom_box_width_offset = 5
zoom_box_height_offset = 0.01

fig, (ax_2, ax_1) = plt.subplots(nrows=2, figsize=(10, 9))
for i, x in enumerate(xs.T):
    if i < number_of_labelled_strategies:
        ax_1.plot(x[:zoom], label=f"$x_{{{i}}}$")
        ax_2.plot(x, label=f"$x_{{{i}}}$")
    else:
        ax_1.plot(x[:zoom])
        ax_2.plot(x)

ax_1.set_xlabel("$t$")
ax_2.set_xlabel("$t$")
ax_1.set_ylabel("$x_i$")
ax_2.set_ylabel("$x_i$")

ax_1.set_title("Zoom of early populations")
ax_2.set_title("All populations")

ax_2.add_patch(
    patches.Rectangle(
        xy=(-zoom_box_width_offset, -zoom_box_height_offset), 
        width=zoom + zoom_box_width_offset,
        height=xs[:zoom].max() + zoom_box_height_offset, 
        fc='none', 
        color="black", 
        linewidth=1, 
        linestyle="dashed",
        zorder=2,
    )
)
ax_2.legend()
fig.tight_layout()
fig.savefig("main.pdf", transparent=True)
