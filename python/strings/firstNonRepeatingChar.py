# Difficulty: Easy
# Complexity O(2n) time, O(1) space * due to alphabet constriction==static
# This function finds the index of first non-Repeating Char
def firstNonRepeatingCharacter(string):
    # Initialize a dictionary
    test = {}
    # Iterate the input string
    for char in string:
        # Initialize value/ += the exisiting value
        test[char] = test.get(char, 0) + 1

    count = 0
    for char in string:
        # identify the character at each index
        if test[char] == 1:
            return count
        count +=1
    return -1

print(firstNonRepeatingCharacter("abcdabd"))

# Alternative for loop
    # for idx in range(len(string)):
    #     # identify the character at each index
    #     character = string[idx]
    #     if test[character] == 1:
    #         return idx