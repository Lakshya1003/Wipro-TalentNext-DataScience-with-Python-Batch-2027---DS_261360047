def figure_out_the_factorial(the_starting_number):
    if the_starting_number == 0:
        return 1
    
    current_calculation = 1
    for every_step in range(1, the_starting_number + 1):
        current_calculation = current_calculation * every_step
        
    return current_calculation

number_to_test = 5
the_result = figure_out_the_factorial(number_to_test)

print(f"The factorial of {number_to_test} is {the_result}")
