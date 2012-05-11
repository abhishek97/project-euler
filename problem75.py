#!/usr/bin/env python
import math

"""
had to do a little wikipedia dive for this one, looked at generating primitive
pythagorean triples.  found euclid's formula:

http://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple

m and n, such that m > n, m+n is odd, and m and n are coprime

a = m*m - n*n
b = 2mn
c = m*m + n*n

also we know that:
a + b + c <= 1500000

from the formula:
c = m*m + n*n

maximum value for c is 1499997 (a < b < c, 1 < 2 < 1499997) so we can
figure out a good upper bound for m:

c < 2(m*m)
1499997 < 2(m*m)
sqrt(1499997/2) < m
"""
L = 1500000
max_c = L - 3
max_m = int(math.sqrt(max_c / 2)) + 1
is_odd = lambda s: s % 2 == 1

def memo(fn):
    _memo = {}
    def inner(n):
        if n not in _memo:
            _memo[n] = fn(n)
        return _memo[n]
    return inner

@memo
def divisors(n):
    d = set()
    for s in range(1, int(math.sqrt(n)) + 1):
        if n % s == 0:
            d.add(s)
            d.add(n/s)
    return d

coprime = lambda m, n: divisors(m) & divisors(n) == set([1])
counts = {}

for m in range(2, max_m):
    for n in range(1, m):
        if is_odd(m+n) and coprime(m, n):
            a = (m*m) - (n*n)
            b = 2*m*n
            c = (m*m) + (n*n)

            length = a + b + c
            
            while length < L:
                counts.setdefault(length, 0)
                counts[length] += 1
                length += (a+b+c)

print sum([v for v in counts.values() if v == 1])
