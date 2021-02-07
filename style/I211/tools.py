#-------------------------------
# Official Tools Module for I211
#           Version 1
#-------------------------------

#---------------------------------------------------------------------
#To use this file, place it in the same directory as your python code,
#then add the line:
#               from tools import *
#to the top of your python code. You can then use these functions.
#---------------------------------------------------------------------

#------------------------------
# string manipulation functions
#------------------------------

#pads out a string with dashes until it's 20 characters long
def dasher(string):
    if len(string) > 20:
        string = "Error"
    dashes =(20 - len(string))

    formatted = "-" * (dashes/2) + string + "-" * (dashes/2)

    if (dashes % 2 == 1):
        formatted += "-"
    return formatted

#removes the vowels from a string, returns a version without them
def disenvowel(string):

    VOWELS = "aeiou"

    #we'll build up the new string, starting from nothing
    new_word = ""

    for letter in string:
        if letter.lower() not in VOWELS:
            #if we get here, letter is a consonant, add it
            new_word += letter

    return new_word


#------------------------------
# number manipulation functions
#------------------------------

#returns True if a number is odd, False otherwise
def odd(number):
    return number % 2 == 1

#prompt the user for an integer between mini and maxi. Validates pos. ints.
def get_range_int(mini, maxi):
    while True:
        num = raw_input("Enter an integer between " + str(mini) + " and " + str(maxi) + ": ")
        if num.isdigit():
            num = int(num)
            if num >= mini and num <= maxi:
                break
    return num

#recursive version of factorial that computes num!
def factorial(num):
    if(num == 1):
        return 1
    else :
        return num * factorial(num - 1)

#------------------------------
# sequence manipulation functions
#------------------------------

#takes a sequence of headers and a nested sequence of values
#and prints them out, with dashes between
def table_print(headers, values):
    for col in headers:
        print "\t", col,
    print "\n\t", "-" * (15*len(headers))

    for entry in values:
        for elem in entry:
            print "\t", elem,
        print

    print "\t", "-" * (15*len(headers))

#swaps the position of two elements in a list
def swap(my_list, x, y):
    temp = my_list[x]		#temp is our 'empty cup'
    my_list[x] = my_list[y]
    my_list[y] = temp

#-----------------------------
# test code goes here
#-----------------------------

if __name__ == "__main__":
    print dasher("this is a test")
