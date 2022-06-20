
nums = [2,2,2,2]
def fourSum(nums, target):
    nums.sort()
    res, quad = [], []

    def helper(k, start, target):
        if k!=2:
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

print(fourSum(nums, 8))