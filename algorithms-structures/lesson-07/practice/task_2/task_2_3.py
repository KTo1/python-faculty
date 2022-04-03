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

"""
Встроенная функция:
10 + 1 элемент: 0.0005252000000000034
100 + 1 элемент: 0.004054399999999986
1000 + 1 элемент: 0.0835871
"""

"""
ВЫВОДЫ:
Встроенная функция опять оказалась быстрее, думаю тут два фактора: это реализация не на питоне и алгоритм, 
сам алгоритм встроенной функции я не нашел и не разобрал, но думаю сейчас пока это и не требуется.   
Далее идет сортировка кучей(O(nlog (n))) и без сортировки (O(n^2)), на малых объемах алгоритм без сортировки оказывается
быстрее, но с увеличением числа элементов сложность дает о себе знать) алгоритм проигрывает. 

Как резюме: стоит использовать встроенную функцию.
"""

from random import randint
from timeit import timeit
from statistics import median


if __name__ == '__main__':
    m = 5
    original_array = [randint(-100, 99) for i in range(2 * m + 1)]
    print(timeit('median(original_array)', number=1000, globals=globals()))

    m = 50
    original_array = [randint(-100, 99) for i in range(2 * m + 1)]
    print(timeit('median(original_array)', number=1000, globals=globals()))

    m = 500
    original_array = [randint(-100, 99) for i in range(2 * m + 1)]
    print(timeit('median(original_array)', number=1000, globals=globals()))