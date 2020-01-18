#Brett Byron, Group 1

#Assignment 1 (individual): Math Quiz Program
#Written by: Brett Byron
#Description: This program runs a math quiz consisting of 1 or more problems
#   involving operands between 1 and 10, 1 and 25, or 1 and 50 depending on
#   the user's difficulty choice.

import random

#Function to display header for number of quiz
def show_quizHead(num):
    #Show quiz number
    print "|" + "-"*24 + "|"
    if len(str(num)) == 2:
        print "|" + ("-"*7) + " Quiz #" + str(num) + " " + ("-"*7) + "|"
    else:
        print "|" + ("-"*8) + " Quiz #" + str(num) + " " + ("-"*7) + "|"
    print "|" + "-"*24 + "|"

#Function to prompt user for number of questions.
def get_numQuestions():
    #Get user input for # of questions
    while True:
        try:
            #Attempt to get integer from input
            questions = int(raw_input("How many questions would you like?: "))
        except ValueError as e:
            #If user doesn't enter integer...
            print "\nError:", e
            print "You must enter a number.\n"
        else:
            #If user enters integer, check if # is > 0
            if questions <= 0:
                #If user's integer is < 0, raise exception.
                try:
                    raise Exception("Invalid number of questions.")
                except:
                    print "You must have at least 1 question."
            else:
                break
    return questions

#Function to print a menu of available challenging levels
def show_levelMenu():
    #Show user the difficulty levels to choose from
    print "|" + "-"*24 + "|"
    print "|" + ("-"*8) + " Levels " + ("-"*8) + "|"
    print "|" + "-"*24 + "|"
    print "|1) Beginner" + " "*13 + "|"
    print "|2) Intermediate" + " "*9 + "|"
    print "|3) Advanced" + " "*13 + "|"
    print "|" + "-"*24 + "|"

#Function to obtain user's difficulty preference.
def get_userLevel():
    #Get user input for level difficulty
    while True:
        try:
            #Attempt to get integer from input
            level = int(raw_input("Choose your difficulty: "))
        except ValueError as e:
            #If user doesn't enter integer...
            print "\nError:", e
            print "You must enter 1, 2, or 3."
        else:
            #If user enters integer out of range...
            if level > 3:
                try:
                    #Raise exception for out of range level
                    raise Exception("No such level.")
                except:
                    print "You must enter 1, 2, or 3."
            elif level < 1:
                try:
                    #Raise exception for out of range level
                    raise Exception("No such level.")
                except:
                    print "You must enter 1, 2, or 3."
            else:
                break

    return level

#Function to set the range of operands according to difficulty level
def set_level(level):
    max_range = 0
    if level == 1:
        max_range = 10
    elif level == 2:
        max_range = 25
    else:
        max_range = 50

    return max_range

#Function to show a header containing the level of difficulty the user chose
def show_levelHeader(level):
    #Level dictionary for header printing...
    levels = {1:" Beginner ",2:" Intermediate ",3:" Advanced "}
    header = levels[level]
    header_len = len(levels[level])
    if header_len % 2 != 0:
        print "|" + "-"*24 + "|"
        print "|" + "-"*((24-header_len)/2) + header + "-"*((24-header_len)/2) + "|"
        print "|" + "-"*24 + "|"
    else:
        print "|" + "-"*24 + "|"
        print "|" + "-"*((24-header_len)/2) + header + "-"*((24-header_len)/2) + "|"
        print "|" + "-"*24 + "|"

#Function to show a menu containing the types of questions for the quiz
def show_typeMenu():
    print "|" + "-"*24 + "|"
    print "|" + "-"*3 + " Type of Question " + "-"*3 + "|"
    print "|" + "-"*24 + "|"
    print "|1) Addition" + " "*13 + "|"
    print "|2) Subtraction" + " "*10 + "|"
    print "|3) Multiplication" + " "*7 + "|"
    print "|4) Mixed" + " "*16 + "|"
    print "|" + "-"*24 + "|"

