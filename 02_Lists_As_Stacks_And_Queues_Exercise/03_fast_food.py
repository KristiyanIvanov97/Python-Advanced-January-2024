from collections import deque

quantity_of_food = int(input())

orders = deque([int(order) for order in input().split()])

print(max(orders))

for order in orders.copy():
    if order <= quantity_of_food:
        orders.popleft()
        quantity_of_food -= order
    else:
        orders_left = [str(order) for order in orders]
        print(f"Orders left: {' '.join(orders_left)}")
        break
else:
    print("Orders complete")
