class Node:
    left = None
    right = None

    def __init__(self, key, val):
        self.key = key
        self.val = val


def insert(node, key, val):
    if node is None:
        return Node(key, val)
    if node.key == key:
        node.val = val
    elif node.key < key:
        node.left = insert(node.left, key, val)
    else:
        node.right = insert(node.right, key, val)
    return node


def search(node, key):
    if node is None:
        raise KeyError
    if node.key == key:
        return node.val
    elif node.key < key:
        return search(node.left, key)
    else:
        return search(node.right, key)


class BSTree:
    '''
    >>> tree = BSTree()

    >>> tree['a'] = 10

    >>> tree['b'] = 20

    >>> tree['b']
    20

    >>> 'b' in tree
    True

    >>> 'c' in tree
    False
    '''
    root = None

    def __setitem__(self, key, val):
        self.root = insert(self.root, key, val)

    def __getitem__(self, key):
        return search(self.root, key)

    def __contains__(self, key):
        try:
            search(self.root, key)
        except KeyError:
            return False
        return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
