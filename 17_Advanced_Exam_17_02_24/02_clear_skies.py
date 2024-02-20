def print_airspace(board):
    for row in board:
        print(''.join(row))


size = int(input())

airspace = []
jet_position = []
total_enemies = 0
jet_armor = 300


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    airspace.append(list(input()))
    if "J" in airspace[row]:
        jet_position = [row, airspace[row].index("J")]
        airspace[row][jet_position[1]] = "-"
    if "E" in airspace[row]:
        total_enemies += airspace[row].count("E")


while True:
    direction = input()

    if jet_armor == 0:
        break

    next_row = jet_position[0] + directions[direction][0]
    next_col = jet_position[1] + directions[direction][1]

    target = airspace[next_row][next_col]
    jet_position = [next_row, next_col]
    airspace[next_row][next_col] = "-"
    if target == "E":
        total_enemies -= 1
        if not total_enemies:
            airspace[jet_position[0]][jet_position[1]] = "J"
            print("Mission accomplished, you neutralized the aerial threat!")
            print_airspace(airspace)
            exit()
        else:
            jet_armor -= 100
            if jet_armor == 0:
                airspace[jet_position[0]][jet_position[1]] = "J"
                print(f"Mission failed, your jetfighter was shot down!"
                      f" Last coordinates [{jet_position[0]}, {jet_position[1]}]!")
                print_airspace(airspace)
                exit()
    elif target == "R":
        jet_armor = 300
