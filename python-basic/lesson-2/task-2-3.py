
def is_int_digit(str_digit):
    for i in str_digit:
        code = ord(i)
        if (code < 48 or code > 57) and code != 43 and code != 45:
            return False
    return True


some_list = ['в', '5', 'часов', '17', 'минут', '+5.0', 'температура', 'воздуха', 'была', '+5', 'градусов', '-1']

for i in range(len(some_list) - 1, -1, -1):
    word = some_list[i]
    if is_int_digit(word):
        sing, length = '', '02d'
        if word[0] == '-':
            length = '03d'
        elif word[0] == '+':
            sing = '+'

        some_list[i] = f'{sing}{int(word):{length}}'

        some_list.insert(i + 1, '>"')
        some_list.insert(i, '"<')

print(' '.join(some_list).replace('"< ', '"').replace(' >"', '"').capitalize())

