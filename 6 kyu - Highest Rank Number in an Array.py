"""
Complete the method which returns the number which is most frequent in the given input array.
If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.

Examples

[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3
"""


def highest_rank(arr):
    freq = 0
    for i in arr:
        if arr.count(i) > arr.count(freq):
            freq = i
        elif arr.count(i) == arr.count(freq):
            freq = max([i, freq])
    return freq



print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]))