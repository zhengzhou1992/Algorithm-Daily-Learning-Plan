from utils.test_misc_func import test_sort


def ins_sort_rec(seq, i=None):
    if i is None:
        i = len(seq) - 1
    if i == 0:
        return
    ins_sort_rec(seq, i - 1)
    j = i
    while j > 0 and seq[j - 1] > seq[j]:
        seq[j - 1], seq[j] = seq[j], seq[j - 1]
        j -= 1


def ins_sort(seq):
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j - 1] > seq[j]:
            seq[j - 1], seq[j] = seq[j], seq[j - 1]
            j -= 1


def sel_sort_rec(seq, i=None):
    if i is None:
        i = len(seq)
    if i == 0:
        return

    for j in range(i - 1):
        if seq[j] > seq[j + 1]:
            seq[j], seq[j + 1] = seq[j + 1], seq[j]

    sel_sort_rec(seq, i - 1)


def sel_sort(seq):
    for i in range(len(seq), 0, -1):
        for j in range(i - 1):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]


def main():
    test_sort(ins_sort_rec)
    test_sort(ins_sort)
    test_sort(sel_sort_rec, test_arr_length=5)
    test_sort(sel_sort)


if __name__ == '__main__':
    main()
