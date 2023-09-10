"""Модуль содержит класс Матрица."""


class Matrix:
    """Класс Матрица."""

    def __init__(self, num_lst: list[list[int]]):
        """Конструктор принимает двумерный массив целых чисел."""
        self.rows = len(num_lst[0])
        self.columns = len(num_lst)
        self.elements = num_lst

    def __str__(self):
        """Метод печати."""
        return '\n'.join('\t'.join(map(str, row)) for row in self.elements)

    def __eq__(self, other):
        """Метод проверки на равенство."""
        if self.rows == other.rows and self.columns == other.columns:
            flag_list = [self.elements[i][j] == other.elements[i][j]
                         for j in range(self.rows) for i in range(self.columns)]
            if False in flag_list:
                return False
        return True

    def __add__(self, other):
        """Метод вычисления суммы двух матриц."""
        if self.rows == other.rows and self.columns == other.columns:
            return Matrix([list(map(sum, zip(*i))) for i in zip(self.elements, other.elements)])
        wrong_matrix_raiser(self, other)

    def __sub__(self, other):
        """Метод вычисления разности двух матриц."""
        if self.rows == other.rows and self.columns == other.columns:
            return Matrix([[self.elements[i][j] - other.elements[i][j]
                            for j in range(self.rows)] for i in range(self.columns)])
        wrong_matrix_raiser(self, other)

    def __mul__(self, other):
        """Метод вычисления произведения двух матриц."""
        if self.rows == other.columns:
            return Matrix([list(sum(a * b for a, b in zip(row_self, col_other)) for col_other in
                                zip(*other.elements)) for row_self in self.elements])
        wrong_matrix_raiser(self, other)


class WrongMatrixConfig(Exception):
    def __init__(self, text, f_matrix, s_matrix):
        self.txt = text
        self.f_matrix = f_matrix
        self.s_matrix = s_matrix


def wrong_matrix_raiser(f_matrix: Matrix, s_matrix: Matrix):
    raise WrongMatrixConfig(f"Неподходящие матрицы!\n"
                            f"Первая матрица:\n\t"
                            f"строки - {f_matrix.rows}, столбцы - {f_matrix.columns}.\n"
                            f"Вторая матрица:\n\t"
                            f"строки - {s_matrix.rows}, столбцы - {s_matrix.columns}.",
                            f_matrix, s_matrix)


if __name__ == '__main__':
    matrix1 = Matrix([[1, 2], [4, 5], [3, 2]])
    matrix2 = Matrix([[1, 2, 3], [4, 5, 4], [3, 2, 1]])

    print(f'Первая матрица:\n{matrix1}')
    print(f'Вторая матрица:\n{matrix2}')
    print(f'Их сумма:\n{matrix1 + matrix2}')
    print(f'Их разность:\n{matrix1 - matrix2}')
    print(f'Их произведение:\n{matrix1 * matrix2}')
    print(f'Матрицы равны: {matrix1 == matrix2}')
