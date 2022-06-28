# difficulty: medium
# O(n) time, O(1) space

# this takes advantage of the pop() O(1) time, to make this a linear time complexity

array = [0,0,1,2,2,2,3,4,8,8,10]

def removeDuplicates(array):
    left = 0
    right = left + 1
    while right < len(array):
        if array[right] > array[left]:
            left +=1
            array[right], array[left] = array[left], array[right]
        else:
            right +=1
    for i in range(left, len(array)-1):
        array.pop()
    return array


print(removeDuplicates(array))
