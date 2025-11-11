# Handles gameplay, alternates players, runs the game

import MovePrediction
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
        global statesExamined
        debugBool = False
        pruningSwitch = False
        outputFile = "minimaxSequences.txt"

        # game loop
        while running:

            # if player is the user, get and validate their move, update and display board, calculate score, and yield to next player
            if currentPlayer.identity == "SELF":
                # To do: predict possible moves
                listPotentialMoves = self.board.getPotentialMoves(self.matrix, currentPlayer.color)
                
                if len(listPotentialMoves) > 0:
                    row, column = currentPlayer.move(self.matrix)
                    toFlip = self.board.legalize(self.matrix, currentPlayer.color, row, column)

                    if len(toFlip) == 0:
                        print("Invalid move. Please try again. ")
                        continue

                    self.board.updateBoard(self.matrix, currentPlayer.color, toFlip, row, column)
                    self.board.display(self.matrix)
                    self.board.score(self.matrix)
                    print(" ")
                
                else:
                    print("There wasn't a move available. Yielding to other player...")

            # if player is AI, copy current board, use mini max and alpha beta pruning to return a move, update board,
            # calculate score, yield to next player
            elif currentPlayer.identity == "AI":
                debugBool = currentPlayer.askDebug()
                pruningSwitch = currentPlayer.askPrune()
                print(currentPlayer.identity + " thinking...")

                MovePrediction.numStatesExamined = 0

                # original board will 'corrupt' if used in AI move calculation, so use a deep copy
                copyCurrentMatrix = copy.deepcopy(self.matrix)

                if debugBool == False:
                    evaluation, bestMove = MovePrediction.minimax(copyCurrentMatrix, 4, True, -999999, 999999, currentPlayer.color, None, debugBool, outputFile, pruningSwitch)
                elif debugBool:
                    evaluation, bestMove = MovePrediction.minimax(copyCurrentMatrix, 4, True, -999999, 999999, currentPlayer.color, [], debugBool, outputFile, pruningSwitch)

                print(str(MovePrediction.numStatesExamined) + " number of states were examined. ")

                if bestMove:
                    #print(str(bestMove))
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
                    print("There wasn't a move available. Yielding to other player...")

            # pass over to next user
            temp = currentPlayer
            currentPlayer = nextPlayer
            nextPlayer = temp



