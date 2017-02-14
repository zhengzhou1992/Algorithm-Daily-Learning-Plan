def naive_topsort(G, S=None):
    if S is None:
        S = set(G)
    if len(S) == 1:
        return list(S)
    v = S.pop()
    seq = naive_topsort(G, S)
    min_i = 0
    for i, x in enumerate(seq):
        if v in G[x]:
            min_i = i + 1
    seq.insert(min_i, v)
    return seq


def topsort(G):
    c = dict((k, 0) for k in G)
    for k in G:
        for x in G[k]:
            c[x] += 1
    Q = [k for k in c if c[k] == 0]
    seq = []
    while Q:
        x = Q.pop()
        seq.append(x)
        for v in G[x]:
            c[v] -= 1
            if c[v] is 0:
                Q.append(v)
    return seq


def dfs_topsort(G):
    seen, res = set(), []

    def recurse(u):
        if u in seen:
            return
        seen.add(u)
        for v in G[u]:
            recurse(v)
        res.append(u)

    for u in G:
        recurse(u)
    res.reverse()
    return res


if __name__ == '__main__':
    G = {'a': ['b', 'f'],
         'e': ['f'],
         'c': ['d'],
         'b': ['c', 'd', 'f'],
         'd': ['e', 'f'],
         'f': []}

    should_be = ['a', 'b', 'c', 'd', 'e', 'f']
    assert should_be == naive_topsort(G)
    assert should_be == topsort(G)
    assert should_be == dfs_topsort(G)
