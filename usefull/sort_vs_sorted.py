# sort - метод списка
# sorted - встроенная функция, аргумент иерируемый объект - возвращает список
# Аргумент key в сортировке
# 1) встроенные функции
# 2) собственные функци
# 3) методы классов
# 4) Анонимные Функции (lambda)
def take_second(elem):
    try:
        return elem[1]
    except:
        return elem[0]

def take_last_num(number):
    """
    Возвращает Последнюю и предпоследнюю Цифры Числа
    """
    return number%10, number//10%10

a = [23, 4, 76, -6, 16, 321]
b = 'hello world'
c = ('hi', 'goodbye', 'abracadabra', 'rich')
d = dict(aaa=1, bbb=2, ccc=3)
f = list(c) + a
print(f)
g = ['aaa 16', 'DDD 38', 'RRR 78', 'ttt 09', 'aaa 98', 'ccc 18.8', 'ccc 025', 'kkk 1.1', 'ZZZ 18.8', 'RRR 98', 'Ggg -6.99']

e = a.copy()
e.sort() # изменяет начальный список
print(e)

sorted(a)
print(a)
a1 = sorted(a)
print(a1)

print(sorted(b))
print(sorted(list(map(str, f)))) # преобразую предварительно числа в строки чб можно было сравнивать и сортировать

print(sorted(c))
print(sorted(c, reverse=True))
# key. Metod 1
print(sorted(a, key=abs))

# key. Metod 2
print(sorted(c, key=take_second)) # сортировка по ключу. По второму символу
print(sorted(a, key=take_last_num)) # сортировка по последней цифре, а при равных последних - по предпоследней

# key. Metod 3
print(sorted(g)) # Заглавные (большие) Буквы всегда идут ранее строчных (малых)
# Можно представить их как все малые или все большие - чтобы при сравнении они были в одном регистре:
print(sorted(g, key=str.lower))
print(sorted(g, key=str.upper))

# key. Metod 4
func = lambda x: float(x.split()[1])
func1 = lambda x: (float(x.split()[1]), x.split()[0])
func2 = lambda x: (float(x.split()[1]), x.split()[0].upper()) # x.upper().split()[0]
print(sorted(g, key=func))
print(sorted(g, key=func1))
print(sorted(g, key=func2))