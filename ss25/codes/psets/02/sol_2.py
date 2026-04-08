#!/usr/bin/env python

import sys
sys.path.append( 
    '/Users/xmiao/WORK/teaching/Programmierkurs_Master_SS23/'
    'python-course-master/code/ch99'
)

### ANCHOR: imports
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

from objective_function import RosenbrockFunction, plot_2d_optimisation
from optimiser import SimpleSteepestDescent, OptimiserBase
### ANCHOR_END: imports


### ANCHOR: simple_conjugate_gradient
### ANCHOR: simple_conjugate_gradient_init
class SimpleConjugateGradient(OptimiserBase):

    def __init__(self, func, p0, maxiter=200, **kwargs):
        # Call the constructor of the base class
        super().__init__(func, p0, maxiter, **kwargs)
        # Set True to start combining gradients
        self.conjugate = False
        # Stores the previous gradient
        self.grad_km1 = np.zeros_like(p0)
        # Stores the s_k vector
        self.s_k = np.zeros_like(p0)
    ### ANCHOR_END: simple_conjugate_gradient_init

    def next_step(self):
        alpha = self.kwargs.get('alpha', 0.01)
        grad = self.func(self.p, deriv=1)
        if self.conjugate:
            beta_k = np.dot(grad, grad) / np.dot(self.grad_km1, self.grad_km1)
            beta_k = max(0.0, beta_k)
            self.s_k = (-grad + beta_k * self.s_k) / (1.0 + beta_k)
        else:
            self.s_k = -np.copy(grad)
            self.conjugate = True
        self.grad_km1 = np.copy(grad)
        
        return self.p + alpha * self.s_k
    
    def check_convergence(self):
        return self._check_convergence_grad()
### ANCHOR_END: simple_conjugate_gradient

### ANCHOR: simple_conjugate_gradient_plot
norm = LogNorm()

rf = RosenbrockFunction(args=(1.0, 100.0))
xs = np.linspace(-2.0, 2.0, 200)
ys = np.linspace(-1.0, 3.0, 200)

fig, axs = plt.subplots(1, 2, figsize=(10, 4))

p0 = [0.0, 0.0]

axs[0].set_title('Steepest descent')
optimiser = SimpleSteepestDescent(rf, p0, maxiter=10000, alpha=0.005)
popt, info = optimiser.run(full_output=True)
plot_2d_optimisation(axs[0], rf, xs, ys, norm=norm, traj=info['p_traj'])

axs[1].set_title('Conjugate gradient')
optimiser = SimpleConjugateGradient(rf, p0, maxiter=10000, alpha=0.005)
popt, info = optimiser.run(full_output=True)
plot_2d_optimisation(axs[1], rf, xs, ys, norm=norm, traj=info['p_traj'])

fig.tight_layout()
plt.show()
### ANCHOR_END: simple_conjugate_gradient_plot

fig.savefig('../../../src/figures/psets/02/conjugate_gradient.svg')
