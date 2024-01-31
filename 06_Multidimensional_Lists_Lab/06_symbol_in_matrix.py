rows = int(input())

matrix = [list(input()) for row in range(rows)]
symbol = input()

for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == symbol:
            print(f"({row}, {col})")
            exit()

print(f"{symbol} does not occur in the matrix")
