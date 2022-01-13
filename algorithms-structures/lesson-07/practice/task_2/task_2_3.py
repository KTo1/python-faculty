"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""
from random import randint
from timeit import timeit
from statistics import median


def time_it(m):
    original_array = [randint(-100, 99) for i in range(2*m + 1)]
    print(f'Массив длиной {2*m + 1} элементов')
    print(timeit('median(array.copy())', setup='array = original_array.copy()', number=100000, globals=globals()))


if __name__ == '__main__':
    time_it(5)
    time_it(50)
    time_it(500)
