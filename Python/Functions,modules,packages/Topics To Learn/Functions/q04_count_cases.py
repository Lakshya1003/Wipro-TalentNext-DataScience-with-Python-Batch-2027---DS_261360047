def count_upper_and_lower_case_letters(the_big_string):
    uppercase_tally = 0
    lowercase_tally = 0
    
    for single_letter in the_big_string:
        if single_letter.isupper():
            uppercase_tally += 1
        elif single_letter.islower():
            lowercase_tally += 1
            
    print(f"Upper case letters: {uppercase_tally}")
    print(f"Lower case letters: {lowercase_tally}")

sentence_to_test = "Hello World! It is a Great Day."
count_upper_and_lower_case_letters(sentence_to_test)
