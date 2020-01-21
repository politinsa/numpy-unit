# numpy-unit

This package provides a tool for scientific computing by keeping track of the unit when performing classical operations on a multi-dimensionnal array with (almost) no extra-cost comparing to the standard numpy array.  
The `ArrayUnit` class supports every operation a numpy.ndarray can handle (because it is a derived class of numpy.ndarray) but the operators are overloaded in order to perform transformations on the `Unit` contained in every `ArrayUnit`.


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
```

The following rules applied (where {op} is one of the following: [``+``, ``-``, ``*``, ``/``, ``//``, ``%``]):  

* ArrayUnit {op} Object returns an ArrayUnit with the same unit as the ArrayUnit
* Object {op} ArrayUnit returns an ArrayUnit with the same unit as the ArrayUnit
* ArrayUnit {op} ArrayUnit returns an ArrayUnit combining the Unit of the 2 ArrayUnit or an Error
* An Error might be raised only when two ArrayUnit are conflicting and that ArrayUnit.is_strict is set to True. Otherwise, it would print a warning.
* An ArrayUnit is equal to a numpy.ndarray if and only if their underlying arrays are equal (np.array_equal) and the Unit of the ArrayUnit is empty.

## Development
Doc of the master branch on [github.io](https://politinsa.github.io/numpy-unit/)

## Features
- [x] Basic unit system handling multiplication, division, modulo and power
- [x] ArrayUnit wrapper for unit + ndarray
- [x] Operators on ArrayUnit (and their variants __r{op}__ and __i{op}__)
     - [x] eq, ne
     - [x] add
     - [x] sub
     - [x] mul
     - [x] truediv, floordiv
     - [x] mod
     - [x] pow (but not __rpow__)
- [ ] Basic ndarray function
     - [ ] mean
     - [ ] std
     - [ ] ...