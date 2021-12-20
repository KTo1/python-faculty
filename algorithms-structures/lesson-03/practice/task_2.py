"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api

У нас на курсе БД была задача по Redis.
"""

import redis
from random import randint
from hashlib import sha256


def validate(password, vault):
    salt = vault.get(password)
    if salt:
        return vault.get(password + salt) == sha256(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()
    else:
        salt = str(randint(1, 100000))
        hash = sha256(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()
        vault.set(password, salt)
        vault.set(password + salt, hash)
        return hash


if __name__ == '__main__':
    vault = redis.StrictRedis(host='192.168.25.108',
                              port=6379,
                              password='',
                              charset='utf-8',
                              decode_responses=True)

    password = input('Введите пароль: ')
    print(validate(password, vault))
    password = input('Введите пароль еще раз для проверки: ')
    print(f'Вы ввели {"верный" if validate(password, vault) else "неверный"} пароль')