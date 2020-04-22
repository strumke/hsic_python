# HSIC Python 

This repository contains code for calculating the Hilbert-Schmidt Independence
Criterion in Python as in 
[1] [Measuring Statistical Dependence with Hilbert-Schmidt
Norms](https://link.springer.com/chapter/10.1007/11564089_7) (2005)
and
[2] [Kernel-based Tests for Joint
Independence](https://www.researchgate.net/publication/301818817_Kernel-based_Tests_for_Joint_Independence)
(2016)

### Files

- `hsic.py`: Contains the code needed to calculate the HSIC
- `run_examples.py`: Examples for usage

### Dependencies

The scripts are written for Python 3.6 and require Numpy

### Usage 

Download the file hsic.py, and (add it to the system path, or) from within the
same directory execute the following from within a Python REPL or a .py file
```python
from hsic import dHSIC
dHSIC(X, Y, ...)
```
where all inputs to dHSIC, `X` and `Y` etc, are of type `numpy.ndarray`.
If only two inputs `X` and `Y` are passed to `dHSIC`, the simpler `HSIC` is
automatically called, and the hsic value is computed as in [1], eq. (9).
If more than two inputs are passed to `dHSIC`, the computation is done as in
[2], Definition 2.6. 
