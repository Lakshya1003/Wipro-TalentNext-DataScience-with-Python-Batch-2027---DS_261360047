file_name = input("Enter the name of the file to read: ")

with open(file_name, 'r') as user_file:
    file_content = user_file.read()

print(file_content)
