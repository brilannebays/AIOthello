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
        self.DIRECTIONS = [
            (0, 1),     # up
            (1, 1),     # up-right
            (1, 0),     # right
            (1, -1),    # down-right
            (0, -1),    # down
            (-1, -1),   # down-left
            (-1, 0),    # left
            (-1, 1),    # up-left

        ]
    
    def create(self):
        matrix = [["-" for i in range(10)] for j in range(10)]
        for i in range(10):
            for j in range(10):
                matrix[0][j] = "V"
                matrix[i][0] = "V"
                matrix[9][j] = "V"
                matrix[i][9] = "V"

        # black is 0, white is 1
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

    def legalize(self, matrix, pieceColor, row, column):
        piecesToFlip = []

        if pieceColor == "BLACK":
            # 1 indicates white
            oppColor = 1

        else:
            # 0 indicated black
            oppColor = 0

        for x, y in self.DIRECTIONS:
            foundOpp = False
            numOpps = 0
            xStep = row
            yStep = column


            while True:
                xStep += x
                yStep += y 

                if (matrix[xStep][yStep] == "V") or (matrix[xStep][yStep] == "-"):
                    break

                if matrix[xStep][yStep] == oppColor:
                    foundOpp = True
                    numOpps += 1
                    continue

                if matrix[xStep][yStep] == pieceColor:
                    if foundOpp and numOpps > 0:
                        xStepBack = xStep
                        yStepBack = yStep
                        for i in range(numOpps):
                            xStepBack -= x 
                            yStepBack -= y 
                            piecesToFlip.append((xStepBack, yStepBack))
                    break

        return piecesToFlip

    def updateBoard(self, matrix, pieceColor, flippingArray, row, column):
        if pieceColor == "BLACK":
            selfColor = 0
        else:
            selfColor = 1

        matrix[row][column] = selfColor

        for x, y in flippingArray:
            matrix[x][y] = selfColor

        

                        


