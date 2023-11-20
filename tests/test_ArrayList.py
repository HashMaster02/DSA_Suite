import unittest
from src.ArrayList import ArrayList


class TestArrayList(unittest.TestCase):

    def setUp(self):
        self.list = ArrayList()

    def test_function(self):
        self.list.append(5)
        self.list.append(7)
        self.list.append(9)

        self.assertTrue(self.list.get(2), 9)
        self.assertTrue(self.list.remove_at(1), 7)
        self.assertTrue(self.list.length, 2)

        self.list.append(11)
        self.assertTrue(self.list.remove_at(1), 9)
        self.assertTrue(self.list.remove(9), None)
        self.assertTrue(self.list.remove_at(0), 5)
        self.assertTrue(self.list.remove_at(0), 11)
        self.assertTrue(self.list.length, 0)

        self.list.prepend(5)
        self.list.prepend(7)
        self.list.prepend(9)

        self.assertTrue(self.list.get(2), 5)
        self.assertTrue(self.list.get(0), 9)
        self.assertTrue(self.list.remove(9), 9)
        self.assertTrue(self.list.length, 2)
        self.assertTrue(self.list.get(0), 7)


if __name__ == '__main__':
    unittest.main()