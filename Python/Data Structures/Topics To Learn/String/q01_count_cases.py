the_text_to_examine = input("Type in a sentence: ")

tally_of_uppercase_letters = 0
tally_of_lowercase_letters = 0

for single_character in the_text_to_examine:
    if single_character.isupper():
        tally_of_uppercase_letters += 1
    elif single_character.islower():
        tally_of_lowercase_letters += 1

print(f"Total uppercase letters found: {tally_of_uppercase_letters}")
print(f"Total lowercase letters found: {tally_of_lowercase_letters}")
