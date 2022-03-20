
# result = [12, 44, 4, 10, 78, 123]
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# Cписком
result = [elem for idx, elem in enumerate(src) if elem > src[idx-1] and idx > 0]
print(result)

# Оптимизация по памяти, генератором
result = (elem for idx, elem in enumerate(src) if elem > src[idx-1] and idx > 0)
print(result)
