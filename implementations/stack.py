from typing import Any, Iterable

from implementations.node import Node


class Stack:
    """A simple stack implementation in Python.

    This class represents a stack data structure, which follows the Last In,
    First Out (LIFO) principle. Elements are added and removed from the top of
    the stack.
    """

    def __init__(self, items: Iterable = None):
        self._top_node = None
        self._size = 0

        if items != None:
            self._get_items_from_iterable(items)

    @property
    def size(self) -> int:
        """Number of elements of the stack."""

        return self._size

    @property
    def top(self) -> Any:
        """The element at the top of the stack."""

        return self._top_node.data

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        items = []

        current_node = self._top_node

        while current_node != None:
            items.append(str(current_node.data))
            current_node = current_node.next_node

        return f"[{', '.join(items)}]"

    def is_empty(self) -> bool:
        """Return True if stack has no elements; otherwise, return False."""

        return self.size == 0

    def push(self, item):
        """Add an element to the top of the stack."""

        new_node = Node(item)

        new_node.next_node = self._top_node
        self._top_node = new_node

        self._size += 1

    def pop(self) -> Any:
        """Remove and return the element from the top of the stack."""

        if self.is_empty():
            raise IndexError("pop from empty stack")

        top_data = self._top_node.data
        self._top_node = self._top_node.next_node
        self._size -= 1

        return top_data

    def _get_items_from_iterable(self, iterable: Iterable):
        """Incorporate items from iterable into the stack."""

        for item in iterable:
            self.push(item)
