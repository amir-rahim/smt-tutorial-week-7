import unittest
from hypothesis import given, strategies as st
from question1 import mysum

class T(unittest.TestCase):
    @given(st.lists(st.integers()))
    def test_sum_is_positive(self, list_of_ints):
        self.assertGreaterEqual(mysum(list_of_ints), 0)

unittest.main()