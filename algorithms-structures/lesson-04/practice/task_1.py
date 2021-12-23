"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

"""
ВЫВОДЫ:
чтобы найти все индексы с нечетными значениями, в любом случае нужно обойти весь список, поэтому я вижу 
оптимизацию только в алгорите вычисления четности 

"""

from timeit import timeit
from random import randint


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


if __name__ == '__main__':
    nums = [randint(0, 10000) for i in range(10000)]

    print(timeit('func_1(nums)', number=1000, globals=globals()))
    print(timeit('func_2(nums)', number=1000, globals=globals()))

    print(func_1(nums) == func_2(nums))
    # print(nums)
    # print(func_1(nums))
    # print(func_2(nums))
    # print(func_3(nums))

