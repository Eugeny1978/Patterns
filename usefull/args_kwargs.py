separs = ' || '
div_line = '-' * 72


def func_args(*args):  # упаковка значений
    print(div_line)
    index = 1
    for i in args:
        end = separs if index != len(args) else ' '
        print(i, end=end)
        index += 1
    print(f"\n{args} {type(args)}")
    print(div_line)


def func_kwargs(**kwargs):
    print(div_line)
    for key, value in kwargs.items():
        print(f"{key=} {value=}")
    print(kwargs, type(kwargs))
    print(div_line)

def func_args_kwargs(*args, **kwargs): # сначала Неименованные параметры, потом Именованные
    print(div_line)
    print(args, sep=separs)
    print(kwargs, sep=separs)
    print(div_line)


if __name__ == '__main__':

    a, b, c = [43, 77, 18]  # больше или меньше аргументов выдаст ошибку!
    print(a, b, c, sep=separs)
    try:
        a, b, c = [43, 77, 18, 45]
    except Exception as error:
        print(error)
    try:
        a, b, c = [43, 77]
    except Exception as error:
        print(error)

    # "распаковка" значений
    lst = [43, 77, 18, 45, 'hello', 455]
    a, *b, c = lst
    print(a, b, c, sep=separs)
    *d, = lst
    (print(d, sep=separs))
    d = *lst,  # Интересный способ преобразовать в кортеж
    print(d, sep=separs)
    *a, b, c, d = [43, 27, 34]  # в а окажется пустой список
    print(a, b, c, d, sep=separs)

    args = [2, 11, 2]
    print(list(range(*args)))

    # "упаковка" значений
    func_args(4, 55, 23, 'sss', True)

    func_kwargs(www=44, rrr=76, ttt=90)

    func_args_kwargs(22, 1, 76, dd=5, ss=78, uu=12)
