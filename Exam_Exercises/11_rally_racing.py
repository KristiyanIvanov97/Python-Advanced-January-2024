size = int(input())
racing_number = input()

car_position = [0, 0]
track = []
kilometers_passed = 0

first_tunnel = []
second_tunnel = []
is_finished = False

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    track.append(input().split())
    if "T" in track[row]:
        if len(first_tunnel) < 1:
            first_tunnel = [row, track[row].index("T")]
        else:
            second_tunnel = [row, track[row].index("T")]

command = input()

while command != "End":
    current_position = [car_position[0] + directions[command][0], car_position[1] + directions[command][1]]
    car_position = current_position
    symbol = track[current_position[0]][current_position[1]]

    if symbol == "F":
        kilometers_passed += 10
        is_finished = True
        print(f"Racing car {racing_number} finished the stage!")
        break
    elif symbol == "T":
        kilometers_passed += 30
        if current_position == first_tunnel:
            car_position = second_tunnel
        else:
            car_position = first_tunnel

        track[first_tunnel[0]][first_tunnel[1]] = "."
        track[second_tunnel[0]][second_tunnel[1]] = "."
    elif symbol == ".":
        kilometers_passed += 10

    command = input()

if not is_finished:
    print(f"Racing car {racing_number} DNF.")

print(f"Distance covered {kilometers_passed} km.")

track[car_position[0]][car_position[1]] = "C"

for row in track:
    print(''.join(row))

