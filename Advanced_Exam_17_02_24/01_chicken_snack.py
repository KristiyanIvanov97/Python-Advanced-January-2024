from collections import deque

amount_of_money = [int(money) for money in input().split()]
prices_of_food = deque([int(food) for food in input().split()])
total_food = 0

while amount_of_money and prices_of_food:
    curr_money = amount_of_money[-1]
    curr_price = prices_of_food[0]

    if curr_money == curr_price:
        amount_of_money.pop()
        prices_of_food.popleft()
        total_food += 1
    elif curr_money > curr_price:
        change = curr_money - curr_price
        amount_of_money.pop()
        if amount_of_money:
            amount_of_money[-1] += change
        prices_of_food.popleft()
        total_food += 1
    elif curr_money < curr_price:
        amount_of_money.pop()
        prices_of_food.popleft()

if total_food >= 4:
    print(f"Gluttony of the day! Henry ate {total_food} foods.")
elif total_food < 4 and total_food != 0:
    if total_food == 1:
        print("Henry ate: 1 food.")
        exit()
    print(f"Henry ate: {total_food} foods.")
else:
    print("Henry remained hungry. He will try next weekend again.")
