import unittest
from src.BtInOrder import bt_in_order
from tree import tree

class TestBtInOrder(unittest.TestCase):

    def setUp(self):
        self.tree = tree

    def test_function(self):
        self.assertEquals(bt_in_order(tree), [5, 7, 10, 15, 20, 29, 30, 45, 50, 100])


if __name__ == '__main__':
    unittest.main()