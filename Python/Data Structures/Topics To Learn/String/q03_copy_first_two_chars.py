original_word = input("Enter a word that has at least two letters: ")

how_long_the_word_is = len(original_word)
the_first_two_letters = original_word[:2]

the_new_generated_word = the_first_two_letters * how_long_the_word_is

print("Here is your newly generated string:", the_new_generated_word)
