import unittest
from src.BtPostOrder import bt_post_order
from tree import tree

class TestBtPostOrder(unittest.TestCase):

    def setUp(self):
        self.tree = tree

    def test_function(self):
        self.assertEqual(bt_post_order(tree), [7, 5, 15, 10, 29, 45, 30, 100, 50, 20])


if __name__ == '__main__':
    unittest.main()