the_name_of_the_file = input("What is the name of the file you want to open? ")

try:
    with open(the_name_of_the_file, 'r') as the_opened_document:
        all_the_text_inside = the_opened_document.read()
        
        the_text_in_title_format = all_the_text_inside.title()
        
        print(the_text_in_title_format)
        
except FileNotFoundError:
    print("I searched everywhere, but I couldn't find a file with that name!")
except Exception as some_other_issue:
    print(f"I ran into a bit of trouble: {some_other_issue}")
