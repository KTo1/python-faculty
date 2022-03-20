# Подумайте: полезен ли будет вам оператор распаковки?
#   Может если мы будем использовать вместо горы параметров список?
# Как поступить, если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?
#   Думаю зависит задачи, зачем вообще сортировка? Можно сортировать ключи, потом по этим ключам обращаться

def thesaurus(dict_names, *names):
    for name in names:
        dict_names.setdefault(name[0].upper(), []).append(name)

    return dict_names


def thesaurus_adv(*full_names):
    dict_full_names = dict()
    for full_name in full_names:
        first_char = full_name.split(' ')[1][0].upper()
        dict_full_names.setdefault(first_char, thesaurus(dict(), full_name)).update(thesaurus(dict_full_names[first_char], full_name))

    return dict_full_names


# print(thesaurus(dict(), "Петр G", "Иван B", "Мария", "Илья"))
print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
print(type(-5+4j))

