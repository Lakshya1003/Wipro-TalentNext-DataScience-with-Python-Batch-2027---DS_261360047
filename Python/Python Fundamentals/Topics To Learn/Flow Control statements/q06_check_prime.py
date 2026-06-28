number = int(input("Enter a number: "))
is_prime = True

if number <= 1:
    is_prime = False
else:
    for divider in range(2, number):
        if number % divider == 0:
            is_prime = False
            break

if is_prime:
    print("Prime")
else:
    print("Not Prime")
