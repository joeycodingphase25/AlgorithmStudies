# O(m*n) time, O(c) space

def minimumCharactersForWords(words):
    # make a map for the first word
    mainMap = {}
    for word in words:
        tempMap = {}
        for letter in word:
            if letter not in mainMap:
                # add to main
                mainMap[letter] = mainMap.get(letter, 0) + 1
            # add to temp
            tempMap[letter] = tempMap.get(letter,0) + 1
            # if letter in both maps, check values
            if tempMap[letter] > mainMap[letter]:
                mainMap[letter] += 1
    res = []
    for key, value in mainMap.items():
        while value > 0:
            res.append(key)
            value -= 1
    return res