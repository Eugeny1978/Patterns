from time import time

div_line = '-' * 120
dw_line = '=' * 120

def benchmark(func):
    """
    Декоратор. Добавляет Время выполнения Оборачиваемой функции.
    Не подходит для Рекурсивных Функций.
    """
    from time import time
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        # func()
        finish = time()
        print('[*] Время выполнения: {} секунд.'.format(finish - start), sep='\n')
        return result
    return wrapper

def recurs(n: int):
    """
    Элементарный Пример Рекурсивной Функции.
    Выводит на экран порядок (Стек) вызовов Рекурсии
    """
    if n <= 10:
        print(n, end=' | ')
        recurs(n + 1)
        print(n, end=' || ')

def factorial(n: int):
    " Возвращет  Факториал N!"
    if n == 0: return 0
    if n == 1: return 1
    return factorial(n - 1) * n

def fibonaci(n: int):
    """
    Возвращает Значение N-го элемента в ряду Фибоначи.
    Использет Рекурсию.
    Минус этой функции: повторяющиеся ветки вычислений, т.е. дублирование расчетов
    """
    if n == 1: return 0
    if n == 2: return 1
    return (fibonaci(n - 1) + fibonaci(n - 2))

def fibonaci_fast(n: int):
    """
    Возвращает Значение N-го элемента в ряду Фибоначи
    """
    if n == 1: return 0
    if n == 2: return 1
    fib = [0, 1]
    for i in range(3, n + 1):
        fib.append(fib[i - 3] + fib[i - 2])
    return fib[-1]


@benchmark
def fibonaci_fast2(n: int):
    """
    Дубликат Функции fibonaci_fast(n). Используется в учеб целях с Декоратором
    """
    if n == 1: return 0
    if n == 2: return 1
    fib = [0, 1]
    for i in range(3, n + 1):
        fib.append(fib[i - 3] + fib[i - 2])
    return fib[-1]

# Словарь доступных функций для вызова по ключу в функции process()
functions = {
    'fib': fibonaci,
    'fib_f': fibonaci_fast,
    'fact': factorial
}

def process(func_key: str, n: int):
    """
    Вариант Функции Обертки для вычисления Времени Выполнения передаваемой Функции (по Ключу)
    Словарь Доступных функций: functions
    Напрямую функцию как переменную передавать некорректно, тк в данн случае сначала выполнится эта функция
    и только потом начнет выполняться тело обертки
    """
    start = time()
    result = functions[func_key](n)
    finish = time()
    if result > 10**10: result = '{:e}'.format(result)
    print(f"{func_key.upper()}({n}) = {result}", f"Время выполнения: {(finish - start):.6f} сек.", div_line, sep='\n')

def ispolindrom(string: str) -> bool:
    """
    Переданная Фраза Полиндром или нет
    """
    if len(string) < 2: return True
    if string[0] != string[-1]: return False
    else: return ispolindrom(string[1:-1])

def add_staples(string: str) -> str:
    """
    Добавляет зеркально Открывающие и Закрывающие скобки после каждого символа
    """
    if len(string) < 3: return string
    return string[0] + '(' + add_staples(string[1:-1]) + ')' + string[-1]

def bypass_nested_lists(multitude: list or tuple or set, level=1):
    """
    Обход многоуровневого множества
    Похожее применение для обхода папок на компьютере (см модуль bypass_dirs)
    """
    text = f" || {level = }"
    if len(multitude):
        print(*multitude, text)
    else:
        print('Пусто', text)
    for value in multitude:
        if isinstance(value, (list, tuple, set)):
            bypass_nested_lists(value, level=level+1)

def get_flat_turple(multitude: list or tuple or set, lst=[]):
    """
    Разворачивает вложенные итерируемые множества в один Плоский Список.
    Возвращает результат в виде Кортежа.
    Похожее применение для обхода папок на компьютере (см модуль bypass_dirs)
    """
    for value in multitude:
        if isinstance(value, (int, float, str)):
            lst.append(value)
        else:
            get_flat_turple(value)
    return tuple(lst)



if __name__ == '__main__':

    recurs(0)
    print('', dw_line, sep='\n')

    print(f"{factorial(10) = }")
    print(f"{fibonaci(20) = }")
    print(f"{fibonaci_fast(20) = }")
    print(dw_line)

    process('fact', 37)
    process('fib', 37)
    process('fib_f', 37)
    print(dw_line)

    process('fib_f', 50)
    print(f"{fibonaci_fast2(50) = }")
    print(dw_line)

    phrase1, phrase2, phrase3 = ('davorrovad', 'hello', 'кобан упал и лапу набок')
    print(f"Фраза '{phrase1}' - это полиндром? - {ispolindrom(phrase1)}")
    print(f"Фраза '{phrase2}' - это полиндром? - {ispolindrom(phrase2)}")
    print(f"Фраза '{phrase3}' - это полиндром? - {ispolindrom(phrase3)}")
    print(dw_line)

    print(add_staples('hgggfhgh'))
    print(add_staples('hggfhgh'))
    print(dw_line)

    sss = [3,4, (3,), 34, 66, [34, 67, [34, 11, 5, [], 341, 22]], (2, 8, (37, 'rtrt',
        (45, 22, [32, 'ww', (33, 2, 1), 45] , 11), 55) , 55), 34, [34, [], {56, 3}]]
    bypass_nested_lists(sss)
    print(dw_line)

    print(get_flat_turple(sss))
    print(dw_line)
