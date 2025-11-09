# Brilanne Bays
# Desc:

# TO-DO:
# - ask player for input
# - check input validity 
# - update board state after each move
# - detect win/loss conditions
# - display scores
# - display winner and loser
# - manage turns 
from MovePrediction import minimax
import copy 

class Gameplay:
    def __init__(self, player1, player2, boardObject, initializedBoard):
        self.player1 = player1
        self.player2 = player2
        self.board = boardObject
        self.matrix = initializedBoard 
    
    def runGame(self):
        running = True
        currentPlayer = self.player1
        nextPlayer = self.player2

        while running:
            if currentPlayer.identity == "SELF":
                row, column = currentPlayer.move(self.matrix)
                toFlip = self.board.legalize(self.matrix, currentPlayer.color, row, column)

                if len(toFlip) == 0:
                    print("Invalid move. Please try again. ")
                    continue

                self.board.updateBoard(self.matrix, currentPlayer.color, toFlip, row, column)
                self.board.display(self.matrix)
                self.board.score(self.matrix)
                print(" ")

            elif currentPlayer.identity == "AI":
                print(currentPlayer.identity + "thinking...")

                copyCurrentMatrix = copy.deepcopy(self.matrix)

                evaluation, bestMove = minimax(copyCurrentMatrix, 4, True, -999999, 999999, currentPlayer.color)

                if bestMove:
                    print(str(bestMove))
                    row = bestMove[0]
                    column = bestMove[1]
                    toFlip = self.board.legalize(self.matrix, currentPlayer.color, row, column)

                    if len(toFlip) == 0:
                        print("Invalid move. Please try again. ")
                        continue

                    self.board.updateBoard(self.matrix, currentPlayer.color, toFlip, row, column)
                    self.board.display(self.matrix)
                    self.board.score(self.matrix)
                    print(" ")
                else:
                    print("There wasn't a best move")

            temp = currentPlayer
            currentPlayer = nextPlayer
            nextPlayer = temp



