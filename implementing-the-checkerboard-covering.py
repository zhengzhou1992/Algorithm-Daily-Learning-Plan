def cover(board, lab=1, y_off=0, x_off=0, length=None):
    if not length:
        length = len(board[0])

    mid = length // 2

    offset = (0, -1), (length - 1, 0)

    for x_outer, x_inner in offset:
        for y_outer, y_inner in offset:
            if not board[y_off + y_outer][x_off + x_outer]:
                board[y_off + mid + y_inner][x_off + mid + x_inner] = lab

    lab += 1
    if mid < 2:
        return lab

    for x_plus in [0, mid]:
        for y_plus in [0, mid]:
            lab = cover(board, lab, y_off + y_plus, x_off + x_plus, mid)

    return lab


def cover_test():
    c = 16
    board = [[0] * c for j in range(c)]
    board[c - 1][c - 1] = -1
    cover(board)
    for row in board:
        print(' %2i' * c % tuple(row))


if __name__ == '__main__':
    cover_test()
