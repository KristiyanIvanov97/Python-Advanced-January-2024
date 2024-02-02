rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]
identical_squares = 0
for row in range(rows - 1):
    for col in range(cols - 1):
        current_symbol = matrix[row][col]
        right_symbol = matrix[row][col + 1]
        bottom_right_symbol = matrix[row + 1][col + 1]
        bottom_symbol = matrix[row + 1][col]
        if current_symbol == right_symbol and current_symbol == bottom_symbol and current_symbol == bottom_right_symbol:
            identical_squares += 1

print(identical_squares)
