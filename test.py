
n= 1000
res = 0
while n:
    # is end 1
    res += n % 2
    # shift bits
    n = n>>1
    print(n)
print(res)