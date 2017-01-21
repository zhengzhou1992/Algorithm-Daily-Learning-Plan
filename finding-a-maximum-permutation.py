from collections import Counter


def naive_max_perm(M, A=None):
    if not A:
        A = set(range(len(M)))
    if len(A) == 1:
        return A
    B = set(M[i] for i in A)
    C = A - B
    if C:
        A.remove(C.pop())
        return naive_max_perm(M, A)
    return A


def max_perm(M):
    A = set(range(len(M)))
    c = Counter(dict(zip(range(len(M)), [0] * len(M))))
    for x in M:
        c[x] += 1
    q = [x for x in c if c[x] == 0]
    while q:
        i = q.pop()
        A.remove(i)
        j = M[i]
        c[j] -= 1
        if c[j] == 0:
            q.append(j)
    return A


def main():
    M = [2, 2, 0, 5, 3, 5, 7, 4]
    should_ret = {0, 2, 5}
    assert should_ret == naive_max_perm(M)
    assert should_ret == max_perm(M)


if __name__ == '__main__':
    main()
