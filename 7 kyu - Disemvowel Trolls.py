"""
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
"""


def disemvowel(string_):
    lista = list(string_)

    while 'a' in lista:
        lista.remove('a')
    while 'e' in lista:
        lista.remove('e')
    while 'i' in lista:
        lista.remove('i')
    while 'o' in lista:
        lista.remove('o')
    while 'u' in lista:
        lista.remove('u')
    while 'A' in lista:
        lista.remove('A')
    while 'E' in lista:
        lista.remove('E')
    while 'I' in lista:
        lista.remove('I')
    while 'O' in lista:
        lista.remove('O')
    while 'U' in lista:
        lista.remove('U')

    string_ = ''.join(lista)

    return string_