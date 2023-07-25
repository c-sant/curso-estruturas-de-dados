from typing import Any, Iterable

from implementations.node import Node


class Queue:
    """A simple queue implementation in Python using nodes.

    This class represents a queue data structure, which follows the First In,
    First Out (FIFO) principle. Elements are added to the back of the queue and
    removed from the front.
    """

    def __init__(self, items: Iterable = None):
        self._front_node = None
        self._rear_node = None
        self._size = 0

    @property
    def size(self) -> int:
        """Number of elements of the queue."""

        return self._size

    @property
    def front(self) -> Any:
        """The front element of the queue."""

        return self._front_node.data

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        items = []

        current_node = self._front_node

        while current_node != None:
            items.append(str(current_node.data))
            current_node = current_node.next_node

        return f"[{', '.join(items)}]"

    def is_empty(self) -> bool:
        """Return True if queue has no elements; otherwise, return False."""

        return self.size == 0

    def enqueue(self, item):
        """Add an element to the back of the queue."""

        new_node = Node(item)

        if self._rear_node != None:
            self._rear_node.next_node = new_node
        else:
            self._front_node = new_node

        self._rear_node = new_node
        self._size += 1

    def dequeue(self) -> Any:
        """Remove and return the element from the front of the queue."""

        if self.is_empty():
            raise IndexError("dequeue from empty queue")

        front_node_data = self._front_node.data
        self._front_node = self._front_node.next_node

        if not self._front_node.next_node != None:
            self._rear_node = None

        self._size -= 1

        return front_node_data

    def _get_items_from_iterable(self, iterable: Iterable):
        """Incorporate items from iterable into the queue."""

        for item in iterable:
            self.enqueue(item)
