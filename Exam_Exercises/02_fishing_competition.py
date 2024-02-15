def next_position(position, direction_mapper, direction, board):
    desired_row = position[0] + direction_mapper[direction][0]
    desired_col = position[1] + direction_mapper[direction][1]

    desired_row = (desired_row + len(board)) % len(board)
    desired_col = (desired_col + len(board)) % len(board)

    return desired_row, desired_col


n = int(input())

QUOTA = 20

board = []
sailor_position = []
collected_fish = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(n):
    board.append(list(input()))
    if "S" in board[row]:
        sailor_position = [row, board[row].index("S")]

command = input()

while command != "collect the nets":
    next_row_index, next_col_index = next_position(sailor_position, directions, command, board)

    symbol = board[next_row_index][next_col_index]
    board[next_row_index][next_col_index] = "S"
    board[sailor_position[0]][sailor_position[1]] = "-"
    sailor_position = [next_row_index, next_col_index]

    if symbol.isdigit():
        collected_fish += int(symbol)
    elif symbol == "W":
        print(f"You fell into a whirlpool! "
              f"The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{sailor_position[0]},{sailor_position[1]}]")
        exit()

    command = input()

if collected_fish >= QUOTA:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! "
          f"You need {QUOTA - collected_fish} tons of fish more.")

if collected_fish > 0:
    print(f"Amount of fish caught: {collected_fish} tons.")

for row in board:
    print(f"{''.join(str(x) for x in row)}")
