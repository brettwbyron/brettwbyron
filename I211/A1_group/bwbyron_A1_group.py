#Brett Byron, Evan Russell: Group 1


#Program: Text File Analysis
#Written by: Brett Byron

def get_file():
    #Empty string to hold file contents
    contents = ""

    #Open the file with error handling
    try:
        the_file = open("sample.txt", "r")
    except IOError as e:
        print "ERROR:", e
    else:
        #Read the contents of the file into the string variable
        contents = the_file.read()
        the_file.close()

    #Return the contents of the file in all lowercase letters
    return contents.lower()

def get_letters(contents):
    #Characters allowed
    allowed = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
               "q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5",
               "6","7","8","9","0",".",",","-"]

    #Removing characters not listed in the allowed characters list
    contents = [char for char in contents for other in allowed if char == other]

    #Lists for letters and frequencies of those letters
    letters = []
    frequencies = []

    #For each allowed character in the file's contents
    for char in contents:
        #If the character is not yet in the letters list, add the letter
        if char not in letters:
            letters.append(char)
            frequencies.append(1)

        #If the character is already in the letters list, add 1 to the frequency
        #of that letter
        else:
            index = letters.index(char)
            frequencies[index] += 1

    #Create dictionary to sort both lists in sync
    letter_dict = dict(zip(letters, frequencies))
    letters = sorted(letter_dict, key=letter_dict.__getitem__, reverse = True)
    frequencies = sorted(letter_dict.values(), reverse=True)

    #Return two sorted lists, the unique letters and their relative frequencies
    return letters, frequencies

def get_words(letters, contents):
    #Splitting the files contents by whitespace
    contents = contents.split()

    #Lists for words and frequencies of those words
    words = []
    frequencies = []

    #For each word in the files contents
    for each in contents:
        #If the word is not yet in the words list, add the word
        if each not in words:
            words.append(each)
            frequencies.append(1)
        #If the word is already in the words list, add 1 to the frequency
        #of that word.
        else:
            index = words.index(each)
            frequencies[index] += 1

    #Create dictionary to sort both lists in sync
    word_dict = dict(zip(words, frequencies))
    words = sorted(word_dict, key=word_dict.__getitem__, reverse=True)
    frequencies = sorted(word_dict.values(), reverse=True)

    #Return two sorted lists, the unique words and their relative frequencies
    return words, frequencies

def most_common(words, frequencies):
    #Dictionary for word distribution
    distribution = {}
    #Most common word(s)
    common = []

    #'zip()' joins the indecies of both lists into a list of tuples
    dist_list = zip(frequencies, words)

    #Get the index for any words with the max frequency and append
    #the tuple from the list 'dist_list' to the most common words list
    for index, freq in enumerate(frequencies):
        if freq == max(frequencies):
            common.append((dist_list[index]))

    #Return a list of one or more of the most common word
    return common

def format_content(letter_lst, letter_dst, word_lst, word_dst, most_freq):
    #Empty string to add formatted text into
    formatted = ""

    #Add header to formatted output
    formatted += "|" + "-"*40 + "|\n"
    formatted += "|" + "-"*14 + " Statistics " + "-"*14 + "|\n"
    formatted += "|" + "-"*40 + "|\n"
    formatted += "|" + " "*40 + "|\n"

    #Format letter distribution
    letters = "|" + "-"*40 + "|\n"
    letters += "|" + "-"*9 + " Letter Distributions " + "-"*9 + "|\n"
    letters += "|" + "-"*14 + " " \
               + str(len(letter_lst)) + " Letters " \
               + "-"*14 + "|\n"
    letters += "|" + "-"*40 + "|\n"
    for num, (letter, dist) in enumerate(zip(letter_lst, letter_dst), start=1):
        right_border = 24 - (len(str(num)) + len(letter) + len(str(dist)))
        letters += "|" + str(num)
        letters += ")\t" + str(letter)
        letters += ": " + str(dist)
        letters += " "*right_border + "\t |\n"
    letters += "|" + "-"*40 + "|\n"
    letters += "|" + " "*40 + "|\n"

    #Format word distribution
    words = "|" + "-"*40 + "|\n"
    words += "|" + "-"*10 + " Word Distributions " + "-"*10 + "|\n"
    words += "|" + "-"*15 + " " \
               + str(len(word_lst)) + " Words " \
               + "-"*14 + "|\n"
    words += "|" + "-"*40 + "|\n"
    for num, (word, dist) in enumerate(zip(word_lst, word_dst), start=1):
        right_border = 24 - (len(str(num)) + len(word) + len(str(dist)))
        words += "| " + str(num)
        words += ")\t" + str(word)
        words += ": " + str(dist)
        if len(str(num)) > 2:
            words += " "*right_border + "\t\t |\n"
        else:
            words += " "*right_border + "\t |\n"
    words += "|" + "-"*40 + "|\n"
    words += "|" + " "*40 + "|\n"

    #Format most frequent word(s)
    freq = "|" + "-"*40 + "|\n"
    freq += "|" + "-"*9 + " Most Frequent Word(s) " + "-"*8 + "|\n"
    freq += "|" + "-"*40 + "|\n"
    for i in range(len(most_freq)):
        right_border = 24 - (len(str(i+1)) +
                             len(most_freq[i][1]) +
                             len(str(most_freq[i][0])))
        freq += "| " + str(i+1)
        freq += ")\t" + str(most_freq[i][1])
        freq += ": " + str(most_freq[i][0])
        freq += " "*right_border + "\t |\n"
    freq += "|" + "-"*40 + "|\n"

    #Add all formatted strings to final string
    formatted += letters
    formatted += words
    formatted += freq

    return formatted


def save_file(content):
    try:
        the_file = open("statistics.txt", "w")
    except IOError as e:
        print "ERROR:", e
    else:
        the_file.write(content)
        the_file.close()


#Main

#Get contents of the file as a string
contents = get_file()
letters, letter_dist = get_letters(contents)
words, word_dist = get_words(letters, contents)
most_freq = most_common(words, word_dist)
formatted = format_content(letters, letter_dist, words, word_dist, most_freq)
save_file(formatted)
