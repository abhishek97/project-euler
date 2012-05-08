#!/usr/bin/env python

def memo(fn):
    _memo = {}
    def inner(k, n):
        tup = (k, n)
        if tup not in _memo:
            _memo[tup] = fn(k, n)
        return _memo[tup]
    return inner

@memo
def p(k, n):
    if k > n:
        return 0
    if k == n:
        return 1
    return p(k+1, n) + p(k, n-k)

# subtract 1 since we don't count n + 0
print p(1, 100) - 1
