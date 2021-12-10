class Matrix:
    def __init__(self, input_data):
        self.input = input_data

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.input])

    def __add__(self, other):
        var = ''
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                    return 'Ошибка'

                sum_line = [x + y for x, y in zip(line_1, line_2)]
                var += ' '.join(map(str, sum_line)) + '\n'
        return var


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
print(matrix_1, '\n')
print(matrix_2, '\n')
print(matrix_1 + matrix_2)
