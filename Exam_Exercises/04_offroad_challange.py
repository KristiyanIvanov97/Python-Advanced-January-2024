from collections import deque

initial_fuel = [int(x) for x in input().split()]
additional_consumption_index = deque([int(x) for x in input().split()])
amount_of_fuel_needed = deque([int(x) for x in input().split()])
counter = 0
max_count = len(initial_fuel)

while initial_fuel and additional_consumption_index and amount_of_fuel_needed:
    fuel = initial_fuel.pop()
    index = additional_consumption_index.popleft()
    fuel_needed = amount_of_fuel_needed.popleft()

    if fuel - index >= fuel_needed:
        counter += 1
        print(f"John has reached: Altitude {counter}")
    else:
        print(f"John did not reach: Altitude {counter + 1}")
        break

if max_count > counter and counter:
    print(f"John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(f'Altitude {x}' for x in range(1, counter + 1))}")
elif initial_fuel:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")

if max_count == counter:
    print("John has reached all the altitudes and managed to reach the top!")
