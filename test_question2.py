import unittest
from hypothesis import given, strategies as st
from question2 import quick_sort

class T(unittest.TestCase):
    def test_it_works_on_one_example(self):
        self.assertEqual(quick_sort([8,2,1,7,8]),[1,2,7,8,8]);

    @given(st.lists(st.integers()))
    def test_quick_sort(self, arr):
        self.assertEqual(quick_sort(arr), sorted(arr))        

unittest.main()