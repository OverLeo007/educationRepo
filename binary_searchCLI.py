import argparse


def bin_find(arr, el, bds=None):
    if bds:
        ind = bds[0]
        arr = arr[bds[0]: bds[-1] + 1]
    else:
        ind = 0
    while True:
        if len(arr) == 1 and arr[0] != el:
            return False
        mid_el = arr[(n := int(len(arr) / 2))]
        if el > mid_el:
            ind += n
            arr = arr[n:]
        elif el < mid_el:
            arr = arr[:n]
        else:
            return ind + n


parser = argparse.ArgumentParser(description='Бинарный поиск элемента в массиве')
parser.add_argument('-arr', '--array_to_search', dest='arr', nargs='*', default=[1, 2, 3, 4, 5], type=int,
                    help='Отсортированный по неубыванию массив')
parser.add_argument('-el', '--element_to_find', dest='elem', default=3, type=int,
                    help='Элемент, индекс которго требуется найти')
parser.add_argument('-bds', '--bounds_of_seach', dest='bds', nargs=2, default=None, type=int,
                    help='Границы поиска элемента в массиве')

args = parser.parse_args()
print(f'Индекс элемента: {bin_find(args.arr, args.elem, args.bds)}')
