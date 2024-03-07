# sort - метод списка
# sorted - встроенная функция, аргумент иерируемый объект - возвращает список

def take_second(elem):
    try:
        return elem[1]
    except:
        return elem[0]

a = [23, 4, 76, -6, 16, 321]
b = 'hello world'
c = ('hi', 'goodbye', 'abracadabra', 'rich')
d = dict(aaa=1, bbb=2, ccc=3)
f = list(c) + a
print(f)

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
print(sorted(c, key=take_second)) # сортировка по ключу. По второму символу
print(sorted(c, reverse=True))





