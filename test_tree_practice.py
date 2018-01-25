from tree_practice import Tree


def test_tree():
    t4 = Tree(4, [])
    t6 = Tree(6, [])
    t7 = Tree(7, [])
    t8 = Tree(8, [])

    t5 = Tree(5, [t8])

    t2 = Tree(2, [t4, t5])
    t3 = Tree(3, [t6, t7])

    t1 = Tree(1, [t2, t3])

    bft_values = [t.value for t in t1.bft()]
    assert bft_values == range(1, 9)
