text_provided = input("Enter your string here: ")
result_text = text_provided

if result_text.startswith('x'):
    result_text = result_text[1:]
    
if result_text.endswith('x'):
    result_text = result_text[:-1]

print("The string after processing those x characters:", result_text)
