cuRAND
======

Provides `pseudo-random number generator` (PRNG) and `quasi-random generator` (QRNG).
See `NVIDIA cuRAND <http://docs.nvidia.com/cuda/curand/index.html>`_.

class PRNG
-----------

.. autoclass:: pycudalib.rand.PRNG
   :members:


class QRNG
------------

.. autoclass:: pycudalib.rand.QRNG
   :members:


Top Level PRNG Functions
--------------------------

Simple interface to the PRNG methods.

.. note:: This methods automatically create a PRNG object.

.. autofunction:: pycudalib.rand.uniform

.. autofunction:: pycudalib.rand.normal

.. autofunction:: pycudalib.rand.lognormal

.. autofunction:: pycudalib.rand.poisson

Top Level QRNG Functions
--------------------------

Simple interface to the QRNG methods.

.. note:: This methods automatically create a QRNG object.

.. autofunction:: pycudalib.rand.quasi
