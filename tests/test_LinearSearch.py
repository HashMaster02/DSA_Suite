import unittest
from src.LinearSearchList import linear_search


class TestLinearSearch(unittest.TestCase):

    def setUp(self):
        self.nums = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]

    def test_function(self):
        self.assertTrue(linear_search(self.nums, 69))
        self.assertFalse(linear_search(self.nums, 1336))
        self.assertTrue(linear_search(self.nums, 69420))
        self.assertFalse(linear_search(self.nums, 69421))
        self.assertTrue(linear_search(self.nums, 1))
        self.assertFalse(linear_search(self.nums, 0))


if __name__ == '__main__':
    unittest.main()