from itertools import count
from heapq import heapify, heappop, heappush


def huffman(seq, frq):
    '''
    >>> seq = "abcdefghi"
    >>> frq = [4, 5, 6, 9, 11, 12, 15, 16, 20]
    >>> huffman(seq, frq)
    [['i', [['a', 'b'], 'e']], [['f', 'g'], [['c', 'd'], 'h']]]
    '''
    num = count()
    trees = list(zip(frq, num, seq))
    heapify(trees)

    while len(trees) > 1:
        fa, _, a = heappop(trees)
        fb, _, b = heappop(trees)
        n = next(num)
        heappush(trees, (fa + fb, n, [a, b]))

    return trees[0][-1]


def codes(tree, prefix=''):
    '''
    >>> tree = [['i', [['a', 'b'], 'e']], [['f', 'g'], [['c', 'd'], 'h']]]
    >>> list(codes(tree))
    [('i', '00'), ('a', '0100'), ('b', '0101'), ('e', '011'), ('f', '100'), ('g', '101'), ('c', '1100'), ('d', '1101'), ('h', '111')]
    '''
    if len(tree) == 1:
        yield (tree, prefix)
        return
    for bit, child in zip('01', tree):
        for pair in codes(child, prefix + bit):
            yield pair


if __name__ == '__main__':
    import doctest
    doctest.testmod()
