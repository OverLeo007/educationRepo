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


while (array := input('Введите элементы исходного массива через пробел'
                      ' или "end" для завершения программы:\n')) != 'end':
    try:
        array = list(map(lambda z: float(z) if '.' in z else int(z), array.split(' ')))
    except ValueError as e:
        print(f'Ошибка:\n\x1b[31m{e}\x1b[0m')
        continue
    try:
        element = input('Введите искомый элемент:\n')
        element = float(element) if '.' in element else int(element)
    except ValueError as e:
        print(f'Ошибка:\n\x1b[31m{e}\x1b[0m')
        continue
    bounds = input('Введите границы поиска (в виде числового отрезка) или нажмите Enter'
                   ' если вы не хотите задавать границы и вам сложно помочь компьютеру найти элемент\n')
    if bounds:
        try:
            bounds = tuple(map(int, bounds.split(' ')))
        except ValueError as e:
            print(f'Ошибка:\n\x1b[31m{e}\x1b[0m')
            continue
    res = bin_find(array, element, bounds)
    if res:
        print(f'Индекс элемента {element} - {res}')
    else:
        print('Вы обманули компьютер! В массиве нет этого элемента.')

