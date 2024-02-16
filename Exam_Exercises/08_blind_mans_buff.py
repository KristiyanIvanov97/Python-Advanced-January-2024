rows, cols = [int(x) for x in input().split()]

man_position = []
matrix = []
touched_opponents = 0
moves_made = 0
total_opponents = 3

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(rows):
    matrix.append(input().split())
    if "B" in matrix[row]:
        man_col = matrix[row].index("B")
        man_position = [row, man_col]

while True:
    command = input()
    if command == "Finish":
        break

    desired_row, desired_col = [
        man_position[0] + directions[command][0],
        man_position[1] + directions[command][1]
    ]

    if not (0 <= desired_row < rows and 0 <= desired_col < cols):
        continue
    symbol = matrix[desired_row][desired_col]

    if symbol == "O":
        continue

    moves_made += 1
    if symbol == "P":
        touched_opponents += 1
        matrix[man_position[0]][man_position[1]] = "-"
        matrix[desired_row][desired_col] = "B"
        man_position = [desired_row, desired_col]
        if touched_opponents == 3:
            break
    elif symbol == "-":
        matrix[man_position[0]][man_position[1]] = "-"
        matrix[desired_row][desired_col] = "B"
        man_position = [desired_row, desired_col]

print(f"Game over!\nTouched opponents: {touched_opponents} Moves made: {moves_made}")
