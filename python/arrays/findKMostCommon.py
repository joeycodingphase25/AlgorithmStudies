
# O(n)* logN time, o(n) space
nums = [1,1,1,2,3]
k = 2

def findK(nums, k):
    finalReturnArray = []
    resArray = []
    nums.sort()
    i = 1
    count = 1
    while i <= len(nums)-1:
        while i <= len(nums):
            if i == len(nums):
                resArray.append((nums[i-1], count))
                i += 1
            elif nums[i] == nums[i-1]:
                count += 1
                i +=1
            elif nums[i] != nums[i-1]:
                resArray.append((nums[i-1], count))
                count = 1
                i +=1

    resArray.sort(key=lambda x: x[1])
    count = -1
    while k > 0:
        finalReturnArray.append(resArray[count][0])
        count -= 1
        k -= 1
    return finalReturnArray
print(findK(nums, k))


#### another approach O(n) time, O(n) sapce

def findK(nums, k):
    hashmap = {}
    bucketArray = [[] for _ in range(len(nums)-1)]
    for num in nums:
        hashmap[num] = 1 + hashmap.get(num, 0)
    for num, value in hashmap.items():
        # store index == value in bucket array
        bucketArray[value].append(num)

    res = []
    for lists in reversed(bucketArray):
        for list in bucketArray[lists]:
            res.append(list)
            if len(res) == k:
                return res
    