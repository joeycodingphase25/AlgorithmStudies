# Difficuly: easy
# O(n) time, O(d) space

def productSum(array, multiplier=1):
    # reset sum every time
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element, multiplier + 1)
        else:
            sum += element
    # Base Case return and keeps track of nested genius
    return sum*multiplier