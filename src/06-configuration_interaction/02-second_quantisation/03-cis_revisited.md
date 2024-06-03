### CIS Revisited

Now we are ready to revisit the CIS method and derive the CIS equation using
the language of second quantisation. We shall at first bring the Hamiltonian
into normal order. Although this is not necessary for the derivation, but will
make our results more intepretable.

#### Normal Ordering of the Hamiltonian

Let us examine the one-electron part at first. Using Wick's theorem, we obtain
<p align="center">
  <img src="../../assets/figures/06-configuration_interaction/wick/operator_normal_order_1e.svg">
</p>

Since the contraction will only be nonzero if $p$ and $q$ are both 
occupied, we can identify the indices with $i$ and $j$.

The two-electron part is a bit more complicated, but it follows the same
principle:
<p align="center">
  <img src="../../assets/figures/06-configuration_interaction/wick/operator_normal_order_2e.svg">
</p>

where we renamed some summation indices and used the symmetry
$g_{pqrs} = g_{rspq}$ in the last step.

Now we can identify
$$
\begin{aligned}
  \sum_i h_{ii} + \frac{1}{2} \sum_{ij} (g_{iijj} - g_{ijji}) 
    &= E_{\mathrm{HF}} \quad &\mathrm{HF\ energy} \\\\
  h_{pq} + \sum_i (g_{iipq} - g_{ipqi}) 
    &= f_{pq} \quad &\mathrm{Fock\ matrix\ element}
\end{aligned}
$$
and write the Hamiltonian as
$$
\begin{aligned}
	\hat{H} &= \sum_{pq} f_{pq} :\mathrel{a_p^\dagger a_q}: +
	\frac{1}{2} \sum_{pqrs} g_{pqrs} :\mathrel{a_p^\dagger a_r^\dagger a_s a_q}: +
	E_{\mathrm{HF}}	\\\\
	&= \hat{F}_N + \hat{V}_N + E_{\mathrm{HF}}
\end{aligned}
$$

#### The CIS Hamiltonian

We can now take a look at the matrix elements of the CIS Hamiltonian.

##### The Element $\langle \Phi_0 | \hat{H} | \Phi_0 \rangle$
Since $\Phi_0$ is the Fermi vacuum, and the first two terms of the Hamiltonian
are normal ordered, they do not contribute to the matrix element. Therefore,
$$
\langle \Phi_0 | \hat{H} | \Phi_0 \rangle = 
  \langle \Phi_0 | E_{\mathrm{HF}} | \Phi_0 \rangle = E_{\mathrm{HF}}
$$

##### The Elements $\langle \Phi_0 | \hat{H} | \Phi_i^a \rangle$
We at first take a look at the one-electron part:
<p align="center">
  <img src="../../assets/figures/06-configuration_interaction/wick/cis_hf_ia_1e.svg">
</p>
Because only fully contracted string contribute to the matrix element, and
contractions within a normal ordered string are zero, we only have to consider
one contraction. Because it has zero crossings, its sign is positive.

For the two-electron part, because only two ladder operators are not within the
normal ordered part, we can at most have nonzero double contractions. But
because we have 6 ladder operators in total, these contractions cannot be
full contractions and therefore do not contribute to the matrix element.

The zero-electron part is easy:
$$
	\langle \Phi_0 | E_{\mathrm{HF}} | \Phi_i^a \rangle = E_{HF} \langle \Phi_0 | a_a^\dagger a_i | \Phi_0 \rangle = 0
$$

Wrapping everything up, we get
$$
	\langle \Phi_0 | \hat{H} | \Phi_i^a \rangle = f_{ia}
$$
If the sites are HF orbitals, the converged Fock matrix is diagonal and thus
$f_{ia}$, which is certainly off-diagonal, is zero. We have hereby shown
Brillouin's theorem.

##### The Elements $\langle \Phi_i^a | \hat{H} | \Phi_j^b \rangle$
Again, we start with the one-electron part:
<p align="center">
  <img src="../../assets/figures/06-configuration_interaction/wick/cis_ia_jb_1e.svg">
</p>
The minus sign appears because the first contraction has three crossings.

Then, we move to the two-electron part:
<p align="center">
  <img src="../../assets/figures/06-configuration_interaction/wick/cis_ia_jb_2e.svg">
</p>

Again, the zero-electron part is easy:
<p align="center">
  <img src="../../assets/figures/06-configuration_interaction/wick/cis_ia_jb_0e.svg">
</p>


Putting everything together, we get
$$
  \langle \Phi_i^a | \hat{H} | \Phi_j^b \rangle 
  = f_{ab} \delta_{ij} - f_{ij}^{*} \delta_{ab} + g_{jbai} - g_{jiab} + 
    E_{\mathrm{HF}} \delta_{ij} \delta_{ab}
$$

If the sites are HF orbitals, we again have a diagonal Fock matrix, so the
matrix elements $f_{ab} = f_{aa} \delta_{ab}$ and 
$f_{ij} = f_{ii} \delta_{ij}$.
The diagonal elements $f_{aa}$ and $f_{ii}$ can be identified as 
orbital energies $\epsilon_a$ and $\epsilon_i$, respectively. 
Therefore, we obtain
$$
  \langle \Phi_i^a | \hat{H} | \Phi_j^b \rangle 
  = (E_{\mathrm{HF}} + \epsilon_a - \epsilon_i) \delta_{ij} \delta_{ab} + 
    g_{jbai} - g_{jiab}
$$
which we have used to implement our CIS routine.

