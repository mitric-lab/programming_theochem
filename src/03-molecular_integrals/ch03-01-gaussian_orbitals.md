# Gaussian Type Orbitals

The Schrödinger equation of the hydrogen atom can be solved analytically 
and the obtained wave functions have the radial part
$$
R_{nl}(r) = N_{nl} \left[ L_{n-l-1}^{2l+1} \left( \frac{2r}{na} \right) \right] \left( \frac{2 r}{n a} \right)^l \exp\left(-\frac{r}{na}\right)
$$
where \\(n\\), \\(l\\) are the principal and azimuthal quantum number, 
respectively, \\(N_{nl}\\) is the normalisation constant, 
\\(L_{n-l-1}^{2l+1}\\) is the associated Laguerre polynomial and 
\\(a\\) stands for Bohr radius. 

Ignoring the normalisation constant and the polynomial factor, 
the wavefunction boils down to \\(\exp(-\zeta r)\\). One may assume 
that all atomic orbitals have this general form, the so-called 
Slater type orbitals (STO). These orbitals have a cusp in the origin, 
which accurately describes the electron distribution at nuclei. 

STOs, however, are not very easy to integrate. Analytically expressions 
of one-electron integrals involving STOs can be obtained, though they 
are rather cumbersome. Two-electron integrals involving STOs cannot be 
solved analytically, so ei)ther numerical integration or approximations 
must be applied. This make the use of STOs in quantum chemistry very 
impractical. 

Instead, the Gaussian type orbitals (GTO), which has the general form 
\\(\exp(-\alpha r^2)\\), is widely used for quantum chemistry. Although 
it does not accurately represents the correct electronic density at nuclei, 
relatively simple analytical expressions for molecular integrals involving 
GTOs, including two-electron integrals, exist, even for two-electron integrals

### Cartesian Gaussian Orbitals
The most intuitive form of GTOs is the Cartesian form, which is expressed as
$$
g_{nl}(\vec{r};\alpha, \vec{A}) = 
  N_{nl}(\alpha)\ \\|\vec{r} - \vec{A}\\|^{n-l-1}
  \ (x-A_x)^{l_x} (y-A_y)^{l_y} (z-A_z)^{l_z} 
  \ \mathrm{e}^{-\alpha \\| \vec{r}-\vec{A} \\|^2}
$$
with the nucleus sitting at \\(\vec{A}\\) and \\(l_x + l_y + l_z = l\\). 
Some examples values of \\(l\\) and the corresponding atomic orbitals are 
shown in the following table:

| \\(l_x\\) | \\(l_y\\) | \\(l_z\\) | Orbital |
| --- | --- | --- | ------- |
| 0   | 0   | 0   | \\(s\\)       |
| 1   | 0   | 0   | \\(p_x\\)   |
| 0   | 1   | 0   | \\(p_y\\)   |
| 0   | 0   | 1   | \\(p_z\\)   |
| 1   | 1   | 0   | \\(d_{xy}\\) |
| 1   | 0   | 1   | \\(d_{xz}\\) |
| 0   | 1   | 1   | \\(d_{yz}\\) |
| 2   | 0   | 0   | \\(d_{x^2}\\) |
| 0   | 2   | 0   | \\(d_{y^2}\\) |
| 0   | 0   | 2   | \\(d_{z^2}\\) |


### Gaussian Product Theorem
The existence of relatively simple expressions molecular integrals 
involving GTOs is partly due to the Gaussian product theorem, 
which states that the product between two 1s Gaussians 
(\\(n=0\\), \\(l_x = l_y = l_z = 0\\)) is another 1s Gaussian. 
We shall demonstrate this theorem for two (unnormalized) 1D-Gaussians
$$
\begin{align}
  g(x;\alpha,A_x) &= \exp\left(-\alpha ( x - A_x )^2 \right) \\\\
  &\text{and} \\\\
  g(x;\beta,B_x) &= \exp\left(-\beta ( x - B_x )^2 \right)
\end{align}
$$

By taking the product of the two Gaussian functions, we obtain

$$
g(x;\alpha,A_x) \cdot g(x;\beta,B_x) = \exp\left(-\alpha ( x - A_x )^2\right) \cdot \exp\left(-\beta ( x - B_x )^2\right)
$$

We can simplify this expression by using the properties of exponents:

$$
\begin{align}
g(x;\alpha,A_x) \cdot g(x;\beta,B_x) 
&= \exp\left(-\alpha ( x^2 - 2A_x x + A_x^2 )\right) 
  \cdot \exp\left(-\beta ( x^2 - 2B_x x + B_x^2 )\right) \\\\
&= \exp\left(-\alpha x^2 + 2\alpha A_x x - \alpha A_x^2 \right)
  \cdot \exp\left(-\beta x^2 + 2\beta B_x x - \beta B_x^2 \right) \\\\
