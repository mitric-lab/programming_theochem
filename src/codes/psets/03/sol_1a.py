#!/usr/bin/env python

### ANCHOR: imports
import numpy as np
import matplotlib.pyplot as plt
### ANCHOR_END: imports

### ANCHOR: def_double_well
def double_well(q, q0, delta, e_ts):
    pot = (delta / (2.0 * q0)) * (q - q0) \
            + ((e_ts - 0.5 * delta) / q0**4) \
            * (q - q0)**2 * (q + q0)**2
    return pot
### ANCHOR_END: def_double_well


### ANCHOR: optimise_double_well
from scipy.optimize import minimize

args = (2.0, 1.0, 2.0)
q_init = [3.0]
res = minimize(double_well, q_init, args=args, method='BFGS')
print('q_opt: ', res.x)
### ANCHOR_END: optimise_double_well

plot_x = np.linspace(-5.0, 5.0, 1000)
plot_y = double_well(plot_x, *args)

plt.plot(plot_x, plot_y)
plt.scatter(res.x, double_well(res.x, *args), c='r')

plt.show()

