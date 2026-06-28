for current_number in range(10, 100):
    is_prime = True
    
    if current_number <= 1:
        is_prime = False
    else:
        for divider in range(2, current_number):
            if current_number % divider == 0:
                is_prime = False
                break
                
    if is_prime:
        print(current_number)
