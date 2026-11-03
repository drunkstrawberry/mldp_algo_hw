class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    def __init__(self):
        self.root = None

    def _height(self, node):
        return 0 if node is None else node.height

    def _update(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance(self, node):
        return self._height(node.left) - self._height(node.right)

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self._update(node)
        self._update(new_root)
        return new_root

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self._update(node)
        self._update(new_root)
        return new_root

    def _rebalance(self, node):
        self._update(node)
        balance = self._balance(node)
        if balance > 1:
            if self._balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1:
            if self._balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if node is None:
            return Node(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        else:
            return node
        return self._rebalance(node)

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if node is None:
            return None
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            next_node = node.right
            while next_node.left is not None:
                next_node = next_node.left
            node.val = next_node.val
            node.right = self._delete(node.right, next_node.val)
        return self._rebalance(node)

    def search(self, val):
        def find(node):
            if node is None:
                return False
            if val == node.val:
                return True
            if val < node.val:
                return find(node.left)
            return find(node.right)

        return find(self.root)
