cuFFT
=======

Provides FFT and inverse FFT for 1D, 2D and 3D arrays.
See `NVIDIA cuFFT <http://docs.nvidia.com/cuda/cufft/index.html>`_.


.. note::  cuFFT only supports FFT operations on numpy.float32, numpy float64,
           numpy.complex64, numpy.complex128 with C-contiguous datalayout.


Forward FFT
------------

.. py:function:: pycudalib.fft.fft(ary, out[, stream])
.. py:function:: pycudalib.fft.fft_inplace(ary[, stream])

    :param ary: The input array. The inplace version stores the result in here.
    :param out: The output array for non-inplace versions.
    :param stream: The CUDA stream in which all operations will take place.


Inverse FFT
------------

.. py:function:: pycudalib.fft.ifft(ary, out[, stream])
.. py:function:: pycudalib.fft.ifft_inplace(ary[, stream])

    :param ary: The input array. The inplace version stores the result in here.
    :param out: The output array for non-inplace versions.
    :param stream: The CUDA stream in which all operations will take place.

FFTPlan
--------

.. autoclass:: pycudalib.fft.FFTPlan
    :members:

