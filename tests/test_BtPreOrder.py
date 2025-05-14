import unittest
from src.BtPreOrder import bt_pre_order
from tree import tree

class TestBtPreOrder(unittest.TestCase):

    def setUp(self):
        self.tree = tree

    def test_function(self):
        self.assertEqual(bt_pre_order(tree), [20, 10, 5, 7, 15, 50, 30, 29, 45, 100])


if __name__ == '__main__':
    unittest.main()