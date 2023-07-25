from typing import Any, Iterable

from implementations.node import Node


class Stack:
    """Uma implementação simples da pilha (stack) em Python utilizando nós.

    Essa classe representa a estrutura de dados pilha, a qual segue o princípio
    Last-In-First-Out (LIFO). Operações de adição e remoção só podem ser realizadas
    no topo da pilha.
    """

    def __init__(self, items: Iterable = None):
        self._top_node = None
        self._size = 0

        if items != None:
            self._get_items_from_iterable(items)

    @property
    def size(self) -> int:
        """Número de elementos da pilha."""

        return self._size

    @property
    def top(self) -> Any:
        """O elemento no topo da pilha."""

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
        """Retorna True se a pilha não tiver elementos; caso contrário, retorna False."""

        return self.size == 0

    def push(self, item):
        """Adiciona um elemento ao topo da pilha."""

        new_node = Node(item)

        new_node.next_node = self._top_node
        self._top_node = new_node

        self._size += 1

    def pop(self) -> Any:
        """Remove e retorna o elemento do topo da pilha."""

        if self.is_empty():
            raise IndexError("pop from empty stack")

        top_data = self._top_node.data
        self._top_node = self._top_node.next_node
        self._size -= 1

        return top_data

    def _get_items_from_iterable(self, iterable: Iterable):
        """Incorpora itens de um iterável à pilha."""

        for item in iterable:
            self.push(item)
