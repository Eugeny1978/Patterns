# \\ - экранируется \
# \' - экранируется '
# \" - экранируется "
# \a - звонок
# \b - забой
# \f - перевод формата
# \n - новая строка
# \r - перевод каретки
# \t - горизонтальная табуляция
# \v - вертикальная табуляция

div_line = '-' * 120
symbols = ['\\', '\'', '\"', '\a', '\b', '\f', '\n', '\r', '\t', '\v']

def dprint(*args):
    print(*args, div_line, sep='\n')

# for symb in symbols:
#     print(symb)

# Чтобы не происхожило такого ИНОГДА НЕЖЕЛАТЕЛЬНОГО Экранирования
# Например, при ссылок на путь к файлам и папкам. Перд строкой необходимо добавить r:
noncorrect_path = 'F:\new_music\tommorow'
correct_path = r'F:\new_music\tommorow'
dprint(f"{noncorrect_path = }", noncorrect_path, f"{len(noncorrect_path) = }")
dprint(f"{correct_path = }", correct_path, f"{len(correct_path) = }")



