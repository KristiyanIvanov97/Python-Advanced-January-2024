rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:
    command = input().split()
    if command[0] == "END":
        break
    command_type, row, col, value = command[0], int(command[1]), int(command[2]), int(command[3])
    if not (0 <= row < rows and 0 <= col < rows):
        print("Invalid coordinates")
    elif command_type == "Add":
        matrix[row][col] += int(value)
    elif command_type == "Subtract":
        matrix[row][col] -= int(value)

[print(*row) for row in matrix]
