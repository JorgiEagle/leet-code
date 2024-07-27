"""
Given an integer, n

A super string is any bit string (0, 1)s that can be generated from the bit representation of n, by changing zero or more bits from 0 to 1

E.g 21
Base 2: 10101

Super strings:

10101 (0 bits changed)
10111 (1 bit changed)
11101 (1 bit changed)
11111 (2 bits changed)

Given a list of bit strings, and a defualt length l, what is the total number of unique super strings

e.g.
bit_strings = [21, 7]
k = 5

super bit strings:

10101
10111
11101 
11111

00111
01111
10111
11111

Total super strings: 6
(11111 and 10111 are repeated)
"""
from random import randint
from typing import Sequence
from time import time

def independent_inputs(func):
    def inner(bit_strings, k):
        bit_strings = bit_strings.copy()
        return func(bit_strings, k)
    return inner


def timer(func):
    def inner(*args):
        start = time()
        result = func(*args)
        end = time()
        return end-start, result
    return inner
    

@independent_inputs
@timer
def super_strings(bit_strings: Sequence[int], k: int):
    super_strings = set()
    while bit_strings:
        current_number = bit_strings.pop()
        super_strings.add(current_number)
        # Get zero positions
        for index in range(k):
            if (current_number >> index) % 2:
                continue
            perm = current_number | (1 << index)
            if perm not in super_strings:
                bit_strings.append(perm)
    return len(super_strings)


@independent_inputs
@timer
def super_strings_2(bit_strings: Sequence[int], k: int):
    bit_strings = sorted(bit_strings, reverse=True)
    super_strings = set()
    while bit_strings:
        current_number = bit_strings.pop()
        super_strings.add(current_number)
        # Get zero positions
        for index in range(k):
            if (current_number >> index) % 2:
                continue
            perm = current_number | (1 << index)
            if perm not in super_strings:
                bit_strings.append(perm)
    return len(super_strings)


k = 20
inputs = [randint(0, (2**k) - 1) for x in range(1000000)]

print(super_strings(inputs, k))
print(super_strings_2(inputs, k))