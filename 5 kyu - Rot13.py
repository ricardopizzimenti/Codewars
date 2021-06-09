"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.
ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13.
If there are numbers or special characters included in the string, they should be returned as they are.
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""


def rot13(message):
    numb = [ord(i) for i in message]
    new = []
    for i in numb:
        if 97 <= i <= 123:
            if i + 13 >= 123:
                new.append(chr((i + 13) - 26))
            else:
                new.append(chr(i + 13))
        elif 65 <= i <= 91:
            if i + 13 >= 91:
                new.append(chr((i + 13) - 26))
            else:
                new.append(chr(i + 13))
        else:
            new.append(chr(i))

    return ''.join(new)
