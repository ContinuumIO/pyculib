============
CUDA Sorting
============

Pycudalib provides routines for sorting arrays on CUDA GPUs.

Sorting Large Arrays
====================

The :py:class:`pycudalib.sorting.RadixSort` class is recommended for
sorting large (approx. more than 1 million items) arrays of numeric types.

.. autoclass:: pycudalib.sorting.RadixSort
   :members:

Sorting Many Small Arrays
=========================

Using :py:class:`pycudalib.sorting.RadixSort` on small (approx. less than
1 million items) arrays has significant overhead due to multiple kernel
launches. 

A better alternative is to use :py:func:`pycudalib.sorting.segmented_sort`-which launches a single kernel for sorting a batch of many small arrays.

.. autofunction:: pycudalib.sorting.segmented_sort
