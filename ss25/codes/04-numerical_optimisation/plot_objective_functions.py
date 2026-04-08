#!/usr/bin/env python

### ANCHOR: code
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from objective_function import RosenbrockFunction, HimmelblauFunction, \
    plot_2d_objective_function

norm = LogNorm()

hf = HimmelblauFunction()
xs1 = np.linspace(-6.0, 6.0, 200)
ys1 = np.linspace(-6.0, 6.0, 200)

rf = RosenbrockFunction(args=(1.0, 100.0))
xs2 = np.linspace(-2.0, 2.0, 200)
ys2 = np.linspace(-1.0, 3.0, 200)

fig, axs = plt.subplots(1, 2, figsize=(10, 4))

axs[0].set_title('Himmelblau\'s function')
plot_2d_objective_function(axs[0], hf, xs1, ys1, norm=norm)

axs[1].set_title(r'Rosenbrock function ($a = 1;\ b = 100$)')
plot_2d_objective_function(axs[1], rf, xs2, ys2, norm=norm)

fig.tight_layout()
plt.show()
### ANCHOR_END: code

fig.savefig('../../assets/figures/04-numerical_optimisation/plot_objective_functions.svg')

