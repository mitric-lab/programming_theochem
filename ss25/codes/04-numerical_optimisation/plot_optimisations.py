#!/usr/bin/env python3

### ANCHOR: imports
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from objective_function import RosenbrockFunction, HimmelblauFunction, \
    plot_2d_optimisation
from optimiser import SimpleSteepestDescent, BFGS
### ANCHOR_END: imports

### ANCHOR: define_objective_functions
norm = LogNorm()

hf = HimmelblauFunction()
xs1 = np.linspace(-6.0, 6.0, 200)
ys1 = np.linspace(-6.0, 6.0, 200)

rf = RosenbrockFunction(args=(1.0, 100.0))
xs2 = np.linspace(-2.0, 2.0, 200)
ys2 = np.linspace(-1.0, 3.0, 200)
### ANCHOR_END: define_objective_functions

### ANCHOR: plot_steepest_descent
fig_sd, axs_sd = plt.subplots(1, 2, figsize=(10, 4))

p0 = [0.0, 0.0]
optimiser = SimpleSteepestDescent(hf, p0, maxiter=200, 
                                  alpha=0.01, grad_tol=1e-6)
popt, info = optimiser.run(full_output=True)
axs_sd[0].set_title(f'Converged after {info["niter"]} iterations')
plot_2d_optimisation(axs_sd[0], hf, xs1, ys1, norm=norm, traj=info['p_traj'])

p0 = [0.0, 0.0]
optimiser = SimpleSteepestDescent(rf, p0, maxiter=50000,
                                  alpha=0.001, grad_tol=1e-6)
popt, info = optimiser.run(full_output=True)
axs_sd[1].set_title(f'Converged after {info["niter"]} iterations')
plot_2d_optimisation(axs_sd[1], rf, xs2, ys2, norm=norm, traj=info['p_traj'])

fig_sd.tight_layout()
plt.show()
### ANCHOR_END: plot_steepest_descent
fig_sd.savefig('../../assets/figures/04-numerical_optimisation/plot_optimisation_sd.svg')

### ANCHOR: plot_bfgs
fig_bfgs, axs_bfgs = plt.subplots(1, 2, figsize=(10, 4))

p0 = [0.0, 0.0]
optimiser = BFGS(hf, p0, maxiter=200, alpha0=1.0, grad_tol=1e-6)
popt, info = optimiser.run(full_output=True)
axs_bfgs[0].set_title(f'Converged after {info["niter"]} iterations')
plot_2d_optimisation(axs_bfgs[0], hf, xs1, ys1, norm=norm, traj=info['p_traj'])

p0 = [0.0, 0.0]
optimiser = BFGS(rf, p0, maxiter=5000, alpha0=1.0, grad_tol=1e-6)
popt, info = optimiser.run(full_output=True)
axs_bfgs[1].set_title(f'Converged after {info["niter"]} iterations')
plot_2d_optimisation(axs_bfgs[1], rf, xs2, ys2, norm=norm, traj=info['p_traj'])

fig_bfgs.tight_layout()
plt.show()
### ANCHOR_END: plot_bfgs
fig_bfgs.savefig('../../assets/figures/04-numerical_optimisation/plot_optimisation_bfgs.svg')

