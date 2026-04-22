# Create the following infinite iterators:
# (a) returning 0, 1, 0, 1, 0, 1, ...,

def iter_a():
    while True:
        yield 0
        yield 1

# (b) returning randomly 0 or 1 on demand,

import random

def iter_b():
    while True:
        yield random.choice([0, 1])
      
# (c) returning 0, 1, 0, -1, 0, 1, 0, -1, ... 

from itertools import cycle

iter_c = cycle([0, 1, 0, -1])
