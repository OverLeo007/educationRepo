from itertools import combinations, permutations


# Хочу ачивку))
def is_vampire(n):
    return [i for i in
            list(set(
                [i for i in combinations(
                    list(map(lambda x: int(''.join(map(str, x))),
                             permutations(list(map(int, list(n))), len(n) // 2))), 2)
                 if i[0] * i[1] == int(n)]))
            if sorted(list(map(int, list(str(i[0])))) +
                      list(map(int, list(str(i[1]))))) ==
            sorted(list(map(int, list(n))))
            and not (str(i[0]).endswith('0')
                     and str(i[1]).endswith('0'))]


print(*is_vampire('13078260'), sep='\n')
