from collections import deque

worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])
matches = 0
# fitted_worms = 0
total_worms = len(worms)

while worms and holes:
    current_worm = worms[-1]
    current_hole = holes[0]

    if current_worm == current_hole:
        worms.pop()
        holes.popleft()
        matches += 1
        # fitted_worms += 1
    else:
        holes.popleft()
        worms[-1] -= 3
        if worms[-1] <= 0:
            worms.pop()

if matches > 0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worms and matches == total_worms:
    print("Every worm found a suitable hole!")
elif not worms:
    print("Worms left: none")
else:
    print(f"Worms left: {', '.join(str(worm) for worm in worms)}")

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(str(hole) for hole in holes)}")
