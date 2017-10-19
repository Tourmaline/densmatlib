import import_dirs

import numpy as np

import densmatlib
from densmatlib import recexpfns as rexp
from densmatlib import densematrix 
from densmatlib.densematrix import matfunctions as mf

def test_rec_exp():
    n = 10
    nocc = 4
    D = list(np.linspace(0, 1, n))
    X = mf.DenseSymmMatrix()
    X.set_matrix(D)
    
    INPUT_INFO = {}
    INPUT_INFO['nocc'] = nocc;
    OUTPUT_INFO = [];
    Xf = rexp.run_recursive_expansion(X, INPUT_INFO, OUTPUT_INFO);
    Xf_trace = Xf.mtrace();
    assert(abs(Xf_trace - nocc) < 1E-5)

