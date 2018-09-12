# Задача: Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

import sys


def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')


a = "Если ввести символ '0', то ввод чисел будет завершен"
print(a)
show_size(a)
# type = <class 'str'>, size = 142, object = Если ввести символ '0', то ввод чисел будет завершен

b = "Ведите натуральное число: "
show_size(b)
# type = <class 'str'>, size = 90, object = Ведите натуральное число:

n = int(input(b))
show_size(n)
# type = <class 'int'>, size = 14, object = 456

max_s = 0
show_size(max_s)
# type = <class 'int'>, size = 12, object = 0

max_m = 0
show_size(max_m)
# type = <class 'int'>, size = 12, object = 0

while n != 0:
    m = n
    show_size(m)
    # type = <class 'int'>, size = 14, object = 456
    s = 0
    show_size(s)
    # type = <class 'int'>, size = 12, object = 0
    while n > 0:
        s += n % 10
        show_size(s)
        # type = <class 'int'>, size = 14, object = 6
        n //= 10
        show_size(n)
    if s > max_s:
        max_s = s
        show_size(max_m)
# type = <class 'int'>, size = 14, object = 45
# type = <class 'int'>, size = 14, object = 11
# type = <class 'int'>, size = 14, object = 4
# type = <class 'int'>, size = 14, object = 15
# type = <class 'int'>, size = 12, object = 0

    k = int(input(b))
    show_size(k)
    # type = <class 'int'>, size = 12, object = 0

c = "Число имеет максимальную сумму цифр: "
show_size(c)
# type = <class 'str'>, size = 112, object = Число имеет максимальную сумму цифр:

print(f"Число {max_m} имеет максимальную сумму цифр: {max_s}")
show_size((sys.getsizeof(a) + sys.getsizeof(b) + sys.getsizeof(n)+ sys.getsizeof(max_s) + sys.getsizeof(max_m) +
           sys.getsizeof(s) + sys.getsizeof(m) + sys.getsizeof(k)))
# type = <class 'int'>, size = 14, object = 312
