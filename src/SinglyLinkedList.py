from typing import TypeVar

T = TypeVar('T')


class SinglyLinkedList:

    def __init__(self):
        self.length = 0

    def prepend(self, item: T):
        pass

    def insert_at(self, item: T, idx: int):
        pass

    def append(self, item: T):
        pass

    def remove(self, item: T) -> T | None:
        pass

    def get(self, idx: int) -> T | None:
        pass

    def remove_at(self, idx: int) -> T | None:
        pass
