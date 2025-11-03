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

class Gameplay:
    def __init__(self, player1, player2, boardObject, initializedBoard):
        self.player1 = player1
        self.player2 = player2
        self.board = boardObject
        self.matrix = initializedBoard 
    
    def runGame(self):
        running = True

        while running:
            row, column = self.player1.move(self.matrix)
            toFlip = self.board.legalize(self.matrix, self.player1.color, row, column)
            self.board.updateBoard(self.matrix, self.player1.color, toFlip, row, column)
            self.board.display(self.matrix)

            move2 = self.player2.move(self.matrix)
        
