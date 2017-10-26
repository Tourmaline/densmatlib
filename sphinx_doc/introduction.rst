Density matrix in electronic structure calculations
===================================================

The problem of computing the *density matrix* is one of the most computationally demanding in `electronic structure calculations <https://en.wikipedia.org/wiki/Electronic_structure>`__, in particular Hartree-Fock [1]_ 
and Kohn-Sham density functional theory [2]_ [3]_.


The one-electron density matrix D corresponding to a given Fock or Kohn-Sham matrix F is the matrix for orthogonal projection onto the subspace spanned by eigenvectors of F that correspond to occupied orbitals:

.. math::
  :nowrap:

  \begin{eqnarray}
    Fy_i = \lambda_iy_i \\
    D = \sum_{i=1}^{n_{occ}}y_iy_i^T 
  \end{eqnarray}

where :math:`\lambda_1 \geq \lambda_2 \geq \lambda_{n_{occ}} > \lambda_{n_{occ}+1} \geq \lambda_N`



A straightforward approach to obtain the density matrix is a diagonalization of the matrix F. Note, here we focus on the dense symmetric matrices. In practice, F and D matrices are sparse, thus methods avoiding explicit diagonalization and preserving matrix sparsity are introduced.


Recursive density matrix expansion
-----------------------------------

The problem of computing the density matrix D from F can be formulated as a problem of evaluating a matrix function:

.. math::
  :nowrap:
  
  \begin{eqnarray}
    D = \theta(\mu I - F)
  \end{eqnarray}
  
where :math:`\theta` is a `Heaviside step function <https://en.wikipedia.org/wiki/Heaviside_step_function>`__, and :math:`\mu` is located in the gap between :math:`\lambda_{n_{occ}}` and :math:`\lambda_{n_{occ}+1}` and :math:`I` is the identity matrix.
The step function can be approximated by a smooth function, which can be constructed by **recursively** applying second order polynomials:

.. math::
  :nowrap:

  \begin{align}
    &X_0 = \frac{\lambda_{1}I - F}{\lambda_{1} - \lambda_{N}}\\
    &\text{while ( stopping criterion not fulfilled, for } i = 1,2,\dots \text{)}\\
    &\quad\text{if (} |\text{trace}(X_{i-1}^2) - n_{occ}| < |\text{trace}(2X_{i-1}-X_{i-1}^2) - n_{occ}|  \text{)} \\
    &\quad\quad  X_{i} = X_{i-1}^2\\
    &\quad\text{else} \\
    &\quad\quad   X_{i} = 2X_{i-1}-X_{i-1}^2
  \end{align}

The polynomials and condition for selecting polynomials applied in each iteration can be chosen differently [4]_.

With this approach, if matrices are sufficiently sparse, the *linear scaling computational cost* may be achieved. The sparsity of intermediate matrices  is usually ensured by removing small matrix elements during the course of the recursive expansion. We note again, that here we focus on the dense matrices, thus no truncation is performed.


Example of a quantum chemistry program
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As an example of the code performing realistic electronic structure calculations we provide `ErgoSCF <http://www.ergoscf.org/>`__. It is a quantum chemistry program for large-scale self-consistent field calculations, in particular it implements density matrix computation using recursive expansion and utilizing sparsity structure of matrices.


.. [1] Roothaan, C. C. J. Rev. Mod. Phys. 1951, 23, 69–89.
.. [2] Hohenberg, P.; Kohn, W. Phys. Rev. 1964, 136, B864–B871.
.. [3] Kohn, W.; Sham, L. J. Phys. Rev. 1965, 140, 1133.
.. [4] Kruchinina, A.; Rudberg, E.; Rubensson, E. H. J. Chem. Theory Comput. 2016, 12, 5788–5802

