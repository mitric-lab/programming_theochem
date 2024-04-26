## Testing on molecules

> From now on, we will define several classes to help us with the 
> calculation of molecular integrals. We will start with the minimal 
> structure of these classes and extend them throughout this chapter. 
> The most recent version of these classes can be found in subsection 
> [4.4.1](ch03-04a-latest_classes.md]).

We have written our own routine for calculating overlap integrals. To confirm 
its functionality, we shall do some testing on real molecules. For this, we 
define several [classes](https://docs.python.org/3/tutorial/classes.html) to 
make a convenient interface for molecules and basis sets.

### The `Atom` Class
Chemists work often with atomic symbols, which are not intuitive for 
computers. They would prefer atomic numbers. Therefore, we first define 
a dictionary that has atomic symbols as keys and atomic numbers as values:
```python
{{#include ../codes/03-molecular_integrals/atomic_data.py:atomic_number}}
```
We save this dictionary in a file called `atomic_data.py`.

The `Atom` class should represent an atom with a specific symbol Vand 
coordinate. The class should therefore include the following attributes:
- `atomic_number`: A dictionary with keys corresponding to atomic symbols 
and values corresponding to atomic numbers.
- `symbol`: The atomic symbol of the atom.
- `coord`: The coordinate of the atom.
- `atnum`: The atomic number corresponding to the symbol of the atom.

The class includes one method, `__init__`, which initializes a new atom 
with the given symbol and coordinate. The optional argument `unit` specifies 
the unit of the given coordinates and can be either `A` (&#8491;ngström) or 
`B` (Bohr).
```python
{{#include ../codes/03-molecular_integrals/atom.py:imports}}
```
```python
{{#include ../codes/03-molecular_integrals/atom.py:atom_class}}
```
This class is saved in a file called `atom.py`.

Because we are chemists, we are not satisfied with only atoms. We want to 
combine them into molecules, hence a `Molecule` class is needed.


### The `Molecule` Class

The `Molecule` class should represent a molecule, therefore, the following 
attributes can be useful:
- `atomlist`: A list of `Atom` objects representing the atoms in the molecule.
- `natom`: The number of atoms in the molecule.
- `basisfunctions`: A list of `Gaussian` objects representing the 
basis functions of the molecule.
- `S`: A matrix representing the overlap integrals between basis functions.

```python
{{#include ../codes/03-molecular_integrals/molecule.py:imports}}
```
```python
{{#include ../codes/03-molecular_integrals/molecule.py:molecule_base}}
```
```python
{{#include ../codes/03-molecular_integrals/molecule.py:molecule_overlap}}
```

We have utilized the `BasisSet` class to initialize basis sets for our 
molecule, which we will define now.

### The `BasisSet` Class
The `BasisSet` class should contain a set of GTOs and be able to calculate 
molecular integrals between them. Therefore, we shall define the `Gaussian` 
class first for the integral handling.
```python
{{#include ../codes/03-molecular_integrals/basis_set.py:imports_base}}
```
```python
{{#include ../codes/03-molecular_integrals/basis_set.py:imports_overlap}}
```
```python
{{#include ../codes/03-molecular_integrals/basis_set.py:gaussian_base}}
```
```python
{{#include ../codes/03-molecular_integrals/basis_set.py:gaussian_overlap}}
```

```admonish info
Currently, this class can only calculate overlap integrals. We will extend 
this class with other molecular integrals in the coming lectures.
```

We can now construct the `BasisSet` class. It should be able to read 
basis sets in [JSON format](https://en.wikipedia.org/wiki/JSON) and 
instance objects from the `Gaussian` class.
```python
{{#include ../codes/03-molecular_integrals/basis_set.py:basis_set_class}}
```

You can download various basis sets from the
[Basis Set Exchange](https://www.basissetexchange.org/)
website. Make sure to download the basis sets in the JSON format.

You can also download some common basis sets from the list
- <a href="../assets/basis_sets/sto-3g.json" download>STO-3G</a>: 
  A minimal basis set.
- <a href="../assets/basis_sets/6-31g.json" download>6-31G</a>: 
  A Pople basis set.
- <a href="../assets/basis_sets/6-31g_st.json" download>6-31G*</a>: 
  A Pople basis set with polarization functions.
- <a href="../assets/basis_sets/cc-pvdz.json" download>cc-pVDZ</a>:
  A Dunning basis set (with polarization functions).

