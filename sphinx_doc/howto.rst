Programming in python
======================


Numpy and multithreading
-------------------------

Numpy is a powerful python library with various highly optimized operations on the arrays. 
To install numpy one can use pip:

.. code-block:: bash

  $ pip install numpy


Some functions are implemented on top of BLAS library, which is automatically parallelized on most platforms. However, there is a limited number of operations which are utilizing parallel BLAS. Unfortunately, there is no clear way to check which operations are doing so and which not. The easiest way to check is multiple threads are used is testing (see also http://scipy.github.io/old-wiki/pages/ParallelProgramming).


To check which library numpy is using behind the scene, one can run:

>>> import numpy as np
>>> np.config_show()


Numpy and ATLAS
^^^^^^^^^^^^^^^^
If numpy is compiled with ATLAS, the number of threads cannot be changed at runtime. It is defined during the compilation time of the ATLAS library (see also http://math-atlas.sourceforge.net/faq.html#tnum).



Numpy and OpenBLAS
^^^^^^^^^^^^^^^^^^^^^
OpenBLAS allows to change number of threads during runtime. For example, to set number of threads to 8 we execute:
.. code-block:: bash

  $ export OMP_NUM_THREADS = 8


Measuring execution time
-------------------------

The easy way to measure the execution time of a small code is using timeit:

>>> import timeit
>>> timeit.timeit('B=np.dot(A, A)', setup='import numpy as np;  n = 2000; A = np.random.rand(n,n)', number=1)
1.154828032002115
>>> 


For larger pieces of code one can use time library:

>>> import time
>>> startt = time.time()
>>> # your code
>>> endt = time.time()
>>> print(endt-startt)


Tests
^^^^^^^^^^^^^^^^

We have noticed interesting timing result comparing operations A+A and 2*A, which result in a same matrix:

>>> timeit.timeit('A+A', setup='import numpy as np; A = np.asmatrix(np.random.rand(20000, 20000));', number=1)
0.5255228559999523
>>> timeit.timeit('2*A', setup='import numpy as np; A = np.asmatrix(np.random.rand(20000, 20000));', number=1)
5.227032694999934

Our guess is that A+A function is calling optimized BLAS routine, however, 2*A does not do it. Moreover, looking at the top output, it seems that our implementation of numpy is utilizing multiple threads for 2*A operation, but not for A+A. 


.. _prog_in_python:

Profiling
---------

In this project we use module **line_profiler** for doing line-by-line profiling of functions. 

To install it, run:

.. code-block:: bash

  $ pip install line_profiler


To enable profiling of a particular function, add decorator @profile above the function. Now, to get the profiling results we run script *kernprof* as following:

.. code-block:: bash

  $ kernprof -l -v your_module.py [args]
  
  
Example output (part):

.. code-block:: text

  51         1         3622   3622.0      0.2      Xsq = X.msquare();
  52                                           
  53         1            2      2.0      0.0      maxit=400;
  54         1            0      0.0      0.0      iterOutput = {};
  55                                               
  56        42           33      0.8      0.0      while i < maxit:
  57        42         3420     81.4      0.2          poly = get_polynomial(INPUT_INFO, X, Xsq)
  58                                                   
  59        42       125580   2990.0      8.1          X=apply_polynomial(X, Xsq, poly);
  60        42      1260461  30011.0     81.6          Xsq = X.msquare();
  61                                                   
  62        42       151310   3602.6      9.8          normXmXsq = X.mnormF_diff(Xsq);


This results show that the most time consuming operation was matrix-matrix square, taking almost 81.6% of the total execution time.



Continuous integration with Travis CI and Coveralls
----------------------------------------------------

**Continuous Integration is the practice of merging in small code changes frequently - rather than merging in a large change at the end of a development cycle.** (see `Continuous Integration <https://docs.travis-ci.com/user/for-beginners/#What-is-Continuous-Integration-(CI)%3F>`__)

There are plenty of online sources on how to manage continuous integration of the code with specialized tools. In this project we used `Travis CI <https://travis-ci.org>`__ and `Coveralls <https://coveralls.io/>`__. You can see badges in our github page showing the status of the latest build.


Travis CI best practices
^^^^^^^^^^^^^^^^^^^^^^^^^^

* Commits that have [ci skip] or [skip ci] anywhere in the commit messages are
  ignored by Travis CI

* Each build runs in one of the virtual environments provided by Travis CI. At
  this point there are supported a very limited number Linux distributions and OS X. The current default distribution is Ubuntu Trusty 14.04 (see `Build Environment Overview <https://docs.travis-ci.com/user/reference/overview/>`__).

* M. Beller, G. Gousios and A. Zaidman, "Oops, My Tests Broke the Build: An
  Explorative Analysis of Travis CI with GitHub," 2017 IEEE/ACM 14th International Conference on Mining Software Repositories (MSR), Buenos Aires, 2017, pp. 356-367, doi: 10.1109/MSR.2017.62, `URL <http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7962385&isnumber=7962336>`__.

*Online references:*

* http://eng.localytics.com/best-practices-and-common-mistakes-with-travis-ci/
* https://docs.travis-ci.com/user/customizing-the-build
* Some  notes about security:   
  https://docs.travis-ci.com/user/best-practices-security/
* http://docs.python-guide.org/en/latest/scenarios/ci/


Coveralls with Python
^^^^^^^^^^^^^^^^^^^^^^^^^^

* https://coveralls.zendesk.com/hc/en-us/articles/201342869-Python




