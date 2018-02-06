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
        else:
            return costs_table.get(phone_number)

    return route_cost

def write_costs_to_file(costs_table, file_to_read):
    """Given a dictionary of phone numbers and costs and the name of a file
    with phone numbers, write the costs of calling each of the given numbers to
    the file."""
    numbers = file_to_read[19:-1 - 3]
    output_file = "test_files/route-costs-" + numbers + ".txt"
    with open(file_to_read, 'r') as f:
        for line in f:
            cost = search_hashtable(costs_table, line)
            with open(output_file, 'a') as g:
                g.write(line.strip('\n') + "," + str(cost) + '\n')

if __name__ == '__main__':
    costs_table = read_to_hashtable('data/route-costs-10000000.txt')
    write_costs_to_file(costs_table, 'data/phone-numbers-1000.txt')
    
    # costs_table = read_to_hashtable('data/route-costs-106000.txt')
    # print(search_hashtable(costs_table, '+3314087756'))

    # print(read_to_hashtable('data/route-costs-10.txt'))
