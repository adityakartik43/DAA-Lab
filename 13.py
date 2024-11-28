from sortedcontainers import SortedSet

class RedBlackTree:
    def __init__(self):
        self.tree = SortedSet()

    def insert(self, value):
        self.tree.add(value)

    def delete(self, value):
        self.tree.discard(value)

    def __str__(self):
        return str(list(self.tree))

rb_tree = RedBlackTree()
rb_tree.insert(10)
rb_tree.insert(20)
rb_tree.delete(16)
rb_tree.delete(112)
rb_tree.delete(122)
print("Red-Black Tree:", rb_tree)

