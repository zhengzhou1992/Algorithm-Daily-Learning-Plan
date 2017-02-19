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


def partition(seq):
    pi, seq = seq[0], seq[1:]
    lo = [x for x in seq if x < pi]
    high = [x for x in seq if x > pi]
    return lo, pi, high


def select(seq, k):
    lo, pi, high = partition(seq)
    m = len(lo)
    if m == k:
        return pi
    elif m > k:
        return select(lo, k)
    else:
        return select(high, k - m - 1)


def quick_sort(seq):
    if len(seq) <= 1:
        return seq
    lo, pi, high = partition(seq)
    return quick_sort(lo) + [pi] + quick_sort(seq)


def merge_sort(seq):
    mid = len(seq) / 2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1:
        lft = merge_sort(lft)
    if len(rgt):
        rgt = merge_sort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] > rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res


if __name__ == '__main__':
    import doctest
    doctest.testmod()
