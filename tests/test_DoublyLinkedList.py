import unittest
from src.DoublyLinkedList import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        self.llist = DoublyLinkedList()

    def test_function(self):
        self.llist.append(5)
        self.llist.append(7)
        self.llist.append(9)

        self.assertEqual(self.llist.get(2), 9)
        self.assertEqual(self.llist.remove_at(1), 7)
        self.assertEqual(self.llist.length, 2)

        self.llist.append(11)
        self.assertEqual(self.llist.remove_at(1), 9)
        self.assertIsNone(self.llist.remove(9))
        self.assertEqual(self.llist.remove_at(0), 5)
        self.assertEqual(self.llist.remove_at(0), 11)
        self.assertEqual(self.llist.length, 0)

        self.llist.prepend(5)
        self.llist.prepend(7)
        self.llist.prepend(9)

        self.assertEqual(self.llist.get(2), 5)
        self.assertEqual(self.llist.get(0), 9)
        self.assertEqual(self.llist.remove(9), 9)
        self.assertEqual(self.llist.length, 2)
        self.assertEqual(self.llist.get(0), 7)


if __name__ == '__main__':
    unittest.main()
