def more_10(x):
    # return True if x > 10 else False
    return x > 10



lst = [3, 5, -2, 14, 52, 17, -6, 12, 56, -7, 8, 9, 3]
lst2 = [3, 5, 7,'' , 'tttRRR', -2, 14, 0, 17, -6, 0, '', 12, 'wwwQQQ', 56, [], 0, [0, 2], 3]
longstring = '45 rjkjkj5ljljl5HTjl;rk;lWMk0ih0- -hf -h-PP -9yu-09yM-90-y9u-r'
cities = dict(moscow=1023, london=987, riga=129, samara=174, berlin=802)

if __name__ == '__main__':

    f1 = list(filter(more_10, lst))
    f2 = list(filter(lambda x: x > 10, lst))
    comp1 = [i for i in lst if i > 10]
    f3 = list(filter(bool, lst2))
    f3_analog = list(filter(None, lst2)) # передал None - аналогично как передать bool
    print(f"{f1 = }")
    print(f"{f2 = }")
    print(f"{comp1 = }")
    print(f"{f3 = }")
    print(f"{f3_analog = }")

    f4 = list(filter(str.isalpha, longstring))
    f5 = list(filter(str.isdigit, longstring))
    f6 = list(filter(str.isdecimal, longstring))
    f7 = list(filter(str.isupper, longstring))
    f8 = list(filter(str.islower, longstring))
    print(f"{f4 = }", f"{f5 = }", f"{f6 = }", f"{f7 = }", f"{f8 = }", sep='\n')

    # Фильтр Словаря:
    f9 = (list(filter(lambda x: cities[x] > 100, cities)))
    print(f"{f9 = }")
