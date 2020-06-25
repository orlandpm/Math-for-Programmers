from collections import namedtuple

empty_tree = None
BinaryTree = namedtuple('BinaryTree', ['value','left','right'])

def insert(tree,value):
    if tree is empty_tree:
        return BinaryTree(value, empty_tree, empty_tree)
    elif value > tree.value:
        return BinaryTree(tree.value, tree.left, insert(tree.right, value))
    elif value < tree.value:
        return BinaryTree(tree.value, insert(tree.left,value), tree.right)
    else:
        return tree

def traverse(tree):
    if tree is not empty_tree:
        for value in traverse(tree.left): yield value
        yield tree.value
        for value in traverse(tree.right): yield value

def copy(tree):
    if tree is not empty_tree:
        return BinaryTree(tree.value, copy(tree.left), copy(tree.right))
    else:
        return empty_tree

def map(f, tree):
    if tree is not empty_tree:
        return BinaryTree(f(tree.value), map(f,tree.left), map(f,tree.right))
    else:
        return empty_tree


def contains(tree, value):
    if tree is empty_tree:
        return False
    elif tree.value == value:
        return True
    else:
        return contains(tree.left, value) or contains(tree.right, value)

def contains(tree, value):
    if tree is empty_tree:
        return False
    elif tree.value == value:
        return True
    elif tree.value > value:
        return contains(tree.left, value)
    else:
        return contains(tree.right, value)

t = BinaryTree(8,
    BinaryTree(4,
        BinaryTree(2,
            BinaryTree(1,empty_tree,empty_tree),
            BinaryTree(3,empty_tree,empty_tree)),
        BinaryTree(6,
            BinaryTree(5,empty_tree,empty_tree),
            BinaryTree(7,empty_tree,empty_tree))),
    BinaryTree(12,
        BinaryTree(10,
            BinaryTree(9,empty_tree,empty_tree),
            BinaryTree(11,empty_tree,empty_tree)),
        BinaryTree(14,
            BinaryTree(13,empty_tree,empty_tree),
            BinaryTree(15,empty_tree,empty_tree))))

print(list(traverse(insert(insert(insert(empty_tree, 3), 2), 5))))
