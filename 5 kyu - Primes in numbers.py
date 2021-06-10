"""
Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
"""


def prime_factors(n):
    res = n
    div = 2
    val = []
    while res != 1:
        while res % div == 0:
            res /= div
            val.append(div)
        div += 1
    new = []
    for i in sorted(set(val)):
        if val.count(i) > 1:
           new.append(f'({i}**{val.count(i)})')
        else:
            new.append(f'({i})')
    return ''.join(new)




print(prime_factors(18195729))
