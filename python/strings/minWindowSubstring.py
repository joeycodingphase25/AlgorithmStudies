
# every character t (dups) is included in window, else ""

def minWindow(string1, string2):
    string2Map = {}
    for letter in string2:
        string2Map[letter] = string2Map.get(letter, 0) + 1
    start = 0
    end = len(string2)
    tempEnd = len(string2)
    # break if no more can be searched
    while start < (len(string1) - (end+1)):
        if end == len(string1)-1:
            start = 0
            tempEnd +=1
            end = tempEnd
        x = string2Map.copy()
        ans = checker(string1[start:end], x)
        if ans:
            return ans
        start+=1
        end+=1
    return ''

# return ans
def checker(string1Splice, string2Map):
    for letter in string1Splice:
        if letter in string2Map:
            string2Map[letter] -= 1
    if sum(string2Map.values()) == 0:
        return string1Splice
    return ''

print(minWindow("ADOBECODEBANC","ABC"))