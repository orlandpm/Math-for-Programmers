


class BinaryTree():
    def __init__(self,value=None,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
    def insert(self, value):
        if self.value is None:
            return BinaryTree(value, BinaryTree(), BinaryTree())
        elif value > self.value:
            return BinaryTree(self.value, self.left, self.right.insert(value))
        elif value < self.value:
            return BinaryTree(self.value, self.left.insert(value), self.right)
        else:
            return self
    def traverse(self):
        if self.left:
            for val in self.left.traverse():
                yield val
        if self.value:
            yield self.value
        if self.right:
            for val in self.right.traverse():
                yield val
