# Difficulty : Easy
# O(n) time | O(n) space

class Solution:
    # Target not necessary considering guaruntee match
    def twoSum(nums, target):
        numCompliment = {}
        for i in range(len(nums)):
            if nums[i] not in numCompliment:
                # store the index with key() of target-num[i]
                numCompliment[target-nums[i]] = i
            else:
                # when num[i] in dict, then i is the second index value
                return [numCompliment[nums[i]], i]