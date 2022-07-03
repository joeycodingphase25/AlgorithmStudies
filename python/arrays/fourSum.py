
nums = [2,2,2,2,2,2]
def fourSum(nums, target):
    nums.sort()
    res, quad = [], []

    def helper(k, start, target):
        if k != 2:
            for i in range(start, len(nums)-k+1):
                if i > start and nums[i] == nums[i-1]:
                    continue
                quad.append(nums[i])
                helper(k-1, i+1, target-nums[i])
                quad.pop()
            return
        
        l,r = start, len(nums)-1
        while l<r:
            if nums[l] + nums[r] < target:
                l +=1
            elif nums[l] + nums[r] > target:
                r -=1
            else:
                res.append(quad + [nums[l], nums[r]])
                l +=1
    
    helper(4, 0, target)
    return res




# print(fourSum(nums, 8))
def fourSum(nums, target):
    def findNsum(l, r, target, N, result, results):
        if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:  # early termination
            return
        if N == 2: # two pointers solve sorted 2-sum problem
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        else: # recursively reduce N
            for i in range(l, r+1):
                if i == l or (i > l and nums[i-1] != nums[i]):
                    findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)

    nums.sort()
    results = []
    findNsum(0, len(nums)-1, target, 4, [], results)
    return results

print(fourSum(nums, 8))