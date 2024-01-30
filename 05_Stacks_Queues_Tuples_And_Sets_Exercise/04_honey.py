from collections import deque
working_bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(x for x in input().split())

total_honey = 0

while working_bees and nectar:
    curr_bee = working_bees.popleft()
    curr_nectar = nectar.pop()

    if curr_nectar >= curr_bee:
        symbol = symbols.popleft()
        if symbol == "+":
            total_honey += curr_bee + curr_nectar
        elif symbol == "-":
            total_honey += abs(curr_bee - curr_nectar)
        elif symbol == "*":
            total_honey += abs(curr_bee * curr_nectar)
        elif symbol == "/":
            if curr_nectar != 0:
                total_honey += abs(curr_bee / curr_nectar)
    else:
        working_bees.appendleft(curr_bee)

print(f"Total honey made: {total_honey}")

if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
elif nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
