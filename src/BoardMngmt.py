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
        matrix[4][4], matrix[5][5] = "1", "1"
        matrix[4][5], matrix[5][4] = "0", "0"

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
            selfColor = "0"
            oppColor = "1"

        else:
            # 0 indicated black
            selfColor = "1"
            oppColor = "0"

        for x, y in self.DIRECTIONS:
            foundOpp = False
            numOpps = 0
            xStep = row
            yStep = column

            # keep taking steps unless we reach the bounds, encounter an empty space, or reach our own color
            while True:
                xStep += x
                yStep += y 

                if (matrix[xStep][yStep] == "V") or (matrix[xStep][yStep] == "-"):
                    break

                if matrix[xStep][yStep] == oppColor:
                    foundOpp = True
                    numOpps += 1
                    continue

                if matrix[xStep][yStep] == selfColor:
                    if foundOpp and numOpps > 0:
                        xStepBack = xStep
                        yStepBack = yStep
                        for i in range(numOpps):
                            xStepBack -= x 
                            yStepBack -= y 
                            piecesToFlip.append((xStepBack, yStepBack))
                    break

        #print(piecesToFlip)
        return piecesToFlip

    def updateBoard(self, matrix, pieceColor, flippingArray, row, column):
        if pieceColor == "BLACK":
            selfColor = "0"
        else:
            selfColor = "1"

        matrix[row][column] = selfColor

        for x, y in flippingArray:
            matrix[x][y] = selfColor

    def score(self, matrix):
        black = 0
        white = 0

        for i in range(10):
            for j in range(10):
                if matrix[i][j] == "0":
                    black += 1
                elif matrix[i][j] == "1":
                    white += 1
        
        print("BLACK: " + str(black) + "     WHITE: " + str(white))

    # find every single move available to a piece color currently on the board
    def getPotentialMoves(self, matrix, pieceColor):
        potentialMoves = []
        if pieceColor == "BLACK":
            # 1 indicates white
            selfColor = "0"
            oppColor = "1"

        else:
            # 0 indicated black
            selfColor = "1"
            oppColor = "0"

        # look at every spot on the board
        for i in range(1, 9):
            for j in range(1, 9):

                # we're only looking at our pieces
                #print("We're looking at piece: " + str(i) + str(j))
                if (matrix[i][j] == "-") or (matrix[i][j] == oppColor):
                    continue
                
                if (matrix[i][j] == selfColor):
                    #print("We've found our piece at " + str(i) + str(j))
                    # when we've found one of our pieces, check every direction of that piece
                    for x, y in self.DIRECTIONS:
                        xStep = i
                        yStep = j
                        opps = 0

                        while True:
                            xStep += x 
                            yStep += y 
                            emptySpotCoords = []

                            # stop stepping when you hit the boarder or our own piece
                            if (matrix[xStep][yStep]) == "V" or (matrix[xStep][yStep] == selfColor):
                                #print("We stepped on the boarder or ourself")
                                #print(str(xStep) + str(yStep))
                                break 

                            # yay, an open spot! we'll add this to potential moves
                            if matrix[xStep][yStep] == "-":
                                if opps > 0:
                                    emptySpotCoords.append(xStep)
                                    emptySpotCoords.append(yStep)
                                    #print(str(emptySpotCoords))
                                    potentialMoves.append(emptySpotCoords)
                                    break 
                                if opps == 0:
                                    break


                            # opponent color? keep looking
                            if matrix[xStep][yStep] == oppColor:
                                #print("We've stepped on an opp")
                                opps +=1
                                continue

        return potentialMoves

        

                        


