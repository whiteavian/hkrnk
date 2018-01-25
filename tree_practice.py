from collections import deque


class Tree:
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def bft(self):
        order = []

        to_visit = deque()
        to_visit.append(self)

        while len(to_visit) > 0:
            next_node = to_visit.popleft()
            order.append(next_node)

            for c in next_node.children:
                to_visit.append(c)

        return order
