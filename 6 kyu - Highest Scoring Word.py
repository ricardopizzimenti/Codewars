"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
"""


def high(x):
    letter = 'abcdefghijklmnopqrstuvwxyz'
    scores = []
    word = x.split()
    for i in word:
        point = 0
        for e in i:
            point += letter.index(e) + 1
        scores.append(point)
        point = 0
    return word[scores.index(max(scores))]


print(high('man i need a taxi up to ubud'))