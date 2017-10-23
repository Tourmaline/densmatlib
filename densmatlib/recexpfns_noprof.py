import sys

import numpy as np;
from numpy import linalg as la;

import densematrix 
from densematrix import matfunctions as mf


def apply_polynomial(X, Xsq, poly):
    if poly == 1:
        X = Xsq;
    else:
        X = 2*X-Xsq;
    return X 


def plot_idemp_error(totalOutput):
    # extract error
    err = [];
    for val in totalOutput:
        err.append(val['idemp_err']);

    import matplotlib.pyplot as plt
    plt.semilogy(err, 'r*-')
    plt.xlabel('Iteration')
    plt.ylabel('Idempotency error')
    plt.grid(True)
    plt.show()


def get_polynomial(INPUT_INFO, X, Xsq):
    # if INPUT_INFO['poly_seq'] is given
    # return INPUT_INFO['poly_seq'][i]
        Xtr = X.mtrace();
        Xsq_tr = Xsq.mtrace();
        nocc = INPUT_INFO['nocc']
        if abs(Xsq_tr - nocc) < abs(2*Xtr - Xsq_tr - nocc):
            poly = 1;
        else:
            poly = 0;
        return poly

def run_recursive_expansion(X, INPUT_INFO, totalOutput):
    """
    Run recursive expansion for matrix X.
    """
    i = 1;

    Xsq = X.msquare();

    maxit=400;
    iterOutput = {};
    
    while i < maxit:
        poly = get_polynomial(INPUT_INFO, X, Xsq)
        
        X=apply_polynomial(X, Xsq, poly);
        Xsq = X.msquare();
        
        normXmXsq = X.mnorm2_diff(Xsq);
        
        iterOutput['i'] = i;
        iterOutput['p'] = poly;
        iterOutput['idemp_err'] = normXmXsq;

        # stop = check_stopping_criterion
        stop = 0;
        if normXmXsq < 1E-12:
            print('Stop iterations: i = {}'.format(i))
            stop = 1;
                
        totalOutput.append(iterOutput.copy()); # make a deep copy of a dictionary
        
        if stop == 1:
            break;
        i += 1
        # end of while
    
    return X



TOL = 1E-6

def main():
    argc = len(sys.argv)
    if argc == 3:
        try:
            n = int(sys.argv[1])
        except ValueError: 
                    print("{} : {} is not a number".format(sys.argv[0], sys.argv[1]))
                    sys.exit()
        try:
            nocc = int(sys.argv[2])
        except ValueError: 
                    print("{} : {} is not a number".format(sys.argv[0], sys.argv[2]))
                    sys.exit()
    else:
        if argc == 1:
            n=4;
            nocc = 2;
        else:
            print("Usage: {} n nocc".format(sys.argv[0]))
            sys.exit()
    
    print("Starting recursive expansion with parameters:")
    print("  n    = {} ".format(n))
    print("  nocc = {} ".format(nocc))
    
    D = list(np.linspace(0, 1, n))
    X = mf.DenseSymmMatrix()
    X.set_matrix(D)
    print('Created diagonal matrix.')
    
    INPUT_INFO = {}
    INPUT_INFO['nocc'] = nocc;
    
    OUTPUT_INFO = [];
    Xf = run_recursive_expansion(X, INPUT_INFO, OUTPUT_INFO);
    
    print('Done!')
    Xf_trace = Xf.mtrace();
    print('Iterations converged after {} iterations.'.format(len(OUTPUT_INFO)))
    print('Trace of the density matrix is {}'.format(Xf_trace))
    assert(abs(Xf_trace - nocc) < TOL)
    
    #plot_idemp_error(OUTPUT_INFO);


if __name__ == '__main__':
    main()
