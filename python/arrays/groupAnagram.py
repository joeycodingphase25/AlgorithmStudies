
stringList = ["eat","tea","tan","ate","nat","bat"]

def groupAnagram(stringList):
    returnHash = {}
    for string in stringList:
        key = "".join(sorted(string))
        returnHash[key] = returnHash.get(key, []) + [string]
    return list(returnHash.values())

print(groupAnagram(stringList))