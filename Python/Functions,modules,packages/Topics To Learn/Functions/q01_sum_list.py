def add_all_the_numbers_together(the_bunch_of_numbers):
    running_total = 0
    for single_number in the_bunch_of_numbers:
        running_total += single_number
    return running_total

my_sample_numbers = (8, 2, 3, 0, 7)
the_final_sum = add_all_the_numbers_together(my_sample_numbers)

print(the_final_sum)
