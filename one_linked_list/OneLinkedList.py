from typing import Any
from one_linked_list.Node import Node


class OneLinkedList:
    def __init__(self) -> None:
        self.head = self.tail = None
        self.size = 0

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if self.size:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node
        self.size += 1

    def pop(self) -> Any:
        if self.size == 0:
            raise IndexError('pop from empty list')
        self.size -= 1
        if self.head is self.tail:
            pop_value = self.head.value
            self.head = self.tail = None
            return pop_value
        current_node = self.head
        while current_node.next is not self.tail:
            current_node = current_node.next
        pop_value = current_node.next.value
        current_node.next = None
        self.tail = current_node
        return pop_value

    def pop_first(self):
        if self.size == 0:
            raise IndexError('pop from empty list')
        self.size -= 1
        if self.head is self.tail:
            pop_value = self.head.value
            self.head = self.tail = None
            return pop_value
        pop_value = self.head.value
        self.head = self.head.next
        return pop_value

    def remove(self, remove_value: Any) -> None:
        if self.size == 0:
            raise ValueError('one_linked_list.remove(x): x not in one_linked_list')
        if self.head.value == remove_value:
            self.pop_first()
            return
        current_node = self.head
        while current_node.next and current_node.next.value != remove_value:
            current_node = current_node.next
        if not current_node.next:
            raise ValueError('one_linked_list.remove(x): x not in one_linked_list')
        if current_node.next is self.tail:
            self.pop()
            return
        current_node.next = current_node.next.next
        self.size -= 1

    def is_empty(self) -> bool:
        return not bool(self.size)

    def __len__(self) -> int:
        return self.size

    def show_list(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.value, end=' ')
            current_node = current_node.next
        print()

    def append_left(self, value: Any) -> None:
        new_node = Node(value)
        if self.size == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def index(self, value):
        if self.size == 0:
            raise ValueError('one_linked_list.index(x): x not in one_linked_list')
        current_node = self.head
        counter = 0
        if current_node.value == value:
            return counter
        while current_node.next and current_node.value != value:
            current_node = current_node.next
            counter += 1
        if current_node.value == value:
            return counter
        else:
            raise ValueError('one_linked_list.index(x): x not in one_linked_list')

    def find(self, value):
        if self.size == 0:
            return -1
        current_node = self.head
        counter = 0
        if current_node.value == value:
            return counter
        while current_node.next and current_node.next.value != value:
            current_node = current_node.next
            counter += 1
        if current_node.value == value:
            return counter
        else:
            return -1

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.value
            current_node = current_node.next

    def __contains__(self, item) -> bool:
        for value in self:
            if value == item:
                return True
        return False
