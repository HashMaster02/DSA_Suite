import unittest
from src.BinarySearchList import binary_search


class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.nums = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]

    def test_function(self):
        self.assertTrue(binary_search(self.nums, 69))
        self.assertFalse(binary_search(self.nums, 1336))
        self.assertTrue(binary_search(self.nums, 69420))
        self.assertFalse(binary_search(self.nums, 69421))
        self.assertTrue(binary_search(self.nums, 1))
        self.assertFalse(binary_search(self.nums, 0))


if __name__ == '__main__':
    unittest.main()