&= \exp\left(-(\alpha + \beta)x^2 + 2(\alpha A_x + \beta B_x)x - (\alpha A_x^2 + \beta B_x^2)\right) \\\\
&= \exp\left(-( \alpha + \beta) \left(x^2 - 2\dfrac{\alpha A_x + \beta B_x}{\alpha + \beta} x + \dfrac{\alpha^2 A_x^2 + \beta^2 B_x^2}{(\alpha + \beta)^2} - \dfrac{\alpha B_x^2 + \beta A_x^2}{\alpha + \beta} \right)\right) \\\\
&= \exp\left(-( \alpha + \beta) \left(x - \dfrac{\alpha A_x + \beta B_x}{\alpha + \beta}\right)^2 - \dfrac{\alpha\beta}{\alpha + \beta}(A_x - B_x)^2 \right)
\end{align}
$$

In the last step, we completed the square inside the exponent to obtain 
a Gaussian function. By defining
$$
\begin{align}
  p &= \alpha + \beta \\\\
  \mu &= \frac{\alpha \beta}{\alpha + \beta} \\\\
  X_{AB} &= A_x - B_x \\\\
  P_x &= \frac{\alpha A_x + \beta B_x}{\alpha + \beta}
\end{align}
$$
we obtain
$$
g(x;\alpha,A_x) \cdot g(x;\beta,B_x) = g(x;p,P_x) \exp\left( -\mu X_{AB}^2 \right)
$$
a new Gaussian at the "center of mass" \\(P_x\\) with the total exponent 
\\(p\\), scaled by \\(\exp\left( \mu X_{AB}^2 \right)\\). Since Gaussian 
orbitals can be easily factored into Cartesian directions, a proof for 
3D-Gaussians follow trivially from the proof for 1D-Gaussians.

### Contracted Gaussians
Because Gaussians do differ quite a bit from Slater functions, we can make 
them more accurate by using a linear comination of Gaussians, i.e.
$$
G(x; {\alpha_i}, {c_i}, \vec{A}) = \sum_{i=1}^N c_i g(\vec{x}; \alpha_i, \vec{A})
$$
where \\(G(x; {\alpha_i}, {c_i}, \vec{A})\\) is called a _contracted Gaussian_. 
To avoid confusion, we shall call \\(g(\vec{x}; \alpha_i, \vec{A})\\) 
_primitive Gaussian_.

Apart from being more accurate, another advantage of using contracted Gaussian 
is the exclusive use of orbitals without radial nodes. In other words, we only 
need Gaussians of the form
$$
g_{l}(\vec{r};\alpha, \vec{A}) = 
  N_{l}(\alpha)\ (x-A_x)^{l_x} (y-A_y)^{l_y} (z-A_z)^{l_z} 
  \ \mathrm{e}^{-\alpha \\| \vec{r}-\vec{A} \\|^2}
$$
Note that the factor \\(\\|\vec{r} - \vec{A}\\|^{n-l-1}\\) is gone and the 
orbital no longer depends on the principal quantum number \\(n\\). Because 
we can now omit the index \\(n\\) on \\(g\\), we can use \\(i\\), \\(j\\) 
and \\(k\\) instead of the verbose \\(l_x\\), \\(l_y\\) and \\(l_z\\), which 
are difficult to read when written as exponents. Such Cartesian Gaussians 
can thus be written as
$$
g_{ijk}(\vec{r};\alpha, \vec{A}) = 
  N_{l}(\alpha)\ (x-A_x)^{i} (y-A_y)^{j} (z-A_z)^{k} 
  \ \mathrm{e}^{-\alpha \\| \vec{r}-\vec{A} \\|^2}
$$

This simplification can be done out of two reasons: On the one hand, 
the radial nodes are located in the neighborhood of core orbitals, which 
do not contribute much to chemical bonding. On the other hand, a linear 
combination of primitive Gaussians with some negative contraction coefficients 
can approximate an atomic orbital with nodes.

We shall now take a look at an example of Gaussian basis sets:
```
#BASIS SET: (6s,3p) -> [2s,1p]
C    S
      0.7161683735E+02       0.1543289673E+00
      0.1304509632E+02       0.5353281423E+00
      0.3530512160E+01       0.4446345422E+00
C    SP
      0.2941249355E+01      -0.9996722919E-01       0.1559162750E+00
      0.6834830964E+00       0.3995128261E+00       0.6076837186E+00
      0.2222899159E+00       0.7001154689E+00       0.3919573931E+00
```
This is the STO-3G basis set for the carbon atom. The first line with the 
notation `(6s,3p) -> [2s,1p]` tells us that this basis set consists of 
6 primitive Gaussian functions of the s-type and 3 primitive Gaussian 
functions of the p-type. These primitive functions are then contracted 
to form 2 s-type and 1 p-type contracted Gaussian functions.

The rest of this snippet contains two blocks, with every block starting with 
a line clarifying the atom and orbital type. The other lines have either two 
or three columns. The first block describes an s-type basis function with the 
exponents listed in the first column and the contraction coefficients listed 
in the second column. The second block describes an s-type and a p-type basis 
function with the same orbital exponents listed in the first column. The next 
two columns contain the contraction coefficients for s-orbitals and 
p-orbitals, respectively. 

> **Note**: The contraction coefficients do **NOT** include the normalization 
> constants for the primitive Gaussians. So you have to include it when 
> constructing contracted Gaussians.
