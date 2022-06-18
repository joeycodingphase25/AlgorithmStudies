# Difficulty: Medium
# O(n) time, O(n) space

def firstDuplicateValue(array):
    # Initialize a dictionary to keep track of values
    test = {}
    for x in array:
        # if you find a value in dict, its a duplicate
        if x not in test:
            test[x] = 1
        else:
            return x
    return -1