a = list(range(1, 32))
b = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']

day = 0
while day != 31:
    for i in b:
        if day < 31:
            a[day] = (a[day], i)
            day += 1
        else:
            break

res = [i[0] for i in a if i[-1] == 'сб' or i[-1] == 'вс']
print(*res)