word_to_check = input("Enter a word to see if it's a palindrome: ")

word_flipped_around = word_to_check[::-1]

if word_to_check == word_flipped_around:
    print("Yes, it reads exactly the same backwards!")
else:
    print("No, that is not a palindrome.")
