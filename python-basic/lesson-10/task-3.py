
class Cell:

    def check_type(func):
        def wrapper(self, other):
            if not isinstance(other, Cell):
                raise TypeError('All of operands must be a Cell')
            return func(self, other)

        return wrapper

    def __init__(self, start_cell_count):
        self._count = start_cell_count

    def __setattr__(self, key, value):
        if key == '_count' and value == 0:
            raise AttributeError('start_cell_count must be greater than 0.')
        super().__setattr__(key, value)

    @check_type
    def __add__(self, other):
        return Cell(self.get_count() + other.get_count())

    @check_type
    def __sub__(self, other):
        return Cell(self.get_count() - other.get_count())

    @check_type
    def __mul__(self, other):
        return Cell(self.get_count() * other.get_count())

    @check_type
    def __floordiv__(self, other):
        return Cell(self.get_count() // other.get_count())

    @check_type
    def __truediv__(self, other):
        return Cell(self.get_count() // other.get_count())

    def __call__(self, row_count=0):
        return self.make_order(row_count)

    def get_count(self):
        return self._count

    def make_order(self, row_count):
        if not row_count:
            row_count = 1

        row = self.get_count() // row_count
        if not row:
            return '*' * self.get_count() + '\n'

        result = ''
        for i in range(row):
            result += '*' * row_count + '\n'

        remains = self.get_count() - row * row_count
        if remains:
            result += '*' * remains + '\n'

        return result


cell1 = Cell(17)
cell2 = Cell(1)
cell3 = Cell(14)
cell4 = Cell(160)
cell5 = Cell(1487)

print(cell1.make_order(4))
cell = cell1 + cell2
print(cell.make_order(6))
cell = (cell1 + cell5 + cell3 - cell4) / cell2
print(cell(56))
cell = cell1 + 1

