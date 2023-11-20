from typing import TypeVar

T = TypeVar('T')


class Queue:

    def __init__(self):
        self.length = 0

    def enqueue(self, item: T):
        pass

    def deque(self) -> T | None:
        pass

    def peek(self) -> T | None:
        pass
