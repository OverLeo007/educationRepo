from math import factorial


def mk_kat(n):
    return int((1 / (n + 1)) * (factorial(2 * n) // factorial(n) ** 2))


def is_kat(n):
    for i in range(1, n + 1):

        if mk_kat(i) == n:
            return i + 1
    return False


while (num := input('Введите n или "end" для завершения работы программы\n')) != 'end':
    if not num.isdigit() or num.startswith('0'):
        print('Ошибка: некорректное введенное значение')
        continue
    else:
        num = int(num)
    if num >= 515:
        print(f'{num}-е число Каталана невычислимо из-за особенностей питона (OverflowError)')
        continue
    print(f'{num}-е число Каталана:\n{mk_kat(num)}')
    if res := is_kat(num):
        print(f'{num} является {res} числом Каталана')
    else:
        print(f'{num} не является числом Каталана')
