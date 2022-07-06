import collections
from typing import Counter
# O(n) time and space

def isAnagram(s,t):
    return Counter(s) == Counter(t)

