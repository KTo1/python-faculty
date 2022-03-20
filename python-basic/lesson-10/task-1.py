from copy import deepcopy


class Matrix:

    def __init__(self, init_list):
        self._data = init_list

    def __str__(self):
        if not self.get_data():
            return ''

        max_len = len(str(max(max(self.get_data()))))
        result = ''
        for i in self.get_data():
            for j in i:
                result += str(j).rjust(max_len, ' ') + ' '
            result += '\n'
        return result

    def __add__(self, other):
        if not self == other:
            raise TypeError('matrix must be equal.')

        self_data = self.get_data()
        other_data = other.get_data()

        result = deepcopy(self_data)
        for i in range(len(self_data)):
            for j in range(len(self_data[i])):
                result[i][j] += other_data[i][j]

        return Matrix(result)

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False

        self_data = self.get_data()
        other_data = other.get_data()

        if len(self_data) != len(other_data):
            return False

        for i in range(len(self_data)):
            if len(self_data[i]) != len(other_data[i]):
                return False

        return True

    def get_data(self):
        return self._data


matrix1 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
matrix2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
matrix3 = Matrix([[2, 2, 2], [2, 2, 2], [1, 1]])

print('matrix1:\n', matrix1, sep='')
print('matrix2:\n', matrix2, sep='')
print('matrix1 == matrix2\n', matrix1 == matrix2, sep='')
print('matrix1 + matrix2 + matrix2\n', matrix1 + matrix2 + matrix2, sep='')
print('matrix1:\n', matrix1, sep='')
print('matrix2:\n', matrix2, sep='')
print('matrix1 + matrix3\n', matrix1 + matrix3, sep='')
