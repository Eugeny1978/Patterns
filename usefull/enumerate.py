div_line = '-'*120
arrow = [10, 20, 30, 40, 50, 60, 70]
dct = dict(aaa=10, bbb=20, ccc=30, ddd=40, eee=50)
tpl = ('apple', 'mando', 'carrot', 'potato')
sig_end = ' | '
sig_sep = ' = '


if __name__ == '__main__':
    # Необходитмо для обхода циклом каждый раз употреблять enumerate(arrow)
    # тк после первого обхода там не останется элементов

    print(f"{enumerate(arrow) = }")
    print(f"{tuple(enumerate(arrow)) = }")
    print(div_line)

    print("Pairs in enumerate(arrow)")
    for pair in enumerate(arrow):
        print(pair, end=sig_end)
    print('\n', div_line, sep='')

    print("*Pairs in enumerate(arrow)")
    for pair in enumerate(arrow):
        print(*pair, sep=sig_sep, end=sig_end)
    print('\n', div_line, sep='')

    print("indexs, values in enumerate(arrow)")
    for index, value in enumerate(arrow):
        print(index, value, sep=sig_sep, end=sig_end)
    print('\n', div_line, sep='')

    for index, value in enumerate(arrow):
        arrow[index] = value + 5 # поменять значения в ряду можно только обращаясб по индексу
    print(f"{arrow = }")
    print(div_line)

    print("indexs, keys in enumerate(dct)") # Выведет Только ключи. Также не понятно в каком порядке выведет
    for index, key in enumerate(dct):
        print(index, key, sep=sig_sep, end=sig_end)
    print('\n', div_line, sep='')

    print("indexs, values in enumerate(range(5, 16, 2)")
    for index, value in enumerate(range(5, 16, 2)):
        print(index, value, sep=sig_sep, end=sig_end)
    print('\n', div_line, sep='')

    print("indexs, values in enumerate(tpl)")
    for index, value in enumerate(tpl):
        print(index, value, sep=sig_sep, end=sig_end)
    print('\n', div_line, sep='')

    print("indexs, values in enumerate(tpl, start=10)")
    for index, value in enumerate(tpl, start=10):
        print(index, value, sep=sig_sep, end=sig_end)
    print('\n', div_line, sep='')
