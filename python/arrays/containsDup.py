
# O(n) time, O(n) space
# https://leetcode.com/problems/contains-duplicate/
def containsDuplicate(nums):
    dup = set()
    for num in nums:
        if num in dup:
            return True
        dup.add(num)
    return False