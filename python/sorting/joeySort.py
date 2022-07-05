array = [5,2,34,4,1,2]

def sorter(array):
    left, right = 0, len(array) -1
    while left < right:
        if array[left] > array[right]:
            array[left], array[right] = array[right], array[left]
            right = len(array)- 1
        while array[left] < array[right]:
            right -= 1
    return array

print(sorter(array))