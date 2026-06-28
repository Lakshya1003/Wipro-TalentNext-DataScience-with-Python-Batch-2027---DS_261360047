available_fruits = ("mango", "orange", "pineapple", "kiwi")

fruit_to_search_for = "orange"

if fruit_to_search_for in available_fruits:
    print(f"Yes, we have {fruit_to_search_for} in our collection!")
else:
    print(f"Sorry, {fruit_to_search_for} is missing from the collection.")
