import numpy as np
import rundiag as diag
import sys
import time

sys.path.append('..')
sys.path.append('../densmatlib')
sys.path.append('../densmatlib/densematrix')
import densmatlib
from densmatlib import recexpfns as rexp
from densmatlib import densematrix 
from densmatlib.densematrix import matfunctions as mf


def main():
    argc = len(sys.argv)
    if argc == 3:
        try:
            n = int(sys.argv[1])
        except ValueError: 
                    print("{} : {} is not a number".format(sys.argv[0], sys.argv[1]))
                    sys.exit()
        try:
            gap = float(sys.argv[2])
        except ValueError: 
                    print("{} : {} is not a number".format(sys.argv[0], sys.argv[2]))
                    sys.exit()
        assert(gap < 1 and gap > 0)
    else:
        if argc == 1:
            n=4;
            gap = 0.1;
        else:
            print("Usage: {} n gap".format(sys.argv[0]))
            sys.exit()
    
    print("Starting computations with parameters:")
    print("  n    = {} ".format(n))
    print("  gap = {} ".format(gap))
    
    homo = 0.5 + gap;
    lumo = 0.5 - gap;
    nocc = n/2
    D = list(np.linspace(0, lumo, nocc)) + list(np.linspace(homo, 1, n-nocc))
    X = mf.DenseSymmMatrix()
    X.rand_symm_matrix_given_eig(D)
    print("Random symmetric matrix is generated.")
    
    starttime = time.time() 
    DM_diag = diag.get_density_matrix(X, nocc)
    endtime = time.time() 
    print("Density matrix computation using diagonalization took {} sec".format(endtime-starttime))
    #print(DM_diag.get_matrix())
    
    
    starttime = time.time() 
    INPUT_INFO = {}
    INPUT_INFO['nocc'] = nocc;
    OUTPUT_INFO = [];
    DM_rex = rexp.run_recursive_expansion(X, INPUT_INFO, OUTPUT_INFO);
    endtime = time.time() 
    print("Density matrix computation using recursive expansion took {} sec".format(endtime-starttime))
    #print(DM_rex.get_matrix())
    
    print("Compare obtained matrices...")
    assert(np.allclose(DM_diag.get_matrix(), DM_rex.get_matrix()))
    print("OK!")
        
    


if __name__ == '__main__':
    main()
    