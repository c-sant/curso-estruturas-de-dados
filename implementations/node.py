from typing import Self


class Node:
    """Um objeto que contém um dado e uma referêcia para outro nó (Node).

    Sendo um objeto que aponta para outro nó, ele pode ser usado para criar uma
    estrutura baseada na ligação entre diferentes elementos.
    """

    def __init__(self, data, next_node: Self = None):
        self.data = data
        self.next_node = next_node
