# ЗАМЫКАНИЯ
# Создаются свои зоны видимости. Похоже на работу экземпляров Классов

from datetime import datetime
from time import sleep, perf_counter


def main_func(temp_name):
    name = temp_name
    def inner_func():
        print('Hello, my friend', name)
    return inner_func

def adder(value):
    """
    Добавляет Значение
    """
    def inner(a):
        return value + a
    return inner

def counter():
    """
    Считает сколько раз вызвали
    """
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

def average_numbers():
    numbers = []
    def inner(num):
        numbers.append(num)
        print(numbers)
        return round(sum(numbers)/len(numbers), 4)
    return inner

def average_v2():
    summa = 0
    count = 0
    def inner(value):
        nonlocal summa, count
        summa = summa + value
        count += 1
        return round(summa / count, 4)
    return inner

def timer():
    # start = datetime.now()
    start = perf_counter()
    def inner():
        # return datetime.now() - start
        return round(perf_counter() - start, 1)
    return inner

def add2(a, b):
    return a + b

def counter_func(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Функция '{func.__name__}' вызывалась {count} раз")
        return func(*args, **kwargs)
    return inner

if __name__ == '__main__':

    ivan = main_func('Ivan')
    misha = main_func('Misha')
    egor = main_func('Egor')
    ivan()
    misha()
    egor()

    add_2 = adder(2)
    add_10 = adder(10)
    print(add_2(5))
    print(add_2(10))
    print(add_10(2))
    print(add_10(10))

    c1 = counter()
    c2 = counter()
    for i in range(5):
        print(f"{i = }", f"{c1() = }")
    print(f"{c1() = }")
    print(f"{c2() = }")


    av1 = average_numbers()
    print(av1(5))
    print(av1(7))
    print(av1(2))

    av2 = average_v2()
    print(av2(5))
    print(av2(7))
    print(av2(2))

    t1 = timer()
    sleep(1)
    print(f"{t1() = }")
    sleep(2)
    print(f"{t1() = }")

    ad2 = counter_func(add2)
    print(ad2(5, 17))
    print(ad2(45, 23))
