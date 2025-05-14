import unittest
from src.BtBfs import bt_bfs
from tree import tree

class TestBTBFS(unittest.TestCase):

    def setUp(self):
        self.tree = tree

    def test_function(self):
        self.assertTrue(bt_bfs(tree, 45))
        self.assertTrue(bt_bfs(tree, 7))
        self.assertFalse(bt_bfs(tree, 69))


if __name__ == '__main__':
    unittest.main()