#Function to get user's quiz type choice
def quiz_type():
    #Dictionary with each question type
    type_dict = {"+":1,"-":2,"*":3,"mixed":4}
    #Get user input for question type
    while True:
        try:
            question_type = int(raw_input("What type of questions would you like? "))
        except ValueError as e:
            print "\nError:", e
            print "You must choose 1, 2, 3, or 4.\n"
        else:
            if question_type < 1 or question_type > 4:
                try:
                    raise Exception("Invalid question type.")
                except:
                    print "You must choose 1, 2, 3, or 4.\n"
            else:
                break

    return sorted(type_dict, key=type_dict.__getitem__), question_type-1

#Function to get user's answer, containing validation
def get_answer(num1, num2, q_type, question_type):
    while True:
        try:
            ans = int(raw_input("What is " + str(num1) + q_type[question_type] + str(num2) + "? "))
        except ValueError as e:
            print "\nError:", e
            print "Your answer must be an integer.\n"
        else:
            break
    return ans

#Function to print out correct output of quiz results
def outcome_msg(correct, total):
    if float(correct)/total > (3.0/4):
        print "Well done!"
    elif float(correct)/questions <= (3.0/4) and float(correct)/questions >= (1.0/2):
        print "You need more practice."
    else:
        print "Please ask your math teacher for help."

#Function to get user input in order to allow a new quiz without restart
def end_quiz():
    while True:
        again = raw_input("Would you like to take another quiz?\n"\
                          "Y/N: ")
        if again.lower() != "y" and again.lower() != "n":
            print "\nYou must enter \"Y\" or \"N\"\n"
        elif again.lower() == "y":
            print "\n"
            return True
        elif again.lower() == "n":
            print "\nKeep studying!"
            raw_input("Press enter to exit...")
            return False

#Function to calculate the answer according to the type of quiz question
def quiz(num1, num2, subject):
    if subject == 0:
        solution = num1 + num2
    elif subject == 1:
        solution = num1 - num2
    elif subject == 2:
        solution = num1 * num2

    return solution


#Main
quizzing = True     #Quiz loop flag
quiz_num = 0        #Quiz number
while quizzing:
    #Next quiz number
    quiz_num += 1
    #Shows quiz number header
    show_quizHead(quiz_num)
    #Number of correct answers
    correct = 0
    #Get user's input for number of questions in quiz
    questions = get_numQuestions()
    #Show menu for difficulty levels
    show_levelMenu()
    #Get user input for quiz difficulty level
    level = get_userLevel()
    #Set max range for random operands
    max_range = set_level(level)
    #Show menu for math qustion types
    show_typeMenu()
    #Get list of math question types, and user's choice of math question type
    q_type, selected = quiz_type()
    #Show header of user's difficulty level for beginning of quiz
    show_levelHeader(level)

    for i in range(questions):
        num1 = random.randint(1, max_range)
        num2 = random.randint(1, max_range)
        if selected == 3:
            question_type = random.randint(0,2)
            #Get user's answer
            answer = quiz(num1, num2, question_type)
        elif selected == 2:
            question_type = 2
            #Get user's answer
            answer = quiz(num1, num2, 2)
        elif selected == 1:
            question_type = 1
            #Get user's answer
            answer = quiz(num1, num2, 1)
        elif selected == 0:
            question_type = 0
            #Get user's answer
            answer = quiz(num1, num2, 0)

        #Calculate answer depending on operands and question type
            #Passes two operands, question type list, and the
            #   question type chosen for question output.
        ans = get_answer(num1, num2, q_type, question_type)

        if ans == answer:
            print "That's right -- well done.\n"
            correct += 1
        else:
            print "No, I'm afriad the answer is ", answer, "\n"

    print "\nI asked you " + str(questions) + " questions. You got " \
          + str(correct) + " of them right."

    #Print output statement according to ratio of
    #   correct answers to total questions asked.
    outcome_msg(correct, questions)

    #Allow user to end quiz, or take another.
    quizzing = end_quiz()


    
