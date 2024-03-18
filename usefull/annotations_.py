"""
Any - любой тип данных
Optional - либо тот что указан либо None (пустой)
Union - объединение типов с версии Питон 3.10 аналогично int | float | str
Literal - список возможных Значений

"""

from typing import List, Dict, Literal, Any, Optional, Union

Vals = Literal['first', 'second', 'third']

aaa: dict[str, int] = {'rrr': 555, 'ttt': 888}
bbb: Any = 444
bbb = 'rtrtrt'




def sum_numbers(a: int | float | str, b: int | float | str) -> int:
    return a + b


def list_upper(lst: List[str], dct: Dict[str, int], v: Vals):
    for elem in lst:
        print(elem.upper())
    for key, value in dct.items():
        print(key, '=', value)


if __name__ == '__main__':
    print(sum_numbers(55, 66))
    print(sum_numbers('hello', ' world'))
    print(sum_numbers([2, 5, 7], [6, 3]))
    print(sum_numbers.__annotations__)
    print(list_upper(['ttt', '444'], {'fff': 44, 'eee': 666}, 'second'))
