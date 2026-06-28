def is_this_a_prime_number(the_number_in_question):
    if the_number_in_question <= 1:
        print("Not a prime number")
        return
        
    for possible_divisor in range(2, the_number_in_question):
        if the_number_in_question % possible_divisor == 0:
            print("Not a prime number")
            return
            
    print("Yes, it is a prime number!")

number_to_check = 17
is_this_a_prime_number(number_to_check)
