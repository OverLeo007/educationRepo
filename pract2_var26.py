"""Соколов Лев Макимович КИ21-17/1Б вар26"""
from random import randint as rand
from numpy import mean


class Matrix:
    def __init__(self):
        """Инициализация экземляра Matrix"""
        self.matrix = 'Матрица не сгенерирована'
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
        """Генерация матрицы по заданному размеру"""
        n = input('Введите размер матрицы n*n:\n')
        if n.isdigit() and n[0] != '0':
            n = int(n)
            self.matrix = [[rand(-10, 1000) for _ in range(n)] for _ in range(n)]
            self.stats = 'Характеристики матрицы не сгенерированы'
            return 'Матрица создана'
        return 'Ошибка, некорректный ввод'

    def get_matrix(self):
        """Возвращает матрицу в читабельном виде, если она существует"""
        if isinstance(self.matrix, list):
            return '\n'.join(map(lambda x: '\t'.join(map(str, x)), self.matrix))
        return self.matrix

    def get_stats(self):
        """Возвращает характеристики матрицы"""
        if isinstance(self.stats, dict):
            printable_stats = ''
            for key, vals in self.stats.items():
                newstr = f'{key}:\n'
                for val in vals:
                    newstr += f'    {" ".join(map(str, val))}\n'
                printable_stats += newstr
            return printable_stats[:-1]

        return self.stats

    def transpose(self):
        """Транспонирует матрицу, если она существует"""
        if isinstance(self.matrix, list):
            self.matrix = list(zip(*self.matrix))
            return 'Матрица траспонирована'
        return self.matrix

    def __get_transpose(self):
        """Возвращает транспонированную матрицу"""
        return list(zip(*self.matrix))

    def make_stats(self):
        """Генерирует характеристики для матрицы"""
        if isinstance(self.matrix, list):
            self.stats = {'mean_row': [(nr, mean(row)) for nr, row in enumerate(self.matrix)],
                          'mean_col': [(nr, mean(row)) for nr, row in enumerate(self.__get_transpose())]}
            return 'Характеристики матрицы сгенерированы'
        return self.matrix

    def get_closer(self):
        """Находит приближенное значение к введенному пользователем"""
        if isinstance(self.matrix, list):
            zn = input('Введите число:\n')
            if self.my_is_num(zn):
                zn = float(zn) if '.' in zn else int(zn)
                res = []
                for rn, row in enumerate(self.matrix):
                    for eln, elem in enumerate(row):
                        res.append((rn, eln, abs(elem - zn)))
                return ' '.join(map(str, min(res, key=lambda x: x[2])))
            else:
                return 'Ошибка, некорректный ввод'
        return self.matrix


matrix = Matrix()
menu = {'1': ('Сгерерировать матрицу', matrix.update_matrix),
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
