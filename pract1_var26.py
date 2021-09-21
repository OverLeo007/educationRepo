"""Соколов Лев Макимович КИ21-17/1Б вар26"""
import sys

from math import cos, degrees, radians, sin, asin
from itertools import combinations


def eq(ea, eb):
    """Функция, производящее нечеткое сравнение данных ей аргументов"""
    if abs(ea - eb) < 0.000000000001:
        return True
    else:
        return False


def my_is_num(num: str):
    """Проверка строки на то, является ли ее содержимое числом
    (в отличии от стандартных методов строки поддерживает отрицательные значения)"""
    try:
        float(num)
        return True
    except ValueError:
        return False


def main(a, b, ab):
    """Тело программы, на вход поступают корректные значения и обрабатываются"""
    ab = radians(ab)
    c = (a ** 2 + b ** 2 - 2 * a * b * cos(ab)) ** 0.5
    bc = asin((a * sin(ab) / c))
    ac = asin((b * sin(bc)) / a)
    ab, bc, ac = degrees(ab), degrees(bc), degrees(ac)

    angles = (ab, bc, ac)
    sides_comp = list(combinations((a, b, c), 2))

    is_find = False
    sn = 0
    for i in sides_comp:
        if eq(*i):
            sn += 1
    if sn == 1:
        is_find = True
        print('\x1b[32m[RES]\x1b[0mТреугольник равнобедренный')
    elif sn == 3:
        is_find = True
        print('\x1b[32m[RES]\x1b[0mТреугольник равносторонний')
    for i in angles:
        if eq(90, i):
            is_find = True
            print('\x1b[32m[RES]\x1b[0mТреугольник прямоугольный')
    if not is_find:
        print('\x1b[32m[RES]\x1b[0mНу, это треугольник')


is_test_mode = False
while (test := input('Запустить режим ввода примеров? Y/N\n\x1b[33m[INP]\x1b[0m')) not in 'YNyn':
    continue

if test == 'Y' or test == 'y':
    print('\x1b[32mЗапускаю...\x1b[0m')
    sys.stdin = open('test_input.txt', 'r')
    is_test_mode = True


while 'exit' not in (x := input('Введите входные данные или "exit" для завершения работы программы\n'
                                '\x1b[33m[INP]\x1b[0m').split(' ')):
    if is_test_mode:
        print(f'\x1b[32m{" ".join(x)}\x1b[0m')

    if len(x) > 3:
        print('\x1b[31m[ERR]\x1b[0mВведено больше значений чем требуется')
        continue

    is_nums = True
    for i in x:
        if not my_is_num(i) or i.startswith('0'):
            print('\x1b[31m[ERR]\x1b[0mВведен не числовой тип данных, либо значение не корректно')
            is_nums = False
            break
    if is_nums is False:
        continue

    is_val_corr = True
    side1, side2, angle = map(lambda z: float(z) if '.' in z else int(z), x)
    if side1 <= 0 or side2 <= 0:
        print('\x1b[31m[ERR]\x1b[0mСтороны треугольника не могут быть <= 0')
        is_val_corr = False
    if not 0 < angle < 180:
        print('\x1b[31m[ERR]\x1b[0mУгол не лежит в области допустимых значиений (0, 180)')
        is_val_corr = False
    if not is_val_corr:
        continue

    main(side1, side2, angle)
if is_test_mode:
    print('exit')

print('\x1b[36m[FIN]\x1b[0mПрограмма успешно завершена')
