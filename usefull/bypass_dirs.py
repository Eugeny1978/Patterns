import os
path = 'C:\\Users\\Admin\\Desktop\\Скрины\\'

def bypass_dirs_flat(path: str, lst=[]):
    for elem in os.listdir(path):
        lst.append(elem)
        temp_path =  f"{path}\\{elem}"
        if os.path.isdir(temp_path):
            bypass_dirs_flat(temp_path)
    return lst

def bypass_dirs_levels(path: str, level=0):
    # text = f" || {level = }"
    # if len(multitude):
    #     print(*multitude, text)
    # else:
    #     print('Пусто', text)
    # for value in multitude:
    #     if isinstance(value, (list, tuple, set)):
    #         bypass_nested_lists(value, level=level + 1)
    pass



if __name__ == '__main__':

    # print(os.listdir(path))

    print(bypass_dirs_flat(path))



