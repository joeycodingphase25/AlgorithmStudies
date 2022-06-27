# Difficulty: Medium
# Time: O(n*n!) | O(n*n!) space

# All permutations
def getPermutations(array):
    permutations = []
    permutationsHelper(array, [], permutations)
    return permutations

def permutationsHelper(array, currentPermutation, permutations):
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i+1:]
            newPermutation = currentPermutation + [array[i]]
            permutationsHelper(newArray, newPermutation, permutations)



# Permutations 2 // Unique Only
array = [1,1,2]
def permutateUnique(array):
    res = []
    perm = []
    count = {n:0 for n in array}
    for n in array:
        count[n] +=1
    
    def dfs():
        if len(perm) == len(array):
            res.append(perm.copy())
            return
        for n in count:
            if count[n] > 0:
                perm.append(n)
                count[n] -= 1

                dfs()

                count[n] += 1
                perm.pop()
    dfs()
    return res
print(permutateUnique(array))