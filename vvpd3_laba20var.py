'''
Вывести три целых положительных числа: 𝑅 – суммарное число рёбер
многогранников, 𝑇 – суммарное число углов многогранников. 𝑀 – суммарное
количество граней всех многогранников в коллекции.
'''
p_body = {'Tetrahedron': (6, 4, 4),
          'Hexahedron': (12, 8, 6),
          'Octahedron': (12, 6, 8),
          'Dodecahedron': (30, 20, 12),
          'Icosahedron': (30, 12, 20)}

inp_body = input('Введите многоу    гольники:\n').split(' ')
res = [0, 0, 0]
for body in inp_body:
    try:
        r, t, m = p_body[body]
    except KeyError:
        print(f'Слово {body} написано с ошибкой, '
              f'данный многогранник не будет учтен')
        continue

    res[0] += r
    res[1] += t
    res[2] += m
print(*res)