import matfunctions as mf
import numpy as np


def test_create_empty():
    X = mf.DenseSymmMatrix()
    assert(X.size == 0)
    
    
def test_set_matrix():
    A = np.array([[1, 2], [4, 5]])
    X = mf.DenseSymmMatrix()
    X.set_matrix(A)
    assert(X.size == 2)
    Acp = X.get_matrix()
    assert(np.array_equal(A, Acp))
    
    D = [1,2,3,4,5]
    X.set_matrix(D)
    assert(X.size == 5)

    
def test_square():
    X = mf.DenseSymmMatrix(10)
    X.msquare()
    assert(X.size == 10)
    