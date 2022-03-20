
def print_price(price_list):
    end = ', '
    for idx, elem in enumerate(price_list):
        ruble = int(elem)
        penny = int((elem - ruble) * 100)
        if idx == len(price_list) - 1:
            end = ''
        print(f'"{ruble} руб {penny:02d} коп"', end=end)
    print()
    print()

price_list = [57.8, 46.51, 97, 115, 0.5, 0.01, 15.06, 1111, 10001.01, 57, 658.00]

print("Исходный список:")
print_price(price_list)

print("Список отсортированный по возрастанию:")
id_before_sort = id(price_list)
price_list.sort()
print_price(price_list)
print("Объект списка изменился после сортировки:", not id_before_sort == id(price_list))

print("Новый список отсортированный по убыванию:")
print_price(sorted(price_list, reverse=True))

print("Топ 5 цен по возрастанию:")  # Список уже отсортирован, берем последние 5
print_price(sorted(price_list[:5:-1]))
