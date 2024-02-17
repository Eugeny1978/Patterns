div_line = '-' * 100
lst = [22, 44, 66, 44, 77]


def func():
    return lst


def gen_func():
    sss = 5
    for i in lst:
        yield i
        print(f'Продолжаем Работу. Внутренняя Переменная {sss = }')
        sss += 10


def get_factorial(n: int) -> int:
    if n < 1: return [0]
    if n == 1: return [1]
    facts = [1]
    for i in range(2, n + 1):
        facts.append(facts[-1] * i)
    return facts


def get_factorial_2(n):
    pr = 1
    facts = []
    for i in range(1, n + 1):
        pr *= i
        facts.append(pr)
    return facts


def get_generator_factorial(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= i
        yield pr


if __name__ == '__main__':

    # fn = func()
    # gf = gen_func()
    #
    # print(fn)
    # print(fn)
    # print(gf)
    # print(next(gf))
    # print(next(gf))
    # print(div_line)
    #
    # for i in gen_func():
    #     print(i)

    # print(f"{get_factorial(7)=}")
    # print(f"{get_factorial_2(7)=}")
    # print(f"{get_factorial(0)=}")
    # print(f"{get_factorial_2(0)=}")
    # print(f"{get_factorial(1)=}")
    # print(f"{get_factorial_2(1)=}")
    # print(f"{get_factorial(2)=}")
    # print(f"{get_factorial_2(2)=}")

    i = 1
    for fact in get_generator_factorial(7):
        print(f"Factorial {i} = {fact}")
        i += 1
