"""
Write Number in Expanded Form

You will be given a number and you will need to return it as a string in Expanded Form.

For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.
"""


def expanded_form(num):
    txt = [i for i in str(num)]
    lst = []
    count = 1
    for i in txt:
        if i != '0':
            lst.append(i + ('0' * (len(str(num)) - count)))
        count += 1
    return ' + '.join(lst)


print(expanded_form(381395))
