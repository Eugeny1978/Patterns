import openpyxl
from pprint import pprint

# Работа с Файлами Excel
# предварительно установи пакет pip install openpyxl
# Чтобы отображалось Автозаполнение (подсказки по атрибутам и модулям) удали папку помощи по адресу:
# C:\Program Files\JetBrains\PyCharm Community Edition 2023.2\plugins\python-ce\helpers\typeshed\stubs\openpyxl
# И перезагрузи IDE

file = r'files/Prices.xlsx'

pprint(locals())
pprint(dir(openpyxl))


book = openpyxl.load_workbook(file, read_only=True) # ==  openpyxl.open(file, read_only=True)
sheet = book.active

print(sheet["C10"].value) # обратиться через Адрес ячейки
print(sheet[1][0].value) # обратиться через Индексы ячейки: [Строка - нач с 1] [Колонка - нач с 0]
print(sheet[10][2].value) # обратиться через Индексы ячейки: [Строка - нач с 1] [Колонка - нач с 0]

# sheet.max_row

for row in range(7, 85):
    number = sheet[row][0].value
    article = sheet[row][1].value
    name = sheet[row][2].value
    image = sheet[row][3].value
    stock = sheet[row][4].value
    price = sheet[row][5].value
    order = sheet[row][6].value
    print(number, article, name, image, stock, price, order, sep=' | ')
