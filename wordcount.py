

with open("input.txt", "r") as file: # open the file
    text = file.read() # read the file
    words = text.split() # split the text into words
    word_count = len(words) # count the number of words
    with open("word_count.txt", "w") as file: # open the file
        file.write(str(word_count)) # write the number of words