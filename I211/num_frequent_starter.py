def open_file(filename):
    lines = []

    #try to open filename. If it doesn't exist, ask the user for another file.
    #repeat until they give you a valid one.
    #open it and read the lines from it into lines

    return lines

def list_freq(num_list):
    numbers = {}

    #given a list, create a dictionary where a number is a key and the number of times
    #you've seen it is the value

    return numbers

#main
the_file = raw_input("Please enter a filename: ")

counts = list_freq(open_file(the_file))

num = raw_input("Please enter a number: ")

print num, "occurs", "?" , "times in the file."     #change "?" here to something else
