"""You have a carrier route list with 100,000 (100K) entries (in arbitrary
order) and a single phone number. How quickly can you find the cost of calling
this number?"""


import sys
sys.path.append('../source/')

from strings import find_all_indexes


with open('data/route-costs-106000.txt', 'r') as f:
    data = f.read()
    number = '+3346182'
    indexes = find_all_indexes(data, number)
    index = indexes[0]
    test = data[index + len(number) + 1:index + len(number) + 5]
print(test)

# Command-F works a lot faster if a coworker is asking for the cost of a single
# route.
