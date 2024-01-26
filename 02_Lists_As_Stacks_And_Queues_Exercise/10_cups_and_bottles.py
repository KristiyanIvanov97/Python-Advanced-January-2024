from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = deque([int(y) for y in input().split()])
wasted_water = 0
is_bottles_left = True
while cups:
    if not bottles:
        is_bottles_left = False
        break
    current_cup = cups.popleft()
    current_bottle = bottles.pop()

    if current_cup <= current_bottle:
        wasted_water += current_bottle - current_cup
    elif current_cup > current_bottle:
        cups.appendleft(current_cup - current_bottle)

if not is_bottles_left:
    remaining_cups = [str(cup) for cup in cups]
    print(f"Cups: {' '.join(remaining_cups)}")
else:
    remaining_bottles = [str(bottle) for bottle in bottles]
    print(f"Bottles: {' '.join(remaining_bottles)}")

print(f"Wasted litters of water: {wasted_water}")
