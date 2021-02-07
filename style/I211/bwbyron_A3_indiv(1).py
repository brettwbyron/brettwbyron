#Assignment 3, Individual: Timing Recursion
#Brett Byron, Group 1

import time

##I couldn't find the fibonacci and factorial functions in the sample code,
##  or within the homework Word documents, so I've written my own.


#Factorial function
def factorial(num):
    if(num == 1):   #base case
        return 1
    else :
        return num * factorial(num - 1)

#Fibonacci function
def fibonacci(num):
    if(num == 0) or (num == 1):	#base cases
        return 1
    else :
        return fibonacci(num - 1) + fibonacci(num - 2)


#Functions I wrote..

###Fibonacci function
##def fib(num):
##    if num < 2:
##        return num
##    else:
##        return fib(num - 1) + fib(num - 2)
##
###Factorial function
##def fact(num):
##    if num > 2:
##        return num * fact(num - 1)
##    else:
##        return num


#Get user's upper bound
while True:
    try:
        upper = int(raw_input("Please enter an upper bound (int): "))
    except ValueError:
        print "That's not an integer."
    else:
        if upper < 0:
            try:
                raise Exception("")
            except:
                "Integer must be non-negative."
        else:
            break

#Calculate numbers and timing
while True:
    calc = raw_input("Please enter FIB for fibonacci or FACT for factorial: ")
    if calc.lower() == "fib" or calc.lower() == "fact":
        start = time.time()
        for i in range(1, upper+1):
            if calc.lower() == "fib":
                fib_num = fibonacci(i)
                print "Calculating fibonacci(" + str(i) + ") = " + str(fib_num) + \
                      " took: " + str(time.time() - start) + " seconds."
            elif calc.lower() == "fact":
                fact_num = factorial(i)
                print "Calculating factorial(" + str(i) + ") = " + str(fact_num) + \
                      " took: " + str(time.time() - start) + " seconds."
        print "Total time: " + str(time.time() - start) + " seconds."
        break
    else:
        continue
