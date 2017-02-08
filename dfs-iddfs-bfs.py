def rec_dfs(G, s, S=None):
    if S is None:
        S = set()
    S.add(s)
    for v in G[s]:
        if v in S:
            continue
        rec_dfs(G, v, S)


def iter_dfs(G, s):
    S, Q = set(), list(s)
    while Q:
        u = Q.pop()
        if u in S:
            continue
        print(G[u])
        Q.extend(G[u])
        S.add(u)
        yield u


if __name__ == '__main__':
    G = {
        'a': set(['b', 'c', 'd']),
        'b': set(['a', 'd']),
        'c': set(['a', 'd']),
        'd': set(['a', 'b', 'c'])
    }

    print(list(iter_dfs(G, 'a')))
