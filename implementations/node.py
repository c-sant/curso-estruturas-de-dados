from typing import Self


class Node:
    """A container that contains data and a pointer to another node.

    As a container with a pointer to another container, the Node can be used to
    create a link between two elements, constituting a data structure.
    """

    def __init__(self, data, next_node: Self = None):
        self.data = data
        self.next_node = next_node
