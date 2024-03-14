"""
Принятые Соглашения (форматы) оформления документирования Кода
Менять Формат можно:
Settings / Python Integrated Tools / Docstring Format - выбрать из выпадающего списка
По умолчанию reStructuredText
Мне понравился стиль Numpy (см ниже)
Можно документировать:
Модули
Классы
Функции
"""

from typing import Literal
import pandas as pd
Marks = Literal['light', 'dark', 'blue']

def any_function(data:dict, adder:int=100, mark:Marks='light') -> pd.DataFrame:
    """
    Function convert dict-data into DataFrame (table)
    Parameters
    ----------
    data
    adder
    mark

    Returns
    -------

    """
    return pd.DataFrame(data)

if __name__ == '__main__':

    help(any_function) # Полностью информация!
    print(any_function.__doc__) # Только docstring
    # help(pd)




