"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Нужно написать функцию-рекурсию только для левой части выражения!
Результат нужно сверить с правой частью.

Решите через рекурсию. Решение через цикл не принимается.
"""


def sum_recursion(n):
    if n <= 0:
        return 0
    return n + sum_recursion(n - 1)


if __name__ == '__main__':
    n = 5
    print(f'n = {n}, сумма рекурсией: {sum_recursion(n)}, сумма по формуле (n(n+1)/2): {n * (n + 1) / 2}')
    n = 100
    print(f'n = {n}, сумма рекурсией: {sum_recursion(n)}, сумма по формуле (n(n+1)/2): {n * (n + 1) / 2}')
    n = 23
    print(f'n = {n}, сумма рекурсией: {sum_recursion(n)}, сумма по формуле (n(n+1)/2): {n * (n + 1) / 2}')
