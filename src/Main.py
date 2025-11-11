# Name: Brilanne Bays
# Student ID: 10393040
# Date Due: 11/11/25
# Date Completed: 11/8/25
# Assignment #3
# Description: Main is the entry point to the game Othello. A player is able to choose whether to play against themselves
# or an AI player. The player can also choose to go first (black), or yield to AI (white). The program utilizes the 
# Minimax algorithm with alpha-beta pruning for the AI. The player is allowed to exit the game at any point by typing 
# 'stop' into the console, which returns the player to the main menu. 

from BoardMngmt import Board
from PlayerMngmt import Player
from GameplayMngmt import Gameplay
import os 
import sys

def restart():
    python = sys.executable 
    os.execl(python, python, *sys.argv)

def main():
    print()
    print("Welcome to Othello. ")

    while True:

        # validate user choice for opponent
        print("Would you like to play against SELF or AI?")
        opponent = input()
        print()

        if opponent.upper() == "STOP":
            restart()

        if opponent.upper() in ["AI", "SELF"]:
            print("Your opponent is " + opponent.upper() + ".")
        else:
            print("Invalid: must choose either SELF or AI.")
            continue

        # validate user choice for color
        print("Would you like to play BLACK or WHITE? Note that BLACK will go first.")
        pieceColor = input()
        print()

        if pieceColor.upper() == "STOP":
            restart()

        if pieceColor.upper() in ["BLACK", "WHITE"]:
            print("Your color is " + pieceColor.upper() + ".")
            print()
        else:
            print("Invalid: must choose either BLACK or WHITE.")
            continue

        # create the players
        if opponent.upper() in ["AI", "SELF"]:

            # player1 is always BLACK, player 2 is always WHITE
            if pieceColor == "BLACK":
                player2 = Player(opponent, "WHITE")
                player1 = Player("SELF", pieceColor)
            else:
                player1 = Player(opponent, "BLACK")
                player2 = Player("SELF", pieceColor)


        # initialize game state
        board = Board()
        initBoard = board.create()
        board.display(initBoard)

        newGame = Gameplay(player1, player2, board, initBoard)
        newGame.runGame()


# execute all
if __name__ == "__main__":
    main()


