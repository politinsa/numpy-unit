# numpy-unit

[![Build Status](https://travis-ci.org/politinsa/numpy-unit.svg?branch=master)](https://travis-ci.org/politinsa/numpy-unit)
[![Documentation Status](https://readthedocs.org/projects/numpy-unit/badge/?version=latest)](https://numpy-unit.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/numpy-unit.svg)](https://badge.fury.io/py/numpy-unit)
[![codecov](https://codecov.io/gh/politinsa/numpy-unit/branch/master/graph/badge.svg)](https://codecov.io/gh/politinsa/numpy-unit)
[![license](https://img.shields.io/badge/license-Unlicense-blue)](https://github.com/politinsa/numpy-unit/blob/master/LICENSE)


This package provides a tool for scientific computing by keeping track of the unit when performing classical operations on a multi-dimensionnal array with (almost) no extra-cost comparing to the standard numpy array.  
The `ArrayUnit` class supports every operation a numpy.ndarray can handle (because it is a derived class of numpy.ndarray) but the operators are overloaded in order to perform transformations on the `Unit` contained in every `ArrayUnit`.  

Because **any `ArrayUnit` is a numpy.ndarray**, classical ndarray methods work and returns an `ArrayUnit` whenever possible. It means that ``mean``, ``std``, ``var``, ``min``, ``max``, ``ravel``, ``flatten``, ``fill``, ``reshape``, ``diagonal``, ``sum``, ``prod`` behaves as you expect and the result is encapsulated in an `ArrayUnit` with the `Unit` corresponding (:warning: ``var`` and ``prod`` do change the `Unit`).

## Install

    pip install numpy-unit

## Examples

```python
>>> import numpy as np
>>> from numpy_unit import Unit, ArrayUnit
>>> 
>>> m = Unit('m')
>>> sm2 = Unit('s', -2)
>>> complex_unit = Unit({'my_unit': 0.5, '€': 1, 'capita': 2}) * (sm2**0.5) / m
>>> print(complex_unit)
€·capita²·my_unit^0.5·m⁻¹·s⁻¹
>>>
>>> arr = np.linspace(1,10,10, dtype=float)
>>> a = ArrayUnit(arr, m)
>>> b = ArrayUnit(arr**2, sm2)
>>> print(a, '\\n+\\n', 1, '\\n=\\n', a + 1)
[ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.] m
+
1 
=
[ 2.  3.  4.  5.  6.  7.  8.  9. 10. 11.] m
>>> print(a, '\\n*\\n', b, '\\n=\\n', a * b)
[ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.] m
*
[  1.   4.   9.  16.  25.  36.  49.  64.  81. 100.] s⁻²
=
[   1.    8.   27.   64.  125.  216.  343.  512.  729. 1000.] m·s⁻²
>>>
>>>
>>> b = ArrayUnit(np.random.random((2, 4)), Unit('banana'))
>>> b
ArrayUnit([[0.7257637 , 0.04797737, 0.88016759, 0.69852201],
           [0.12102613, 0.07913234, 0.38511503, 0.3645144 ]]) banana
>>> b.mean(axis=0)
ArrayUnit([0.42339491, 0.06355485, 0.63264131, 0.5315182 ]) banana
>>> b.prod(axis=1)
ArrayUnit([0.02140805, 0.00134443]) banana⁴

```

The following rules applied (where {op} is one of the following: [``+``, ``-``, ``*``, ``/``, ``//``, ``%``]):  

* ArrayUnit {op} Object returns an ArrayUnit with the same unit as the ArrayUnit
* Object {op} ArrayUnit returns an ArrayUnit with the same unit as the ArrayUnit
* ArrayUnit {op} ArrayUnit returns an ArrayUnit combining the Unit of the 2 ArrayUnit or an Error
* An Error might be raised only when two ArrayUnit are conflicting and that ArrayUnit.is_strict is set to True. Otherwise, it would print a warning.
* An ArrayUnit is equal to a numpy.ndarray if and only if their underlying arrays are equal (np.array_equal) and the Unit of the ArrayUnit is empty.

## Development
Doc of the master branch on [readthedocs.io](https://numpy-unit.readthedocs.io/en/latest/).

## Features
- [x] Basic unit system handling comparison, multiplication, division, modulo and power
- [x] ArrayUnit wrapper for unit + ndarray
- [x] Operators on ArrayUnit (and their variants __r{op}__ and __i{op}__)
     - [ ] eq, ne // how to deal with this? Current implementation should be changed because we can't use array mask now
     - [x] add
     - [x] sub
     - [x] mul
     - [x] truediv, floordiv
     - [x] mod
     - [x] pow (but not __rpow__)
- [x] Rewrite ndarray methods changing the Unit
     - [x] var
     - [x] prod
- [ ] conda release
- [ ] push to a dev branch before master?! (not mandatory when no one is using the package though)
