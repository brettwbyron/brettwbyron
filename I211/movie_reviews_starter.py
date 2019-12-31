from tools import *

def find_reviews(title, sequence):
    rev = []

    #find the correct reviews here

    return rev

def movie_names(sequence):
    print "We have reviews for the following movies:"

    #print out the available movies

all_reviews = [("Frozen", 4, "My kids loved it."), ("Frozen", 3, "The music is stuck in my head!"), \
               ("X:Men", 4, "It was a little confusing."), ("X:Men", 2, "I don't like superheroes."), \
               ("X:Men", 5, "Great action scenes!"), ("It", 1, "Clowns are scary!")]

while True:
    movie = raw_input("Please enter a movie name to see its reviews or Enter to stop: ")

    #fill in the rest here. You'll want to use table_print from tools as follows:
    #table_print(("Name", "Rating", "Comments", <something goes here!>)
