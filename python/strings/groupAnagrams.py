from collections import Counter
# Difficulty: Medium
#  O(w*n*log(n)) time, O(wn) space (words, length)

def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]
    return list(anagrams.values())

    
# Credit- Aron Teh (Genius solution)
# O(wn) time/space
def groupAnagrams(words):
    anagrams = {}
    for word in words:
        wordCounterHashKey = frozenset(Counter(word).items())
        if wordCounterHashKey not in anagrams:
            anagrams[wordCounterHashKey] = []
        anagrams[wordCounterHashKey].append(word)
    return list(anagrams.values())

# my personal take on the problem
# lessons learned: Counter Object is special properties can 
# record key, value when converted to frozen set
def groupAnagrams(words):
    compare = {}
    for word in words:
        var = frozenset(to_dict(word))
        if var not in compare:
            compare[var] = []
        compare[var].append(word)
    return list(compare.values())

def to_dict(word):
    #returns dict value to serve as key
    test = {}
    for letter in word:
        if letter not in test:
            test[letter] = 1
        else:
            test[letter] += 1
    return test