wrs = list(range(int(input('Кол-во войнов:\n'))))
while len(wrs) > 1:
    del wrs[::3]
print(*wrs)



