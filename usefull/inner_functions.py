g = 'gray'

def dprint(*args):
    print(*args, sep=' | ')

def colors(param='r'):

    y = 'yellow'
    g = 'green'

    def print_red():
        nonlocal y
        r = 'red'
        dprint(r, y, g)
        y = 'y was changed'

    def print_blue():
        b = 'blue'
        dprint(b, y, g)


    if param == 'r':
        print_red()
    elif param == 'b':
        print_blue()
    else:
        print("I don't know this colour")




if __name__ == '__main__':

    colors()
    colors('b')
    colors('g')