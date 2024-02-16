div_line = '-' * 100
from datetime import datetime


print('BLOCK 1 Отображение Числа')
num1: int = 100000000
num2: int = 100_000_000
num3: float = 1e8
num4: int = 100, 000, 000  # некорректно
print(num1, num2, num3, num4, f"{num1:_}", f"{num1:,}", f"{num1: }", sep=' | ')
print(div_line)

print('BLOCK 2 Выравнивание')
var: str = 'var'
print(f"{var:>20}:")  # выравнивание по ПРАВОМУ краю
print(f"{var:20}:")   # выравнивание по ЛЕВОМУ краю
print(f"{var:<20}:")  # выравнивание по ЛЕВОМУ краю
print(f"{var:^20}:")  # выравнивание по ЦЕНТРУ

print(f"{var:_>20}:")  # выравнивание c заполнением
print(f"{var:|<20}:")
print(f"{var:#^20}:")
print(div_line)

print('BLOCK 3 Время')
dt_now: datetime = datetime.now()
print(f"{dt_now:%d.%m.%Y %H:%M:%S}") # можно играться различными форматами
print(f"{dt_now:%c}")
print(f"{dt_now:%I%p}")
print(div_line)

print('BLOCK 4 Округление')
num: float = 13456.676574355585303
print(f"{num:.3f}")
print(f"{num:,.3f}")
print(div_line)

print('BLOCK 5 Отладка')
a: int = 5
b: int = 10
txt: str = 'Bob says, Hi'
print(f"a + b = {a+b}")
print(f"{a + b = }")
print(f"{txt = }")