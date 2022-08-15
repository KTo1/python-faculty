
def type_logger_decorator(func):
    def wrapper(*args):
        for arg in args:
            print(f'{func.__name__}, {arg}:{type(arg)},', end='')
        return func(*args)
    return wrapper


@type_logger_decorator
def calc_cube(x):
    return x ** 3


print(calc_cube(3))
print(calc_cube(4))
print(calc_cube(5))
