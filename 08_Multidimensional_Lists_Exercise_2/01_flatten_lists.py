text = [[y for y in x.split()]for x in input().split("|")]

print(*[' '.join(sub_list) for sub_list in text[::-1] if sub_list])
