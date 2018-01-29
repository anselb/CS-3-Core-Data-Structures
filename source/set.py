#!python

class Set(object):

    def __init__(self, elements=None):
        """Initialize this set, and add each element if elements is given."""
        self.set = list()
        self.size = 0  # Number of items in set
        for item in elements:
            self.add(item)
