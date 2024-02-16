def shop_from_grocery_list(budget, product_list, *products):
    for prod_name, price in products:
        if prod_name in product_list:
            if price <= budget:
                budget -= price
                product_list.remove(prod_name)
            else:
                break

    if len(product_list) == 0:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    return f"You did not buy all the products. Missing products: {', '.join(product_list)}."


# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("meat", 22),
# ))

# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat", "chocolate"],
#     ("cola", 15.8),
#     ("chocolate", 30),
#     ("tomato", 15.85),
#     ("chips", 50),
#     ("meat", 22.99),
# ))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))