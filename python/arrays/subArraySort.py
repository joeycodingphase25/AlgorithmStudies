# Difficulty: Hard
# O(nlogn) time, 0(n) space

## FIXED
def subarraySort(array):
    compare = sorted(array)
    res = []
    leftHolder = False
    rightHolder = False
    left = 0
    right = len(array)-1
    
    while left < right and leftHolder == False: 
        if array[left] != compare[left]:
            leftHolder = True
            res.append(left)
        else:
            left += 1
    while left < right and rightHolder == False:
        if array[right] != compare[right]:     
            rightHolder = True
            res.append(right)
        else:
            right -= 1
    if len(res) == 0:
        return [-1,-1]
    return res

# Option 2
# O(n) time, 0(1) space

