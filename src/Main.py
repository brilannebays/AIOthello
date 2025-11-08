# Desc:

# TO-DO:
# - display menu
# - give user option for color at beginning of game
# - create board
# - create player
# - create AI player

from BoardMngmt import Board
from PlayerMngmt import Player
from GameplayMngmt import Gameplay

def main():
    board = Board()
    initBoard = board.create()

    print("Welcome to Othello. ")
    print("Would you like to play against SELF or AI?")
    opponent = input()

    print("Your opponent is " + opponent + ".")
    print("Would you like to play BLACK or WHITE? Note that BLACK will go first.")
    pieceColor = input()


    if opponent.upper() in ["AI", "SELF"]:

        # player1 will always be first because player1 always has BLACK
        if pieceColor == "BLACK":
            player2 = Player(opponent, "WHITE", board)
            player1 = Player("SELF", pieceColor, board)
        else:
            player1 = Player(opponent, "BLACK", board)
            player2 = Player("SELF", pieceColor, board)

    board.display(initBoard)

    newGame = Gameplay(player1, player2, board, initBoard)
    newGame.runGame()




if __name__ == "__main__":
    main()


