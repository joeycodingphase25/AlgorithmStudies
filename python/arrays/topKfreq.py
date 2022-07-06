# O(n logn) time, O(n) space

def topKFrequent(nums):
    hashMap = {}
    res = []
    for num in nums:
        hashMap[num] = hashMap.get(num, 0) + 1
    list1 = sorted(list(hashMap.items()), key=lambda x: x[1], reverse=True)
    print(list1)
    for tuple in list1:
        if k == 0:
            return res
        res.append(tuple[0])
        k-=1
    return res