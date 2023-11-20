import unittest
import random
from src.TwoCrystalBalls import two_crystal_balls


class TestTwoCrystalBalls(unittest.TestCase):

    def setUp(self):
        self.idx = random.randint(0, 10000)
        self.data = [False for _ in range(10000)]
        for i in range(self.idx, 10000):
            self.data[i] = True

    def test_function(self):
        self.assertEqual(two_crystal_balls(self.data), self.idx)
        self.assertEqual(two_crystal_balls([False for _ in range(821)]), -1)


if __name__ == '__main__':
    unittest.main()
