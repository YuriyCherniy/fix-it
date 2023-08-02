# 1
# Смысл функции я понял так:
# Функция принимает строку вида "string-to_camel-case"
# и возвращает stringToCamelCase, строка начинается 
# с маленькой буквы

import re

def to_camel_case(text):
    result = ''
    for word in re.split('_|-', text)[1::]:
        result += word.title()
    return re.split('_|-', text)[0] + ''.join(result)


# 2
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


# 3
count_bits = lambda n: bin(n).count('1')


# 4
def digital_root(n):
    if n < 10:
     return n
    else:
     return digital_root(sum(map(int, str(n))))


# 5
even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"
