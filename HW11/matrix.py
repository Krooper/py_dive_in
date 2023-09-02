class Matrix:
    def __init__(self, num_lst: list[list[int]]):
        self.rows = len(num_lst[0])
        self.columns = len(num_lst)
        self.elements = num_lst

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.elements)

    def __eq__(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            flag_list = [self.elements[i][j] == other.elements[i][j]
                         for j in range(self.rows) for i in range(self.columns)]
            if False in flag_list:
                return False
        return True

    def __add__(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            return Matrix([list(map(sum, zip(*i))) for i in zip(self.elements, other.elements)])
        return None

    def __sub__(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            return Matrix([[self.elements[i][j] - other.elements[i][j]
                            for j in range(self.rows)] for i in range(self.columns)])
        return None

    def __mul__(self, other):
        if self.rows == other.columns:
            return Matrix([list(sum(a * b for a, b in zip(row_self, col_other)) for col_other in
                                zip(*other.elements)) for row_self in self.elements])
        return None


if __name__ == '__main__':
    matrix1 = Matrix([[1, 2, 3], [4, 5, 4], [3, 2, 1]])
    matrix2 = Matrix([[1, 2, 3], [4, 5, 4], [3, 2, 1]])

    print(f'Первая матрица:\n{matrix1}')
    print(f'Вторая матрица:\n{matrix2}')
    print(f'Их сумма:\n{matrix1 + matrix2}')
    print(f'Их разность:\n{matrix1 - matrix2}')
    print(f'Их произведение:\n{matrix1 * matrix2}')
    print(f'Матрицы равны: {matrix1 == matrix2}')
