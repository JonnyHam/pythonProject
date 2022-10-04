"""

def hi():
    hello = 'hello'
    total = ''
    num = 5
    while num >= 0:
        total += hello + '\n'
        num -= 1
    return total


print(hi())

"""
from typing import Callable, Any


def calculator(f, n1, n2):
    return f(n1, n2)


multiply = lambda n1, n2: n1 * n2
print(calculator(multiply, 5, 4))

add = lambda n1, n2: n1 + n2
print(calculator(add, 5, 4))