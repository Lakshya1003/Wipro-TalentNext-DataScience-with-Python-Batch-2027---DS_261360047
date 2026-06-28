def a_function_that_stops_early():
    print("This runs.")
    return
    print("This will never run.")

the_magic_keyword = "return"
print(f"The '{the_magic_keyword}' keyword immediately ends the execution of a function.")
