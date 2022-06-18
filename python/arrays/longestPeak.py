# difficulty: medium
# O(n) time, O(1) space

def longestPeak(array):
    longest = 0
    i = 1
    # flag to traverse array
    while i < len(array) - 1:
        # while-continue boolean checker
        isPeak = array[i-1] < array[i] and array[i] > array[i+1]
        if not isPeak:
            i+=1
            continue
        leftIdx = i-2
        # flag for index out of range and boolean decreasing logic
        while leftIdx >=0 and array[leftIdx] < array[leftIdx+1]:
            leftIdx -=1
        rightIdx=i+2
        # flag for index out of range and boolean decreasing logic
        while rightIdx < len(array) and array[rightIdx]<array[rightIdx-1]:
            rightIdx+=1

        # grab the distance between two points
        currentPeakLength=rightIdx - (leftIdx +1)
        # update the longest value every time
        longest = max(longest, currentPeakLength)
        i = rightIdx
    return longest