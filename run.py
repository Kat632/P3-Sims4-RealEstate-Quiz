# Developer: Katherine Biggs
# Date of release: TBA
# Subject: Code Institute Portfolio Project 3 - Python
# Program Name: "The Sims 4 Real Estate Quiz"

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
    os.system('printf "\ec"')


def game_over():
    """
    Prints "Game Over" text and exits game.
    """
    print("\nThank you for playing! Dag dag!")
    print('''\u001b[32m
 _____                        _____ 
|  __ \                      |  _  |               
| |  \/ __ _ _ __ ___   ___  | | | |_   _____ _ __ 
| | __ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
| |_\ \ (_| | | | | | |  __/ \ \_/ /\ V /  __/ |
 \____/\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|
\u001b[0m''')

    time.sleep(3)
    print("Click the blue button at the top to replay the game!")
    print()
    sys.exit()


# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M
dt_string = now.strftime("%d/%m/%Y %H:%M")


def run_instructions():
    """
    Prints the instructions for the game
    """
    print("This game is based on Sims 4, the social simulation video game,")
    print("released in 2014.  If you have never played Sims 4, you may find")
    print("this game difficult since it is a quiz game where all of the")
    print("questions are based around real estate and worlds in Sims 4.")
    print()
    print('''\u001b[32m===========================================\u001b[0m''')
    print("1. All you need to do is press a, b or c for your answer.")
    print("2. The program will tell you if you are correct or incorrect.")
    print("3. The program will add up your scores.")
    print("4. The program tells you your score at the end.")
    print("5. The game is also timed.")
    print("6. You will be able to save your score to the leaderboard.")
    print('''\u001b[32m===========================================\u001b[0m''')
    print()
    print("*****     Simlish Translations     *****")
    print()
    print("          Sul sul = Hello               ")
    print("          Dag dag = Goodbye             ")
    print("          Veena frendishay = Let's play ")
    print()
    print('''\u001b[32m===========================================\u001b[0m''')
    print()


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
name = input("Please enter your name:\n")
time.sleep(1)
clear_terminal()
print('''\u001b[32m===============================================\u001b[0m''')
if any(c.isalpha() for c in name):
    print("Thank you for stopping by, " + name)
