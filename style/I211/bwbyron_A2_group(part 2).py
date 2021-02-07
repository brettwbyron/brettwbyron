#Brett Byron, Group 1
#Homeword 2, Group Word: Problem 1; Real Numbers

print "The sum of REAL numbers is " + str((sum([int(each.strip("REAL: ").strip()) for each in open("HW 2 Sample.txt", "r").readlines() if "REAL" in each]))) + "."
