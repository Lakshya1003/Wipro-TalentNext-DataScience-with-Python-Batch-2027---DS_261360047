def pull_out_the_even_numbers(the_full_list):
    just_the_evens = []
    
    for a_single_item in the_full_list:
        if a_single_item % 2 == 0:
            just_the_evens.append(a_single_item)
            
    print(just_the_evens)

big_list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pull_out_the_even_numbers(big_list_of_numbers)
