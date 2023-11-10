import unittest
from hypothesis import given, strategies as st
from question2 import quick_sort

class T(unittest.TestCase):
    def test_it_works_on_one_example(self):
        self.assertEqual(quick_sort([8,2,1,7,8]),[1,2,7,8,8]);
    
    #Reinforcing the failing test works again
    def test_it_works_on_another_example(self):
        self.assertEqual(quick_sort([0, 1, 0]),[0, 0, 1]);

    @given(st.lists(st.integers()))
    def test_quick_sort(self, arr):
        self.assertEqual(quick_sort(arr), sorted(arr))

    # Testing whether that it equals itself when passed through twice
    @given(st.lists(st.integers()))
    def test_quick_sort_equals_itself(self, arr):
        self.assertEqual(quick_sort(arr), quick_sort(quick_sort(arr)))    

unittest.main()