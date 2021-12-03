# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from datetime import datetime
import time
import random
import os
import sys
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Sims4-RealEstateQuiz-Leaderboard')

scores = SHEET.worksheet('scores')
data = scores.get_all_values()


def clear_terminal():
    """
    Clears terminal
    """
    os.system('clear')


def game_over():
    """
    Prints "Game Over" text and exits game.
    """
    print("\nThank you for playing! Dag dag!")
    print("""
 _____                        _____ 
|  __ \                      |  _  |               
| |  \/ __ _ _ __ ___   ___  | | | |_   _____ _ __ 
| | __ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
| |_\ \ (_| | | | | | |  __/ \ \_/ /\ V /  __/ |
 \____/\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|
""")

    time.sleep(3)
    sys.exit()


# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M
dt_string = now.strftime("%d/%m/%Y %H:%M")


print('''\u001b[32m
                @@@@@@@@@@@@@@@@@@@@
                @@@@@@@@@ * &@@@@@@@
                @@@@@@@. ,*( .@@@@@@
                @@@@@@  ,***(  @@@@@
                @@@@@ .,,***((/ @@@@
                @@@@ ,,,*****((( @@@
                @@@ ,,,******(((( #@
                @. ,,,,*******(((( .
                @, ((((///////%%%% .
                @@@ (((//////%%%% @@
                @@@@ (((/////%%% @@@
                @@@@@ *((///%%( @@@@
                @@@@@@  (///%  @@@@@
                @@@@@@@. (/% .@@@@@@
                @@@@@@@@& / &@@@@@@@
                @@@@@@@@@@@@@@@@@@@@
\u001b[0m''')

print("Sul sul!  Welcome to the Sims 4 Real Estate Quiz...\n")
print('''\u001b[32m===============================================\u001b[0m''')
name = input("Please enter your name:\n ")
time.sleep(1)
clear_terminal()
print('''\u001b[32m===============================================\u001b[0m''')
print("Thank you for stopping by, " + name)
print('''\u001b[32m===============================================\u001b[0m''')


class Question:
    """
    Questions instance, gets the question
    and the answer
    """
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
     "Who lives at Cypress Terrace in Willowcreek?\n \
     (a)The Spencer-Kim-Lewis family\n \
     (b)The Goth family\n \
     (c)The Pancakes Family\n ",

     "What is the neighbourhood where the Pancake family live called?\n \
     (a)Garden Essence\n \
     (b)Courtyard Lane\n \
     (c)Sage Estates\n ",

     "Who lives at Ophelia Villa?\n \
     (a)The Goth Family\n \
     (b)The Landgraab Family\n \
     (c)Judith Ward\n ",

     "Which Sims are in the BFF household?\n \
     (a)Miko Ojo, Akira Kibo, and Darling Walsh\n \
     (b)Maike Haas, Ulrike Faust\n \
     (c)Travis Scott, Liberty Lee, Summer Holiday\n ",

     "How much is the Goth family home worth at the start of the game?\n \
     (a)$256,807\n \
     (b)$254,721\n \
     (c)$228,639\n ",

     "In which world is Shady Acres one of the neighbourhoods?\n \
     (a)Oasis Springs\n \
     (b)Forgotten Hollow\n \
     (c)Strangerville\n ",

     "In which world do the Partihaus household live?\n \
     (a)San Myshuno\n \
     (b)Windenburg\n \
     (c)Britechester\n ",

     "Who owns the most expensive property in Windenburg?\n \
     (a)The Villareal Family\n \
     (b)The Fyres Family\n \
     (c)The Bjergsen Family\n ",

     "What is the name of the house where the Bjergsen Family live?\n \
     (a)Bjergsen House\n \
     (b)The Island\n \
     (c)The Lighthouse\n ",

     "Who lives at Slipshod Mesquite in Oasis Springs?\n \
     (a)Johnny Zest\n \
     (b)George Cahill\n \
     (c)Salim Benali\n ",

     "Penny Pizzazz lives in which neighbourhood of San Myshuno? \n \
     (a)Art Quarter\n \
     (b)Fashion District\n \
     (c)Uptown\n ",

     "What is the name of the house where the Hecking family live?\n \
     (a)Dogpaw Cottage\n \
     (b)Chateau Rosie\n \
     (c)It's A Good House\n ",

     "In which world would you find the Feng family?\n \
     (a)Willowcreek\n \
     (b)San Myshuno\n \
     (c)Del Sol Valley\n ",

     "Who lives at Cacti Casa in Oasis Springs?\n \
     (a)Zoe Patel, Mitchell Kalani, J Huntington III, Gavin Richards\n \
     (b)Travis Scott, Liberty Lee, Summer Holiday\n \
     (c)Katrina, Dina and Nina Caliente and Don Lothario\n ",

     "Who owns the cheapest house in Windenburg?\n \
     (a)The Free Spirits household\n \
     (b)The Bro household\n \
     (c)The Behr Family\n ",

     "In which world would you find The Pinnacles neighbourhood?\n \
     (a)Mt. Komorebi\n \
     (b)Oasis Springs\n \
     (c)Del Sol Valley\n ",

     "What is the name of George Cahill’s property in Strangerville?\n \
     (a)Old Rosie\n \
     (b)Old Penelope\n \
     (c)Old Smokey\n ",

     "What is the name of Catarina Lynx’s property in Brindleton Bay?\n \
     (a)Catscratch Cottage\n \
     (b)Catsclaw Cottage\n \
     (c)Whiskerman's Wharf\n",

     "Where is Isle of Volpe National Park?\n \
     (a)Sulani\n \
     (b)Selvadorada\n \
     (c)Henford-on-Bagley\n",

]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "c"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "c"),
    Question(question_prompts[6], "b"),
    Question(question_prompts[7], "a"),
    Question(question_prompts[8], "c"),
    Question(question_prompts[9], "a"),
    Question(question_prompts[10], "b"),
    Question(question_prompts[11], "c"),
    Question(question_prompts[12], "b"),
    Question(question_prompts[13], "a"),
    Question(question_prompts[14], "a"),
    Question(question_prompts[15], "c"),
    Question(question_prompts[16], "b"),
    Question(question_prompts[17], "a"),
    Question(question_prompts[18], "c"),
]


