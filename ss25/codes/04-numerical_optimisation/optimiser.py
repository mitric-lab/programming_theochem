#!/usr/bin/env python

### ANCHOR: imports
import numpy as np
from abc import ABC, abstractmethod
### ANCHOR_END: imports


### ANCHOR: armijo_line_search
def armijo_line_search(func, p0, vec, maxiter=100, 
                       alpha0=1.0, c=0.5, tau=0.5):
    m = np.dot(func(p0, deriv=1), vec)
    t = -c * m
    alpha = alpha0

    for _ in range(0, maxiter):
        if func(p0, deriv=0) - func(p0 + alpha * vec, deriv=0) > alpha * t:
            break
        else:
            alpha *= tau
    return alpha
### ANCHOR_END: armijo_line_search


### ANCHOR: optimiser_base
class OptimiserBase(ABC):

    def __init__(self, func, p0, maxiter=200, **kwargs):
        self.func = func
        self.p = np.copy(p0)
        self.p_new = np.copy(p0)
        self.maxiter = maxiter
        self.kwargs = kwargs

    @abstractmethod
    def next_step(self):
        pass

    @abstractmethod
    def check_convergence(self):
        pass

    def _check_convergence_grad(self):
        tol = self.kwargs.get('grad_tol', 1e-6)
        grad_norm = np.linalg.norm(self.func(self.p, deriv=1))
        return grad_norm < tol

    def run(self, full_output=False):
        converged = False
        ps = [self.p]
        for i in range(0, self.maxiter):
            self.p_new = self.next_step()
            ps.append(self.p_new)
            converged = self.check_convergence()
            if converged:
                break
            else:
                self.p = np.copy(self.p_new)
        if converged:
            print(f'Optimisation converged in {i + 1} iterations!')
        if not converged:
            print('WARNING: Optimisation could not converge '
                  f'after {i + 1} iterations!')

        if full_output:
            info_dict = {
                'niter': len(ps),
                'p_opt': self.p_new,
                'fval_opt': self.func(self.p_new, deriv=0),
                'grad_opt': self.func(self.p_new, deriv=1),
                'p_traj': np.array(ps),
            }
            return self.p_new, info_dict
        else:
            return self.p_new
### ANCHOR_END: optimiser_base


### ANCHOR: simple_steepest_descent
class SimpleSteepestDescent(OptimiserBase):

    def next_step(self):
        alpha = self.kwargs.get('alpha', 0.01)
        grad = self.func(self.p, deriv=1)
        return self.p - alpha * grad

    def check_convergence(self):
        return self._check_convergence_grad()
### ANCHOR_END: simple_steepest_descent


### ANCHOR: steepest_descent
class SteepestDescent(OptimiserBase):

    def next_step(self):
        alpha0 = self.kwargs.get('alpha0', 1.0)
        grad = self.func(self.p, deriv=1)
        # alpha0 *= max(1.0, np.linalg.norm(grad))
        alpha = armijo_line_search(
            self.func, self.p, -grad, alpha0=alpha0,
        )
        return self.p - alpha * grad

    def check_convergence(self):
        return self._check_convergence_grad()
### ANCHOR_END: steepest_descent


### ANCHOR: conjugate_gradient
class ConjugateGradient(OptimiserBase):

    def __init__(self, func, p0, maxiter=200, **kwargs):
        super().__init__(func, p0, maxiter, **kwargs)
        self.conjugate = False
        self.grad_km1 = np.zeros_like(p0)
        self.s_k = np.zeros_like(p0)

    def next_step(self):
        alpha0 = self.kwargs.get('alpha0', 1.0)
        grad = self.func(self.p, deriv=1)
        alpha0 *= max(1.0, np.linalg.norm(grad))
        if self.conjugate:
            # beta after Polak and Ribière
            beta_k = np.dot(grad, grad - self.grad_km1) \
                     / np.dot(self.grad_km1, self.grad_km1)
            beta_k = max(0, beta_k)
            self.s_k = -grad + beta_k * self.s_k
            alpha = armijo_line_search(
                self.func, self.p, self.s_k, alpha0=alpha0,
            )
        else:
            alpha = armijo_line_search(
                self.func, self.p, -grad, alpha0=alpha0,
            )
            self.s_k = -np.copy(grad)
            self.conjugate = True
        self.grad_km1 = np.copy(grad)

        return self.p - alpha * grad

    def check_convergence(self):
        return self._check_convergence_grad()
### ANCHOR_END: conjugate_gradient


### ANCHOR: bfgs
class BFGS(OptimiserBase):

    def __init__(self, func, p0, maxiter=200, **kwargs):
        super().__init__(func, p0, maxiter, **kwargs)
        self.b_k = np.eye(len(p0))

    def next_step(self):
        alpha0 = self.kwargs.get('alpha0', 1.0)
        grad = self.func(self.p, deriv=1)
        v_k = -np.dot(self.b_k, grad)
        alpha = armijo_line_search(
            self.func, self.p, v_k, alpha0=alpha0,
        )
        s_k = alpha * v_k
        y_k = self.func(self.p + s_k, deriv=1) - self.func(self.p, deriv=1)
        self.b_k = self.b_k \
            + (np.dot(s_k, y_k) + np.linalg.multi_dot((y_k, self.b_k, y_k))) \
                * np.outer(s_k, s_k) / np.dot(s_k, y_k)**2 \
            - (np.outer(np.dot(self.b_k, y_k), s_k) \
                + np.outer(s_k, np.dot(y_k, self.b_k))) / np.dot(s_k, y_k)

        return self.p + s_k

    def check_convergence(self):
        return self._check_convergence_grad()
### ANCHOR_END: bfgs

