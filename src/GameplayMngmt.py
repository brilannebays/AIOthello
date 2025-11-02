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
    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.board = board 
    
    def runGame(self):
        running = True

        while running:
            self.player1.move(self.board)
            self.player2.move(self.board)
        
