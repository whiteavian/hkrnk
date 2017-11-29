class BinaryTree:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    @property
    def leaf(self):
        return not self.left and not self.right

    def traverse_preorder(self, height=False):
        """Traverse tree in root, left, right ordering."""
        if self.data is not None:
            yield self.data
            if height and self.leaf:
                yield "LEAF"

        if self.left and self.left.data is not None:
            for n in self.left.traverse_preorder():
                yield n
        if self.right and self.right.data is not None:
            for n in self.right.traverse_preorder():
                yield n

    def traverse_inorder(self):
        """Traverse tree in left, root, right ordering."""
        if self.left and self.left.data is not None:
            for n in self.left.traverse_inorder():
                yield n
        if self.data is not None:
            yield self.data
        if self.right and self.right.data is not None:
            for n in self.right.traverse_inorder():
                yield n

    def traverse_postorder(self):
        """Traverse tree in left, right, root ordering."""
        if self.left and self.left.data is not None:
            for n in self.left.traverse_postorder():
                yield n
        if self.right and self.right.data is not None:
            for n in self.right.traverse_postorder():
                yield n
        if self.data is not None:
            yield self.data

    def traverse_depth(self, depth):
        """Traverse tree in root, left, right ordering."""
        if self.data is not None:
            yield depth
        if self.left and self.left.data is not None:
            for n in self.left.traverse_depth(depth + 1):
                yield n
        if self.right and self.right.data is not None:
            for n in self.right.traverse_depth(depth + 1):
                yield n
