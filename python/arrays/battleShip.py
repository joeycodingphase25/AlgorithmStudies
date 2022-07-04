battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
[1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
[1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def validate_battlefield(field):
    hashMapValidator = {}
    totalShips = {
        '4': 1,
        '3':2,
        '2':3,
        '1':4
    }
    row, col = 0, 0
    maxRow, maxCol = len(field), len(field[0])
    # Find How big the Ship is and return  
    def isValidShip(row, col, maxRow, maxCol, count):
       # downwards path ?
        if (row + 1) < maxRow and (field[row+1][col]) == 1:
            row += 1
            while row < maxRow and (field[row][col]) == 1:
                hashMapValidator[f'{row}, {col}'] = True
                count += 1       
                row += 1
            return count
        #  rightwards path ?
        if (col + 1) < maxCol and (field[row][col+1]) == 1:
            col += 1
            while (col) < maxCol and (field[row][col]) == 1:
                hashMapValidator[f'{row}, {col}'] = True
                count += 1   
                col += 1
            return count
        # if submarine ?
        else:
            return count  
    # Find out if it is touching another corner
    # def isTouching()
    # TRAVERSAL PORTION 
    while row < maxRow and col < maxCol:
        if field[row][col] == 1 and f'{row}, {col}' not in hashMapValidator:
            hashMapValidator[f'{row}, {col}'] = True
            # recieve count and type of battleship
            tempRow = row
            count = isValidShip(row, col, maxRow, maxCol, count=1)
            row = tempRow
            if count > 4:
                return False
            totalShips[str(count)] -= 1
            # flag too many ships
            if totalShips[str(count)] < 0:
                return False
        col += 1
        # iterate next line
        if col == maxCol:
            row += 1
            col = 0
    # final condition
    return True if sum(list(totalShips.values())) == 0 else False


validate_battlefield(battleField)