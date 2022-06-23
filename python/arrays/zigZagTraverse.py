# Difficulty: Hard
# O(n) time, O(n) space
array = [
    [1, 3],
    [2, 4],
    [5, 7],
    [6, 8],
    [9, 10]
  ]

def zigzagTraverse(array):
    height = len(array) - 1
    width = len(array[0]) - 1
    result = []
    row, col = 0,0
    goingDown = True
    # Check to avoid out of bounds errors (O(1) time)
    while not isOutOfBounds(row, col, height, width):
        result.append(array[row][col])
        # downwards Boolean
        if goingDown:
            # if you have reached an edge / the end change bool to false
            if col == 0 or row == height:
                goingDown = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row +=1
                col -=1
        else:
            if row == 0 or col == width:
                goingDown = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -=1
                col +=1
    return result

def isOutOfBounds(row, col, height, width):
    return row < 0 or row > height or col < 0 or col > width

print(zigzagTraverse(array))