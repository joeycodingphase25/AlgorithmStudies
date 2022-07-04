
# O(1) time, space

# neet code
n= 1000
res = 0
def hammingWeight(n):
    while n:
        # is end 1
        res += n % 2
        # shift bits
        n = n>>1
    return res