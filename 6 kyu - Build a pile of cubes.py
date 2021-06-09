"""
Your task is to construct a building which will be a pile of n cubes. The cube at the bottom will have a volume of n^3, the cube above will have volume of (n-1)^3 and so on until the top which will have a volume of 1^3.

You are given the total volume m of the building. Being given m can you find the number n of cubes you will have to build?

The parameter of the function findNb (find_nb, find-nb, findNb, ...) will be an integer m and you have to return the integer n such as n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n.

Examples:

findNb(1071225) --> 45

findNb(91716553919377) --> -1
"""


def find_nb(m):
    res = m
    n = 1
    while res > 0:
        res -= n ** 3
        if res > 0:
            n += 1
    if res == 0:
        return n
    else:
        return -1

print(find_nb(4183059834009))

"""
n ** 3 = x0
n - 1 ** 3 = x0 + x1
n - 2 ** 3 = x1 + x2

5 ** 3 = 125
4 ** 3 = 125 + 64
3 ** 3 = 189 + 27
2 ** 3 = 216 + 8
1 ** 3 = 224 + 1
225

225 - 1 = 1 ** 3
224 - 8 = 2 ** 3

"""