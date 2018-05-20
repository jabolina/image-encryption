def xor(a, b, pbar):
    pbar.update(1)
    return a ^ b


def shift(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]


def get_column(matrix, j):
    column = []
    for i in range(len(matrix)):
        column.append(matrix[i][j])
    return column


def set_column(matrix, j, column):
    for i in range(len(matrix)):
        matrix[i][j] = column[i]

    return matrix


def sum_row(i, matrix):
    value = 0
    for j in range(len(matrix[i])):
        value += matrix[i][j]
    return value


def sum_column(j, matrix):
    value = 0
    for i in range(len(matrix[j])):
        value += matrix[i][j]
    return value
