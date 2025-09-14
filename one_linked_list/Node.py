from typing import Any


class Node:
    def __init__(self, value: Any = None, next_node: 'Node' = None) -> None:
        self.value = value
        self.next = next_node
