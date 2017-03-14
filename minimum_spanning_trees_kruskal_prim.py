from heapq import heappop, heappush


def naive_find(C, u):
    while C[u] != u:
        u = C[u]
    return u


def naive_union(C, u, v):
    u = naive_find(C, u)
    v = naive_find(C, v)
    C[u] = v


def naive_kruskal(G):
    E = [(G[u][v], u, v) for u in G for v in G[u]]
    T = set()
    C = {u: u for u in G}

    for _, u, v in sorted(E):
        if naive_find(C, u) != naive_find(C, v):
            T.add((u, v))
            naive_union(C, u, v)
    return T


def prim(G, s):
    P, Q = {}, [(0, None, s)]
    while Q:
        _, p, u = heappop(Q)
        if u in P:
            continue
        P[u] = p
        for v, w in G[u].items():
            heappush(Q, (w, u, v))
    return P
