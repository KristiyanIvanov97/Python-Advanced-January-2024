from collections import deque

quantity_of_water = int(input())

name = input()
people = deque()

while name != "Start":
    people.append(name)
    name = input()

command = input().split()

while command[0] != "End":
    if command[0] == "refill":
        water_to_refill = int(command[1])
        quantity_of_water += water_to_refill
    else:
        water_wanted = int(command[0])
        if quantity_of_water >= water_wanted:
            print(f"{people.popleft()} got water")
            quantity_of_water -= water_wanted
        else:
            print(f"{people.popleft()} must wait")

    command = input().split()

print(f"{quantity_of_water} liters left")
