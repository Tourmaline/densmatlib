Density matrix in electronic structure calculations
===================================================

The problem of computing the density matrix is one of the most computationally demanding in `electronic structure calculations <https://en.wikipedia.org/wiki/Electronic_structure>`__, in particular Hartree-Fock [1]_ 
and Kohn-Sham density functional theory [2]_ [3]_.


The one-electron density matrix D corresponding to a given Fock or Kohn-Sham matrix F is the matrix for orthogonal projection onto the subspace spanned by eigenvectors of F that correspond to occupied orbitals:

.. math::
  :nowrap:

  \begin{eqnarray}
    Fy_i = \lambda_iy_i \\
    D = \sum_{i=1}^{n_{occ}}y_iy_i^T 
  \end{eqnarray}




A straightforward approach to obtain the density matrix is a diagonalization of the matrix F. Note, here we focus on the dense symmetric matrices. In practice, F and D matrices are sparse, thus methods avoiding explicit diagonalization and preserving matrix sparsity are introduced.


Recursive density matrix expansion
-----------------------------------









References
-----------

.. [1] Roothaan, C. C. J. Rev. Mod. Phys. 1951, 23, 69–89.
.. [2] Hohenberg, P.; Kohn, W. Phys. Rev. 1964, 136, B864–B871.
.. [3] Kohn, W.; Sham, L. J. Phys. Rev. 1965, 140, 1133.




