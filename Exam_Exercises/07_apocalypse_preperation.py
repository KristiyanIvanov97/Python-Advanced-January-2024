from collections import deque

textiles = deque([int(x) for x in input().split()])
medicaments = [int(x) for x in input().split()]

items = {"Patch": 30,
         "Bandage": 40,
         "MedKit": 100,
         }
items_created = {}
while textiles and medicaments:
    curr_textile = textiles[0]
    curr_med = medicaments[-1]

    sum_of_two = curr_textile + curr_med

    if sum_of_two > items["MedKit"]:
        if "MedKit" not in items_created:
            items_created["MedKit"] = 0
        items_created["MedKit"] += 1
        textiles.popleft()
        medicaments.pop()
        remaining_resources = sum_of_two - items["MedKit"]
        medicaments[-1] += remaining_resources
        continue

    for item_name, resources in items.items():
        if resources == sum_of_two:
            if item_name not in items_created:
                items_created[item_name] = 0
            items_created[item_name] += 1
            textiles.popleft()
            medicaments.pop()
            break
    else:
        textiles.popleft()
        medicaments[-1] += 10

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

sorted_items = sorted(items_created.items(), key=lambda x: (-x[1], x[0]))

for item_name, quantity in sorted_items:
    print(f"{item_name} - {quantity}")

if len(medicaments) > 0:
    print(f"Medicaments left: {', '.join(str(med) for med in reversed(medicaments))}")
if len(textiles) > 0:
    print(f"Textiles left: {', '.join(str(textile) for textile in textiles)}")
