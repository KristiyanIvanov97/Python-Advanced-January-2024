def check_lose(row, col, size):
    return 0 <= row < size and 0 <= col < size


def print_board(board):
    for row in board:
        print(''.join(row))


size = int(input())

money = 100
board = []
position = None

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    data = list(input())

    if "G" in data:
        current_col = data.index("G")
        position = [row, current_col]
    board.append(data)

command = input()

while command != "end":
    row = position[0] + directions[command][0]
    col = position[1] + directions[command][1]

    if not check_lose(row, col, size):
        print("Game over! You lost everything!")
        exit()

    symbol = board[row][col]
    board[row][col] = "G"
    board[position[0]][position[1]] = "-"
    position = [row, col]

    if symbol == "W":
        money += 100
    elif symbol == "P":
        money -= 200
        if money <= 0:
            money = 0
            print("Game over! You lost everything!")
            exit()
    elif symbol == "J":
        money += 100_000
        print(f"You win the Jackpot!")
        print(f"End of the game. Total amount: {money}$")
        print_board(board)
        exit()

    command = input()

print(f"End of the game. Total amount: {money}$")
print_board(board)
