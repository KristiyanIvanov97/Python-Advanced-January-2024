number_of_guests = int(input())
guest_numbers = set()
for _ in range(number_of_guests):
    number = input()
    if number not in guest_numbers:
        guest_numbers.add(number)


while True:
    coming_guest = input()
    if coming_guest == "END":
        break
    if coming_guest in guest_numbers:
        guest_numbers.remove(coming_guest)

print(f"{len(guest_numbers)}")
print('\n'.join(sorted(guest_numbers)))
