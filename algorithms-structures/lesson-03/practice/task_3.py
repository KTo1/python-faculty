"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.

Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""
from hashlib import sha256

def count_u_substring(str):
    _ = set()
    for i in range(1, len(str)):
        for j in range(len(str) - i + 1):   # до конца строки не обязательно доходить
            _.add(sha256(str[j:j + i].encode('utf-8')).hexdigest())
    return len(_)


if __name__ == '__main__':
    str = 'pap'
    print(f'{str} - {count_u_substring(str)} уникальных подстрок')
    str = 'papa'
    print(f'{str} - {count_u_substring(str)} уникальных подстрок')
    str = 'asdasdasdgpogeoiumwoig'
    print(f'{str} - {count_u_substring(str)} уникальных подстрок')