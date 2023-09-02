class Matrix:
    def __init__(self, num_lst):
        self.rows = len(num_lst[0])
        self.columns = len(num_lst)
        self.elements = num_lst

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.elements)

    def __add__(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            return Matrix([list(map(sum, zip(*i))) for i in zip(self.elements, other.elements)])
        else:
            return None

    def __mul__(self, other):
        if self.rows == other.columns:
            return Matrix([list(sum(a * b for a, b in zip(row_self, col_other)) for col_other in
                                zip(*other.elements)) for row_self in self.elements])
        else:
            return None


if __name__ == '__main__':
    matrix1 = Matrix([[1, 2, 3], [4, 5, 4], [3, 2, 1]])
    matrix2 = Matrix([[9, 7, 5], [3, 1, 1], [1, 1, 1]])

    print(f'Первая матрица:\n{matrix1}')
    print(f'Вторая матрица:\n{matrix2}')
    print(f'Результат их сложения:\n{matrix1 + matrix2}')
    print(f'Результат их умножения:\n{matrix1 * matrix2}')
