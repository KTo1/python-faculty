
def num_translate_adv(word):
    words = {
        'ONE': 'ОДИН',
        'TWO': 'ДВА',
        'THREE': 'ТРИ',
        'FOUR': 'ЧЕТЫРЕ',
        'FIVE': 'ПЯТЬ',
        'SIX': 'ШЕСТЬ',
        'SEVEN': 'СЕМЬ',
        'EIGHT': 'ВОСЕМЬ',
        'NINE': 'ДЕВЯТЬ',
        'TEN': 'ДЕСЯТЬ'
    }

    if word.upper() in words:
        return words[word.upper()].capitalize()
    else:
        return None


print(num_translate_adv('one'))
print(num_translate_adv('oNe'))
print(num_translate_adv('onE'))
print(num_translate_adv('oNE'))

print(num_translate_adv('oNE1'))

