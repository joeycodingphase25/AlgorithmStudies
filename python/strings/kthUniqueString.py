

stringList = ["d","b","c","b","c","a", "a"]
def kthString(stringList, k):
    uniques = set()
    for string in stringList:
        if string not in uniques:
            uniques.add(string)
        else:
            uniques.remove(string)
    for string in stringList:
        if string in uniques:
            k -= 1
            if k == 0:
                return string
    return ""

print(kthString(stringList, 2))