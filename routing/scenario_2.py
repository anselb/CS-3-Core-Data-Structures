"""You have a carrier route list with 100,000 (100K) entries (in arbitrary
order) and a list of 1000 phone numbers. How can you operationalize the route
cost lookup problem?"""

import sys
sys.path.append('../source/')

from hashtable import HashTable


def read_to_hashtable(file_name):
    """Insert the route cost csv data into a hashtable line by line and
    return the hashtable."""
    route_costs = HashTable()
    with open(file_name, 'r') as f:
        for line in f:
            number_cost = line.strip("\n").split(",")
            route_costs.set(number_cost[0], number_cost[1])
    return route_costs

def search_hashtable():
    """."""
    pass


if __name__ == '__main__':
    print(read_to_hashtable('data/route-costs-10.txt'))
