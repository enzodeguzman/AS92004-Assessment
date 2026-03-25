# Functions
import random


# Test random addition (Print for testing)

x = (random.randint(15, 20))
y = (random.randint(25, 40))
print("Shows the x + y numbers and sum of numbers")
print(x)
print(y)
print(x + y)

# Define Functions

def yes_no(question) :
    while True:

        response = input(question).lower()

        # Checks for a yes or no response
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
           return "no"
        else:
            print("Please enter either yes or no.")


def introduction():
    print("""                     [---➗➕✖️ Welcome to the Math Quest! ✖️➕➗---]
    =====================================================================
    === This quiz will test your basic facts knowledge over multiple questions. ===
    ===       Try your best to get every question correct, and have fun!         ===
    =====================================================================
                                       Made by: Enzo de Guzman
    """)


def rules():
    print("""
                          
                                        [---📜 The Rules 📜---]
                                       
    =====================================================================
    ===   Rule 1.  Do not use any external help/services when solving the       ===
    ===   math problems (e.g a calculator)                                                  ===    
    ===                                                                                                     ===
    ===   Rule 2.  Answer each question with only the options provided            ===
    ===                                                                                                     ===
    ===   Rule 3.  Have fun                                                                         ===
    =====================================================================
    """)

def question1():
    answer1 = int(input(f"Question test. {x} + {y} =  "))
    if answer1 == x + y:
        print("yes")

    else:
        print("no")


# Print Introduction / Instructions / Title card
introduction()

# Asks for users name and stores response to use for a more personalised test.
name = input("Before we begin, Please enter your first name: ")
print(f"Hello {name}, Welcome to Math Quest.")


# Display the rules if the user wants to see them

want_rules = yes_no("Do you want to see the rules before we start?")

if want_rules == "yes" :
    rules()


# Start of Questions
question1()

