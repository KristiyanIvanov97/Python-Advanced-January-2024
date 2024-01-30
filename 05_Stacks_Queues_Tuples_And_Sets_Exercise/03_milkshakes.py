from collections import deque

chocolates = deque(int(x) for x in input().split(", "))
cups_of_milk = deque(int(y) for y in input().split(", "))

done_milkshakes = 0

while done_milkshakes < 5 and chocolates and cups_of_milk:
    curr_chocolate = chocolates.pop()
    curr_cup_of_milk = cups_of_milk.popleft()

    # if curr_chocolate <= 0 or curr_cup_of_milk <= 0:
    #     if curr_chocolate <= 0:
    #         cups_of_milk.appendleft(curr_cup_of_milk)
    #     if curr_cup_of_milk <= 0:
    #         chocolates.append(curr_chocolate)
    #     continue

    if curr_chocolate <= 0 and curr_cup_of_milk <= 0:
        continue
    elif curr_chocolate <= 0:
        cups_of_milk.appendleft(curr_cup_of_milk)
        continue
    elif curr_cup_of_milk <= 0:
        chocolates.append(curr_chocolate)
        continue

    if curr_chocolate == curr_cup_of_milk:
        done_milkshakes += 1
    else:
        cups_of_milk.append(curr_cup_of_milk)
        chocolates.append(curr_chocolate - 5)

if done_milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
# if chocolates:
#     print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
# else:
#     print("Chocolate: empty")
# if cups_of_milk:
#     print(f"Milk: {', '.join(str(y) for y in cups_of_milk)}")
# else:
#     print("Milk: empty")

print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups_of_milk) or 'empty'}")
