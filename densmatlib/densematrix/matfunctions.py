import numpy as np;
from numpy import linalg as la;

def msquare(X):
    """
    Compute matrix square 

    :param array_like X: input matrix
    :returns: matrix square
    :rtype: array_like
    :raises AssertionError: raises an exception when matrix is not square
    """
    assert(matrix_is_square(X))
    Xsq = X**2;
    return Xsq;

def mtrace(X):
    """
    Compute matrix trace 

    :param array_like X: input matrix
    :returns: matrix square
    :rtype: array_like
    :raises AssertionError: raises an exception when matrix is not square
    """
    assert(matrix_is_square(X))
    return np.trace(X);

def mnorm2_diff(A,B):
    """
    Compute spectral norm of the matrix difference A-B 

    :param array_like X: input matrix
    :returns: spectral norm of the matrix difference A-B
    :rtype: float
    :raises AssertionError: raises an exception when matrix is not square
    """
    assert(matrix_is_square(A))
    assert(matrix_is_square(B))
    return la.norm(A-B);

def rand_symm_matrix(n):
    """
    Generate random symmetric matrix

    :param int n: matrix size
    :returns: random symmetric matrix
    :rtype: array_like
    """
    A = np.random.rand(n,n);
    M = np.tril(A) + np.tril(A, -1).T;
    return M

def matrix_is_square(X):
    """
    Check is matrix is square

    :param  array_like X: input matrix
    :returns: True if matrix square, False otherwise
    """
    (n,m) = X.shape
    if n==m:
        return True
    else:
        return False;   

def get_matrix_size(X):
    """
    Compute size of a square matrix

    :param  array_like X: input matrix
    :returns: matrix size
    :rtype: int
    :raises AssertionError: raises an exception when matrix is not square
    """
    (n,m) = X.shape
    assert(n==m)
    return n

def diag_matrix(D):
    """
    Generate diagonal matrix with diagonal equal to D 

    :param list D: matrix diagonal
    :returns: diagonal matrix
    :rtype: array_like
    """
    M=np.diag(D)
    return M
