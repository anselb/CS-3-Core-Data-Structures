#!python

# NOTE: In the intersection method, choosing to iterate based on length of the
# set is pointless because the 'in' keyword will iterate through the other set.
# In a different implementation of the Set class, where iterating through the
# passed in set can be done quicker than O(n), then choosing which set to
# iterate over will matter.
# NOTE: When adding an abstract data type to your code, you should try to use
# the correct implementation of the data structure. Even though a Python list
# may only be composed of unique items and might technically be called a set,
# a duplicate item can still be added and make it not a set.
# NOTE: There is a difference between self.set and self. self.set will refer to
# whatever self.set is; in this Set class, self.set is a list. The self keyword
# will refer its own class and its own methods. Ex: self.set.remove() is the
# list method remove while self.remove() is self's remove method.


class Set(object):

    def __init__(self, elements=None):
        """Initialize this set, and add each element if elements is given."""
        self.set = list()
        self.size = 0  # Number of items in set
        if elements is not None:
            for item in elements:
                self.add(item)

    def contains(self, element):
        """Return True if element is in set, otherwise return False."""
        return element in self.set

    def add(self, element):
        """Add element to set, if not already in set."""
        if not self.contains(element):
            self.set.append(element)
            self.size += 1

    def remove(self, element):
        """Remove element from this set, if not presenet, raise ValueError."""
        if not self.contains(element):
            raise ValueError("'{}' was not found".format(element))
        else:
            # O(n) in every case
            self.set.remove(element)
            self.size -= 1

    def union(self, other_set):
        """Return a new set that is the union of this set and other_set."""
        union_set = self.set + other_set
        return union_set

    def intersection(self, other_set):
        """Return a new set that is the intersection of this set and other_set."""
        intersection_set = Set()
        # if len(self.set) > len(other_set):
        for item in other_set:
            if self.contains(item):
                intersection_set.add(item)

        # else:
        #     for item in self.set:
        #         if item in other_set:
        #             intersection_set.append(item)
        return intersection_set

    def difference(self, other_set):
        """Return a new set that is the difference of this set and other_set."""
        difference_set = Set()
        for item in other_set:
            if not self.contains(item):
                difference_set.add(item)

        for item in self.set:
            if item not in other_set:
                difference_set.add(item)
        return difference_set

    def is_subset(self, other_set):
        """Return a True if other_set is a subset of this set, False otherwise."""
        for item in other_set:
            if item not in self.set:
                return False

        return True
