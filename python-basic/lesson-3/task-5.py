import random


def choice(list_to_random_choice, no_repeat):
    if no_repeat:
        return list_to_random_choice.pop(list_to_random_choice.index(random.choice(list_to_random_choice)))
    else:
        return random.choice(list_to_random_choice)


def get_jokes(count, no_repeat):
    """
    Generate "count" jokes

    :param count: jokes count
    :param no_repeat: no repeat words in jokes
    :return: list contains jokes
    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    if count > len(nouns):
        return "Fun time's over"

    jokes_list = []
    for i in range(count):
        jokes_list.append(f'{choice(nouns, no_repeat)} {choice(adverbs, no_repeat)} {choice(adjectives, no_repeat)}')

    return jokes_list


print(get_jokes(count=3, no_repeat=False))
