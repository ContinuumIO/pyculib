=============
Release notes
=============

Version 0.1.0
=============

NumbaPro and Accelerate have been deprecated, and code generation features have
been moved into open-source Numba. The CUDA library functions have been moved into
Pycudalib. There will be no further updates to NumbaPro or Accelerate.

CUDA libraries
--------------

CUDA library functionality is equivalent to that in Accelerate 2.+, with the
following packages renamed:

===========================  ===========================
Accelerate package           Pycudalib package
===========================  ===========================
``accelerate.cuda.blas``     ``pycudalib.blas``
``accelerate.cuda.fft``      ``pycudalib.fft``
``accelerate.cuda.rand``     ``pycudalib.rand``
``accelerate.cuda.sparse``   ``pycudalib.sparse``
``accelerate.cuda.sorting``  ``pycudalib.sorting``
===========================  ===========================

