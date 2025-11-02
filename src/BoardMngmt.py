# Brilanne Bays 
# Desc:

# TO-DO 
# - keep track of piece colors 
# - generate array of valid moves for EACH TURN
# - Flip discs for a move
# - Count pieces for scoring
# - Print or return a visual of the board

class Board:
    def __init__(self):
        pass
    
    def create(self):
        matrix = [["-" for i in range(10)] for j in range(10)]
        for i in range(10):
            for j in range(10):
                matrix[0][j] = "V"
                matrix[i][0] = "V"
                matrix[9][j] = "V"
                matrix[i][9] = "V"


        matrix[4][4], matrix[5][5] = 1, 1
        matrix[4][5], matrix[5][4] = 0, 0

        return matrix

    def display(self, matrix):
        print("    1 2 3 4 5 6 7 8  ")
        lettering = [" ", "A", "B", "C", "D", "E", "F", "G", "H", " "]
        for i in range(10):
            row = lettering[i] + " "
            for j in range(10):
                row += str(matrix[i][j]) + " "
            print(row)

    def legalize(self, matrix, ):

