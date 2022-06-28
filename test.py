from collections import Counter

words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
def groupAnagrams(words):
    compare = {}
    for word in words:
        var = to_dict(word)
        if var not in compare:
            compare[var] = []
        compare[var].append(word)
    return compare.values()

def to_dict(word):
    #returns dict value to serve as key
    test = {}
    for letter in word:
        if letter not in test:
            test[letter] = 0
        else:
            test[letter] += 1
    return test

groupAnagrams(words)