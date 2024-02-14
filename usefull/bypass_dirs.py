import os
path = 'C:\\Users\\Admin\\Desktop\\Скрины'
slash = '\\'
div_line = '-' * 120

def bypass_dirs_flat(path: str, lst=[]):
    for elem in os.listdir(path):
        lst.append(elem)
        temp_path =  f"{path}\\{elem}"
        if os.path.isdir(temp_path):
            bypass_dirs_flat(temp_path)
    return lst

def bypass_dirs_levels(path: str, level=0):
    dirs = os.listdir(path)
    # folder = path.split(slash)[-1]
    print(f'Folder: {path} ||', dirs, div_line, sep='\n')
    for elem in dirs:
        temp_path = f"{path}\\{elem}"
        if os.path.isdir(temp_path):
            bypass_dirs_levels(temp_path)


if __name__ == '__main__':

    print(bypass_dirs_flat(path), div_line, sep='\n')

    bypass_dirs_levels(path)