else:
    print("Thank you for stopping by, Guest")
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

     "Where is The Caboose?\n \
     (a)Brindleton Bay\n \
     (b)Strangerville\n \
     (c)Evergreen Harbor\n",

     "Where is Larry's Lagoon?\n \
     (a)Britechester\n \
     (b)Brindleton Bay\n \
     (c)Sulani\n",

     "Where does the Charm household live?\n \
     (a)Magic Mansion\n \
     (b)Rock Ridge Canyon\n \
     (c)Creek Side Corner\n",

     "Who lives in the cheapest property in the game?\n \
     (a)George Cahill\n \
     (b)Johnny Zest\n \
     (c)Vanessa Jeong\n",

     "Who owns the most expensive property in Sims 4?\n \
     (a)The Bailey-Moon Family\n \
     (b)Judith Ward\n \
     (c)The Villareal Family\n",

     "The Crawdad Quarter neighbourhood is in which world?\n \
     (a)Willow Creek\n \
     (b)Brindleton Bay\n \
     (c)Sulani\n",

     "Where is Magnolia Blossom Park?\n \
     (a)San Myshuno\n \
     (b)Willow Creek\n \
     (c)Newcrest\n",

     "Where is The Blue Velvet nightclub?\n \
     (a)Willow Creek\n \
     (b)Windenburg\n \
     (c)San Myshuno\n",

     "Who pays the most rent in San Myshuno?\n \
     (a)Diego Lobo\n \
     (b)The Karaoke Legends\n \
     (c)Victor and Lily Feng\n",

     "Who owns The Gnome's Arms?\n \
     (a)Candy and Yuki Behr\n \
     (b)Arun Bheeda and Jesminder Bheeda\n \
     (c)Sara and Simon Scott\n",

     "Who lives at Journey’s End in Sulani?\n \
     (a)Mele and Alike Kahananui\n \
     (b)Keala Hoapili and Lia Hauata\n \
     (c)Kado, Jenna, Taku and Miki Akiyama\n",

     "Who does Francine Spencer live with?\n \
     (a)The Spencer-Kim-Lewis family\n \
     (b)The Greenburg Family\n \
     (c)The Harris Family\n",

     "Where is the venue called Waterside Warble?\n \
     (a)Windenburg\n \
     (b)San Myshuno\n \
     (c)Brindleton Bay\n",

     "Who lives at Straud Manor?\n \
     (a)Count Vladislaus Straud IV\n \
     (b)Count Vladimir Straud III\n \
     (c)Sir Vladislaus Strauss IV\n",

     "Who is the A New Start household?\n \
     (a)Penny Pizzazz\n \
     (b)Cecilia Kang\n \
     (c)Vanessa Jeong\n",

     "Who lives at Dock Den in Windenburg?\n \
     (a)Brent and Brant Hecking\n \
     (b)Candy and Yuki Behr\n \
     (c)Joaquin Le Chien, Sergio Romeo\n",

     "Parched Prospect is a neighbourhood in which world?\n \
     (a)Strangerville\n \
     (b)Oasis Springs\n \
     (c)Sulani\n",

     "The missing housemate: Marcus Flex, Pablo Rocca, Jade Rosa and ???\n \
     (a)Eva Capricciosa\n \
     (b)Sergio Romeo\n \
     (c)Jules Rico\n",

     "Who lives at Pigulock Manor?\n \
     (a)The Watson Family\n \
     (b)The Tinker Family\n \
     (c)The Scott Family\n",

     "What is the name of the child in the Bailey-Moon family?\n \
     (a)Blue\n \
     (b)Yellow\n \
     (c)Orange\n",

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
    Question(question_prompts[19], "c"),
    Question(question_prompts[20], "a"),
    Question(question_prompts[21], "b"),
    Question(question_prompts[22], "c"),
    Question(question_prompts[23], "b"),
    Question(question_prompts[24], "a"),
    Question(question_prompts[25], "b"),
    Question(question_prompts[26], "a"),
    Question(question_prompts[27], "c"),
    Question(question_prompts[28], "c"),
    Question(question_prompts[29], "a"),
    Question(question_prompts[30], "c"),
    Question(question_prompts[31], "b"),
    Question(question_prompts[32], "a"),
    Question(question_prompts[33], "b"),
    Question(question_prompts[34], "c"),
    Question(question_prompts[35], "b"),
    Question(question_prompts[36], "a"),
    Question(question_prompts[37], "b"),
    Question(question_prompts[38], "c"),
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
            time.sleep(2)
            print()
            print('INVALID! Use \'a,\' \'b,\' or \'c\' for your response')
            print('Moving on to next question...')
            time.sleep(2)
            print()
        elif answer == sample.answer:
            score += 1
            time.sleep(2)
            print()
            print("Well done, you are correct!")
            print()
        else:
            time.sleep(2)
            print()
            print("Sorry, you are incorrect!\n")
            print()

    toc = time.perf_counter()
    duration = str(round(toc - tic, 2))
    print("You got", score, "out of 10")
    time.sleep(1)
    print(f"You completed the quiz in {toc - tic:0.2f} seconds")
    time.sleep(2)
    print("\nWould you like to commit your score to the leaderboard, Y or N?")
    print("Or press any other key to exit the game.")
    answer_end = input().lower()
    if answer_end == "y":
        time.sleep(1)
        print("Thank you.  Adding your score to the leaderboard...")
        scores = SHEET.worksheet('scores')
        scores.append_row(values=[name, score, dt_string, duration])
        scores.sort((2, 'des'), (4, 'asc'),)
        time.sleep(1)
        print("Leaderboard updated successfully!\n")
        print('''\u001b[32m======================================\u001b[0m''')
        print("Press 'A' to restart the game\n")
        print("Press 'B' to view the Top Ten scores\n")
        print("Press 'M' to go back to the main menu\n")
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
            answer = (input("Press Y to start the game,\
        M for main menu, or any key to exit\n")).lower()
            if answer == ("y"):
                print("Veena fredishay! Starting a new quiz...")
                time.sleep(1)
                clear_terminal()
                run_quiz(questions)
            if answer == ("m"):
                print("Returning to main menu...")
                time.sleep(1)
                clear_terminal()
                start_game()
            else:
                print("Exiting the game...")
                time.sleep(2)
                clear_terminal()
                game_over()
        if answer_final == "m":
            print("Returning to main menu...")
            time.sleep(1)
            clear_terminal()
            start_game()
        else:
            print("Exiting the game...")
            time.sleep(2)
            clear_terminal()
            game_over()
    else:
        time.sleep(1)
        print("Ok, thank you for playing, " + name)
        time.sleep(1)
        print("Exiting the game...")
        time.sleep(2)
        clear_terminal()
        game_over()


def start_game():
    """
    Function to allow the player to choose what they want to do
    """
    print('''\u001b[32m==========================================\u001b[0m''')
    print()
    print("What would you like to do today?\n")
    print('''\u001b[32m==========================================\u001b[0m''')
    answer = (input("a) Start a new game\nb) View the Top Ten scores\n\
c) View the instructions\nPress any other key to end the game\n").lower())

    if answer == ("a"):
        print("Veena fredishay! Starting a new quiz...")
        time.sleep(1)
        clear_terminal()
        run_quiz(questions)
    if answer == ("b"):
        print("Fetching the leaderboard...")
        time.sleep(1)
        clear_terminal()
        print(tabulate(data[0:11], headers='firstrow', tablefmt='fancy_grid'))
        time.sleep(5)
        answer = (input("Press Y to start the game,\
    M for main menu, or any key to exit\n")).lower()
        if answer == ("y"):
            print("Veena fredishay! Starting a new quiz...")
            time.sleep(1)
            clear_terminal()
            run_quiz(questions)
        if answer == ("m"):
            print("Returning to main menu...")
            time.sleep(1)
            clear_terminal()
            start_game()
        else:
            print("Exiting the game...")
            time.sleep(2)
            clear_terminal()
            game_over()
    if answer == ("c"):
        print("One moment please...")
        time.sleep(1)
        clear_terminal()
        run_instructions()
        time.sleep(8)
        answer = (input("Press Y to start the game,\
    M for main menu or any key to exit\n")).lower()
        if answer == ("y"):
            print("Veena fredishay! Starting a new quiz...")
            time.sleep(1)
            clear_terminal()
            run_quiz(questions)
        if answer == ("m"):
            print("Returning to main menu...")
            time.sleep(1)
            clear_terminal()
            start_game()
        else:
            print("Exiting the game...")
            time.sleep(2)
            clear_terminal()
            game_over()

    else:
        print("Exiting the game...")
        time.sleep(2)
        clear_terminal()
        game_over()


start_game()
