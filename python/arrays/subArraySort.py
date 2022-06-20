# Difficulty: Hard
# O(nlogn) time, 0(n) space

## This will only work if the array > 2 AND the array has two points of failure
# need optimization improvements 
def subarraySort(array):
    compare = sorted(array)
    res = []
    leftHolder = False
    rightHolder = False
    left = 0
    right = len(array)-1
    while True:
        while leftHolder == False: 
            if array[left] != compare[left]:
                leftHolder = True
                res.append(left)
            left += 1
        while rightHolder == False:
            if array[right] != compare[right]:     
                rightHolder = True
                res.append(right)
            right -= 1
        break
    return res

# Option 2
# O(n) time, 0(1) space

