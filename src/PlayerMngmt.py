
class Player:
    def __init__(self, identity, color):
        self.identity = identity.upper()
        self.color = color.upper()

    def move(self, matrix):
        '''
            For self, we want to validate input. Input can't be on another piece, it can't be on the border, and
            it has to be a combination of [A-E][1-8]
        '''
        rows = [" ", "A", "B", "C", "D", "E", "F", "G", "H", " "]
        columns = [0, 1, 2, 3, 4, 5, 6, 7, 8, 0]

        if self.identity == "SELF":
            while True:

                getMove = input(f"Select move [letter][number] for {self.color}: ")

                row = getMove[0]
                column = getMove[1]

                if column.isdigit():
                    column = int(column)
                else:
                    print("The second value entered is not an integer.")
                    continue

                # checking if move is on the board
                if (row in rows) and (column in columns):
                    firstIndex = rows.index(row)
                    secondIndex = columns.index(column)

                    if (firstIndex < 1) or (firstIndex > 8):
                        print("This input is invalid. Please select move in form [letter][number].")
                        continue
                    
                    if (secondIndex < 1) or (secondIndex > 8):
                        print("This input is invalid. Please select move in form [letter][number].")
                        continue
                    
                    if (matrix[firstIndex][secondIndex] == 1) or (matrix[firstIndex][secondIndex] == 0):
                        print("This input is invalid. There is already a piece at this location.")
                        continue

                    return firstIndex, secondIndex

                else:
                    print("This input is invalid. Please select move in form [letter][number].")
                    continue


        if self.identity == "AI":
            return