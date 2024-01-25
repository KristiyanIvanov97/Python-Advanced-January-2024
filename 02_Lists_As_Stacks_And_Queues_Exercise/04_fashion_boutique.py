from collections import deque

clothes = deque([int(x) for x in input().split()])
clothes.reverse()

capacity_of_rack = int(input())
racks_count = 1
current_rack = capacity_of_rack

for cloth in clothes.copy():
    if cloth <= current_rack:
        clothes.popleft()
        current_rack -= cloth
    else:
        racks_count += 1
        current_rack = capacity_of_rack
        current_rack -= cloth

print(racks_count)
