from random import randint

# [выражение for значение_коллекции in коллекция]
# [выражение for значение_коллекции in коллекция if условие]

div_line = '-' * 100
lst = [5, 7, 33, 17, 55]
lst_1 = [i * 2 for i in lst] # генератор списка
tpl_1 = (i * 2 for i in lst) # выражение генератор
rnds = [randint(0, 10) for i in range(20)]  # набор случ чисел
even_rnds = [r for r in rnds if r % 2 == 0]
num_rows, num_colums = 5, 4

mens = [
    ('Sidorov', 1995),
    ('Luchkov', 2002),
    ('Petrov', 1991),
    ('Gorbachev', 1984),
    ('Kostin', 2000),
    ('Isaev', 2005),
    ('Eliseev', 1999),
    ('Kozlov', 2004),
    ('Bukov', 1995),
    ('Gavrilov', 1980),
    ('Efremov', 2006)
]

long_string = 'trytyh r8fgmdddr dr 898dr9 d9t9!! - ...0,,d<< >95,60ev.,f0t50e5t0d0,t506,b'

if __name__ == '__main__':

    print(lst_1, tpl_1, sep='\n')
    for tp in tpl_1:
        print(tp, end=' | ')

    print('', rnds, even_rnds, '', sep='\n')


    arr = [[0] * num_colums for row in range(num_rows)]
    print(arr)
    arr[-1][2] = 1  # [ряд][колонка] | [внеш список][внутренний список]
    for row in arr:
        print(row)
    print(div_line)

    rand_arr = [[randint(10,50) for value in range(num_colums)] for row in range(num_rows)]
    for row in rand_arr:
        print(row)
    print(div_line)

    main_diag = [rand_arr[i][j] for i in range(num_colums) for j in range(num_rows) if i == j]
    row_2a = rand_arr[2]
    row_2b = [rand_arr[2][j] for j in range(num_colums)]
    col_3 = [rand_arr[i][3] for i in range(num_rows)]
    print(f"{main_diag = }", f"{row_2a = }", f"{row_2b = }", f"{col_3 = }", div_line, sep='\n')

    m_table = [[i*j for i in range(1, num_colums+1)] for j in range(1, num_rows+1)]
    for row in m_table:
        print(row)
    print(div_line)

    mu_table = [[(f"{i}*{j} = {i * j}") for i in range(1, num_colums+1)] for j in range(1, num_rows+1)]
    for row in mu_table:
        print(row)
    print(div_line)



    indexs_1 = 'ABCD'
    indexs_2 = range(1, 5)
    indexes = [(i, j) for i in indexs_1 for j in indexs_2]
    print(indexes)

    vals_1 = [3, 8, 9, 17]
    vals_2 = range(1, 5)
    vals = [(i, j, i * j) for i in vals_1 for j in vals_2 if (i * j > 30)]
    print(vals)

    mens_K = [man[0] for man in mens if man[0].startswith('K')]
    mens_2000 = [man for man in mens if man[1] > 2000]
    LIKE = [man[0][0] for man in mens if man[1] > 2000]
    print(f"{mens_K = }", f"{mens_2000 = }", f"{LIKE = }", sep='\n')

    nums = [int(i) for i in long_string if i.isdigit()]
    alphas = [i for i in long_string if i.isalpha()]
    print(nums, alphas, sep='\n')



    # ls = input('Введиде через пробел Числа: ').split()
    # try:
    #     ls = [int(i) for i in ls]
    #     print('Результат:', ls)
    # except:
    #     print('Среди введенных значений есть не числа!')

