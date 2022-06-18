# Difficulty : Medium
# O(3n) time, O(n) space where n is len of array
def arrayOfProducts(array):
    # build the products array, to avoid the 0 product failure
    products = [1 for x in range(len(array))]
    # run array and keep track of increasing product from the left
    left = 1
    for i in range(len(array)):
        products[i] = left
        left *= array[i]

    # run array and keep track of increasing product from the right
    right = 1
    for i in reversed(range(len(array))):
        products[i] *= right
        right *= array[i]
    
    return products
