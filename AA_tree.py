class Node:
    lft = None
    rgt = None
    lvl = 1
    def __init__(self, key, val):
        self.key = key
        self.val = val


def skew(node):
    if None in [node, node.left]:
        return node
    if node.lft.lvl != node.lvl:
        return node
    lft = node.left
    node.lft = lft.rgt
    lft.rgt = node
    return lft


def split(node):
    if None in [node, node.rgt, node.rgt.rgt]:
        return node
    if node.rgt.rgt.lvl != node.lvl:
        return node
    rgt = node.rgt
    node.rgt = rgt.lft
    rgt.lft = node
    rgt.lvl += 1


def insert(node, key, val):
    if node is None:
        return Node(key, val)
    if node.key == key:
        node.val = val
        return node
    elif key < node.key:
        node.lft = insert(node.lft, key, val)
    else:
        node.rgt = insert(node.rgt, key, val)
    skew(node)
    split(node)
    return node
