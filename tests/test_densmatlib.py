import sys
sys.path.append('.')
sys.path.append('..')

import densmatlib
from densmatlib import densematrix 
from densmatlib.densematrix import matfunctions as dmat


def test_create_genmatrix():
    X = dmat.GeneralMatrix()
    assert(X.size == 0)

# def test_generate_random_matrix():
#     X = dmat.rand_symm_matrix(5);
#     assert(dmat.get_matrix_size(X) == 5)    

    
    
def main():
    test_generate_random_matrix()   
    
if __name__ == '__main__':
    main()


