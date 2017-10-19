"""
Module for ...
"""

import numpy as np
from numpy import linalg as la

class DenseSymmMatrix(object):
    
    def __init__(self, n = 0):
        if n < 0:
            raise ValueError('Matrix size has to be non-negative')
        self.rand_symm_matrix(n)
        self.size = n
        
    def __len__(self):
        return self.size
        
    def set_matrix(self, A):
        if type(A) is np.matrix:
            self.X = A
            (n,m) = A.shape
            assert(n==m)
            self.size = n
        else:
            if type(A) is np.ndarray:
                (n,m) = A.shape
                assert(n==m)
                self.size = n
                self.X = np.asmatrix(A)  
            else: 
                if type(A) is list:
                    self.X = np.diag(A)
                    self.size = len(A)
                else: raise ValueError('Input type should be np.matrix, np.ndarray or list') 
            
    def get_matrix(self):
        return np.asarray(self.X).copy()

        
    def rand_symm_matrix(self, n):
        """
        Generate random symmetric matrix
    
        :param int n: matrix size
        :returns: random symmetric matrix
        :rtype: array_like
        """
        self.X = np.asmatrix(np.random.rand(n,n));
        self.X = np.tril(self.X) + np.tril(self.X, -1).T;
        
    def msquare(self):
        """
        Compute matrix square 

        :returns: matrix square
        :rtype: array_like
        """
        self.X = self.X**2;

    def mtrace(self):
        """
        Compute matrix trace 

        :returns: matrix square
        :rtype: array_like
        :raises AssertionError: raises an exception when matrix is not square
        """
        return np.trace(self.X);    
    
    def mnorm2_diff(self, Y):
        """
        Compute spectral norm of the matrix difference 

        :param array_like Y: input matrix
        :returns: spectral norm of the matrix difference 
        :rtype: float
        """
        return la.norm(self.X-Y);
        
        
        