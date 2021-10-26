from binary_search import bin_find
import fire

if __name__ == '__main__':
    fire.Fire(lambda arr, el, bds=None: f'Индекс элемента: {bin_find(arr, el, bds)}')