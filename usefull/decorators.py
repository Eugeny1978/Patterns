# ДЕКОРАТОРЫ

from functools import wraps # декоратор, Способ не потерять имя и справку по декорируемой функции

def say_hello(name, surname):
    print('Hello', surname, name)

def say_bye(name, surname):
    print('Bye', surname, name)

def decorator(func):
    def inner(*args, **kwargs):
        print('Start Decorator...')
        func(*args, **kwargs)
        print('Finish Decorator.')
    return inner

def header(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')
    # Способ не потерять имя и справку по декорируемой функции
    # inner.__name__ = func.__name__
    # inner.__doc__ = func.__doc__
    return inner

def table(func):
    @wraps(func) # Способ не потерять имя и справку по декорируемой функции с помощью готового втроенного декоратора
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')
    # inner.__name__ = func.__name__
    # inner.__doc__ = func.__doc__
    return inner

@header # == header(table(set_text))
@table
def set_text(text: str):
    """
    Documentation set_text
    """
    print(text)



if __name__ == '__main__':

    say_hello = decorator(say_hello)
    say_hello('Nikolay', 'Botvinnik')
    say_bye = decorator(say_bye)
    say_bye('Boris', 'Karaganov')

    # set_text = header(table(set_text)) # см декорирование выше
    set_text('Any Text')
    print(set_text.__name__)
    print(set_text.__doc__)


