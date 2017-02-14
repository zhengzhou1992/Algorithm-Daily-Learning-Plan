def walk(G, s, S=set()):
    P, Q = dict(), set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P, S):
            P[v] = u
            Q.add(v)
    return P


def components(G):
    comp = []
    seen = set()
    for u in G:
        if u in seen:
            continue
        walked = walk(G, u)
        seen.update(walked)
        comp.append(walked)
    return comp


if __name__ == '__main__':
    G = {
        'a': set(['b', 'c', 'd']),
        'b': set(['a', 'd']),
        'c': set(['a', 'd']),
        'd': set(['a', 'b', 'c']),
        'e': set(['f', 'g']),
        'f': set(['e', 'g']),
        'g': set(['e', 'f']),
        'h': set(['i']),
        'i': set(['h'])
    }

    assert [{'e': 'f', 'f': None, 'g': 'f'},
            {'i': 'h', 'h': None},
            {'b': None, 'c': 'a', 'a': 'b', 'd': 'b'}] == components(G)
