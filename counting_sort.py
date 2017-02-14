from collections import defaultdict

from utils.test_misc_func import test_sort


def counting_sort(A, key=lambda x: x):
    B, C = [], defaultdict(list)

    for x in A:
        C[key(x)].append(x)
    for x in range(min(C), max(C) + 1):
        B.extend(C[x])

    return B


def main():
    test_sort(counting_sort)


if __name__ == '__main__':
    main()
