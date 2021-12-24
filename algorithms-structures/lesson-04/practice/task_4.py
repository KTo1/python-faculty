"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

"""
ВЫВОДЫ:
оба предлагаемых решения имеют сложность О(n^2) и даже просто переписав на линейную сложность мы получаем 
выигрыш в производительности.
 
"""

from timeit import timeit


array = [1, 3, 1, 3, 4, 5, 1]
# array = [1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    m, num = 0, 0
    dct = {}
    for i in array:
        dct.setdefault(i, 0)
        dct[i] += 1

    for k, v in dct.items():
        if v > m:
            m, num = v, k

    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_4():
    m, num = 0, 0
    dct = {}
    for i in array:
        dct.setdefault(i, 0)
        dct[i] += 1

    for k, v in dct.items():
        if v > m:
            m, num = v, k

    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


if __name__ == '__main__':
    print(timeit('func_1()', number=100000, globals=globals()))
    print(timeit('func_2()', number=100000, globals=globals()))
    print(timeit('func_3()', number=100000, globals=globals()))
    print(timeit('func_4()', number=100000, globals=globals()))

    print(func_1())
    print(func_2())
    print(func_3())