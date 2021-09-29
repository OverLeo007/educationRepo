from random import randint as rand
from numpy import mean
from pprint import pprint


class Matrix:
    def __init__(self, n=0):
        self.matrix = [[rand(-10, 1000) for _ in range(n)] for _ in range(n)] if n else 'Матрица не сгенерирована'
        self.stats = 'Характеристики матрицы не сгенерированы'

    @staticmethod
    def my_is_num(num: str):
        """Проверка строки на то, является ли ее содержимое числом
        (в отличии от стандартных методов строки поддерживает отрицательные значения)"""
        try:
            float(num)
            return True
        except ValueError:
            return False

    def update_matrix(self):
        n = input('Введите размер матрицы n*n:\n')
        if n.isdigit() and n[0] != '0':
            n = int(n)
            self.matrix = [[rand(-10, 1000) for _ in range(n)] for _ in range(n)]
            return 'Матрица создана'
        else:
            return 'Ошибка, некорректный ввод'

    def get_matrix(self):
        if isinstance(self.matrix, list):
            return '\n'.join(map(lambda x: '\t'.join(map(str, x)), self.matrix))
        else:
            return self.matrix

    def get_stats(self):
        return self.stats

    def transpose(self):
        if isinstance(self.matrix, list):
            self.matrix = list(zip(*self.matrix))
            return 'Матрица траспонирована'
        else:
            return self.matrix

    def get_transpose(self):
        return list(zip(*self.matrix))

    def make_stats(self):
        if isinstance(self.matrix, list):
            self.stats = {'mean_row': [(nr, mean(row)) for nr, row in enumerate(self.matrix)],
                          'mean_col': [(nr, mean(row)) for nr, row in enumerate(self.get_transpose())]}
            return 'Характеристики матрицы сгенерированы'
        else:
            return self.matrix

    def get_closer(self):
        if isinstance(self.matrix, list):
            zn = input('Введите число:\n')
            if self.my_is_num(zn):
                zn = float(zn) if '.' in zn else int(zn)
                print(zn)
                res = []
                for rn, row in enumerate(self.matrix):
                    for eln, elem in enumerate(row):
                        res.append((rn, eln, abs(elem - zn)))
                return ' '.join(map(str, min(res, key=lambda x: x[2])))
            else:
                return 'Ошибка, некорректный ввод'
        else:
            return self.matrix


matrix = Matrix()
menu = {'1': ('Сгерерировать  матрицу', matrix.update_matrix),
        '2': ('Транспонировать матрицу', matrix.transpose),
        '3': ('Сгенерировать характеристики матрицы', matrix.make_stats),
        '4': ('Поиск числа из матрицы, наиболее близкого к введенному  числу', matrix.get_closer),
        '5': ('Вывести характеристики матрицы', matrix.get_stats),
        '6': ('Вывести текущее состояние матрицы', matrix.get_matrix),
        '7': ('Завершить программу', exit)}

while True:
    printable_menu = '\n'.join(map(lambda y: ' - '.join(y), map(lambda x: (x[0], x[1][0]), menu.items())))
    opt = input(f"Выберете опцию:\n{printable_menu}\n")
    try:
        print(menu.get(opt)[-1]())
    except TypeError:
        print('Нет такого варианта выбора')

