#!python

from set import Set
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class SetTest(unittest.TestCase):

    def test_init(self):
        st = Set(['a', 'b', 'c'])
        assert st.size == 3

    def test_contains(self):
        st = Set(['a', 'b', 'c'])
        assert st.contains('a') is True
        assert st.contains('b') is True
        assert st.contains('c') is True

        assert st.contains('d') is False
        assert st.contains('e') is False
        assert st.contains('f') is False

    def test_add(self):
        st = Set()
        st.add('a')
        assert st.size == 1
        assert st.contains('a') is True

        st.add('b')
        assert st.size == 2
        assert st.contains('a') is True
        assert st.contains('b') is True

        st.add('c')
        assert st.size == 3
        assert st.contains('a') is True
        assert st.contains('b') is True
        assert st.contains('c') is True

    def test_removie(self):
        st = Set(['a', 'b', 'c'])
        assert st.size == 3
        assert st.contains('a') is True
        assert st.contains('b') is True
        assert st.contains('c') is True

        st.remove('a')
        assert st.size == 2
        assert st.contains('a') is False
        assert st.contains('b') is True
        assert st.contains('c') is True

        st.remove('b')
        assert st.size == 1
        assert st.contains('a') is False
        assert st.contains('b') is False
        assert st.contains('c') is True

        st.remove('c')
        assert st.size == 0
        assert st.contains('a') is False
        assert st.contains('b') is False
        assert st.contains('c') is False

    def test_union(self):
        st = Set(['a', 'b', 'c'])
        other_set = ['d', 'e', 'f']
        union_set = st.union(other_set)
        assert union_set.size == 6

        assert union_set.contains('a') is True
        assert union_set.contains('b') is True
        assert union_set.contains('c') is True
        assert union_set.contains('d') is True
        assert union_set.contains('e') is True
        assert union_set.contains('f') is True
        assert union_set.contains('g') is False

    def test_intersection(self):
        st = Set(['a', 'b', 'c'])
        other_set = ['b', 'e', 'c', 'f']
        intersection_set = st.intersection(other_set)
        assert intersection_set.size == 2

        assert intersection_set.contains('a') is False
        assert intersection_set.contains('b') is True
        assert intersection_set.contains('c') is True
        assert intersection_set.contains('d') is False
        assert intersection_set.contains('e') is False
        assert intersection_set.contains('f') is False
        assert intersection_set.contains('g') is False

    def test_difference(self):
        st = Set(['a', 'b', 'c'])
        other_set = ['b', 'e', 'c', 'f']
        difference_set = st.difference(other_set)
        assert difference_set.size == 3

        assert difference_set.contains('a') is True
        assert difference_set.contains('b') is False
        assert difference_set.contains('c') is False
        assert difference_set.contains('d') is False
        assert difference_set.contains('e') is True
        assert difference_set.contains('f') is True
        assert difference_set.contains('g') is False

    def test_is_subset(self):
        st = Set(['a', 'b', 'c'])
        other_set = ['a']
        assert st.is_subset(other_set) is True

        other_set = ['b']
        assert st.is_subset(other_set) is True

        other_set = ['c']
        assert st.is_subset(other_set) is True

        other_set = ['a', 'b']
        assert st.is_subset(other_set) is True

        other_set = ['b', 'c']
        assert st.is_subset(other_set) is True

        other_set = ['a', 'b', 'c']
        assert st.is_subset(other_set) is True

        other_set = ['a', 'b', 'c', 'd']
        assert st.is_subset(other_set) is False

        other_set = ['a', 'b', 'd']
        assert st.is_subset(other_set) is False

        other_set = ['d']
        assert st.is_subset(other_set) is False
