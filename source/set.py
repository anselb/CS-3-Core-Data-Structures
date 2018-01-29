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
            self.size += 1

    def remove(self, element):
        """Remove element from this set, if not presenet, raise ValueError."""
        if not self.contains(element):
            raise ValueError("'{}' was not found".format(element))
        else:
            self.set.remove(element)
            self.size -= 1

    def union(self, other_set):
        """Return a new set that is the union of this set and other_set."""
        union_set = self.set + other_set
        return union_set

    def intersection(self, other_set):
        """Return a new set that is the intersection of this set and other_set."""
        intersection_set = []
        if len(self.set) > len(other_set):
            for item in other_set:
                if self.set.contains(item):
                    intersection_set.append(item)

        else:
            for item in self.set:
                if item in other_set:
                    intersection_set.append(item)
        return intersection_set

    def difference(self, other_set):
        """Return a new set that is the difference of this set and other_set."""
        difference_set = []
        for item in other_set:
            if not self.set.contains(item):
                difference_set.append(item)

        for item in self.set:
            if item not in other_set:
                difference_set.append(item)
        return difference_set

    def is_subset(self, other_set):
        """Return a True if other_set is a subset of this set, False otherwise."""
        for item in other_set:
            if item not in self.set:
                return False

        return True
