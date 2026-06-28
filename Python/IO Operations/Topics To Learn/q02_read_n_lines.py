file_name = input("Enter the name of the file: ")
number_of_lines_to_read = int(input("How many lines do you want to read? "))

with open(file_name, 'r') as user_file:
    for current_line_number in range(number_of_lines_to_read):
        line = user_file.readline()
        if not line:
            break
        print(line, end='')
