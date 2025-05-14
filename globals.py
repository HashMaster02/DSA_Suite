from __future__ import annotations
from typing import TypeVar
from dataclasses import dataclass

T = TypeVar('T')

@dataclass
class BinaryTreeNode:
    value: T
    left: BinaryTreeNode | None
    right: BinaryTreeNode | None
