class ValueCannotBeNegative(Exception):
    pass


numbers_count = 5

for _ in range(numbers_count):
    current_number = int(input())
    if current_number < 0:
        raise ValueCannotBeNegative("Number cannot be negative")
