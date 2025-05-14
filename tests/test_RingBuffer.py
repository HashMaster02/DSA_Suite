import unittest
from src.RingBuffer import RingBuffer


class TestRingBuffer(unittest.TestCase):

    def setUp(self):
        self.buffer = RingBuffer()

    def test_function(self):
        self.buffer.push(5)
        self.assertEqual(self.buffer.pop(), 5)
        self.assertEqual(self.buffer.pop(), None)

        self.buffer.push(42)
        self.buffer.push(9)
        self.assertEqual(self.buffer.pop(), 42)
        self.assertEqual(self.buffer.pop(), 9)
        self.assertEqual(self.buffer.pop(), None)

        self.buffer.push(42)
        self.buffer.push(9)
        self.buffer.push(12)
        self.assertEqual(self.buffer.get(2), 12)
        self.assertEqual(self.buffer.get(1), 9)
        self.assertEqual(self.buffer.get(0), 42)


if __name__ == '__main__':
    unittest.main()