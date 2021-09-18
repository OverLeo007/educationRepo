def rep_ins_arr(arr, start, i_arr):
    return arr[:start - 1] + i_arr + arr[start:]


def tab_1(f_name):
    with open(f_name, 'r', encoding='utf-8') as file:
        _n = file.readlines()
    _n = filter(lambda x: x != '', map(lambda x: x.replace('\n', ''), _n))
    _n = list(map(lambda x: x.split('\t') if '-' in x else x, _n))
    n = []
    for i in _n:
        if isinstance(i, str):
            n.append(i)
        else:
            n.extend(i)

    res = []
    for i in range(0, len(n), 10):
        res.append((n[i], n[i + 1: i + 10]))
    res = [(i[0], tuple(map(lambda x: x.replace(',', '.').replace(' ', ''), i[1]))) for i in res]
    res = list(map(lambda x: (
        int(x[0]), tuple(filter(lambda x: x != '', map(lambda y: float(y) if '-' not in y else '', x[1])))), res))
    return res


def tab_23(f_name):
    with open(f_name, 'r') as file:
        n = file.readlines()
    n = list(map(float, filter(lambda x: x != '', map(lambda x: x.replace('\n', ''), n))))
    res = []
    for i in range(0, len(n), 2):
        res.append((n[i], n[i + 1]))
    res = list(map(lambda x: (int(x[0]), x[1]) if x[0] >= 1 else x, res))
    return sorted(res, key=lambda x: x[0])


def tab_4(f_name):
    with open(f_name, 'r', encoding='utf-8') as file:
        n = file.readlines()
    n = list(filter(lambda x: x != '', map(lambda x: x.replace('\n', ''), n)))
    res = []
    for i in n:
        if not set(i).issubset(set('1234567890.')):
            res.append([i])
        else:
            for c, j in enumerate(res):
                if len(j) == 1:
                    res[c].append(i)
                    break

    return list(map(tuple, res))


tab1 = tab_1('tab1.txt')
tab2 = tab_23('tab2.txt')
tab3 = tab_23('tab3.txt')
tab4 = tab_4('tab4.txt')
# print('Рассчитываем энтропию')
# for i in tab1:
