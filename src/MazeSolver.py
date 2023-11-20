from dataclasses import dataclass, astuple
from typing import List


'''
This 'Point' class is used as a structure to model a single point with an x and y coordinate.
e.g.
To create a new point: p = Point(1, 2)
To access a value within a point: p.x / p.y
'''
@dataclass
class Point:
    x: int
    y: int


def maze_solver(maze: List[str], wall: str, start: Point, end: Point) -> List[Point]:
    pass
