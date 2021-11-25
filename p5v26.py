"""Соколов Лев Макимович КИ21-17/1Б вар26"""
import os

import json
import re
from random import randint, choice

CURRENT_DB = 'fly_db.json'


def clear_db(db):
    """
    Очистка базы данных, поданной на вход
    :param db:
    :return:
    """
    serialize(db, {})


def gen_new_db(count_of_lines):
    """
    Запись в файл заново рандомно сгенерированной по кол-ву строк базы данных
    :param count_of_lines:
    :return:
    """
    with open('airports.txt', 'r', encoding='utf-8') as airp:
        airports = list(map(lambda x: x.replace('\n', ''), airp.readlines()))
    clear_db(CURRENT_DB)
    for i in range(count_of_lines):
        line = {'date': '.'.join(
            (str(randint(1, 28)).rjust(2, '0'), str(
                randint(1, 12)).rjust(2, '0'), str(randint(2021, 2022)))),
            'time': ':'.join(
                (str(randint(0, 23)).rjust(2, '0'), str(randint(1, 59)).rjust(2, '0'))),
            'airport': choice(airports),
            'cost': randint(3000, 15000),
            'flytime': randint(30, 720)}
        add_line('fly_db.json', line)


def get_maxlen(my_dict, keyw):
    """
    Нахождение максимальной длинны значения для ключей во вложенных списках
    :param my_dict:
    :param keyw:
    :return:
    """
    return len(max([str(max(list(my_dict.values()),
                            key=lambda x: len(str(x[keyw])))[keyw]), keyw], key=len))


def print_db_tab(my_dict: dict):
    """
    Вывод в консоль двухуровневого списка в виде таблицы
    :param my_dict:
    :return:
    """
    maxlens = {'key': len(max(list(my_dict.keys()) + ['key'], key=len))}
    value_maxlen = {f'{val}': get_maxlen(my_dict, val) for val in list(my_dict.values())[0]}
    maxlens = {**maxlens, **value_maxlen}
    print(*[key.ljust(value, ' ') + '\t' for key, value in maxlens.items()], sep='')
    print(*[''.join([str(value).ljust(maxlens[key], ' ') + '\t' for key, value in line]) for line in
            map(lambda x: ([('key', x[0])] + list(x[1].items())), list(my_dict.items()))], sep='\n')


def deserialize(db):
    """
    Десериализация json объекта в dict объект
    :param db:
    :return:
    """
    with open(db, 'r', encoding='utf-8') as database:
        return json.load(database)


def serialize(db, deserialized_db):
    """
    Сериализация dict объекта в json объект
    :param db:
    :param deserialized_db:
    :return:
    """
    with open(db, 'w', encoding='utf-8') as database:
        json.dump(deserialized_db, database)
        return 'База успешна обновлена'


def add_line(db: str, line: dict):
    """
    Запись новой строки в базу данных
    :param db:
    :param line:
    :return:
    """
    deserial_db = deserialize(db)
    if dbkeys := list(deserial_db.keys()):
        deserial_db[str(int(dbkeys[-1]) + 1)] = line
    else:
        deserial_db["0"] = line
    return serialize(db, deserial_db)


def del_line(db: str, index: int):
    """
    Удаление строки из БД по ключу
    :param db:
    :param index:
    :return:
    """
    deserial_db = deserialize(db)
    deserial_db.pop(str(index))
    deserial_db = dict((i, deserial_db[i]) if int(i) < index
                       else (str(int(i) - 1), deserial_db[i]) for i in deserial_db.keys())
    return serialize(db, deserial_db)


def sort_by(db, kts):
    """
    Вывод отсортированной по ключу БД
    :param db:
    :param kts:
    :return:
    """
    deserial_db = deserialize(db)
    lines = list(deserial_db.items())
    lines.sort(key=lambda x: x[1][kts])
    sorted_db = dict(lines)
    return sorted_db


