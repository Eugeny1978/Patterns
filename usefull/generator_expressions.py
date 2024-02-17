div_line = '-' * 100

# Генератор Списка
lst = [x**2 for x in range(1,6)]
# Чтобы превратить в итератор необходимо:
lst_iter = iter(lst)
print(next(lst_iter))
print(next(lst_iter))
print(next(lst_iter))
print(div_line)


# Генератор Выражения
# Является уже Итератором можно сразу применить функ next()
# Элементы можно обойти ТОЛЬКо 1 раз
# Полезны при большом кол-ве элементов. Позволяют избежать Ошибки недостаточноти Памяти.
# expr = (x**2 for x in range(1,1_000_000_000))
# len(expr), expr[2] # нельзя применить тк элементы подгружаются динамически
expr = (x**2 for x in range(1,6))
print(next(expr)) # 1й
print(next(expr)) # 2й
print(next(expr)) # 3й
print(sum(expr)) # 41 - тк остались только 2 значения
print(sum(expr)) # = 0  - тк не остались значений

