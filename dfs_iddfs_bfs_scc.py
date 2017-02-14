from collections import deque
from topological_sort import dfs_topsort
from finding_connected_components import walk


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
        Q.extend(G[u])
        S.add(u)
        yield u


def graph_traverse(G, s, qtype=set):
    S, Q = set(), qtype()
    Q.add(s)
    while Q:
        u = Q.pop()
        if u in S:
            continue
        for v in G[u]:
            Q.add(v)
        S.add(u)
        yield u


def timing_dfs(G, s, d, f, S=None, t=0):
    if S is None:
        S = set()
    d[s] = t
    t += 1
    S.add(s)
    for v in G[s]:
        if v in S:
            continue
        t = timing_dfs(G, v, d, f, S, t)
    f[s] = t
    t += 1
    return t


def iddfs(G, s):
    yielded = set()

    def recurse(G, s, d, S=None):
        if s not in yielded:
            yield s
            yielded.add(s)
        if d == 0:
            return
        if S is None:
            S = set()
        S.add(s)
        for x in G[s]:
            if x in S:
                continue
            for u in recurse(G, x, d - 1, S):
                yield u

    n = len(G)
    for d in range(n):
        if len(yielded) == n:
            break
        for x in recurse(G, s, d):
            yield x


def bfs(G, s):
    P, Q = {s: None}, deque([s])
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v in P:
                continue
            P[v] = u
            Q.append(v)
    return P


def transpose(G):
    GT = dict()
    for u in G:
        GT[u] = set()
    for u in G:
        for v in G[u]:
            GT[v].add(u)
    return GT


def strongly_connected_components(G):
    GT = transpose(G)
    scc, seen = [], set()

    for u in GT:
        if u in seen:
            continue
        see = walk(GT, u, seen)
        seen.update(see)
        scc.append(see)

    return scc


if __name__ == '__main__':
    G = {
        'a': set(['b', 'c', 'd']),
        'b': set(['a', 'd']),
        'c': set(['a', 'd']),
        'd': set(['a', 'b', 'c'])
    }

    print(list(iter_dfs(G, 'a')))
    print(list(graph_traverse(G, 'a')))

    start_time = dict()
    finish_time = dict()
    timing_dfs(G, 'a', start_time, finish_time)
    print(start_time, finish_time)

    print(list(iddfs(G, 'a')))

    P = bfs(G, 'a')
    a = 'c'
    path = [a]
    while P[a] is not None:
        path.append(P[a])
        a = P[a]
    print(path)

    # TODO: test scc
