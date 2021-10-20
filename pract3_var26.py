"""Соколов Лев Макимович КИ21-17/1Б вар26"""
import random as rand


class MyTuples:
    def __init__(self, bord_a, bord_b, len_a, len_b):
        """Инициализация экземляра MyTuples"""
        self.t_a = tuple([rand.randint(*bord_a) for _ in range(0, len_a)])
        self.t_b = tuple([rand.randint(*bord_b) for _ in range(0, len_b)])
        self.diff = 0

    def clones(self):
        """Метод, находящий количество одинаковых чисел в кортежах"""
        count = 0
        b_usbl = {ind: False for ind, _ in enumerate(self.t_b)}
        for i in self.t_a:
            if i in self.t_b:
                for ind in b_usbl.keys():
                    if self.t_b[ind] == i and b_usbl[ind] is False:
                        b_usbl[ind] = True
                        count += 1
                        break
        self.diff = len(self.t_a) + len(self.t_b) - count * 2
        return f'Кол-во одинаковых чисел: {count}'

    def difference(self):
        """Метод, находящий количество различных чисел в кортежах"""
        self.clones()
        return f'Кол-во различных чисел: {self.diff}'

    def unique(self):
        """Метод, находящий количество уникальных чисел в обоих кортежах"""
        count = 0
        un = self.t_a + self.t_b
        for i in un:
            if un.count(i) == 1:
                count += 1
        return f'Кол-во уникальных чисел: {count}'

    def xor(self):
        """Метод, выполняющий поиск чисел, входящих или в первый или во второй кортеж, но не в оба
        одновременно"""
        res = []
        for i in self.t_a:
            if i not in self.t_b:
                res.append(str(i))
        for i in self.t_b:
            if i not in self.t_a:
                res.append(str(i))
        return f'Числа, входящие или в первый или во второй кортеж,' \
               f' но не в оба одновременно: {" ".join(res)}'

    def another_uniq(self):
        """Метод, выполняющий поиск чисел, которые есть в первом кортеже и нет во втором и
        наоборот"""
        res_a = []
        res_b = []
        for i in self.t_a:
            if i not in self.t_b:
                res_a.append(str(i))
        for i in self.t_b:
            if i not in self.t_a:
                res_b.append(str(i))
        return f'Числа, которые есть в первом кортеже и нет во втором:' \
               f' {" ".join(res_a)}\nЧисла, которые есть во втором' \
               f' кортеже и нет в первом: {" ".join(res_b)}'

    def printable_tuples(self):
        """Метод, создающий строку, содержащую кортежи для вывода на экран"""
        return f'Первый кортеж: {" ".join(map(str, self.t_a))}\nВторой кортеж: {" ".join(map(str, self.t_b))}'


f_border, s_border = (), ()
f_len, s_len = 0, 0
while True:
    try:
        f_border = tuple(map(int, input('Введите границы первого кортежа:\n').split(' ')))
        s_border = tuple(map(int, input('Введите границы второго кортежа:\n').split(' ')))
        f_len = int(input('Введите длину первого кортежа:\n'))
        s_len = int(input('Введите длину второго кортежа:\n'))
        if f_len <= 0 or s_len <= 0:
            raise ValueError('кортеж не может иметь нулевую или отрицательную длину!')
        elif len(f_border) != 2 != len(s_border):
            raise ValueError('при указании границы было введено кол-во чисел != 2')
    except ValueError as error:
        print(f'Какое-то из введенных чисел делает задачу невозможной, так как {error}')
        continue
    else:
        break

do = MyTuples(f_border, s_border, f_len, s_len)
menu = {
    '1': ('Вывод исходного набора на экран', do.printable_tuples),
    '2': ('Количество одинаковых чисел в обоих кортежах', do.clones),
    '3': ('Количество различных чисел в обоих кортежах', do.difference),
    '4': ('Общее количество уникальных чисел', do.unique),
    '5': ('Числа, входящие или в первый или во второй кортеж, но не в оба одновременно', do.xor),
    '6': ('Числа, которые есть в первом кортеже и нет во втором и наоборот', do.another_uniq),
    '7': ('Выход из программы', exit)
}

while True:
    printable_menu = '\n'.join(map(lambda y: ' - '.join(y), map(lambda x: (x[0], x[1][0]), menu.items())))
    opt = input(f"Выберете опцию:\n{printable_menu}\n")
    try:
        print(menu.get(opt)[-1]())
    except TypeError as e:
        print(e)
        print('Нет такого варианта выбора')

