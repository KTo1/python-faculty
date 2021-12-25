a, b = int(input()), int(input())
result = [i for i in range(a, b + 1)]
for i in range(a, int(b ** 0.5) + 1):
    if i == 1:
        result[i - 1] = False
        continue

    for j in range(i, len(result)):
        if result[j]:
            if result[j] % i == 0:
                result[j] = False
for i in result:
    if i:
        print(i)
1
100

