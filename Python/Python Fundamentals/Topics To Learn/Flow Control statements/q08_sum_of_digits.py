number = int(input("Enter a number: "))
sum_of_digits = 0

while number > 0:
    last_digit = number % 10
    sum_of_digits = sum_of_digits + last_digit
    number = number // 10

print(sum_of_digits)
