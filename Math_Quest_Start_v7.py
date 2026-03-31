# ==============================================
# MATH QUEST - AS92004 - ASSESSMENT 2026
# Created by: Enzo de Guzman - L1DIG26
#
# 148 3 to the 3, 6 to the 9 representing the DIG,
# What up GEEZER, leave at the tone.
# ==============================================

# Functions
import random


# Test random addition/other (TESTING ONLY)

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
            print("⚠️ Please enter either yes or no.")

def a_b(question) :
    while True:

        response = input(question).lower()

        # Checks for a yes or no response
        if response == "a":
            return "a"
        elif response == "b":
           return "b"
        else:
            print("Please enter either A or B.")

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
    ===   Rule 2.  Answer each question with only integers                              ===
    ===                                                                                                     ===
    ===   Rule 3.  Please use font size 15pt as this program was                    ===
    ===   designed for it.                                                                             ===
    =====================================================================
    """)

def end_game():
    print("""Thank you for playing Math Quest.
     
     Please press [enter] if you would like to see your game history.""")


# Print Introduction / Instructions / Title card
introduction()

# Asks for users name and stores response to use for a more personalised test.
name = input("Before we begin, Please enter your username: ")
print(f"Hello {name}, Welcome to Math Quest.")


# Different Responses to passing/failing questions

good_list = [f"✅ {name}, That is Correct!", f"Well done {name} 👍", "☑️☑️☑️", f"✅ That's right {name}, You are on a roll! ✅"]

bad_list = [f"❌ {name}, That is Incorrect!", "Incorrect Answer 👎", f"❌ I thought you were better than this {name}.", f"❌ That's wrong! Try harder next time {name}. ❌"]

# Question generator / Question functions

def get_question():
    first_int = (random.randint(15, 20))
    second_int = (random.randint(25, 40))

    answer = int(input(f"{first_int} + {second_int} = "))

    if answer == first_int + second_int:
        print(random.choice(good_list))
    else:
        print(random.choice(bad_list))

    get_question()


# Define game modes. One question / Infinite
def infinite_game():
    get_question()

def standard_game():
    standard_first_int = (random.randint(500, 2000))
    standard_second_int = (random.randint(500, 4000))

    answer = int(input(f"{standard_first_int} + {standard_second_int} = "))

    if answer == standard_first_int + standard_second_int:
        print(random.choice(good_list))
    else:
        print(random.choice(bad_list))

# Request Infinite mode else end the game.

    play_inf = yes_no("Would you like to continue to infinite mode?")
    if play_inf == "yes":
        infinite_game()
    elif play_inf == "no":
        end_game()


# Print responses for testing random function. (TESTING)
# print(random.choice(good_list))
# print(random.choice(bad_list))

# Display the rules if the user wants to see them

want_rules = yes_no("Do you want to see the rules before we start?")

if want_rules == "yes" :
    rules()

# Game mode selection
game = a_b("""
===== Which game mode would you like to play? =====

      [ A. One Question ]                   [ B. Infinite ]
      
      
============= Enter either 'a' or 'b' ==============

""")

if game == "a":
    standard_game()
elif game == "b":
    infinite_game()



