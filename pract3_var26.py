import random as rand


class MyTuples:
    def __init__(self):
        # self.t_a = tuple([rand.randint(-100, 100) for _ in range(0, rand.randint(10, 100))])
        # self.t_b = tuple([rand.randint(-100, 100) for _ in range(0, rand.randint(10, 100))])
        self.t_a = tuple([8, 9, 3, 3, 3, 5])
        self.t_b = tuple([6, 5, 3, 3, 5])
        self.diff = 0

    def clones(self):
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
        self.clones()
        return f'Кол-во различных чисел: {self.diff}'

    def unique(self):
        count = 0
        un = self.t_a + self.t_b
        for i in un:
            if un.count(i) == 1:
                count += 1
        return f'Кол-во уникальных чисел {count}'

    def xor(self):
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


do = MyTuples()
print(do.clones())
print(do.difference())
print(do.unique())
print(do.xor())
print(do.another_uniq())