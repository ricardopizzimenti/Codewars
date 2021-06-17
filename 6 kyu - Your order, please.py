"""
Your task is to sort a given string. Each word in the string will contain a single number.
This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string.
The words in the input String will only contain valid consecutive numbers.

Examples

"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
"""


def order(sentence):
    nl = ['' for i in range(9 - (9 - len(sentence.split())))]
    for i in sentence.split():
        if '1' in i:
            nl[0] = i
        elif '2' in i:
            nl[1] = i
        elif '3' in i:
            nl[2] = i
        elif '4' in i:
            nl[3] = i
        elif '5' in i:
            nl[4] = i
        elif '6' in i:
            nl[5] = i
        elif '7' in i:
            nl[6] = i
        elif '8' in i:
            nl[7] = i
        elif '9' in i:
            nl[8] = i

    return ' '.join(nl)


print(order("4of Fo1r pe6ople g3ood th5e the2"))