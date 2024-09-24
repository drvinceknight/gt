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

ts = np.linspace(0, 500, 1_000)


number_of_labelled_strategies = 11


initial_populations = []
for ratio in (650, 660):
    initial_x = np.ones(101)
    initial_x[0] = ratio
    initial_populations.append(initial_x / initial_x.sum())

fig, ax_array = plt.subplots(nrows=2, figsize=(10, 9))

for initial_x, ax in zip(initial_populations, ax_array):
    xs = scipy.integrate.odeint(func=get_derivative, y0=initial_x, t=ts)

    for i, x in enumerate(xs.T):
        if i < number_of_labelled_strategies:
            ax.plot(x, label=f"$x_{{{i}}}$")
        else:
            ax.plot(x)

    ax.set_xlabel("$t$")
    ax.set_ylabel("$x_i$")
    ax.set_title(f"$x_0^{{(0)}}/x_j^{{(0)}}={initial_x[0]/initial_x[1]}\;\\forall\;j\\ne0$")
    ax.legend()

fig.tight_layout();
fig.savefig("main.pdf", transparent=True)
