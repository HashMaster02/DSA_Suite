from typing import TypeVar

T = TypeVar('T')

class RingBuffer:

    def __init__(self):
        self.length = 0

    def push(self, item: T):
        pass

    def pop(self) -> T:
        pass

    def get(self, index: int) -> T:
        pass