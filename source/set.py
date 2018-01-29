#!python

class Set(object):

    def __init__(self, elements=None):
        """Initialize this set, and add each element if elements is given."""
        self.set = list()
        self.size = 0  # Number of items in set
        for item in elements:
            self.add(item)

    def contains(self, element):
        """Return True if element is in set, otherwise return False."""
        return element in self.set

    def add(self, element):
        """Add element to set, if not already in set."""
        if self.contains(element):
            self.set.append(element)

    def remove(self, element):
        """Remove element from this set, if not presenet, raise ValueError."""
        if not self.contains(element):
            raise ValueError("'{}' was not found".format(element))
        else:
            self.set.remove(element)
    
