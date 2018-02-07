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
        st = Set()
        pass

    def test_intersection(self):
        st = Set()
        pass

    def test_difference(self):
        st = Set()
        pass

    def test_is_subset(self):
        st = Set()
        pass
