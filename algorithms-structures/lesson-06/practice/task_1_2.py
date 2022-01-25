"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для второго скрипта
"""

"""
Курс основ, урок 5, задание 4

Оптимизация используя генератор. 
 
Результаты и выводы:

Собственно задача в этом и заключалась: оптимизировать по памяти. 
В первом варианте lc, во втором генератор

До:    61.1 MiB      0.0 MiB           1       print(result)
После: 57.3 MiB      0.0 MiB           1       print(result)

в случае с генератором приращение настолько мало, что считается нулем.     
"""

from random import randint
from memory_profiler import profile


@profile
def make_list():
    # Cписком
    result = [elem for idx, elem in enumerate(src) if elem > src[idx-1] and idx > 0]
    print(result)


@profile
def make_generator():
    # Оптимизация по памяти, генератором
    result = (elem for idx, elem in enumerate(src) if elem > src[idx-1] and idx > 0)
    print(result)


if __name__ == "__main__":
    src = [randint(0, 100000) for i in range(1000000)]

    make_list()
    make_generator()
