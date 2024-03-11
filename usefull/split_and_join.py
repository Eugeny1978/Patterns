# split - разделить строку на список по элементам
# join - объединить в строку

def inputed_values(string: str) -> list:
    row = string.split()
    form_row = []
    for elem in row:
        try:
            form_row.append(float(elem))
        except:
            form_row.append(elem)
    return form_row

if __name__ == '__main__':

    fio = 'Ivanov Petr  Grigorievich'
    print(f"{fio.split() = }")
    print(f"{fio.split(' ') = }")

    aaa = 'aaaaaaaaa'
    print(f"{aaa.split('a') = }")

    nums = '1,3,6,7,9,22,12'
    print(f"{nums.split(',') = }")

    # elems = inputed_values(input('Введите Элементы:'))
    # print(f"{elems = }")
    #
    # nums2 = input('Введите Целые Числа:').split()
    # nums2_map = map(int, nums2)
    # nums2_list = [int(i) for i in nums2]
    # print(f"{list(nums2_map) = }")
    # print(f"{nums2_list = }")

    # join
    values = [5, 6, 22, -8, 4545, 56 , 23]
    print(f"{values = }")
    print(f"{' '.join(map(str, values)) = }")


