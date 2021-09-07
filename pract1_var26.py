from math import cos, degrees, radians, sin, asin
from itertools import combinations


def eq(a, b):
    if abs(a - b) < 0.000000000001:
        return True
    else:
        return False


def rounder(n: int):
    if isinstance(n, float):
        num = str(n).split('.')
        if num[1] == '0':
            return int(n)
        elif num[1].count('9') > 12:
            return int(num[0]) + 1
        elif num[1].count('0') > 12:
            return int(num[0])
    return n


# a, b, ang1 = map(int, input().split())
a, b, ab = 3.5, 3.5, '90'

if isinstance(a, str) or isinstance(b, str) or isinstance(ab, str):
    print('\x1b[31mОшибка: Введен не числовой тип данных')
    exit()
elif a <= 0 or b <= 0:
    print('\033[91mОшибка: Стороны треугольника не могут быть отрицательными')
    exit()
elif ab <= 0 or ab >= 180:
    print('\033[91mОшибка: Угол не лежит в области допустимых значиений (0, 180)')
    exit()


ab = radians(ab)
c = (a ** 2 + b ** 2 - 2 * a * b * cos(ab)) ** 0.5
bc = asin((a * sin(ab) / c))
ac = asin((b * sin(bc)) / a)
ab, bc, ac = degrees(ab), degrees(bc), degrees(ac)
# ab, bc, ac = map(lambda x: rounder(x), (degrees(ab), degrees(bc), degrees(ac)))

print(a, b, c)
print(ab, bc, ac)
sides = (a, b, c)
angles = (ab, bc, ac)
sr_sid = list(combinations(sides, 2))

sn = 0
for i in sr_sid:
    if eq(*i):
        sn += 1

if sn == 1:
    print('\033[92mТреугольник равнобедренный')
elif sn == 3:
    print('Треугольник равносторонний')
for i in angles:
    if eq(90, i):
        print('Треугольник прямоугольный')
        break
