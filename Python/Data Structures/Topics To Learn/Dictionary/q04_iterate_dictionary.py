favorite_foods = {"Alice": "Pizza", "Bob": "Burger", "Charlie": "Pasta"}

print("Just the names (keys):")
for person_name in favorite_foods.keys():
    print(person_name)

print("\nJust the food (values):")
for food_item in favorite_foods.values():
    print(food_item)

print("\nBoth names and foods (keys and values):")
for person_name, food_item in favorite_foods.items():
    print(f"{person_name} likes {food_item}")
