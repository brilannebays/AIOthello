# The brains of the AI player. We'll run Minimax algorithm, alpha beta pruning, and corner + parity heuristic

from BoardMngmt import Board

# a tree of potential moves that returns the best possible move based on an heuristic score
def minimax(matrix, depth, maximizingPlayer, alpha, beta, aiPieceColor):

    # we return the score of the nodes at the final depth + an empty list to retain format of minimax return
    if depth == 0:
        return diskParity(matrix, aiPieceColor), []

    board = Board()

    # maximizing player will always represent AI, due to heuristic scoring
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

            # the user has a better move than the AI, so will stop checking here, because AI will never choose the "better" move
            if beta <= alpha:
                break

        return maxEval, bestMove

    # minimizing player will always represent user
    else:
        minEval = 999999
        moves = board.getPotentialMoves(matrix, aiPieceColor)
        bestMove = []

        # check if a move generates children moves recursively
        for move in moves:
            row = move[0]
            column = move[1]
            toFlip = board.legalize(matrix, aiPieceColor, row, column)
            board.updateBoard(matrix, aiPieceColor, toFlip, row, column)
            val, bestCurrentMove = minimax(matrix, depth - 1, True, alpha, beta, aiPieceColor)

            # if val gives us a move with a lower score than the other children, we'll consider it our best move
            if val < minEval:
                bestMove.append(row)
                bestMove.append(column) 

            minEval = min(minEval, val)

            # the user has a better move than the AI, so will stop checking here
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
    
    # please forgive me for this Dr. Mike. We're giving each corner a greater value
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



