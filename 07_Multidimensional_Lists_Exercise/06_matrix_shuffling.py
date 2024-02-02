def check_indices_valid(indices):
    row_1, col_1, row_2, col_2 = indices
    return {row_1, row_2}.issubset(range(rows)) and {col_1, col_2}.issubset(range(cols))


def swap_elements(command, indices):
    if command == "swap" and len(coordinates) == 4 and check_indices_valid(indices):
        row_1, col_1, row_2, col_2 = indices
        matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]

        [print(*row) for row in matrix]
    else:
        print("Invalid input!")


rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for row in range(rows)]

while True:
    command, *coordinates = [int(x) if x.isdigit() else x for x in input().split()]

    if command == "END":
        break

    swap_elements(command, coordinates)
