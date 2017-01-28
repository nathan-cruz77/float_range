# float_range ![Build](https://travis-ci.org/nathan-cruz77/float_range.svg?branch=master)
A range-like generator for float numbers.

# Installation
Simply do `pip install float_range` and you are good to go.
If installing from outside of a virtualenv you may need to prefix
that with `sudo` though.

# Requirements
Tests run on CPython 2.6+ and 3.2+. Also Pypy (2.7) and Pypy3 (3.3) are supported.
However it may run smoothly on any Python 2.3+ implementation.

# Usage
```python
import float_range

for i in float_range.range(1, 5, 0.5):
    print(i, end=' ')
# >>> 1 1.5 2.0 2.5 3.0 3.5 4.0 4.5

for i in float_range.range(1, 5, 0.55):
    print(i, end=' ')
# >>> 1 1.55 2.1 2.65 3.2 3.75 4.3 4.85

# Equivalent of range(10) in python3 and xrange(10) in python2
for i in float_range.range(10):
    print(i, end=' ')
# >>> 0 1 2 3 4 5 6 7 8 9

for i in float_range.range(1.5, 5, 0.7):
    print(i, end=' ')
# >>> 1.5 2.2 2.9 3.6 4.3

for i in float_range.range(5, 1.5, -0.7):
    print(i, end=' ')
# >>> 5 4.3 3.6 2.9 2.2
```
