
def val_checker(val_func):
    def _val_checker(func):
        def wrapper(*args):
            for arg in args:
                if val_func(arg):
                    print(f'{func.__name__}, {arg}:{type(arg)},', end='')
                else:
                    raise ValueError(f'Wrong val: {arg}')
            return func(*args)
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(3))
print(calc_cube(4))
print(calc_cube(5))
print(calc_cube(-5))
