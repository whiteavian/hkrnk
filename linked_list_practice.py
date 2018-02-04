class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def reverse(self):
        prev = self
        current = self.next_node
        prev.next_node = None

        while current is not None:
            next_node = current.next_node
            current.next_node = prev
            prev = current
            current = next_node

        return prev

    def traverse(self):
        nodes = []
        pointer = self

        while pointer is not None:
            nodes.append(pointer)
            pointer = pointer.next_node

        return nodes

n4 = Node(4)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

backw = [n.value for n in n1.reverse().traverse()]