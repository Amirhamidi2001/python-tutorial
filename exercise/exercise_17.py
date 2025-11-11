class TreeNode:
    """Node of a binary search tree."""

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)


class BinarySearchTree:
    """Binary Search Tree implementation."""

    def __init__(self):
        self.root = None

    def _insert(self, node, key):
        """Helper method to insert a key starting from given node."""
        if node is None:
            return TreeNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        return node

    def insert(self, key):
        """Insert a key into the BST."""
        self.root = self._insert(self.root, key)

    def _search(self, node, key):
        """Helper method to search for a key starting from given node."""
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def search(self, key):
        """Search for a key in the BST."""
        return self._search(self.root, key)

    def _delete(self, node, key):
        """Helper method to delete a key starting from given node."""
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Node with two children: get the inorder successor
            node.key = self._min_value(node.right)
            node.right = self._delete(node.right, node.key)

        return node

    def delete(self, key):
        """Delete a key from the BST."""
        self.root = self._delete(self.root, key)

    def _min_value(self, node):
        """Find the minimum key starting from given node."""
        current = node
        while current.left is not None:
            current = current.left
        return current.key

    def _inorder_traversal(self, node, result):
        """Helper method for inorder traversal."""
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

    def inorder_traversal(self):
        """Return a list of keys in inorder."""
        result = []
        self._inorder_traversal(self.root, result)
        return result


if __name__ == "__main__":
    bst = BinarySearchTree()
    nodes = [50, 30, 20, 90, 40, 70, 60, 80, 10]

    for node in nodes:
        bst.insert(node)

    print("Inorder traversal:", bst.inorder_traversal())
