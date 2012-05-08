#!/usr/bin/env python

def ct(m, n):
    return ((n*n + n) * (m*m + m)) / 4

diff = 1000000
bits = None

# don't know how to calculate the minimum of
# (n^2 + n)(m^2 + m) - 4000000 = 0

# know that 1, 2000 = 2001000, so we can assume
# upper bound is 2000

for i in range(2, 2000):
    for j in range(i, 2000):
        x = ct(i, j)
        new_diff = abs(2000000 - x)
        if new_diff < diff:
            diff = new_diff
            bits = x, i, j, i*j 
print '%s...%s * %s = %s' % bits
