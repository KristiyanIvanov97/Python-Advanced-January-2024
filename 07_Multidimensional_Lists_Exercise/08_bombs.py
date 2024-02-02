rows = int(input())

matrix = [[int(x) for x in input().split()] for row in range(rows)]

bombs = [[int(curr_bomb) for curr_bomb in bomb.split(",")] for bomb in input().split()]

directions = (
    (-1, 0),  # up
    (1, 0),  # down
    (0, -1),  # left
    (0, 1),  # right
    (-1, 1),  # top_right
    (-1, -1),  # top_left
    (1, -1),  # bottom_left
    (1, 1),  # bottom_right
    (0, 0),  # current
)

for row, col in bombs:
    if matrix[row][col] < 0:
        continue

    for x, y in directions:
        r, c = row + x, col + y

        if 0 <= r < rows and 0 <= c < rows:
            matrix[r][c] -= matrix[row][col] if matrix[r][c] > 0 else 0

alive_cells = [num for row in range(rows) for num in matrix[row] if num > 0]
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

[print(*row) for row in matrix]
