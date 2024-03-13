print('Run "package1.__init__"')

# from .file1 import *
# from .file2 import *

from . import file1, file2
from .. import my_module
from ... import dataframes_filter
# Чтобы не получить ошибки, типа ниже необходимо разобрться глубже!
# ImportError: attempted relative import beyond top-level package
# ImportError: attempted relative import with no known parent package

# .   - текущий каталог
# ..  - каталог на 1 уровень выше
# ... - каталог на 2 уровня выше
# и тд