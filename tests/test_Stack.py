import unittest
from src.Stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_function(self):
        self.stack.push(5)
        self.stack.push(7)
        self.stack.push(9)

        self.assertEqual(self.stack.pop(), 9)
        self.assertEqual(self.stack.length, 2)

        self.stack.push(11)
        self.assertEqual(self.stack.pop(), 11)
        self.assertEqual(self.stack.pop(), 7)
        self.assertEqual(self.stack.peek(), 5)
        self.assertEqual(self.stack.pop(), 5)
        self.assertIsNone(self.stack.pop())

        self.stack.push(69)
        self.assertEqual(self.stack.peek(), 69)
        self.assertEqual(self.stack.length, 1)


if __name__ == '__main__':
    unittest.main()