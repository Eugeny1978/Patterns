a, b = int(input('Первое Число = ')), int(input('Второе Число = '))

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a



print('Наибольший Общий Делитель =', a)