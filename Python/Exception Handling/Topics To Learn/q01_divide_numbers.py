try:
    the_top_number = float(input("Please enter the number to divide: "))
    the_bottom_number = float(input("Please enter the number to divide by: "))
    
    the_final_answer = the_top_number / the_bottom_number
    
    print(f"The result of the division is: {the_final_answer}")
    
except ValueError:
    print("Oops! You need to enter actual numbers, not letters or words.")
except ZeroDivisionError:
    print("Oh no! You can't divide a number by zero.")
except Exception as a_random_weird_error:
    print(f"Something totally unexpected happened: {a_random_weird_error}")
