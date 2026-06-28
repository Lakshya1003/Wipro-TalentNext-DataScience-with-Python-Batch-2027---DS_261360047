first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

first_last_digit = first_number % 10
second_last_digit = second_number % 10

if first_last_digit == second_last_digit:
    print("true")
else:
    print("false")
