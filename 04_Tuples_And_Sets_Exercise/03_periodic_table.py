chemical_el = set()

for _ in range(int(input())):
    for curr_el in input().split():
        chemical_el.add(curr_el)

print(*chemical_el, sep="\n")
