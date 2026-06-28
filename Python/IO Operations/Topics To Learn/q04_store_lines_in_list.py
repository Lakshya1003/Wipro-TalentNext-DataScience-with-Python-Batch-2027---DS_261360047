file_name = input("Enter the name of the file: ")
list_of_lines = []

with open(file_name, 'r') as user_file:
    for line in user_file:
        list_of_lines.append(line.strip())

print("The lines have been extracted and stored in a list successfully.")
print(list_of_lines)
