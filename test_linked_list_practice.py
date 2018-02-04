from linked_list_practice import Node


def test_reverse():
    n4 = Node(4)
    n3 = Node(3, n4)
    n2 = Node(2, n3)
    n1 = Node(1, n2)

    backw = [n.value for n in n1.reverse().traverse()]

    assert backw == [4, 3, 2, 1]