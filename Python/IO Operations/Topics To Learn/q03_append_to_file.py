file_name = input("Enter the name of the file to append to: ")
user_input_text = input("Enter the text you want to append: ")

with open(file_name, 'a') as user_file:
    user_file.write(user_input_text + "\n")

print("Your text has been successfully appended to the file.")
