"""You have a carrier route list with 100,000 (100K) entries (in arbitrary
order) and a list of 1000 phone numbers. How can you operationalize the route
cost lookup problem?"""

import sys
sys.path.append('../source/')

# from hashtable import HashTable
# I realized it is faster to use the built in dictionary


def read_to_hashtable(file_name):
    """Insert the route cost csv data into a hashtable line by line and
    return the hashtable."""
    route_costs = {}
    with open(file_name, 'r') as f:
        for line in f:
            number_cost_pair = line.strip("\n").split(",")
            if (route_costs.get(number_cost_pair[0]) is None or
               route_costs.get(number_cost_pair[0]) > number_cost_pair[1]):
                route_costs[number_cost_pair[0]] = number_cost_pair[1]

    return route_costs

def search_hashtable(costs_table, phone_number):
    """Given a phone number and a hashtable of route costs, find the route cost
    for the phone number and return it."""
    route_cost = 0
    while phone_number != '+':
        if costs_table.get(phone_number) is None:
            phone_number = phone_number[:-1]
            print(phone_number)
        else:
            return costs_table.get(phone_number)

    return route_cost


if __name__ == '__main__':
    costs_table = read_to_hashtable('data/route-costs-106000.txt')
    print(search_hashtable(costs_table, '+3314087756'))
    # print(read_to_hashtable('data/route-costs-10.txt'))
