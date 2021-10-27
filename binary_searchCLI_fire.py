from binary_search import bin_find
import fire


def microfix(arr, el, bds=None):
    if x := bin_find(arr, el, bds):
        return f'Индекс элемента {x}'
    else:
        return 'Элемент не найден'


if __name__ == '__main__':
    fire.Fire(microfix)
