# lambda Переменные:  Условие
sss = lambda *args: sum(args)

def lambda_func(*args): # см функцию выше
    return sum(args)

nums = lambda arg: 'Positive Num' if arg >= 0 else 'Negative Num'

lst_1 = [23, 12, 56, 128, 5000, 55, 55, 234, 1030, 17, 18, 76, 44, 29, 28]
lst_2 = lst_1.copy()
lst_3 = lst_1.copy()

def linear_equation(k,b):
    return lambda x: k*x + b # возвращает функцию!


if __name__ == '__main__':
    print(sss(4, 5, 3, 3, 33))
    print(nums(41))
    print(nums(-12))

    print(lst_1)
    lst_1.sort()
    lst_2.sort(key=lambda arg: arg % 10) # Сотрировка по последней цифре
    lst_3.sort(key=lambda arg: arg // 10 % 10)  # Сотрировка по Пред-последней цифре
    print(lst_1, lst_2, lst_3, sep='\n')

    graph_1 = linear_equation(2, 7)(6)
    print(graph_1)

    y = linear_equation(2, 7)
    for x in range(10):
        print(x, y(x), sep=' - ', end=' || ')
