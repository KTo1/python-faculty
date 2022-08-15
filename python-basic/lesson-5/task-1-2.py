
def odd_nums(max_num):
    for i in range(1, max_num, 2):
        yield i


# Используя yield
odd_nums = odd_nums(15)
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))

# Не используя yield
odd_nums = (i for i in range(1, 15, 2))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
