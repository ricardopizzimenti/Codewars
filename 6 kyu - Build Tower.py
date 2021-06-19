"""
Build Tower

Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

Python: return a list;
JavaScript: returns an Array;
C#: returns a string[];
PHP: returns an array;
C++: returns a vector<string>;
Haskell: returns a [String];
Ruby: returns an Array;
Lua: returns a Table;
Have fun!

for example, a tower of 3 floors looks like below

[
  '  *  ',
  ' *** ',
  '*****'
]
and a tower of 6 floors looks like below

[
  '     *     ',
  '    ***    ',
  '   *****   ',
  '  *******  ',
  ' ********* ',
  '***********'
]
Go challenge Build Tower Advanced once you have finished this :)
"""


def tower_builder(n_floors):
    count = 1
    lst = []

    for i in range(n_floors):
        lst.append(' ' * ((n_floors - i) - 1) + ('*' * (count) + (' ' * ((n_floors - i) - 1))))
        count += 2
    return lst

print(tower_builder(3))