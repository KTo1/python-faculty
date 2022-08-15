
for i in range(1, 101):
    remainder = i % 10
    x = int(i / 100)
    x1 = 100 * x + 11
    x2 = 100 * x + 19

    if i == 0:
        ending = "ов"
    elif remainder == 0 or remainder >= 5 or i >= x1 and i <= x2:
        ending = "ов"
    elif remainder == 1:
        ending = ""
    else:
        ending = "а"

    print(f"{i} процент{ending}")