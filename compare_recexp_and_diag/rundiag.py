import numpy as np
from numpy import linalg as la
import sys

sys.path.append('..')
sys.path.append('../densmatlib')
sys.path.append('../densmatlib/densematrix')
import densmatlib
from densmatlib import densematrix 
from densmatlib.densematrix import matfunctions as mf



def get_density_matrix(X, nocc):
    w, v = X.get_eigv() # sorted in ascending order
    nocc = int(nocc) # ?
    DM = mf.DenseSymmMatrix()
    DM.set_matrix(np.dot(v[:, -nocc:], v[:,-nocc:].T))
    return DM
    


def main():
    n = 4 # matrix size
    nocc = 2
    # sample matrix a
    A = mf.DenseSymmMatrix()
    A.rand_symm_matrix(n)
    w, v = A.get_eigv()
    # print eigenvalues and corresponding eigenvectors
    print("Eigenvalues of the matrix A:")
    for i in range(0, len(w)):
        print(w[i])
        
    DM = get_density_matrix(A, nocc)
    print("Density matrix:")
    print(DM.X)
    PROJ_OCC = DM*A
    w_occ, v_occ = PROJ_OCC.get_eigv()
    print("Eigenvalues of the projected matrix:")
    print(w_occ)
    
    
    
    
if __name__ == '__main__':
    main()