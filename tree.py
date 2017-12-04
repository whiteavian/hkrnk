class BinaryTree:
    def __init__(self, data, left=None, right=None):
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
        """Traverse tree yielding depth."""
        if self.data is not None:
            yield depth
        if self.left and self.left.data is not None:
            for n in self.left.traverse_depth(depth + 1):
                yield n
        if self.right and self.right.data is not None:
            for n in self.right.traverse_depth(depth + 1):
                yield n

    def traverse_width_height(self, width, height):
        """Traverse tree yielding the node, and each width."""
        if self.left and self.left.data is not None:
            for p in self.left.traverse_width_height(width - 1, height + 1):
                yield p
        if self.data is not None and abs(width) == height:
            yield self.data
        if self.right and self.right.data is not None:
            for p in self.right.traverse_width_height(width + 1, height + 1):
                yield p

    def top_view(self):
        """Return the nodes in order from left to right if viewed from above."""
        node_widths = [nw for nw in self.traverse_width_height(0, 0)]
        print " ".join(map(str, node_widths))

    def breadth_first_traverse(self):
        """Traverse the tree breadth first."""
        if self.data is not None:
            yield self.data

        children = self.children()

        while children != []:
            next_children = []

            for child in children:
                next_children.extend(child.children())
                yield child.data

            children = next_children

    def children(self):
        """Return a list of both children."""
        children = []

        if self.left:
            children.append(self.left)
        if self.right:
            children.append(self.right)

        return children

    def insert(self, val):
        """Insert a value in the appropriate location in the tree."""
        if self.data and val >= self.data:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BinaryTree(data=val)
        else:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BinaryTree(data=val)

        return self

    def decode_huff(self, s):
        out = ""
        while len(s) > 0:
            letter, s = self.huff_helper(s)
            out += letter

        print out

    def huff_helper(self, s):
        if not self.left and not self.right:
            return self.data, s
        if s[0] == '0':
            next_node = self.left
        elif s[0] == '1':
            next_node = self.right

        return next_node.huff_helper(s[1:])

    def lca(self, v1, v2):
        """Return the least common ancestor of two numbers."""
        if self.right and v1 > self.data and v2 > self.data:
            return self.right.lca(v1, v2)
        elif self.left and v1 < self.data and v2 < self.data:
            return self.left.lca(v1, v2)
        else:
            return self


class AVLTree(BinaryTree):
    """An AVLTree is a self balancing binary search tree."""

    def insert(self, val):
        super(AVLTree, self).insert(val)

