import unittest
from src.Queue import Queue


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_function(self):

        self.queue.enqueue(5)
        self.queue.enqueue(7)
        self.queue.enqueue(9)

        self.assertEqual(self.queue.deque(), 5)
        self.assertEqual(self.queue.length, 2)

        self.queue.enqueue(11)
        self.assertEqual(self.queue.deque(), 7)
        self.assertEqual(self.queue.deque(), 9)
        self.assertEqual(self.queue.peek(), 11)
        self.assertEqual(self.queue.deque(), 11)
        self.assertIsNone(self.queue.deque())
        self.assertEqual(self.queue.length, 0)

        self.queue.enqueue(69)
        self.assertEqual(self.queue.peek(), 69)
        self.assertEqual(self.queue.length, 1)


if __name__ == '__main__':
    unittest.main()