def filter_by(db, ktf, val, symb):
    """
    Вывод отфильтрованной по ключу БД
    :param db:
    :param ktf:
    :param val:
    :param symb:
    :return:
    """
    deserial_db = deserialize(db)
    lines = list(deserial_db.items())
    variants = {'=': filter(lambda x: x[1][ktf] == val, lines),
                '>': filter(lambda x: x[1][ktf] > val, lines),
                '<': filter(lambda x: x[1][ktf] < val, lines),
                '>=': filter(lambda x: x[1][ktf] >= val, lines),
                '<=': filter(lambda x: x[1][ktf] <= val, lines)}
    f_lines = variants[symb]
    filtred_db = dict(f_lines)
    return filtred_db


def value_check(value, key):
    """
    Проверка значений по их типу
    :param value:
    :param key:
    :return:
    """
    valid = False
    if key == 'date':
        if re.fullmatch(r'\d{2}\.\d{2}\.\d{4}', value):
            valid = True
    elif key == 'time':
        if re.fullmatch(r'\d{2}:\d{2}', value):
            valid = True
    elif key == 'airport':
        if re.fullmatch(r'\D+ - \D+', value):
            valid = True
    elif key in ('cost', 'flytime', 'size'):
        if value.isdigit() and not value.startswith('0'):
            valid = True
    elif key == 'vector':
        if value in ['>', '<', '=', '>=', '<=']:
            valid = True
    elif key == 'key':
        if value in deserialize(CURRENT_DB).keys():
            return value
        else:
            raise KeyError('Ключа не существует')
    if valid:
        return value
    else:
        raise ValueError(f'Неверный формат {key}')


def main():
    """
    Тело программы
    :return:
    """
    if CURRENT_DB not in os.listdir():
        print('База данных создана в текущем каталоге')
        clear_db(CURRENT_DB)
    menu = {'1': ('Добавить запись', add_line),
            '2': ('Удалить запись по ключу', del_line),
            '3': ('Вывести отсортированную по времени в пути базу данных', sort_by),
            '4': ('Вывести отфильтрованную по стоимости базу данных', filter_by),
            '5': ('Вывести базу данных целиком', deserialize),
            '6': ('Сгенерировать новую базу данных', gen_new_db),
            '7': ('Очистить базу данных', clear_db),
            '8': ('Выйти из программы', exit)
            }
    printable_menu = '\n'.join(map(lambda y: ' - '.join(y),
                                   map(lambda x: (x[0], x[1][0]),
                                       menu.items())))
    while True:
        print(printable_menu)
        pick = input()
        if pick == '1':
            try:
                line = {'date': value_check(input('Введите дату в формате дд.мм.гггг\n'), 'date'),
                        'time': value_check(input('Введите время в формате мм:чч\n'), 'time'),
                        'airport': value_check(
                            input('Введите расположение аэропорта в формате "страна '
                                  '- город"\n'), 'airport'),
                        'cost': value_check(input('Введите стоимость перелета\n'), 'cost'),
                        'flytime': value_check(input(
                            'Введите время перелета в минутах\n'), 'flytime')}
                menu[pick][1](CURRENT_DB, line)
            except ValueError as error:
                print(error)
                continue
        elif pick == '2':
            try:
                key = int(value_check(input('Введите ключ строки для удаления\n'), 'key'))
                menu[pick][1](CURRENT_DB, key)
            except KeyError as error:
                print(error)
                continue
        elif pick == '3':
            print_db_tab(menu[pick][1](CURRENT_DB, 'flytime'))
        elif pick == '4':
            try:
                cost = int(value_check(input('Введите стоимость\n'), 'cost'))
                vector = value_check(input('введите вектор поиска (<, >, =, <=, >=)\n'), 'vector')
                print_db_tab(menu[pick][1](CURRENT_DB, 'cost', cost, vector))
            except ValueError as error:
                print(error)
                continue
        elif pick == '5':
            cur_db = menu[pick][1](CURRENT_DB)
            if cur_db:
                print_db_tab(cur_db)
            else:
                print('База пуста')
        elif pick == '6':
            try:
                size = int(value_check(input('Введите кол-во строк в базе данных\n'), 'size'))
                menu[pick][1](size)
            except ValueError as error:
                print(error)
                continue
        elif pick == '7':
            clear_db(CURRENT_DB)
        elif pick == '8':
            menu[pick][1]()


if __name__ == '__main__':
    main()
