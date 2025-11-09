# Brilanne Bays
# Desc:

# TO-DO 
# - Mini Max
# - Alpha Beta Pruning
# - Heuristic: corner moves should be scored higher
# - Decide and return best move


from BoardMngmt import Board

def minimax(matrix, depth, maximizingPlayer, alpha, beta, aiPieceColor):

    # we return the score of the nodes at the final depth + an empty list to retain format of ()
    if depth == 0:
        return diskParity(matrix, aiPieceColor), []

    board = Board()

    if maximizingPlayer:
        maxEval = -999999
        moves = board.getPotentialMoves(matrix, aiPieceColor)
        bestMove = []
        for move in moves:
            row = move[0]
            column = move[1]
            toFlip = board.legalize(matrix, aiPieceColor, row, column)
            board.updateBoard(matrix, aiPieceColor, toFlip, row, column)

            val, bestCurrentMove = minimax(matrix, depth - 1, False, alpha, beta, aiPieceColor)

            if val > maxEval:
                bestMove.append(row)
                bestMove.append(column)
            maxEval = max(maxEval, val)

            alpha = max(alpha, val)

            if beta <= alpha:
                break

        return maxEval, bestMove


    else:
        minEval = 999999
        moves = board.getPotentialMoves(matrix, aiPieceColor)
        bestMove = []
        for move in moves:
            row = move[0]
            column = move[1]
            toFlip = board.legalize(matrix, aiPieceColor, row, column)
            board.updateBoard(matrix, aiPieceColor, toFlip, row, column)
            val, bestCurrentMove = minimax(matrix, depth - 1, True, alpha, beta, aiPieceColor)

            if val < minEval:
                bestMove.append(row)
                bestMove.append(column) 

            minEval = min(minEval, val)

            beta = min(beta, val)
            if beta <= alpha:
                break

        return minEval, bestMove

    
# we're going to normalize the difference of the score
def diskParity(matrix, aiPieceColor):
    if aiPieceColor == "BLACK":
        selfColor = "0"
        oppColor = "1"
    else:
        selfColor = "1"
        oppColor = "0"

    sumSelf = 0
    sumOpp = 0
    for i in range(1, 9):
        for j in range(1, 9):
            if matrix[i][j] == selfColor:
                sumSelf += 1
            if matrix[i][j] == oppColor:
                sumOpp += 1
    
    # please forgive me for this Dr. Mike
    if matrix[1][1] == selfColor:
        sumSelf += 2
    elif matrix[1][1] == oppColor:
        sumOpp += 2
    
    if matrix[1][8] == selfColor:
        sumSelf += 2
    elif matrix[1][8] == oppColor:
        sumOpp += 2

    if matrix[8][1] == selfColor:
        sumSelf += 2
    elif matrix[8][1] == oppColor:
        sumOpp += 2

    if matrix[8][8] == selfColor:
        sumSelf += 2
    elif matrix[8][8] == oppColor:
        sumOpp += 2

    # greater negatives will favor player, while greater positives will favor AI
    # this means that the maximizing player MUST BE AI
    return sumSelf - sumOpp



