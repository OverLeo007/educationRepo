import random as rand


class MyTuples:
    def __init__(self):
        # self.t_a = tuple([rand.randint(-100, 100) for _ in range(0, rand.randint(10, 100))])
        # self.t_b = tuple([rand.randint(-100, 100) for _ in range(0, rand.randint(10, 100))])
        self.t_a = tuple([8, 9, 3, 4])
        self.t_b = tuple([6, 5, 3, 3, 5])
        self.inter = set(self.t_a) & set(self.t_b)

    def clones(self):
        count = 0
        uses = []
        if len(self.t_a) > len(self.t_b):
            for n, i in enumerate(self.t_a):
                if i in self.t_b:
                    count += 1
        return f'Кол-во одинаковых чисел: {count}'

    def difference(self):
        pass


do = MyTuples()
print(do.clones())
