from time import perf_counter
from prettytable import PrettyTable


def filter_list_dict(orig_list):

    result = dict()

    for elem in orig_list:
        result.setdefault(elem, 0)
        result[elem] += 1

    result = [key for key, value in result.items() if value == 1]

    return result


result_table = PrettyTable()
result_table.field_names = ['Действие', 'Результат']
result_table.align['Действие'] = "l"

print('Вычисление.....')

# Проверка правильности
result = [23, 1, 3, 10, 4, 11]
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 2, 4, 11]
result_table.add_row(['Исходный список', src])
result_table.add_row(['Эталон результата', result])
result_table.add_row(['', ''])
result_table.add_row(['Проверка правильности', ''])

# В лоб, первое, что пришло в голову
result_table.add_row(['В лоб', [i for i in src if src.count(i) == 1]])

# Оптимизация
result_table.add_row(['Оптимизация', filter_list_dict(src)])

result_table.add_row(['', ''])

# Замер
result_table.add_row(['Замер производительности', ''])

src = [i for i in range(1, 12 ** 4 + 1)]

# В лоб, плохо тем, что сложность растет экспоненциально
start = perf_counter()
result = [i for i in src if src.count(i) == 1]
result_table.add_row(['В лоб (время): ', perf_counter() - start])

# Оптимизация, вроде как удалось добиться линейности ) но не хватает памяти)
start = perf_counter()
result = filter_list_dict(src)
result_table.add_row(['Оптимизация (время): ', perf_counter() - start])

print(result_table)
