length_of_sets = [int(x) for x in input().split()]

first_set = set(input() for _ in range(length_of_sets[0]))
second_set = set(input() for _ in range(length_of_sets[1]))

print(*list(first_set.intersection(second_set)), sep="\n")

