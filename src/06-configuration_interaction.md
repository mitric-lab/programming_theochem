# Configuration Interaction

To improve upon the Hartree-Fock approximation, which only uses one Slater 
determinant to describe the ground state, it is only natural to consider 
linear combinations of Slater determinants. This is the idea behind 
configuration interaction (CI) methods.

The CI wavefunction can be written as 

$$
  | \Psi^n \rangle = c_0^n | \Phi_0 \rangle 
    + \sum_{i,a} c_{ia}^n | \Phi_i^a \rangle 
    + \sum_{i\lt j,a\lt b} c_{ijab}^{n} | \Phi_{ij}^{ab} \rangle 
    + \cdots 
$$

where the superscript $n$ denotes the state of the system, and the 
indices $i,j,k,\cdots$ and $a,b,c,\cdots$ denote occupied and virtual 
orbitals, respectively. The Slater determinants 
$ | \Phi_{ij\cdots}^{ab\cdots} \rangle $ 
are constructed by removing the electrons in the occupied orbitals 
$i,j,\cdots$ and adding electrons to the virtual orbitals 
$a,b,\cdots$. The coefficients $ c_{ij\cdots,ab\cdots}^n $ are 
determined variationally by solving the Schrödinger equation.

Since the wavefunction given above contains all possible Slater determinants 
(within) a basis set, it is referred to as the full CI (FCI) wavefunction. By 
inspecting the wavefunction expansion, it might become obvious that the number 
of determinants grows rapidly with the size of the system. To be precise, for 
a system with $M$ spin-orbitals, $N_\alpha$ $\alpha$-spin 
electrons and $N_\beta$ $\beta$-spin electrons, the number of 
determinants is given by $ \binom{M}{N_\alpha} \binom{M}{N_\beta} $. 
For a small system, say, benzene with a moderate basis set, e.g. cc-pVDZ, 
there are 21 $\alpha$-spin electrons and 21 $\beta$-spin electrons 
in the closed-shell reference determinant and 228 spin-orbitals in total. 
This leads to over $6 \times 10^{58}$ determinants. Clearly, it is 
impossible to perform FCI calculations (as described above) for such systems 
for such systems with current computational resources.

One very simple way to reduce the number of determinants is to only consider 
excitations up to a certain level. This is often referred to as truncated CI. 
In this section, we will at first implement Configuration Interaction Singles 
(CIS) and use second quantisation techniques to derive the CIS equations, 
as well as the Full CI equations. 

