from collections import deque

some_string = deque(input().split())

colors = ["red", "green", "blue", "yellow", "purple", "orange"]
req_colors = {
    "orange": {"red", "yellow"},
    "purple": {"blue", "red"},
    "green": {"yellow", "blue"},
}
created_colors = []
while some_string:
    first_substring = some_string.popleft()
    second_substring = some_string.pop() if some_string else ""

    for color in (first_substring + second_substring, second_substring + first_substring):
        if color in colors:
            created_colors.append(color)
            break
    else:
        for element in (first_substring[:-1], second_substring[:-1]):
            if element:
                some_string.insert(len(some_string) // 2, element)

for color in set(req_colors.keys()).intersection(created_colors):
    if not req_colors[color].issubset(created_colors):
        created_colors.remove(color)

print(created_colors)
