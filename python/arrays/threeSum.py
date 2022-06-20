# Difficulty: Medium
# O(n^2) time, O(1) space

array = [2,2,2,2,2,2]
def threeSum(nums, target):
    nums.sort()
    result = []
    for left in range(len(nums) - 2): # renamed this to left because this will always be the leftmost pointer in the triplet
        # this step makes sure that we do not have any duplicates in our result output
        if left > 0 and nums[left] == nums[left - 1]: 
            continue 
        mid = left + 1 
        right = len(nums) - 1
        # classic 2SumII problem, with left and right pointer
        while mid < right:
            curr_sum = nums[left] + nums[mid] + nums[right]
            if curr_sum < target:
                mid += 1 
            elif curr_sum > target:
                right -= 1
            else:
                result.append([nums[left], nums[mid], nums[right]])
                # Left side duplicate number flag
                while mid < right and nums[mid] == nums[mid + 1]: 
                    mid += 1
                # right side duplicate number flag
                while mid < right and nums[right] == nums[right - 1]: 
                    right -= 1
                mid += 1
                right -= 1
    return result
print(threeSum(array, 6))

# def threeSum(array, targetSum):
# 	array.sort()
# 	test = []
# 	for i in range(len(array)-2):
# 		right = len(array) - 1
# 		left = i + 1
# 		while left < right:
# 			if array[i] + array[left] + array[right] == targetSum:
# 				test.append([array[i], array[left], array[right]])
# 				left += 1
# 				right -= 1
# 			if array[i] + array[left] + array[right] < targetSum:
# 				left += 1
# 			if array[i] + array[left] + array[right] > targetSum:
# 				right -= 1
# 	return test
# print(threeSum(array, 6))