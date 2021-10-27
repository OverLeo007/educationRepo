import os


def gen_ind(st, fel):
    res = []
    el = 0
    while st:
        if st[0] == fel:
            res.append(el)
        st = st[1:]
        el += 1
    return res


def ind_replace(st, ind, ch):
    return st[:ind] + ch + st[ind + 1:]


def main():
    fword = input('Введите слово:\n')
    os.system('CLS')
    mist = 6
    resword = '_' * len(fword)
    used = []
    while mist != 0:
        print(resword)
        if resword == fword:
            print('Поздравляю с победой, вы успели отгадать слова и спастись от смерти!')
            break
        let = input('Какую букву откроем?\n')
        if let in used:
            print('Была уже такая буква, ты шо')
            continue
        else:
            used.append(let)

        if chind := gen_ind(fword, let):
            for i in chind:
                resword = ind_replace(resword, i, fword[i])
        else:
            mist -= 1
            if mist != 0:
                print(f'Нет такой буквы, еще {mist} ошибок и ты окажешься в петле.')
    else:
        print('Табуретка упала и твои ноги болтаются в воздухе...')


if __name__ == '__main__':
    main()
