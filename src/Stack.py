from typing import TypeVar

T = TypeVar('T')


class Stack:

    def __init__(self):
        self.length = 0

    def push(self, item: T):
        pass

    def pop(self) -> T | None:
        pass

    def peek(self) -> T | None:
        pass
