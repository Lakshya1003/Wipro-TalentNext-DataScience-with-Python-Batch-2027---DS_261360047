first_part = {1: 10, 2: 20}
second_part = {3: 30, 4: 40}
third_part = {5: 50, 6: 60}

combined_dictionary = {}
combined_dictionary.update(first_part)
combined_dictionary.update(second_part)
combined_dictionary.update(third_part)

print("The newly created huge dictionary is:", combined_dictionary)
