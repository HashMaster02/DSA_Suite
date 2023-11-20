import unittest
from src.MazeSolver import solve_maze, Point


class TestMazeSolver(unittest.TestCase):

    def setUp(self):
        self.maze = [
            "xxxxxxxxxx x",
            "x        x x",
            "x        x x",
            "x xxxxxxxx x",
            "x          x",
            "x xxxxxxxxxx",
        ]

        self.maze_result = [
            Point(x=10, y=0),
            Point(x=10, y=1),
            Point(x=10, y=2),
            Point(x=10, y=3),
            Point(x=10, y=4),
            Point(x=9, y=4),
            Point(x=8, y=4),
            Point(x=7, y=4),
            Point(x=6, y=4),
            Point(x=5, y=4),
            Point(x=4, y=4),
            Point(x=3, y=4),
            Point(x=2, y=4),
            Point(x=1, y=4),
            Point(x=1, y=5),
        ]

    def test_function(self):
        result = solve_maze(self.maze, "x", Point(x=10, y=0), Point(x=1, y=5))
        self.assertEqual(result, self.maze_result)


if __name__ == '__main__':
    unittest.main()
