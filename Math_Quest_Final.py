# ==============================================
# MATH QUEST - AS92004 - ASSESSMENT 2026
# Created by: Enzo de Guzman - L1DIG26
# ==============================================

# Functions
import random


# Game History / Results
game_history = []
question_number = 0

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
        if response == "a" or response == "A":
            return "a"
        elif response == "b" or response == "B":
           return "b"
        else:
            print("⚠️ Please enter either A or B.")

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
    input("""Thank you for playing Math Quest.
     
     Please press [enter] if you would like to see your game history.""")

    print("===== Game History ===========")

    for result in game_history:
        print(result)


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
   global question_number

   question_number += 1

   first_int = random.randint(15, 20)
   second_int = random.randint(25, 40)

   correct_answer = first_int + second_int

   # Check if answer meets conditions
   while True:
       user_input = input(f"Question {question_number}: {first_int} + {second_int} = ")

       if user_input == "":
           print("⚠️ Enter a integer")
           continue

       try:
           user_answer = int(user_input)
           break
       except:
           print("⚠️ Integers only")

   # Check if the answer is correct
   if user_answer == correct_answer:
       print(random.choice(good_list))
       result = "Pass"
   else:
       print(random.choice(bad_list))
       result = "Fail"

   # Saves game history
   game_history.append(
       f"Question {question_number} | Pass/Fail: ({result}) | Your Answer: ({user_answer}) | Correct: ({correct_answer})"
   )



# Define game modes. One question / Infinite
def infinite_game():
   while True:
       get_question()

       if yes_no("Would you like another question? ") == "no":
           break

   end_game()


def standard_game():
    while True:
        user_input = input("How many questions do you want? (1 - 10) ")

        if user_input == "":
            print("⚠️ Please enter a integer")
            continue

        try:
            how_many_questions = int(user_input)

            if 1 <= how_many_questions <= 10:
                break
            else:
                print("⚠️ Please enter a number between 1 - 10")
        except:
            print("⚠️ Please enter a integer")

    for i in range(how_many_questions):
        get_question()

    if yes_no("Would you like to continue to infinite mode? ") == "yes":
        infinite_game()
    else:
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

      [ A. Standard Game ]                [ B. Infinite ]
      
      
============= Enter either 'a' or 'b' ==============

""")

if game == "a":
    standard_game()
elif game == "b":
    infinite_game()
