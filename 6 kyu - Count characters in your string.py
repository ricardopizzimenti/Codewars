"""
The main idea is to count all the occurring characters in a string.
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.

# option 1

def count(string):
    dic = {}
    for i in string:
        if i not in dic:
            dic[i] = string.count(i)
    return dic
"""

# option 2

def count(string):
    dic = {i: string.count(i) for i in string}
    return dic

print(count('aba'))