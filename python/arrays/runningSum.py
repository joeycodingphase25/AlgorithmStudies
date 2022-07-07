# O(n) time, O(1) space
def runningSum(array):
    prevNum = 0
    for idx, num in enumerate(array):
        array[idx] = num + prevNum
        prevNum = array[idx]
    return array

print(runningSum([3,1,2,10,1]))