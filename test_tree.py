from tree import BinaryTree


def test_check_bst():
    bst = BinaryTree(
        4,
        left=BinaryTree(2, left=BinaryTree(1), right=BinaryTree(3)),
        right=BinaryTree(6, left=BinaryTree(5), right=BinaryTree(7)),
        )

    assert bst.check_bst()

    non_bst = BinaryTree(
        4,
        left=BinaryTree(2, left=BinaryTree(3), right=BinaryTree(3)),
        right=BinaryTree(6, left=BinaryTree(5), right=BinaryTree(7)),
    )

    assert not non_bst.check_bst()

    non_bst2 = BinaryTree(
        4,
        left=BinaryTree(2, left=BinaryTree(2), right=BinaryTree(3)),
        right=BinaryTree(6, left=BinaryTree(5), right=BinaryTree(7)),
    )
    assert not non_bst2.check_bst()

    non_bst3 = BinaryTree(
        4,
        left=BinaryTree(2, left=BinaryTree(1), right=BinaryTree(4)),
        right=BinaryTree(6, left=BinaryTree(5), right=BinaryTree(7)),
    )
    assert not non_bst3.check_bst()

    non_bst4 = BinaryTree(
        40,
        left=BinaryTree(20, left=BinaryTree(10),
                        right=BinaryTree(30, left=BinaryTree(25), right=BinaryTree(45))),
        right=BinaryTree(60, left=BinaryTree(50), right=BinaryTree(70)),
    )
    assert not non_bst4.check_bst()

