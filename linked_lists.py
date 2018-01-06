class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


def partition(n, pivot):
    pll = PartitionedLinkedList(pivot)

    while n.next_node is not None:
        pll.add(n)
        n = n.next_node

    pll.add(n)
    pll.join()

    return pll.before_first


class PartitionedLinkedList:
    def __init__(self, pivot, before_first=None, after_first=None):
        self.pivot = pivot
        self.before_first = before_first
        self.before_last = before_first
        self.after_first = after_first
        self.after_last = after_first

    def add_n(self, n):
        if n.value < self.pivot:
            self.add(n, self.before_first, self.before_last)
        else:
            self.add(n, self.after_first, self.after_last)

    def add(self, n, first, last):
        if first is None:
            first = n
            last = n
            first.next_node = last
        else:
            last.next_node = n

    def join(self):
        self.before_last.next_node = self.after_first
