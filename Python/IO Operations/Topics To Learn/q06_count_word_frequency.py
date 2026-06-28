file_name = input("Enter the name of the file: ")
target_word = input("Enter the word you want to count: ")
word_frequency = 0

target_word_lower = target_word.lower()

with open(file_name, 'r') as user_file:
    file_content = user_file.read()
    
    clean_content = ""
    for character in file_content:
        if character.isalnum() or character.isspace():
            clean_content += character
        else:
            clean_content += " "
            
    all_words = clean_content.split()
    
    for word in all_words:
        if word.lower() == target_word_lower:
            word_frequency += 1

print(f"The word '{target_word}' appears {word_frequency} times in the file.")
