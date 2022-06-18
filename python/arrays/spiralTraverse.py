# Difficulty: Medium
# O(n) time, O(n) space -> n = len(array)*len(array[0])
array = [
    [1, 2, 3, 4],
    [12,13,14,5],
    [11,16,15,6],
    [10, 9, 8, 7]
    ]
def spiralTraverse(array):
    result = []
    # set your four pointers to have 2d iterations
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0])-1
	# base case flag to stop index out of range and duplicates
    while startRow <= endRow and startCol <= endCol:
        # iterate left to right
        # range inclusive on start, not on end
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])
        # iterate downwards
        # range inclusive on start, not on end
        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])
        # iterate right to left
        # range inclusive on start, not on end
        for col in reversed(range(startCol, endCol)):
            if startRow == endRow:
                break
            result.append(array[endRow][col])
        # iterate upwards
        # range inclusive on start, not on end
        for row in reversed(range(startRow + 1, endRow)):
                if startCol == endCol:
                    break
                result.append(array[row][startCol])
            
        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1
        
    return result
print(spiralTraverse(array))

# Another Stategy/ approach Unfinished

def spiralTraverse(array):
    # create start,end col | start, end row
    startCol, endCol = 0, len(array[0])-1
    startRow, endRow = 0, len(array)-1
    returnList = []
    # create flag to stop parent while loop
    while startCol <= endCol and startRow <= endRow:
        # start iterating the first row
        pointer = startCol
        while pointer <= endCol:
            # this is inclusive of end element
            returnList.append(array[startRow][pointer])
            pointer += 1
        # iterate end column
        pointer = startRow + 1
        while pointer <= endRow:
            returnList.append(array[pointer][endCol])
            pointer += 1
        # iterate backwards the bottom row not inclusive
        pointer = endCol-1
        while pointer >= startCol:
            if startRow == endRow:
                break
            returnList.append(array[endRow][pointer])
            pointer -=1
        # iterate up the left row not inclusive
        pointer = endRow-1
        while pointer > startRow:
            if startCol == endCol:
                    break
            returnList.append(array[pointer][startRow])
            pointer -=1
        startRow +=1
        startCol +=1
        endRow -=1
        endCol -= 1
    return returnList

print(spiralTraverse(array))