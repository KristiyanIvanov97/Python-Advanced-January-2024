from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque(int(y) for y in input().split())
crafted_gifts = []
presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while materials and magic_level:
    curr_material = materials.pop() if magic_level[0] or not materials[-1] else 0
    curr_magic = magic_level.popleft() if curr_material or not magic_level[0] else 0

    if not curr_magic:
        continue

    product = curr_magic * curr_material
    if presents.get(product):
        crafted_gifts.append(presents[product])
    elif product < 0:
        materials.append(curr_material + curr_magic)
    elif product > 0:
        materials.append(curr_material + 15)

if {"Doll", "Wooden train"}.issubset(crafted_gifts) or {"Teddy bear", "Bicycle"}.issubset(crafted_gifts):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")

if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

[print(f"{toy}: {crafted_gifts.count(toy)}") for toy in sorted(set(crafted_gifts))]
