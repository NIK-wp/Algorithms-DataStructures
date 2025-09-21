from typing import Any


class Node:
    def __init__(self, value: Any):
        self.value: Any = value
        self.next: Node | None = None
        self.prev: Node | None = None

    def __str__(self):
        return f'Node({self.value})'

    def __eq__(self, other):
        return self.value == other.value
