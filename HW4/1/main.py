# Напишите функцию для транспонирования матрицы. Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]


MATRIX = [[1, 2, 3], [4, 5, 6]]


def matrix_trans(matrix_to_transpose: list[list[int]]) -> list[list[int]]:
    rows = len(matrix_to_transpose)
    columns = 0
    for i in range(rows):
        columns = len(matrix_to_transpose[i])

    transponed_matrix = [[0 for _ in range(rows)] for _ in range(columns)]

    for i in range(rows):
        for j in range(columns):
            transponed_matrix[j][i] = matrix_to_transpose[i][j]

    return transponed_matrix


if __name__ == '__main__':
    print(matrix_trans(MATRIX))
