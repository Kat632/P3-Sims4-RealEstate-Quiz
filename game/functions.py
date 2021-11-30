import os
import sys


def clear_terminal():
    # Clears terminal.
    os.system('clear')


def game_over():
    # Prints "Game Over" text and exits game.
    print("\nThank you for playing! Dag dag!")
    print("""
 _____                        _____               
|  __ \                      |  _  |               
| |  \/ __ _ _ __ ___   ___  | | | |_   _____ _ __ 
| | __ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
| |_\ \ (_| | | | | | |  __/ \ \_/ /\ V /  __/ |   
 \____/\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|
""")
    
    print"\nWould you like to commit your score to the leaderboard?"
    sys.exit()