"""
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.:

row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8
"""


def row_sum_odd_numbers(n):
    beg = 0
    val = n

    while n > 0:
        beg += n - 1
        n -= 1

    odd = []

    for i in range(1, (val + 1) * val, 2):
        odd.append(i)

    final = beg + val

    return sum(odd[beg:final])