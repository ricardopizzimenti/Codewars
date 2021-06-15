"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example

"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""

# Option 1

def solution(s):
    lst = []
    for i in s:
        if i.isupper():
            lst.append(' ')
            lst.append(i)
        else:
            lst.append(i)
    return ''.join(lst)
"""


# Option 2

def solution(s):
    return ''.join(' ' + i if i.isupper() else i for i in s)


print(solution("helloWorld"))
