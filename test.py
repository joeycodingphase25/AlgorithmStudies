
def largestAvgSubarray(nums, length):
    left = 0
    right = length
    if len(nums) == 1:
        return float(nums[0])
    avg = []
    while right <= len(nums):
        current = 0
        for i in range(left, right):
            current += nums[i]
        avg.append(round(current/length, 2))
        left, right = left+1, right+1
    return max(avg)

print(largestAvgSubarray([1,12,-5,-6,50,3], 4))