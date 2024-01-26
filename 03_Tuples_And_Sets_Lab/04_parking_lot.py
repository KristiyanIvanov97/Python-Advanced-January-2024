number_of_commands = int(input())
car_numbers = set()
for _ in range(number_of_commands):
    direction, number = input().split(', ')
    if direction == "IN":
        if number not in car_numbers:
            car_numbers.add(number)
    else:
        if number in car_numbers:
            car_numbers.remove(number)

if car_numbers:
    print(*car_numbers, sep='\n')
else:
    print("Parking Lot is Empty")