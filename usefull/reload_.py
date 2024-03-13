from importlib import reload
from pprint import pprint
import files.my_module as my_module

print(my_module.s)
my_module.s = 100
print(my_module.s)
my_module.zzz = 333 # новая переменная - !
print(my_module.zzz)
reload(my_module) # перезагрузка - импорт снова! с восстановлением значений!
# Однако если я отсюда добавлю Новые переменные в то простанство имен (см. zzz) - оно при перезагрузке Останется
print(my_module.s)
print(my_module.zzz)

print(my_module.math.pi) # обращение к переменной, импортированной в импортированном модуле
pprint(locals())
pprint(dir(my_module))
pprint(dir(my_module.math))