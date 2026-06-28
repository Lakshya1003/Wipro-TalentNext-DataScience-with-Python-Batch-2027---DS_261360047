employee_data = {"Alice": 25, "Bob": 30, "Charlie": 35}
print("Current employee data:", employee_data)

name_to_search_for = "Bob"

if name_to_search_for in employee_data:
    print(f"Yes, the key '{name_to_search_for}' is already inside the dictionary.")
else:
    print(f"No, the key '{name_to_search_for}' is nowhere to be found.")
