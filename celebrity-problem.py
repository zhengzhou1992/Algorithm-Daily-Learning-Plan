def naive_celeb(G):
    n = len(G)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if G[i][j] or not G[j][i]:
                break
        else:
            return i
    return None


def celeb(G):
    i, j = 0, 1
    n = len(G)
    for c in range(2, n + 1):
        if G[i][j]:
            i = c
        else:
            j = c
    if i == n:
        c = j
    else:
        c = i
    for i in range(n):
        if i == c:
            continue
        if G[c][i] or not G[i][c]:
            break
    else:
        return c
    return None


if __name__ == '__main__':
    from random import randrange

    n = 100
    G = [[randrange(2) for i in range(n)] for j in range(n)]
    c = randrange(n)
    for i in range(n):
        G[i][c] = True
        G[c][i] = False

    assert c == naive_celeb(G)
    assert c == celeb(G)
