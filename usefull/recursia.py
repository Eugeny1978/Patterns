from time import time

div_line = '-' * 72

def benchmark(func):
    """
    Время выплнения Оборачиваемой функции. Не подходит для Рукурсивных Функций
    """
    from time import time
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        # func()
        finish = time()
        print(f"Время выполнения: {(finish - start):.6f} сек.")
        print('[*] Время выполнения: {} секунд.'.format(finish - start), div_line, sep='\n')
        return result
    return wrapper

def recurs(n):
    if n <= 10:
        print(n, end=' | ')
        recurs(n + 1)
        print(n, end=' || ')

def factorial(n):
    if n == 0: return 0
    if n == 1: return 1
    return factorial(n - 1) * n

def fibonaci(n):
    if n == 1: return 0
    if n == 2: return 1
    return (fibonaci(n - 1) + fibonaci(n - 2))
    # минус повторяющиеся ветки дкублирование рассчетов

@benchmark
def fibonaci_fast(n):
    if n == 1: return 0
    if n == 2: return 1
    fib = [0, 1]
    for i in range(3, n + 1):
        fib.append(fib[i - 3] + fib[i - 2])
    return fib[-1]

def fibonaci_fast2(n):
    if n == 1: return 0
    if n == 2: return 1
    fib = [0, 1]
    for i in range(3, n + 1):
        fib.append(fib[i - 3] + fib[i - 2])
    return fib[-1]

functions = {
    'fib': fibonaci,
    'fib_f': fibonaci_fast,
    'fact': factorial
}

def process(func_key, n):
    start = time()
    result = functions[func_key](n)
    finish = time()
    if result > 10**10: result = '{:e}'.format(result)
    print(f"{func_key.upper()}({n}) = {result}", f"Время выполнения: {(finish - start):.6f} сек.", div_line, sep='\n')



if __name__ == '__main__':
    # recurs(0)
    # print()

    # print(factorial(5))
    # print(fibonaci(10))
    # print(fibonaci_fast(10))

    # process(print(f"{factorial(10) = }"))
    # process(print(f"{fibonaci(20) = }"))
    # process(print(f"{fibonaci_fast(20) = }"))

    # print(f"{factorial(10) = }")
    # print(f"{fibonaci(20) = }")
    # print(f"{fibonaci_fast(20) = }")

    # start = time()
    # print(f"{fibonaci(40) = }")
    # finish = time()
    # print(f"Время выполнения: {(finish - start):.3f} сек.", div_line, sep='\n')

    # process('fact', 45)
    # process('fib', 45)
    # process('fib_f', 45)

    process('fib_f', 70)
    print(fibonaci_fast2(70))







