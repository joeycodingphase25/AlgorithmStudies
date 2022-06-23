# Difficulty: Easy

# O(n+m) time , O(c) space


def generateDocument(characters, document):
    map1 = {}
    
    for char in characters:
        if char not in map1:
            map1[char] = 0
        map1[char] += 1
       
    for char in document:
        if char not in map1 or map1[char]==0:
            return False
        map1[char] -= 1
    return True
