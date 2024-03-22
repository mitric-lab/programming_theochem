import sympy as sp

# ANCHOR: radial
def radial(n, l, r):
    n, l, r = sp.sympify(n), sp.sympify(l), sp.sympify(r)
    n_r = n - l - 1
    r0 = sp.sympify(2) * r / n
    c0 = (sp.sympify(2)/(n))**3
    c1 = sp.factorial(n_r) / (sp.sympify(2) * n * sp.factorial(n + l))
    c = sp.sqrt(c0 * c1)
    lag = sp.assoc_laguerre(n_r, 2 * l + 1, r0)
    return c * r0**l * lag * sp.exp(-r0/2)
# ANCHOR_END: radial

# ANCHOR: check_radial
n, l, r = sp.symbols('n l r')
radial(n, l, r)
# ANCHOR_END: check_radial

# ANCHOR: wavefunction
from sympy.functions.special.spherical_harmonics import Ynm

def wavefunction(n, l, m, r, theta, phi):
    return radial(n, l, r) * Ynm(l, m, theta, phi).expand(func=True)
# ANCHOR_END: wavefunction

# ANCHOR: 1s_function
n, l, m, r, theta, phi = sp.symbols('n l m r theta phi')
psi_100 = wavefunction(1, 0, 0, r, theta, phi)
# ANCHOR_END: 1s_function

# ANCHOR: 1s_limit_infty
psi_100_to_infty = sp.limit(psi_100, r, sp.oo)
assert psi_100_to_infty == sp.sympify(0)
# ANCHOR_END: 1s_limit_infty

# ANCHOR: 1s_is_normalized
dr = (r, 0, sp.oo)
dtheta = (theta, 0, sp.pi)
dphi = (phi, 0, 2*sp.pi)
norm = sp.integrate(r**2 * sp.sin(theta) * sp.Abs(psi_100)**2, dr, dtheta, dphi)
assert norm == sp.sympify(1)
# ANCHOR_END: 1s_is_normalized

# ANCHOR: radial_parts
r = sp.symbols('r')
r10 = sp.lambdify(r, radial(1, 0, r))
r20 = sp.lambdify(r, radial(2, 0, r))
r30 = sp.lambdify(r, radial(3, 0, r))
r40 = sp.lambdify(r, radial(4, 0, r))
# ANCHOR_END: radial_parts

# ANCHOR: plot_radial
import matplotlib.pyplot as plt

r0 = 0
r1 = 35
N = 1000
r_values = np.linspace(r0, r1, N)
fig, ax = plt.subplots(1, 1, figsize=(8, 5))
ax.plot(r_values, r_values**2*r10(r_values)**2, color="black", label="1s")
ax.plot(r_values, r_values**2*r20(r_values)**2, color="red", label="2s")
ax.plot(r_values, r_values**2*r30(r_values)**2, color="blue", label="3s")
ax.plot(r_values, r_values**2*r40(r_values)**2, color="green", label="4s")
ax.set_xlim([r0, r1])
ax.legend()
ax.set_xlabel(r"distance from nucleus ($r/a_0$)")
ax.set_ylabel(r"electron probability ($r^2 |R(r)|^2$)")
fig.show()
# ANCHOR_END: plot_radial

# ANCHOR: plot_spherical_harmonics1
from sympy.functions.special.spherical_harmonics import Ynm
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
%config InlineBackend.figure_formats = ['svg']

l, m, theta, phi = sp.symbols("l m theta phi")
Ylm_sym = Ynm(l, m, theta, phi).expand(func=True)

Ylm = sp.lambdify((l, m, theta, phi), Ylm_sym)
# ANCHOR_END: plot_spherical_harmonics1
# ANCHOR: plot_spherical_harmonics2
N = 1000
theta = np.linspace(0, np.pi, N)
phi = np.linspace(0, 2*np.pi, N)
theta, phi = np.meshgrid(theta, phi)

l = 3
m = 0
Ylm_num = 1/2 * np.abs(
    Ylm(l, m, theta, phi) + np.conjugate(Ylm(l, m, theta, phi))
)
# ANCHOR_END: plot_spherical_harmonics2

# ANCHOR: plot_spherical_harmonics3
x = np.cos(phi) * np.sin(theta) * Ylm_num
y = np.sin(phi) * np.sin(theta) * Ylm_num
z = np.cos(theta) * Ylm_num
# ANCHOR_END: plot_spherical_harmonics3

# ANCHOR: plot_spherical_harmonics4
colors = Ylm_num / (Ylm_num.max() - Ylm_num.min())

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(x, y, z, facecolors=cm.seismic(colors))

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
fig.show()
# ANCHOR_END: plot_spherical_harmonics4

