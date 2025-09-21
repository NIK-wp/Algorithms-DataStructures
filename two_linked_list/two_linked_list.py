from two_linked_list.Node import Node
from typing import Any


class TwoLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def append_left(self, value: Any) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def pop(self, index: int = -1) -> Any:
        if self.head is None:
            raise IndexError('pop from empty list')

        if self.head is self.tail:
            pop_value = self.head.value
            self.head = self.tail = None
            return pop_value
        elif index == -1:
            current_node = self.tail
            self.tail.prev.next = None
            self.tail = self.tail.prev
            return current_node.value
        else:
            i = 0
            current_node = self.head
            while current_node is not None and i != index:
                current_node = current_node.next
                i += 1

            if current_node is None:
                raise IndexError('list index out of range')
            elif i == 0:
                pop_value = self.head.value
                self.head.next.prev = None
                self.head = self.head.next
            elif current_node is self.tail:
                pop_value = self.tail.value
                self.tail.prev.next = None
                self.tail = self.tail.prev
            else:
                pop_value = current_node.value
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
        return pop_value

    def remove(self, item: Any) -> None:
        if self.head is None:
            raise ValueError('two_linked_list.remove(x): x not in two_linked_list')
        if self.head.value == item:
            self.pop(0)
            return
        current_node = self.head
        while current_node.next and current_node.next.value != item:
            current_node = current_node.next
        if not current_node.next:
            raise ValueError('two_linked_list.remove(x): x not in two_linked_list')
        if current_node.next is self.tail:
            self.pop()
            return
        current_node.next = current_node.next.next

    def index(self, item: Any) -> int:
        if self.head is None:
            raise ValueError('two_linked_list.index(x): x not in two_linked_list')
        current_node = self.head
        counter = 0
        if current_node.value == item:
            return counter
        while current_node.next and current_node.value != item:
            current_node = current_node.next
            counter += 1
        if current_node.value == item:
            return counter
        else:
            raise ValueError('two_linked_list.index(x): x not in two_linked_list')

    def clear(self) -> None:  # todo relisation frew del
        self.head = None
        self.tail = None

    def __copy__(self) -> 'TwoLinkedList':
        copy_object = TwoLinkedList()
        for i in self:
            copy_object.append(i)
        return copy_object

    def __eq__(self, other: 'TwoLinkedList') -> bool:
        current_node = self.head
        current_node_other = other.head
        while current_node is not None and current_node_other is not None:
            if current_node != current_node_other:
                return False
            current_node = current_node.next
            current_node_other = current_node_other.next
        if current_node is not None or current_node_other is not None:
            return False
        else:
            return True

    def __len__(self) -> int:
        i = 0
        current_node = self.head
        while current_node is not None:
            i += 1
            current_node = current_node.next
        return i

    def __iter__(self) -> Any:
        current_node = self.head
        while current_node is not None:
            yield current_node.value
            current_node = current_node.next
