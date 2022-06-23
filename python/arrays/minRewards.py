# Difficulty: Hard

# O(n) time, O(n) space

def minRewards(scores):
    # build the rewards array to keep track of adjacent values
    rewards = [1 for x in scores]
    # iterate rightwards
    for i in range(1, len(scores)):
        if scores[i] > scores[i-1]:
            rewards[i] = rewards[i-1] + 1
    # Iterate leftwards
    for i in reversed((range(len(scores)-1))):
        if scores[i] > scores[i+1]:
            rewards[i] = max(rewards[i], rewards[i+1]+1)
    return sum(rewards)






# O(n^2) time, O(n) space
array = [1,2,3,4,5,6,1,2,3,4,5,1]

def minRewards(scores):
    rewards = [1 for x in scores]
    for i in range(1, len(scores)):
        j = i - 1
        if scores[i] > scores[j]:
            rewards[i] = rewards[j] + 1
        else:
            while j >= 0 and scores[j] > scores[j+1]:
                rewards[j] = max(rewards[j], rewards[j+1]+1)
                j -= 1
    return sum(rewards)

print(minRewards(array))