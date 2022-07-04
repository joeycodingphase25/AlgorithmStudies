def longestSubstringWithoutDuplication(string):
    if len(string) == 0:
            return {}
    if len(string) == 1:
        return string[0]
    # make l, r pointers and dupMap
    l, r = 0, 1
    res = [l, r]
    dupMap = {}
    while r < len(string):
        leftLetter = string[l]
        rightLetter = string[r]
        dupMap[leftLetter] = (leftLetter, l)
        if rightLetter not in dupMap:
            # make values
            dupMap[rightLetter] = (rightLetter, r)
            r += 1
            
        elif rightLetter == leftLetter:
            if (r-l) > (res[1]-res[0]):
                res = [l, r]
            l += 1
            r = l+1
            dupMap = {}
        else:
            # is this index range biggeR? keep track
            if (r-l) > (res[1]-res[0]):
                res = [l, r]
            l = dupMap[rightLetter][1]
            r = l+1
            dupMap = {}

    return string[res[0]:res[1]]