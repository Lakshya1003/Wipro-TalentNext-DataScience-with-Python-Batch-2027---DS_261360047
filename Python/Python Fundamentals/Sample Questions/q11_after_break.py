print("Can we write statements after break keyword? Yes, but they will not execute.")

for number in range(5):
    if number == 3:
        print("Breaking the loop at 3.")
        break
        print("This line is after the break and will never be printed.")
