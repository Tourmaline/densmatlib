import import_dirs

import matfunctions as mf
import numpy as np

def test_create_empty():
    """ Create a zero matrix """
    X = mf.DenseSymmMatrix()
    assert(len(X) == 0)
    
    
def test_set_matrix():
    A = np.array([[1, 2], [4, 5]])
    X = mf.DenseSymmMatrix()
    X.set_matrix(A)
    assert(X.size == 2)
    Acp = X.get_matrix()
    assert(np.array_equal(A, Acp))
    
    D = [1,2,3,4,5]
    X.set_matrix(D)
    assert(len(X) == 5)

    
def test_square():
    X = mf.DenseSymmMatrix(10)
    Xsq = X.msquare()
    assert(len(Xsq) == 10)
    D = [1,2,3,4,5]
    X.set_matrix(D)
    Xsq = X.msquare()
    assert(len(Xsq) == 5)
    
def test_trace():
    """ Compute the matrix trace """
    D = [1,2,3,4,5]
    X = mf.DenseSymmMatrix()
    X.set_matrix(D)
    assert(len(X) == 5)
    assert(X.mtrace() == 15)
    Xsq = X.msquare()
    assert(Xsq.mtrace() == 55)
        
    
# def test_get_item():    
#     D = [1,2,3,4,5]
#     X = mf.DenseSymmMatrix()
#     X.set_matrix(D)
#     X[1,1]
    
if __name__ == '__main__':
     test_square()
    