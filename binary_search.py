import re


def bin_find(arr, el, bds=None):
    if bds:
        arr = arr[bds[0]: bds[-1] + 1]

    ind = 0
    while True:
        mid_el = arr[(n := int(len(arr) / 2))]
        print(arr, mid_el)
        if el > mid_el:
            ind += n

            arr = arr[n:]
        elif el < mid_el:
            arr = arr[:n]
        else:
            print(f'Индекс {el} - {ind + n}')
            return ind + n


bin_find([0, 1, 2, 3, 4, 5, 6, 7], 5)