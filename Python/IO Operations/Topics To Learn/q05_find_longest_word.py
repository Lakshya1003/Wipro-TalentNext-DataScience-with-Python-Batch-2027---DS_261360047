file_name = input("Enter the name of the file: ")
longest_word_found = ""
maximum_length = 0

with open(file_name, 'r') as user_file:
    file_content = user_file.read()
    
    clean_content = ""
    for character in file_content:
        if character.isalnum() or character.isspace():
            clean_content += character
        else:
            clean_content += " "
            
    all_words = clean_content.split()
    
    for current_word in all_words:
        if len(current_word) > maximum_length:
            maximum_length = len(current_word)
            longest_word_found = current_word

print(f"The longest word in the file is: {longest_word_found}")
