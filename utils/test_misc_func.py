from copy import copy
from functools import reduce

from colorama import Back, Style

from .array import random_array
from .const import LINE_SEPARATOR


def test_sort(sort_func, test_arr_length=10, **kwargs):
    if not test_sort.test_array or \
            test_sort.test_arr_length != test_arr_length:
        test_sort.test_arr_length = test_arr_length
        test_sort.test_array = random_array(test_arr_length)
    test_arr = copy(test_sort.test_array)
    print(LINE_SEPARATOR)
    print('func:', sort_func.__name__, '\narg:\n', test_arr)
    increase = kwargs.get('increase', None)
    if increase:
        sort_func(test_arr, increase=increase)
    else:
        sort_func(test_arr)
    print('result\n', test_arr)

    increase = True if increase is None else increase

    successful = True
    for i in range(len(test_arr) - 1):
        if increase:
            if test_arr[i] > test_arr[i + 1]:
                successful = False
                break
        else:
            if test_arr[i] < test_arr[i + 1]:
                successful = False
                break
    if successful:
        print(Back.GREEN, 'PASSED')
    else:
        print(Back.RED, 'FAILED')
    print(Style.RESET_ALL)


test_sort.test_array = None
