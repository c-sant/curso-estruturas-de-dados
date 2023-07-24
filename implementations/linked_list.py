from typing import Any, Iterable

from implementations.node import Node


class LinkedList:
    def __init__(self, iterable: Iterable = None):
        self._head = None
        self._size = 0

        if iterable != None:
            self._get_iterable_elements(iterable)

    def __len__(self) -> int:
        return self.size

    def __iter__(self) -> Any:
        current_node = self._head

        while current_node:
            yield current_node.data
            current_node = current_node.next_node

    def __str__(self) -> str:
        items = [str(item) for item in self]
        return f"[{', '.join(items)}]"

    def __getitem__(self, index: int):
        if index < 0:
            index = self.size + index

        current_node = self._head
        current_index = 0

        while current_node != None and current_index < index:
            current_node = current_node.next_node
            current_index += 1

        if current_index < index:
            raise IndexError("Index out of range")

        return current_node.data

    @property
    def size(self) -> int:
        return self._size

    def append(self, item):
        """Append object to the end of the list."""
        new_node = Node(item)

        if self._head == None:
            self._head = new_node
        else:
            current_node = self._head
            while current_node.next_node != None:
                current_node = current_node.next_node

            current_node.next_node = new_node

        self._size += 1

    def remove(self, item):
        """Remove first occurrence of value.

        Raises ValueError if the value is not present.
        """

        current_node = self._head
        previous_node = None

        while current_node != None:
            if current_node.data == item:
                if previous_node == None:
                    self._head = current_node.next_node
                else:
                    previous_node.next_node = current_node.next_node

                self._size -= 1

                break

            previous_node = current_node
            current_node = current_node.next_node

        raise ValueError(f"'{item}' not in list")

    def _get_iterable_elements(self, iterable: Iterable):
        for item in iterable:
            self.append(item)