def run_quiz(questions):
    """
    Run the quiz. Start the timer.
    Randomise the questions.
    Keep track of score.
    Send score to leaderboard.
    """
    tic = time.perf_counter()
    score = 0
    sampled_list = random.sample(questions, 10)
    for sample in sampled_list:
        answer = input(sample.prompt).lower()
        if answer not in {'a', 'b', 'c'}:
            print('INVALID! Use \'a,\' \'b,\' or \'c\' for your response')
        elif answer == sample.answer:
            score += 1
            time.sleep(2)
            print("Well done, you are correct!")
        else:
            time.sleep(2)
            print("Sorry, you are incorrect!\n")

    toc = time.perf_counter()
    duration = str(round(toc - tic, 2))
    print("You got", score, "out of 10")
    time.sleep(1)
    print(f"You completed the quiz in {toc - tic:0.4f} seconds")
    time.sleep(2)
    print("\nWould you like to commit your score to the leaderboard, Y or N?")
    answer_end = input().lower()
    if answer_end == "y":
        time.sleep(1)
        print("Thank you.  Adding your score to the leaderboard...")
        scores = SHEET.worksheet('scores')
        scores.append_row(values=[name, score, dt_string, duration])
        scores.sort((2, 'des'), (4, 'des'),)
        time.sleep(1)
        print("Leaderboard updated successfully!\n")
        print('''\u001b[32m======================================\u001b[0m''')
        print("Press 'A' to restart the game\n")
        print("Press 'B' to view the leaderboard\n")
        print("Or press any key to exit the game.")
        print('''\u001b[32m======================================\u001b[0m''')
        answer_final = input().lower()
        if answer_final == "a":
            time.sleep(1)
            print("Veena frendishay.  Starting a new quiz...")
            run_quiz(questions)
        if answer_final == "b":
            clear_terminal()
            print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))
            time.sleep(5)
            print("Would you like to play the game now?\n")
            answer = (input("Press Y to start the game or any key to exit\n"))
            if answer == ("y"):
                print("Veena fredishay! Starting a new quiz...")
                time.sleep(1)
                clear_terminal()
                run_quiz(questions)
        else:
            print("Exiting the game...")
            time.sleep(1)
            game_over()
    else:
        time.sleep(1)
        print("Ok, thank you for playing, " + name)
        time.sleep(1)
        print("Exiting the game...")
        game_over()


def start_game():
    """
    Function to allow the player to choose what they want to do
    """
    print("What would you like to do today?\n")
    answer = (input("a) Start a new game\nb) View the leaderboard\nc)Exit\n"))

    if answer == ("a"):
        print("Veena fredishay! Starting a new quiz...")
        time.sleep(1)
        clear_terminal()
        run_quiz(questions)
    if answer == ("b"):
        print("Fetching the leaderboard...")
        time.sleep(1)
        clear_terminal()
        print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))
        time.sleep(5)
        print("Would you like to play the game now?\n")
        answer = (input("Press Y to start the game or any key to exit\n"))
        if answer == ("y"):
            print("Veena fredishay! Starting a new quiz...")
            time.sleep(1)
            clear_terminal()
            run_quiz(questions)
        else:
            print("Exiting the game...")
            time.sleep(1)
            game_over()
    else:
        print("Exiting the game...")
        time.sleep(1)
        game_over()


start_game()
