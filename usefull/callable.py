# Вызываемые объекты - используются круглые скобки ()


# 1. Встроенные Функции (классы)
value = 345.54
sss = 'Hello, World!'

print(callable(int))
print(callable(str))
print(int(value))
print(str(value))
print(callable(value)) # переменные не вызываемы
# value() # TypeError: 'float' object is not callable


# 2. Методы встроенных классов
print(callable(sss.upper))
print(sss.upper())

# 3. Собственные Функции ( в том числе lambda)
def hello_print():
    print('Hello')

hi = lambda : 'Hi'

print(callable(hello_print))
hello_print()

print(callable(hi))
print(hi())


# 4. Классы и 5. их методы

class Cat:
    def __call__(self, *args, **kwargs):
        """
        Функция для того чтобы сделать объект этого класса тоже вызываемым
        """
        print('may')


class Dog:
    def gaf(self):
        print('gafff')


mursik = Cat()
muhtar = Dog()

print(callable(Cat))
print(callable(Dog))
print(callable(mursik))
print(callable(muhtar))
mursik() # == mursik.__call__()
muhtar.gaf()

# 6. Функции Генераторы

def yield_func():
    n = 0
    while True:
        yield n
        n += 1

print(callable(yield_func))
