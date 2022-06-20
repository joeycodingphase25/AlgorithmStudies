# Difficulty: Medium
# O(n^2) time, O(1) space

array = [2,2,2,2,2,2]

def threeSum(array, targetSum):
	array.sort()
	test = []
	for i in range(len(array)-2):
		right = len(array) - 1
		left = i + 1
		while left < right:
			if array[i] + array[left] + array[right] == targetSum:
				test.append([array[i], array[left], array[right]])
				left += 1
				right -= 1
			if array[i] + array[left] + array[right] < targetSum:
				left += 1
			if array[i] + array[left] + array[right] > targetSum:
				right -= 1
	return test
print(threeSum(array, 6))