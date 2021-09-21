def ph(n):
    wars = list(range(1, n + 1))
    while len(wars) != 1:
        del wars[::3]
    return wars[0]


print(ph(41))
