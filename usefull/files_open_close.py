# Работа с Файлами

path = r'files/my_file.txt'
# Для быстрого копирования более полного пути ПКМ на этом файле в Pycharm Copy Path/

end = ''

file = open(path, encoding='utf-8') # mode='r+w'
# info = file.read(10) # read(10) - кол-во прочитанных символов
# print(info)
# print(len(info))

print(file.read(10))
print(file.read(10)) # начинает с того места где остановился

# Чтобы откатиться назад:
file.seek(0)
print(file.read(10))

# Считывание По строкам:
file.seek(0)
print(file.readline(), end=end)
print(file.readline())

# Обойти все строки
file.seek(0)
for row in file:
    print(row, end=end)
print()

# Сохранение текста файла в виде списка, каждый элемент - строка
file.seek(0)
rows = file.readlines()
print(rows)

# Читабелен или нет файл
file.readable()

# Запись в файл
file = open(path, mode='a', encoding='utf-8')
file.write('\n')
file.write('Add 1 info by file.write\n')
file.write('Add 2 info by file.write\n')

file = open(path, encoding='utf-8')
print(file.read())

file = open(path, mode='a+', encoding='utf-8')
file.write('Add 3 info by file.write\n')
file.write('Add 4 info by file.write\n')
file.seek(0)
print(file.read())

file.close() # закрываем файл

# чтобы происходило автоматическое закрытие
# использую конструкцию with



