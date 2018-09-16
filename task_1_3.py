# Задача: Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import random
import sys


def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')


def show_size_1(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'item'):
            for y in x.items():
                show_size(y, level + 1)
    elif not isinstance(x, str):
        for y in x:
            show_size(y, level + 1)


M = 5
show_size(M)
# type = <class 'int'>, size = 14, object = 5

N = 4
show_size(N)
# type = <class 'int'>, size = 14, object = 4

arr = []
show_size_1(arr)
# type = <class 'list'>, size = 36, object = []

a = "В следующей матрице:"
print(a)
show_size(a)
# type = <class 'str'>, size = 78, object = В следующей матрице:

for i in range(N):
    tmp = []
    for j in range(M):
        num = int(random() * 100)
        tmp.append(num)
        # print(f"\t{num}", end='')
        arr.append(tmp)
        show_size(num)
        show_size_1(tmp)
    print()
# type = <class 'int'>, size = 14, object = 7
#  type = <class 'list'>, size = 52, object = [7]
#  type = <class 'int'>, size = 14, object = 94
#  type = <class 'list'>, size = 52, object = [7, 94]
#  type = <class 'int'>, size = 14, object = 52
#  type = <class 'list'>, size = 52, object = [7, 94, 52]
#  type = <class 'int'>, size = 14, object = 10
#  type = <class 'list'>, size = 52, object = [7, 94, 52, 10]
#  type = <class 'int'>, size = 14, object = 67
#  type = <class 'list'>, size = 68, object = [7, 94, 52, 10, 67]
#
#  type = <class 'int'>, size = 14, object = 86
#  type = <class 'list'>, size = 52, object = [86]
#  type = <class 'int'>, size = 14, object = 14
#  type = <class 'list'>, size = 52, object = [86, 14]
#  type = <class 'int'>, size = 14, object = 26
#  type = <class 'list'>, size = 52, object = [86, 14, 26]
#  type = <class 'int'>, size = 14, object = 64
#  type = <class 'list'>, size = 52, object = [86, 14, 26, 64]
#  type = <class 'int'>, size = 14, object = 6
#  type = <class 'list'>, size = 68, object = [86, 14, 26, 64, 6]
#
#  type = <class 'int'>, size = 14, object = 87
#  type = <class 'list'>, size = 52, object = [87]
#  type = <class 'int'>, size = 14, object = 85
#  type = <class 'list'>, size = 52, object = [87, 85]
#  type = <class 'int'>, size = 14, object = 11
#  type = <class 'list'>, size = 52, object = [87, 85, 11]
#  type = <class 'int'>, size = 14, object = 38
#  type = <class 'list'>, size = 52, object = [87, 85, 11, 38]
#  type = <class 'int'>, size = 14, object = 83
#  type = <class 'list'>, size = 68, object = [87, 85, 11, 38, 83]
#
#  type = <class 'int'>, size = 14, object = 43
#  type = <class 'list'>, size = 52, object = [43]
#  type = <class 'int'>, size = 14, object = 65
#  type = <class 'list'>, size = 52, object = [43, 65]
#  type = <class 'int'>, size = 14, object = 94
#  type = <class 'list'>, size = 52, object = [43, 65, 94]
#  type = <class 'int'>, size = 14, object = 66
#  type = <class 'list'>, size = 52, object = [43, 65, 94, 66]
#  type = <class 'int'>, size = 14, object = 62
#  type = <class 'list'>, size = 68, object = [43, 65, 94, 66, 62]

show_size_1(arr)
# type = <class 'list'>, size = 136, object = [[7, 94, 52, 10, 67], [7, 94, 52, 10, 67], ...]

mx = -1
show_size(mx)
# type = <class 'int'>, size = 14, object = -1

for j in range(M):
    mn = 100
    show_size(mn)
    # type = <class 'int'>, size = 14, object = 100
    for i in range(N):
        if arr[i][j] < mn:
            mn = arr[i][j]
    if mn > mx:
        mx = mn
c = "максимальный элемент среди минимальных элементов столбцов матрицы:"
show_size(c)
# type = <class 'str'>, size = 170, object = максимальный элемент среди минимальных элементов столбцов матрицы:
print(c, mx)
