import unittest
from src.QuickSort import quick_sort


class TestQuickSort(unittest.TestCase):

    def setUp(self):
        self.arr = [9, 3, 7, 4, 69, 420, 42]

    def test_function(self):
        quick_sort(self.arr)
        self.assertEqual(self.arr, [3, 4, 7, 9, 42, 69, 420])


if __name__ == '__main__':
    unittest.main()
