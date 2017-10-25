"""
Module containing class DenseSymmMatrix representing a dense symmetric matrix and various operations on it.

"""

import numpy as np
from numpy import linalg as la

import time

import copy
import numbers
from numbers import Number

class DenseSymmMatrix(object):
    """
    Class for dense symmetric matrix
    """
    
    def __init__(self, inp = 0):
        """
        Initialize matrix
        
        :param int, optional n: size
        :returns: symmetric matrix
        :rtype: DenseSymmMatrix        
        """
        if type(inp) is int:
            if inp < 0:
                raise ValueError('Matrix size has to be non-negative')
            self.rand_symm_matrix(inp)
            self.size = inp
        else:
            raise ValueError('Input type should be int') 
                
    def copy(self):
        """
        Create a copy of a matrix.

        :returns: symmetric matrix
        :rtype: DenseSymmMatrix
        """
        return copy.deepcopy(self)
        
    def __len__(self):
        """
        Get matrix size
        
        :returns: matrix size
        :rtype: int
        """
        return self.size
        
    def set_matrix(self, A):
        """
        Create a DenseSymmMatrix from a given input:
        
        * if A is numpy.matrix or numpy.ndarray:
            create matrix containing data from the array
        * if A is list: create diagonal matrix with a diagonal from a list
    
        :param A: matrix or matrix diagonal
        :returns: symmetric matrix
        :rtype: DenseSymmMatrix
        """
        if type(A) is np.matrix:
            self.X = A.copy()
            (n,m) = A.shape
            assert(n==m)
            self.size = n
        else:
            if type(A) is np.ndarray:
                (n,m) = A.shape
                assert(n==m)
                self.size = n
                self.X = np.matrix(A)  
            else: 
                if type(A) is list:
                    self.X = np.diag(A)
                    self.size = len(A)
                else: raise ValueError('Input type should be np.matrix, np.ndarray or list') 
            
    def get_matrix(self):
        """
        Get matrix as an numpy.array

        :returns: matrix
        :rtype: numpy.array
        """
        return np.asarray(self.X).copy()

        
    def rand_symm_matrix(self, n):
        """
        Generate random symmetric matrix
    
        :param int n: matrix size
        :returns: random symmetric matrix
        :rtype: DenseSymmMatrix
        """
        self.X = np.matrix(np.random.rand(n,n))
        self.X = np.tril(self.X) + np.tril(self.X, -1).T
        self.size = n
        
    def rand_symm_matrix_given_eig(self, D):
        """
        Generate random symmetric matrix with a given eigenvalues
    
        :param list D: desired eigenvalues
        :returns: random symmetric matrix
        :rtype: DenseSymmMatrix
        :raise LinAlgError: if qr factorization fails
        """
        n = len(D)
        A = np.matrix(np.random.rand(n, n))
        try:
            Q, R = np.linalg.qr(A)
        except(LinAlgError):
            print("rand_symm_matrix_given_eig: QR factorization failed")
            sys.exit()
        self.X = np.dot(np.dot(Q, np.diag(D)), Q.T)
        self.size = n
        
    def msquare(self):
        """
        Compute matrix square 

        :returns: matrix square
        :rtype: DenseSymmMatrix
        """
        Xsq = DenseSymmMatrix()
        Xsq.X = np.dot(self.X, self.X)
        Xsq.size = self.size
        return Xsq

    def mtrace(self):
        """
        Compute matrix trace 

        :returns: matrix trace
        :rtype: float
        """
        return np.trace(self.X);    
    
    def mnorm2_diff(self, Y):
        """
        Compute spectral norm of the matrix difference 

        :param array_like Y: input matrix
        :returns: spectral norm of the matrix difference 
        :rtype: float
        """
        return la.norm(self.X-Y.X, 2);
    
    def mnormF_diff(self, Y):
        """
        Compute Frobenius norm of the matrix difference 

        :param array_like Y: input matrix
        :returns: Frobenius norm of the matrix difference 
        :rtype: float
        """
        T = self.X-Y.X
        return la.norm(T, 'fro')
        
    def get_eigv(self):
        """
        Compute eigenvalues and eigenvectors of the matrix.
        
        :returns: tuple (eigenvalues, eigenvectors)
        :rtype: tuple 
        """
        
        # eigh: return the eigenvalues and eigenvectors of a Hermitian or symmetric matrix.
        return la.eigh(self.X)
        
    def __add__(self, V):
        if type(V) is DenseSymmMatrix:
            R = DenseSymmMatrix()
            R.X = self.X+V.X;
            R.size = self.size
            return R
        else:
            raise TypeError("Input should be DenseSymmMatrix")
    
    def __sub__(self, V):
        if type(V) is DenseSymmMatrix:
            R = DenseSymmMatrix()
            R.X = self.X-V.X;
            R.size = self.size
            return R
        else:
            raise TypeError("Input should be DenseSymmMatrix")
    
    def __mul__(self, v):
        if type(v) is int:
            R = DenseSymmMatrix()
            if v == 2: # use BLAS
                R.X = self.X+self.X
            else:
                R.X = v*self.X
            R.size = self.size
            return R    
        else:
            if type(v) is DenseSymmMatrix:
                M = DenseSymmMatrix()
                M.X = np.dot(v.X,self.X) 
                M.size = self.size
                return M
            else:
                raise TypeError("Input should be a number")
        return None
    
    def __rmul__(self, v):
        if type(v) is int:
            R = DenseSymmMatrix()
            if v == 2: # use BLAS
                R.X = self.X+self.X
            else:
                R.X = self.X*v
            R.size = self.size
            return R  
        else:
            if type(v) is DenseSymmMatrix:
                M = DenseSymmMatrix()
                M.X=np.dot(self.X,v.X)
                M.size = self.size
                return M
            else:
                raise TypeError("Input should be a number")
        return None
        
        
        
        
        