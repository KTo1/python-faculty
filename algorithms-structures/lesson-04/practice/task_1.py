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

"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def func_3(nums):
    pass
    # return [i for i in range(0, len(nums), 2)]


if __name__ == '__main__':
    nums = list(range(10000))
    print(timeit('func_1(nums)', number=1000, globals=globals()))
    print(timeit('func_2(nums)', number=1000, globals=globals()))
    print(timeit('func_3(nums)', number=1000, globals=globals()))

    print(func_1(nums) == func_2(nums) == func_3(nums))
