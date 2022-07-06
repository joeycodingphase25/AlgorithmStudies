# O(logN) time, O(1) space
def singleNumber(nums):
        nums.sort()
        left= 0
        right = 1
        while left < len(nums)-1 and nums[left] == nums[right]:
            left += 2
            right += 2
        return nums[left]

# Leetcode solution
def singleNumber(self, nums):
        a = 0
        # use XOR operator to cancel out all duplicates
        for i in nums:
            a ^= i
        return a