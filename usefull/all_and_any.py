
def any_all_func(value, func='any'):
    cond1 = value%2 == 0
    cond2 = value > 0
    cond3 = value%10 == 0
    conds = (cond1, cond2, cond3)
    if func == 'any':
        return any(conds)
    elif func == 'all':
        return all(conds)
    else:
        print("Допускается применение функций только 'any' или 'all'.")



if __name__ == '__main__':

    print(any_all_func(250))
    print(any_all_func(-36, 'all'))
    print(any_all_func(120, func='rrr'))

