# Difficulty: Hard
# O(n) time, O(n) space

def largestRange(array):
    # declare your variables
    bestRange = []
    longestLength = 0
    nums = {}
    # create map with iteration
    for num in array:
        nums[num] = True
    # compare map to array
    for num in array:
        # simple flag for traversed values if not False
        if not nums[num]:
            continue
        # set the traversed value to false and create pointers
        nums[num] = False
        currentLength = 1
        left = num - 1
        right = num + 1
        # traverse outwards and find the left and right pointer stop values
        while left in nums:
            nums[left] = False
            currentLength += 1
            left -= 1
        while right in nums:
            nums[right] = False
            currentLength += 1
            right += 1
        # Simple check to determine if bestRange need updated
        if currentLength > longestLength:
            longestLength = currentLength
            bestRange = [left+1, right-1]
    return bestRange