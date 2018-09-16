# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Задача: Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

import sys


def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')


p = 'Введите три числа:'
print(p)
show_size(p)
# type = <class 'str'>, size = 74, object = Введите три числа:

a = int(input("a = "))
show_size(a)
# type = <class 'int'>, size = 14, object = 5

b = int(input("b = "))
show_size(b)
# type = <class 'int'>, size = 14, object = 6

c = int(input("c = "))
show_size(c)
# type = <class 'int'>, size = 14, object = 7

m = 'Среднее:'
show_size(m)
# type = <class 'str'>, size = 54, object = Среднее:

if (b < a < c) or (c < a < b):
    print(m, a)
elif (a < b < c) or (c < b < a):
    print(m, b)
else:
    print(m, c)

show_size((sys.getsizeof(p) + sys.getsizeof(a) + sys.getsizeof(b)+ sys.getsizeof(c) + sys.getsizeof(m)))
# type = <class 'int'>, size = 14, object = 170
