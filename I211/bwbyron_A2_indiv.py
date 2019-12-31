#Homework 2, Individual: Personnel File
#Written by: Brett Byron (Group 1)

#Description: Using list comprehension and the tools.py modules,
#this program reads in a file of names and ages, and prints them out in a table

from tools import *

table_print(["Name", "Age"], [each.split() for each in open("people.txt", "r").read().split("\n")])
