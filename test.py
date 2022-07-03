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
    
    while row < maxRow and col < maxCol:
        # have we seen this square?
        if [row,col] in hashMapValidator:
            continue
        # base case
        if field[row][col] == 1:
            # recieve count
            count = isValidShip(row, col, maxRow, maxCol, count=1, hashMapValidator)
            if count > 4:
                return False
            totalShips['count'] -= 1
            if totalShips['count'] < 0:
                return False
    # final condition
    return True if sum(list(totalShips.values())) == 0 else False


def isValidShip(row, col, maxRow, maxCol, count, hashMapValidator):
    # handle idx errors and find traverse path
    # downwards path
    if (row + 1) < maxRow and (row + 1) == 1:
        tempRow = row
        while (tempRow + 1) < maxRow and (tempRow +1) == 1:
            hashMapValidator['tempRow, tempCol'] = True
            count += 1       
        return count
    #  rightwards path
    if (col + 1) < maxCol and (col +1) == 1:
        tempCol = col
        while (tempCol + 1) < maxCol and (tempCol +1) == 1:
            hashMapValidator['tempRow, tempCol'] = True
            count += 1   
    # if submarine
    else:
        hashMapValidator['row, col'] = True
        return count