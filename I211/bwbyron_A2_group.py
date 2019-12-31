#Brett Byron, Group 1
#Homework 2, Group Work: Problem 1; Number & Letter Filter

string = "Hello 34215 World 5620 From 384 Bloomington"
#print str(" | ".join(["".join([letter for letter in string if letter.isalpha() or letter.isspace()]), "".join(sorted([num for num in string if num.isdigit()]))])).replace("  ", " ")

print "".join(x for x  in string if not x.isdigit()) +" | "+ "".join(sorted(x for x  in string if x.isdigit() ))
