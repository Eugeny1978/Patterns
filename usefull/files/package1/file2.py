# можно явно указать какие именно имено могут быть импортированы
# Работает только Если в __init__ импортируем .file2 import *.
__all__ = ['func21']

f21 = 44

def func21():
    print('RRRR')