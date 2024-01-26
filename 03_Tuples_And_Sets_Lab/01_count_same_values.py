numbers = tuple(float(number) for number in input().split())
same_values = {}
for number in numbers:
    if number not in same_values:
        same_values[number] = numbers.count(number)

for number, count in same_values.items():
    print(f"{number} - {count} times")
