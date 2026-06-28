def check_if_this_is_prime(the_number_to_test):
    if the_number_to_test <= 1:
        return False
    for a_possible_factor in range(2, the_number_to_test):
        if the_number_to_test % a_possible_factor == 0:
            return False
    return True

try:
    the_raw_input_from_user = input("Give me a number to check if it's prime: ")
    the_actual_integer = int(the_raw_input_from_user)
    
    if check_if_this_is_prime(the_actual_integer):
        print("Yep, that is definitely a prime number!")
    else:
        print("Nope, that is not a prime number.")
        
except ValueError:
    print("Hold on there! You need to type a real whole number, nothing else.")
