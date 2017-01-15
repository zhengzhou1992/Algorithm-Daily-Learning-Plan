from random import randint


def random_array(length):
    return [randint(0, 1000) for _ in range(length)]
