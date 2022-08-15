
def sumdigit(digit):
    sum = 0
    while True:
        remainder = digit % 10
        sum += remainder
        digit = digit // 10
        if digit <= 0:
            break

    return sum


cube_list = [i ** 3 for i in range(1, 1000, 2)]

# print(cube_list)

sum = 0
for elem in cube_list:
    if sumdigit(elem) % 7 == 0:
        sum += elem

print('Сумма 1:', sum)

sum = 0
for i in range(len(cube_list)):
    cube_list[i] += 17
    if sumdigit(cube_list[i]) % 7 == 0:
        sum += cube_list[i]

print('Сумма 2:', sum)
