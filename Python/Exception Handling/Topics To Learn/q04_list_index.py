my_collection_of_ten_numbers = [42, -5, 17, 0, -99, 8, -3, 21, -12, 100]

try:
    the_spot_they_chose = input("Pick a spot in the list (from 0 to 9): ")
    the_actual_index = int(the_spot_they_chose)
    
    the_number_we_found = my_collection_of_ten_numbers[the_actual_index]
    
    if the_number_we_found > 0:
        print(f"The number at that spot is {the_number_we_found}, which is positive!")
    elif the_number_we_found < 0:
        print(f"The number at that spot is {the_number_we_found}, which is negative!")
    else:
        print(f"The number at that spot is exactly zero.")
        
except ValueError:
    print("That's not a valid number! You need to type an integer.")
except IndexError:
    print("Whoa, that spot doesn't exist! You have to pick a number between 0 and 9.")
