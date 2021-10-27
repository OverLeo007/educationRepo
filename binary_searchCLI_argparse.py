import argparse
from binary_search import bin_find

parser = argparse.ArgumentParser(description='Бинарный поиск элемента в массиве')
parser.add_argument('-arr', '--array_to_search', dest='arr', nargs='*', default=[1, 2, 3, 4, 5], type=int,
                    help='Отсортированный по неубыванию массив')
parser.add_argument('-el', '--element_to_find', dest='elem', default=3, type=int,
                    help='Элемент, индекс которго требуется найти')
parser.add_argument('-bds', '--bounds_of_search', dest='bds', nargs=2, default=None, type=int,
                    help='Границы поиска элемента в массиве')
args = parser.parse_args()

if x := bin_find(args.arr, args.elem, args.bds):
    print(f'Индекс элемента: {x}')
else:
    print('Элемент не найден')
