def flip_the_word_backwards(the_original_text):
    the_reversed_version = the_original_text[::-1]
    return the_reversed_version

starting_string = "1234abcd"
the_flipped_string = flip_the_word_backwards(starting_string)

print(the_flipped_string)
