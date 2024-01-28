odd_names = set()
even_names = set()

for row in range(1, int(input()) + 1):
    curr_name = sum(ord(char) for char in input()) // row

    if curr_name % 2 == 0:
        even_names.add(curr_name)
    else:
        odd_names.add(curr_name)

if sum(even_names) == sum(odd_names):
    print(*even_names.union(odd_names), sep=", ")
elif sum(even_names) < sum(odd_names):
    print(*odd_names.difference(even_names), sep=", ")
elif sum(even_names) > sum(odd_names):
    print(*even_names.symmetric_difference(odd_names), sep=", ")


