#Assignment 5, individual(2/2): Book Catalog
#Brett Byron, Group 1

import xml.etree.ElementTree as ET

#Prints the title, author and price of book with "book_id"
def book_info(book_id):
    root = ET.parse(source="books.xml")

    #Get books from book id
    books = [item for item in root.findall("BOOK") if item.items()[0][1] == book_id]

    #Print out book info
    for book in books:
        print " " + "-"*80
        print "| " + str("Title").center(38) + " | " + \
              str("Author").center(21) + " | " + \
              str("Price").center(13) + " |"
        print "| " + book.find("TITLE").text.ljust(38) + " | " +\
              book.find("AUTHOR").text.center(21) + " | " + \
              str("$"+book.find("PRICE").text).center(13) + " |"

#Main
root = ET.parse(source="books.xml")

#List of book ids
book_ids = [item.items()[0][1] for item in root.findall("BOOK")]

#Call book_info() for all book ids
for book_id in book_ids:
    book_info(book_id)
print " " + "-"*80

#Get total cost of Computer books
computer_cost = sum([float(item.find("PRICE").text) for item in root.findall("BOOK") if item.find("GENRE").text == "Computer"])

#Print total cost of Computer books
print "\nThe summed cost of every Computer book is $" + str(computer_cost)

#Get each unique genre of book
genres = set([item.text for item in root.findall("BOOK/GENRE")])

print "\nThe genres included are:"
for genre in genres:
    print "\t\t" + genre
