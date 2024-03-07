
# Преимущества Генератора перед map -
# 1. можно использовать зип и одновременно использовать несколько переменных
# 2. обычно быстрее отрабатывает

def my_func(x): # должна примнимать только одно значение
    return x**2

def my_func2(x, y):
    return x+y

class Words:

    def __init__(self, name):
        self.name = name

    def hi(self):
        return 'Hi, ' + self.name

    def goodbye(self):
        return 'Goodbye, ' + self.name

div_line = '-'*120
lst = [3, 5, -2, 14, 52, 17, -6]
lst2 = [1, 2, -4, 7, 3, 7, -17]
strings = ['Gala', 'Anna', 'Tolya', 'Bob','Zack', 'George']
names = [Words('Gala'), Words('Tolya'), Words('Alena')]



if __name__ == "__main__":

    mp = list(map(lambda x: x+5, lst))
    mpa = list(map(abs, lst))
    mp_analog = [i+5 for i in lst]
    mpa_analog = [abs(i) for i in lst]
    mf = list(map(my_func, lst))
    # mf2 = list(map(my_func2, zip(lst, lst2))) # неправильно
    mf2_analog = [x+y for x, y in zip(lst, lst2)]
    print(f"{lst = }")
    print(f"{mpa = }")
    print(f"{mpa_analog = }")
    print(f"{mp = }")
    print(f"{mp_analog = }")
    print(f"{mf = }")
    # print(F"{mf2 = }")
    print(f"{mf2_analog = }")

    s1 = list(map(str.upper, strings)) # применять методы объектов
    print(s1)
    s2 = list(map(Words.hi, names))
    print(f"{names = }")
    print(f"{s2 = }")

    map_names = list(map(lambda name: Words(name), strings))
    gb = list(map(Words.goodbye, map_names))
    print(f"{gb = }")

    l1 = list(map(list, strings))
    sorted_l1 = list(map(sorted, l1))
    print(f"{l1 = }")
    print(f"{sorted_l1 = }")

    # Ввод нескольких значений - и сохранение их в виде списка
    print(div_line)
    l2 = list(map(float, input('Input the numbers separated by a space: ').split()))
    print(l2, div_line, sep='\n')

