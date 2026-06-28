starting_word = input("Enter the starting string: ")
how_many_chunks = int(input("Enter the number of chunks to slice and repeat: "))

if how_many_chunks == 0:
    the_final_mashup = ""
else:
    the_last_few_characters = starting_word[-how_many_chunks:]
    the_final_mashup = the_last_few_characters * how_many_chunks

print("The newly mashed up word is:", the_final_mashup)
