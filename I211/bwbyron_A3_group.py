#Assignment 3, Group: Pig Latin Translator
#Brett Byron, Group 1

#For UNIX
#!/usr/bin/env python

import datetime, os

def pl_prefix(word):
    for i in range(len(word)):
        if word[i].lower() in vowels:
            return i

def pl_reverse(word):
    pre = pl_prefix(word)
    stem = word[:pre]
    prefix = word[pre:]
    result = str(prefix+stem)
    return result

def pl_translate(word):
    punct = ".,!?"
    stripped = ""
    word = word.strip()

    if len(word) > 0:
        if word[-1] in punct:
            stripped = word[-1]
            word = word[:-1]

    if word[0].lower() in vowels:
        word = pl_reverse(word)
        if word[0].isupper():
            word = pl_reverse(word)
            word = word.capitalize()
        else:
            word = pl_reverse(word)
        return str(word+"yay"), stripped
    else:
        if word[0].isupper():
            word = pl_reverse(word)
            word = word.capitalize()
        else:
            word = pl_reverse(word)
        return str(word+"ay"), stripped

def pl_file(in_file, out_file):
    while True:
        try:
            the_file = open(in_file, "r")
        except IOError:
            print "No such file."
        else:
            contents = the_file.read()
            the_file.close()
            result = str(datetime.datetime.today().strftime("%I:%M%p %A, %B %d, %Y\n"))
            result += "\n"
            for each in contents.split():
                word, punct = pl_translate(each)
                result += word+punct+" "
            result += "\n\nThank you for using the Pig Latin Translator!\n"
            try:
                the_file = open(os.getcwd()+"/translations/" + out_file, "w")
            except IOError:
                print "Error writing to file."
            else:
                print "\n" + "-"*15 + " Contents " + "-"*15 + "\n" + contents
                print "\n" + "-"*13 + " Translation " + "-"*14 + "\n" + result
                print "-"*40
                print "\nYou can find your translated text in the translations folder entitled:\n" \
                      + out_file
                the_file.write(result)
                the_file.close()
                break


#Main
vowels = ["a","e","i","o","u","y"]

while True:
    #Print directory's .txt files
    print "Here is a list of text files in your directory:"
    print "".join([each+"\n" for each in os.listdir(os.getcwd()) if ".txt" in each])

    #Get user input for .txt file in directory
    in_file = raw_input("\nPlease choose a file to open: ")
    if in_file in os.listdir(os.getcwd()):
        break
    else:
        print "ERROR: Please enter a text file from the directory.\n"

#Opens user's chosen file, translates to pig latin, and save translation to "[filename](pig).txt"
pl_file(in_file, in_file.replace(".", "(pig)."))
