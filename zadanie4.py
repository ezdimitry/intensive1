"""Медведев Дмитрий Алексеевич, 1 вариант
Напишите функцию для нахождения НОД произвольного количества чисел.
код задачи 13"""


from functools import reduce
import math

def NOD(*numbers):
    return reduce(math.gcd, numbers)


num = [6, 36, 18, 12]
result = NOD(*num)
print(result)