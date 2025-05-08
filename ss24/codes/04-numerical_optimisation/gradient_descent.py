#!/usr/bin/env python

def simple_steepest_descent(func, p0, alpha=0.01, grad_tol=1e-6, maxiter=200):
    p_k = np.copy(p0)
    p_list = [p_k]
    converged = False
    for i in range(0, maxiter):
        grad = func(p_k, deriv=1)
        if np.linalg.norm(grad) < grad_tol:
            converged = True
            break
        p_k = p_k - alpha * grad
        p_list.append(p_k)
    
    if converged:
        print(f'Optimisation converged in {i + 1} iterations!')
    else:
        print(f'Optimisation could not converge after {i + 1} iterations!')
    
    return p_k, np.array(p_list)
