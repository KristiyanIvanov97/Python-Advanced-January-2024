def cookbook(*receipts):
    receipts_per_cuisine = {}
    for recipe_name, cuisine, ingredients in receipts:
        if cuisine not in receipts_per_cuisine:
            receipts_per_cuisine[cuisine] = []
        receipts_per_cuisine[cuisine].append((recipe_name, ingredients))

    sorted_receipts = sorted(receipts_per_cuisine.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ""

    for curr_cuisine in sorted_receipts:
        result += f"{curr_cuisine[0]} cuisine contains {len(curr_cuisine[1])} recipes:\n"
        for recipe in sorted(curr_cuisine[1]):
            result += f"  * {recipe[0]} -> Ingredients: {', '.join(x for x in recipe[1])}\n"

    return result




# print(cookbook(
#     ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
#     ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
#     ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
#     ("Croissant", "French", ["flour", "butter", "yeast"]),
#     ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
# ))
#
# print(cookbook(
#     ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
#     ))

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))