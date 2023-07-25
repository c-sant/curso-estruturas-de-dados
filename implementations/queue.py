from typing import Any, Iterable

from implementations.node import Node


class Queue:
    """Uma simples implementação da fila (queue) em Python usando nós.

    Essa classe representa a estrutura de dados fila, a qual segue o princípio
    First-In-First-Out (FIFO). Elementos novos são adicionados ao fim da fila, e
    apenas o elemento da frente pode ser removido.
    """

    def __init__(self, items: Iterable = None):
        self._front_node = None
        self._rear_node = None
        self._size = 0

        if items != None:
            self._get_items_from_iterable(items)

    @property
    def size(self) -> int:
        """Número de elementos da fila."""

        return self._size

    @property
    def front(self) -> Any:
        """O primeiro elemento da fila."""

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
        """Retorna True se a fila não tiver elementos; caso contrário, retorna False."""

        return self.size == 0

    def enqueue(self, item):
        """Adiciona um elemento ao fim da fila."""

        new_node = Node(item)

        if self._rear_node != None:
            self._rear_node.next_node = new_node
        else:
            self._front_node = new_node

        self._rear_node = new_node
        self._size += 1

    def dequeue(self) -> Any:
        """Remove e retorna o elemento à frente da fila."""

        if self.is_empty():
            raise IndexError("dequeue from empty queue")

        front_node_data = self._front_node.data
        self._front_node = self._front_node.next_node

        if not self._front_node.next_node != None:
            self._rear_node = None

        self._size -= 1

        return front_node_data

    def _get_items_from_iterable(self, iterable: Iterable):
        """Incorpora itens de um iterável à fila."""

        for item in iterable:
            self.enqueue(item)
